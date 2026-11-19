from pathlib import Path
import re,html,argparse
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer,PageBreak
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parent
OWNER="Jason Galanie"
LINKBASE="https://github.com/kazoogh/local-agent-harness/blob/e412a98da498833cc3fe9ff2b5d452d1b85aabff/"
DOC_LABEL="Test Plan";OUTPUT_NAME="Test_Plan.pdf"
NAVY=colors.HexColor('#18334D');PALE=colors.HexColor('#E8EEF4');GRID=colors.HexColor('#D8DEE5')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle('BodyPlan',fontName='Helvetica',fontSize=10,leading=13,spaceAfter=8,allowWidows=0,allowOrphans=0))
styles.add(ParagraphStyle('CellPlan',fontName='Helvetica',fontSize=8.5,leading=10.5))
styles.add(ParagraphStyle('CellHeadPlan',parent=styles['CellPlan'],fontName='Helvetica-Bold',textColor=NAVY))
for key,size,leading in [('Title',20,24),('Heading1',14,18),('Heading2',11,15)]:
 styles[key].fontName='Helvetica-Bold';styles[key].fontSize=size;styles[key].leading=leading;styles[key].textColor=NAVY;styles[key].spaceAfter=9;styles[key].keepWithNext=True
def inline(t):
 pieces=[];pos=0
 for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',t):
  label,path=m.groups();href=LINKBASE+path if path.startswith(('Design_Diagrams/','Planning/')) or path in ['User_Stories.md','Ethics_Statement.md'] else path.replace('.md','.pdf')
  pieces.append(html.escape(t[pos:m.start()]));pieces.append('<link href="'+html.escape(href)+'" color="#18334D">'+html.escape(label)+'</link>');pos=m.end()
 pieces.append(html.escape(t[pos:]));return ''.join(pieces).replace('&lt;br&gt;','<br/>')

def widths(h):
 if h[0]=='ID' and h[1]=='Description':return [42,88,222,112,40]
 if h[0]=='Metric':return [66,195,189,54]
 if h[0]=='Layer':return [70,65,369]
 if h[0]=='Environment':return [80,224,200]
 if h[0]=='Milestone':return [67,239,42,156]
 return [504/len(h)]*len(h)
def render():
 lines=md.splitlines();story=[];i=0;first=True
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line=='<!-- pagebreak -->':story.append(PageBreak());i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    r=[x.strip() for x in lines[i].strip('|').split('|')]
    if not all(re.fullmatch('-+',x) for x in r):rows.append(r)
    i+=1
   h=rows[0];w=widths(h)
   data=[[Paragraph(inline(c),styles['CellHeadPlan'] if j==0 else styles['CellPlan']) for c in row] for j,row in enumerate(rows)]
   t=Table(data,colWidths=w,repeatRows=1,hAlign='LEFT');t.spaceAfter=8
   t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),PALE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F6F8FA')]),('LINEBELOW',(0,0),(-1,0),.8,colors.HexColor('#9AAABB')),('LINEBELOW',(0,1),(-1,-1),.3,GRID),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]));
   if h[0] in ['Task ID','Task ID / same statement']:t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
   story.append(t);continue
  if line.startswith('### '):story.append(Paragraph(inline(line[4:]),styles['Heading2']));i+=1;continue
  if line.startswith('## '):
   if False:story.append(PageBreak())
   first=False;story.append(Paragraph(inline(line[3:]),styles['Heading1']));i+=1;continue
  if line.startswith('# '):story.append(Paragraph(inline(line[2:]),styles['Title']));i+=1;continue
  story.append(Paragraph(inline(line),styles['BodyPlan']));i+=1
 def foot(c,doc):
  c.setStrokeColor(GRID);c.line(54,41,558,41);c.setFont('Helvetica',8);c.setFillColor(NAVY);c.drawString(54,28,'Local Study Assistant | '+DOC_LABEL+' | v1.0 review draft');c.drawRightString(558,28,str(doc.page))
 pdf=OUT/OUTPUT_NAME
 SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=42,bottomMargin=55,title='Local Study Assistant - '+DOC_LABEL,author=OWNER).build(story,onFirstPage=foot,onLaterPages=foot)
 return pdf



if __name__=="__main__":
 parser=argparse.ArgumentParser(description="Render the reviewed test plan.")
 parser.add_argument("--output-directory",type=Path,default=ROOT/"exports")
 args=parser.parse_args();OUT=args.output_directory;OUT.mkdir(parents=True,exist_ok=True)
 md=(REPO/"Test_Plan.md").read_text(encoding="utf-8");print(render())
