const $ = (id) => document.getElementById(id);
let data = { courses: [], sources: [], cards: [], model_available: false };
let selectedSourceId = null;
let suggestions = [];

async function api(path, body) {
  const response = await fetch(path, {
    method: body ? "POST" : "GET",
    headers: body ? { "Content-Type": "application/json" } : {},
    body: body ? JSON.stringify(body) : undefined,
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || "Request failed.");
  return result;
}

function message(text) { $("message").textContent = text; }

async function refresh() {
  data = await api("/api/state");
  render();
}

function courseSelect(element) {
  const previous = element.value;
  element.replaceChildren(new Option("Inbox / no course", ""));
  for (const course of data.courses) element.add(new Option(course.name, course.id));
  element.value = previous;
}

function render() {
  courseSelect($("capture-course"));
  courseSelect($("material-course"));
  const sources = $("sources");
  sources.replaceChildren();
  for (const source of data.sources) {
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `${source.kind === "capture" ? "Note" : "Material"}: ${source.title}`;
    button.setAttribute("aria-pressed", String(source.id === selectedSourceId));
    button.addEventListener("click", () => {
      selectedSourceId = source.id;
      suggestions = [];
      render();
    });
    const course = data.courses.find((item) => item.id === source.course_id);
    li.append(button, document.createTextNode(` ${course?.name || "Inbox"}`));
    sources.append(li);
  }
  if (!data.sources.length) sources.textContent = "No sources yet. Save a rough note above.";
  const selected = data.sources.find((source) => source.id === selectedSourceId);
  $("selected-source").hidden = !selected;
  if (selected) {
    $("source-title").textContent = selected.title;
    $("source-content").textContent = selected.content;
  }
  $("ai-draft").disabled = !selected || !data.model_available;
  $("ai-status").textContent = data.model_available
    ? "Uses the configured Ollama model only when clicked. Check whether that model is local, then review every suggestion."
    : "Optional: set STUDY_MODEL and run a local Ollama model.";
  const drafts = $("drafts");
  drafts.replaceChildren();
  for (const [index, suggestion] of suggestions.entries()) {
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `Edit suggestion ${index + 1}: ${suggestion.question}`;
    button.addEventListener("click", () => {
      $("question").value = suggestion.question;
      $("answer").value = suggestion.answer;
      $("quote").value = suggestion.quote;
      $("question").focus();
    });
    li.append(button);
    drafts.append(li);
  }
  for (const card of data.cards.filter((item) => item.status === "draft")) {
    const li = document.createElement("li");
    const source = data.sources.find((item) => item.id === card.source_id);
    const evidence = document.createElement("blockquote");
    evidence.textContent = `${source?.title || "Deleted source"}: “${card.quote}”`;
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = "Accept card";
    button.addEventListener("click", () => run(async () => {
      await api("/api/cards/accept", { card_id: card.id });
      await refresh();
      message("Card added to practice.");
    }));
    li.append(document.createTextNode(`${card.question} — ${card.answer}`), evidence, button);
    drafts.append(li);
  }
  if (!drafts.childElementCount) drafts.textContent = "No draft cards yet.";
  renderPractice();
}

function renderPractice() {
  const due = data.cards.filter((card) => card.status === "active" && card.due_at <= Date.now() / 1000);
  $("due-count").textContent = `${due.length} card${due.length === 1 ? "" : "s"} due now.`;
  const card = due[0];
  $("practice").hidden = !card;
  $("feedback").hidden = true;
  $("reveal").hidden = false;
  if (card) {
    $("practice-question").textContent = card.question;
    $("practice-answer").textContent = card.answer;
    $("practice-source").textContent = data.sources.find((source) => source.id === card.source_id)?.title || "Unknown";
    $("practice-quote").textContent = card.quote;
    $("practice").dataset.cardId = card.id;
  }
}

async function run(action) {
  try { await action(); }
  catch (error) { message(error.message); }
}

$("course-form").addEventListener("submit", (event) => {
  event.preventDefault();
  run(async () => {
    await api("/api/courses", { name: $("course-name").value });
    $("course-form").reset();
    await refresh();
    message("Course saved.");
  });
});

$("capture-form").addEventListener("submit", (event) => {
  event.preventDefault();
  run(async () => {
    const content = $("capture-text").value.trim();
    const source = await api("/api/sources", {
      course_id: $("capture-course").value || null,
      title: content.slice(0, 60), content, kind: "capture",
    });
    $("capture-text").value = "";
    selectedSourceId = source.id;
    await refresh();
    message("Capture saved. You can make a card from it now.");
  });
});

$("material-form").addEventListener("submit", (event) => {
  event.preventDefault();
  run(async () => {
    const file = $("material-file").files[0];
    if (!file || !/\.(txt|md)$/i.test(file.name) || file.size > 200_000)
      throw new Error("Choose a .txt or .md file under 200 KB.");
    const source = await api("/api/sources", {
      course_id: $("material-course").value || null,
      title: file.name, content: await file.text(), kind: "material",
    });
    $("material-form").reset();
    selectedSourceId = source.id;
    await refresh();
    message("Material saved locally.");
  });
});

$("delete-source").addEventListener("click", () => run(async () => {
  if (!selectedSourceId || !window.confirm("Delete this source and all its cards?")) return;
  await api("/api/sources/delete", { source_id: selectedSourceId });
  selectedSourceId = null;
  suggestions = [];
  await refresh();
  message("Source and cards deleted.");
}));

$("ai-draft").addEventListener("click", () => run(async () => {
  if (!selectedSourceId) return;
  message("Asking the local model for supported draft cards…");
  const result = await api("/api/cards/draft", { source_id: selectedSourceId });
  suggestions = result.cards;
  render();
  message(`${suggestions.length} supported suggestion${suggestions.length === 1 ? "" : "s"} ready to edit.`);
}));

$("card-form").addEventListener("submit", (event) => {
  event.preventDefault();
  run(async () => {
    if (!selectedSourceId) throw new Error("Choose a source first.");
    await api("/api/cards", {
      source_id: selectedSourceId,
      question: $("question").value,
      answer: $("answer").value,
      quote: $("quote").value,
    });
    $("card-form").reset();
    await refresh();
    message("Draft saved. Review and accept it below.");
  });
});

$("reveal").addEventListener("click", () => {
  $("feedback").hidden = false;
  $("reveal").hidden = true;
});

for (const rating of ["again", "good"]) {
  $(rating).addEventListener("click", () => run(async () => {
    await api("/api/reviews", { card_id: $("practice").dataset.cardId, rating });
    await refresh();
    message("Review saved. Your next due card is ready.");
  }));
}

run(refresh);
