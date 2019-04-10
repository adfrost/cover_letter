from fpdf import FPDF
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'Letter')
pdf.set_margins(left = 25, top = 25)	#25.4 mm == 2.54 cm
pdf.set_compression(False)
pdf.set_font('Helvetica', '', 11)	
pdf.add_page()	

dir_path = '/Users/adfrost/Dropbox/cover_letters'	

'''
.split() removes spaces if someone enters one before input 
ex: ' Apple' -> 'Apple'
'''
c = raw_input("Enter the company name:").split()[0]
j = raw_input("Enter the job title:").split()[0]
p = raw_input("Enter product, leave blank for \'their product\':").split()[0]
t = raw_input("Enter team name:").split()[0]

if p == '':
	p = 'their product'

d = {
	'company_name': c,
	'job_title': j,
	'product': p,
	'team_name': t
}

paragraphs = []

paragraphs.append("To the hiring manager in {team_name} at {company_name},")

paragraphs.append("My name is Andrew Frost and I am contacting you to express my\
interest in the {job_title} position at {company_name}. I recently graduated with\
a Bachelor of Science in Computer Science at UC Davis with a minor\
in History. I am very interested in working in a fast paced environment, for\
companies attempting to disrupt industries with new technologies and ideas. I enjoy writing\
code that can simplify or add to the lives of others in meaningful ways,\
and I am excited at the opportunity to do this at {company_name}.")

paragraphs.append("While working towards my bachelor's degree in computer science,\
I took an internship as a full-stack software engineering\
intern for Zenefits during the summer of 2017. During this time, I refined\
my skills as a developer, both in a team and independently. I learned\
many new technologies and concepts, such as database systems, MVC frameworks,\
and unit tests, by creating an internal data-ingestion tool using Python,\
Django ORM, and EmberJS. This tool now saves Zenefits 8000 man-hours per year.")

paragraphs.append("In addition to my internship, I have a created multiple side projects to test\
my skills as a programmer. These side projects show I am motivated, capable of\
learning any new technology or system I put my mind to, and above all, show that\
I enjoy coding. My experience as a Linux System Administrator shows my capacity\
for dealing with others, and my internship at Zenefits show that I can write\
production level code in a collaborative environment. I believe these skills,\
my existing knowledge, and my desire to learn make me perfectly suited to help {company_name}\
add and improve on {product} in any way I can.")

paragraphs.append("I would love the opportunity to discuss the role further, as well as speak \
to my experience and what I can bring to {company_name}.\
I am best reached at andrewfrosttam@gmail.com, or by phone at (415) 235-0076.\n\
\nThank you for your time and consideration, \nAndrew Frost ")

for p in paragraphs:
	pdf.multi_cell(w=0, h=5, align='L', txt=p.format(**d))
	pdf.ln()

file_name = '{company_name} cover letter.pdf'.format(company_name=d['company_name'])
pdf.output(dir_path + file_name, 'F')
