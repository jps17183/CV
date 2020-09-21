# Text Variables
Header = '>>>This resume was generated entirely in Python.\nFor full sourcecode visit: '
Name = 'João P. Roque da Silva'
Title = 'Data Science & Business Analyst'
Contact = 'ADRESS:Rua Professor Vieira de Almeida,\n                nº5 8A, 1600-664 Lisboa\n\nPHONE:  +351 967959317\n\nSKYPE:    jps17183'
ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'BMW Portugal'
ProjectOneDesc = '- Implementation of automatic supply and forecasting replenishment system \n- Excel (VBA automatization for ETL process), Access (SQL), and PowerBI'
ProjectTwoTitle = 'Master\'s Thesis at IPQ'
ProjectTwoDesc = '- International study of statistical models\n   for calculating errors in deviations of standard scales'
WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Polivalor / Consultant'
WorkOneTime = '2018-2018'
WorkOneDesc = '- One year project as Business analyst at BMW Portugal\n- Extract daa from Data warehouse and present insights to costumer\n- Detect and solvin problems\n- Parameterize system of automatic replenishment to each BMW dealer\'s reality\n- Aplication of linear regression models to forecast each BMW dealer\'s needs'
WorkTwoTitle = 'PSA / Procurement'
WorkTwoTime = '2017-2017'
WorkTwoDesc = '- Provisioning aftermarket parts for worldwide dealers\n- Responsable to negotiate with suppliers\n- SAP: Stock analysis and solving logistic problems'
WorkThreeTitle = 'Renault / Manger'
WorkThreeTime = '2014-2016'
WorkThreeDesc = '- Managing workshop activities (i.e. distributing work, customer service etc.)\n- Purchase; Infrastructure maintenance; Solving problems; Price estimation'
WorkFourTitle = 'JAC Products / Quality engineer (trainee)'
WorkFourTime = '2012-2013'
WorkFourDesc = '- Audit and documentation of lean production processes for Lisbon plant\n  (ISO 9001; ISO/TS 16949, ISO 14001)\n- LEAN 6 sigma processes; pneumatics; capability test (RR);\n  gauges instruments and process tests'

EduHeader = 'EDUCATION'
EduOneTitle = 'Master\'s in Philosophy - Univ. Nova de Lisboa'
EduOneTime = '2014-2017'
EduTwoTitle = 'Master\'s in Mechanical Engineer - Univ. Nova de Lisboa'
EduTwoTime = '2004-2011'
SkillsHeader = 'Skills'
SkillsDesc = '- Microsoft Office\n- CAD Tools\n- Fixing Computers\n- Fixing Bikes\n- Self-taught\n- Verbal\n- Writing\n- Pencil Drawing'
AttTitle = 'Atributtes'
AttDesc = '- Machine Thinking\n- Analytic\n- Self-taught\n- Imaginative\n- Curious\n- Logical'
LangTitle = 'Languages'
LangDesc = '- ENGLISH: C1\n- FFRENCH: A2\n- SPANISH: B1'
InfoTitle = 'INFORMATION'
InfoDesc = '- BIRTH DATE: 17/02/1983\n- NATIONALITY: Portuguese'

ProHeader = 'MOTIVATION'
ProDesc = 'My main interest in data science is apply it to social sciences, such as decision\nmaking. The philosophical foundations inherent to the understanding of sociology,\neconomy, anthropology and psychology, combined with mathematical logic is\nusefull for growth hacking. I\'ll further my knowledge in MySQL, Hadoop and R.\nI am objective, critical, intellectually challenging, and autonomous.'

# Setting style for bar graphs
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(Contact, (.685,.895), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02,.83), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04,.79), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02,.760), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04,.720), weight='regular', fontsize=9)
plt.annotate(WorkHeader, (.02,.680), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02,.65), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.63), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.55), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.52), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.5), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.45), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.42), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.40), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04,.365), weight='regular', fontsize=9)
plt.annotate(WorkFourTitle, (.02,.335), weight='bold', fontsize=10)
plt.annotate(WorkFourTime, (.02,.315), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkFourDesc, (.04,.25), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02,.215), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02,.188), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.168), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduTwoTitle, (.02,.14), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02,.12), weight='regular', fontsize=9, alpha=.6)
plt.annotate(ProHeader, (.02,.09), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(ProDesc, (.02,.01), weight='regular', fontsize=9)
plt.annotate(SkillsHeader, (.7,.85), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.70), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(AttTitle, (.7,.66), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(AttDesc, (.7,.545), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(LangTitle, (.7,.50), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(LangDesc, (.7,.44), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(InfoTitle, (.7,.38), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(InfoDesc, (.7,.34), weight='regular', fontsize=10, color='#ffffff')

#add photo
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
photo = mpimg.imread('foto.png')
imagebox = OffsetImage(photo, zoom=0.14)
ab = AnnotationBbox(imagebox, (0.836, 0.175))
ax.add_artist(ab)

plt.savefig('cvds.png', dpi=300, bbox_inches='tight')