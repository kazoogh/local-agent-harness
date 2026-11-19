from pathlib import Path
import argparse,re,html
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer,PageBreak
ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description="Render the reviewed planning Markdown as a PDF.")
parser.add_argument("--input",type=Path,default=ROOT/"Task_and_Milestone_Plan.md")
parser.add_argument("--output-directory",type=Path,default=ROOT)
args=parser.parse_args()
OUT=args.output_directory;OUT.mkdir(parents=True,exist_ok=True)
OWNER="Jason Galanie"
md=args.input.read_text(encoding="utf-8")
NAVY=colors.HexColor('#18334D');PALE=colors.HexColor('#E8EEF4');GRID=colors.HexColor('#D8DEE5')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle('BodyPlan',fontName='Helvetica',fontSize=10,leading=13,spaceAfter=8,allowWidows=0,allowOrphans=0))
styles.add(ParagraphStyle('CellPlan',fontName='Helvetica',fontSize=8.5,leading=10.5))
styles.add(ParagraphStyle('CellHeadPlan',parent=styles['CellPlan'],fontName='Helvetica-Bold',textColor=NAVY))
for key,size,leading in [('Title',20,24),('Heading1',14,18),('Heading2',11,15)]:
 styles[key].fontName='Helvetica-Bold';styles[key].fontSize=size;styles[key].leading=leading;styles[key].textColor=NAVY;styles[key].spaceAfter=9;styles[key].keepWithNext=True
def inline(t):return html.escape(t).replace('&lt;br&gt;','<br/>')
def widths(h):
 if h[0]=='Task ID':return [32,214,48,62,62,86]
 if h[0]=='ID / milestone':return [112,122,90,180]
 if h[0]=='Milestone ID':return [60,152,292]
 if h[0]=='Task ID / same statement':return [260,68,64,60,52]
 if h[0]=='ID / category':return [78,86,250,90]
 if len(h)==3:return [127,190,187]
 return [504/len(h)]*len(h)
def render():
 lines=md.splitlines();story=[];i=0;first=True
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    r=[x.strip() for x in lines[i].strip('|').split('|')]
    if not all(re.fullmatch('-+',x) for x in r):rows.append(r)
    i+=1
   h=rows[0];w=widths(h)
   data=[[Paragraph(inline(c),styles['CellHeadPlan'] if j==0 else styles['CellPlan']) for c in row] for j,row in enumerate(rows)]
   t=Table(data,colWidths=w,repeatRows=1,hAlign='LEFT');t.spaceAfter=8
   t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),PALE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F6F8FA')]),('LINEBELOW',(0,0),(-1,0),.8,colors.HexColor('#9AAABB')),('LINEBELOW',(0,1),(-1,-1),.3,GRID),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]));
   if h[0] in ['Task ID','Task ID / same statement']:t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
   story.append(t);continue
  if line.startswith('### '):story.append(Paragraph(inline(line[4:]),styles['Heading2']));i+=1;continue
  if line.startswith('## '):
   if not first:story.append(PageBreak())
   first=False;story.append(Paragraph(inline(line[3:]),styles['Heading1']));i+=1;continue
  if line.startswith('# '):story.append(Paragraph(inline(line[2:]),styles['Title']));i+=1;continue
  story.append(Paragraph(inline(line),styles['BodyPlan']));i+=1
 def foot(c,doc):
  c.setStrokeColor(GRID);c.line(54,41,558,41);c.setFont('Helvetica',8);c.setFillColor(NAVY);c.drawString(54,28,'Local Study Assistant | Assignments 5 and 6 | Proposed plan');c.drawRightString(558,28,str(doc.page))
 pdf=OUT/'Task_List_and_Project_Plan.pdf'
 SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=42,bottomMargin=55,title='Local Study Assistant - Assignments 5 and 6 (proposed plan)',author=OWNER).build(story,onFirstPage=foot,onLaterPages=foot)
 return pdf

if __name__=="__main__":
 print(render())
