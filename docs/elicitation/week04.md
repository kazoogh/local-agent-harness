# Week 04 elicitation notes

I am keeping these notes as the evidence behind `User_Stories.md`. They summarize what I learned and are not interview transcripts.

## Technique 1: student interviews I conducted

| Participant | Known context | Reported information | Limits |
| --- | --- | --- | --- |
| Kevin Chu | Fellow student | He was one of the two students I spoke with about the gap between receiving course material and getting useful practice from it. | I summarize the shared themes below rather than assigning a specific comment to Kevin. |
| Callie Galanie | My sister and a first-year college student | I included her perspective because a new college student also has to learn from slides and textbooks outside class. | I summarize the shared themes below rather than assigning a specific comment to Callie. |

**Shared themes I heard:** Professors may provide slides or textbooks and expect students to learn independently, while practice using that knowledge is harder to obtain. Kevin and Callie wanted flashcards, practice questions, and help turning course material into a useful guide. I take the idea of a "perfect" study guide as an aspiration, not a promise I can guarantee.

**Follow-up questions I would ask both students:** What materials do you receive now? How do you decide what to study? What do you currently do when slides do not include practice questions? What takes the most time? How do you check that a generated answer is correct? When would you prefer a local model over an online service?

## Technique 2: competitive review

I reviewed published product documentation on 2026-09-28:

- [Quizlet: Studying with Study Guides](https://help.quizlet.com/hc/en-au/articles/18312306436365-Studying-with-Study-Guides) describes uploading or pasting material to create an outline and flashcards, with editing available. This means upload-to-guide by itself is not a distinguishing requirement.
- [Quizlet: Smart Assist](https://help.quizlet.com/hc/en-ca/articles/39606772122509-Creating-study-sets-with-Smart-Assist) describes drafting flashcards from notes or uploads and editing them before publication. Human review is an established workflow worth retaining.
- [Anki manual: Importing](https://docs.ankiweb.net/importing/intro.html) documents text-file and packaged-deck import. Portable study data matters because students may already use another review tool.

**What this means for my design:** Uploading notes to generate flashcards is already available elsewhere. I want to test whether a downloadable, locally run system with practice content traceable to a student's selected material offers a useful difference. This is my product hypothesis, not something I am attributing to the interviews.

I am also considering an interactive lecture companion. Since the student can upload the professor's slides, class notes can focus on extra explanations the professor says instead of copying slide text. The assistant could keep those rough notes beside the slides, help organize them, and ask a follow-up question. It should label slide-backed details separately from what the student actually wrote; it cannot know everything the professor said. This is my design idea prompted by the broader learning problem. I did not record Kevin or Callie requesting this exact in-class flow.

## My maintainer constraints

I want the app to be downloadable and open source, and I want students to be able to run an Ollama model locally. I do not want the app to require a ChatGPT subscription or a hosted API key that creates a bill for me or for students. I am also the person currently expected to deploy and support the app, so I include these as secondary-stakeholder constraints. This is my own design input, not an outside interview.

## Stakeholder gap and next contacts

My interviews with Kevin and Callie cover primary stakeholders, and I have documented my own deployment and support constraints as the maintainer. I still need to ask a student who uses a screen reader or keyboard-only navigation to try the proposed recall flow and identify barriers. Until I do that, US-04 remains a hypothesis. I would also like to ask an instructor or teaching assistant about source fidelity and course policy, although I did not make that role one of the five submitted stories.
