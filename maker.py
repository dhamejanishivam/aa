from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
)
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import reportlab



import os

global data
data = {}

class Main():

    def __init__(self,data1) -> None:
        # Create PDF document
        # global data
        global data
        data = data1
        self.data = data
        self.elements = []
        # Ensure that the resumeFiles directory exists
        if not os.path.exists("resumeFiles"):
            os.makedirs("resumeFiles")

        self.pdf_path = f"resumeFiles//{self.data['name']}_resume.pdf"
        self.doc = SimpleDocTemplate(self.pdf_path, pagesize=letter,leftMargin=25,rightMargin=10, topMargin=30, bottomMargin=10)

        # Styles for the resume
        self.styles = getSampleStyleSheet()

        self.runner()

    def runner(self):
        self.stylers()
        self.headingAndCarrer()
        self.workExperience()
        self.education()
        self.projects()
        self.skills()
        self.additional()

        # Build the PDF
        self.doc.build(self.elements)

        return self.pdf_path



    def stylers(self):
        # Styles for the resume
        styles = self.styles
        self.title_style = ParagraphStyle(
            'Title', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor("#008bdc"), alignment=0
        )
        self.contact_style = ParagraphStyle(
            'Contact', parent=styles['Normal'], fontSize=12, textColor=colors.HexColor("#555555"), alignment=0
        )
        self.section_heading = ParagraphStyle(
            'SectionHeading', parent=styles['Heading5'], fontSize=12, textColor=colors.HexColor("#333333"), spaceAfter=10
        )
        self.body_style = ParagraphStyle(
            'Body', parent=styles['Normal'], fontSize=9, leading=15, textColor=colors.HexColor("#444444")
        )



        self.subheading_style = ParagraphStyle(
            'Body', parent=styles['Heading6'], fontSize=9.8, leading=15, textColor=colors.HexColor("#333333"), alignment=0,spaceAfter=0
        )
        self.link_style = ParagraphStyle(
            'Body', parent=styles['Heading6'], fontSize=9.8, leading=15, textColor=colors.HexColor("#5555BB"), alignment=0,spaceAfter=0
        )
        self.line_style = ParagraphStyle(
            'line_style', parent=styles['Normal'], fontSize=12, leading=15, textColor=colors.HexColor("#C7CACB")
        )



    def headingAndCarrer(self):
        # Header (Name and Contact Information)
        self.elements.append(Paragraph(self.data['name'], self.title_style))
        self.elements.append(Paragraph(f"{self.data['email']} | {self.data['phone']} | {self.data['location']}", self.contact_style))
        self.elements.append(Paragraph("____________________________________________________________________________________", self.line_style))
        self.elements.append(Spacer(1, 20))


        
        # Section: Career Objective
        self.elements.append(Paragraph("CAREER OBJECTIVE", self.section_heading))
        self.elements.append(Paragraph(data['objective'], self.body_style))
        self.elements.append(Spacer(1, 13))

    
    def workExpExists(self):
        if len(data["work_experience"])>=1:
            return True
        else:
            return False
    def workExperience(self):
        if not self.workExpExists():
            return None 
        
        
        # Section: Work Experience
        self.elements.append(Paragraph("WORK EXPERIENCE", self.section_heading))
        for job in data['work_experience']:
            self.elements.append(Paragraph(f"{job['title']} • {job['company']} {job['duration']}", self.body_style))
            self.elements.append(Paragraph(job['description'], self.body_style))
            self.elements.append(Spacer(1, 12))
    

    def education(self):
        # Section: Education
        self.elements.append(Paragraph("EDUCATION", self.section_heading))
        for edu in data['education']:
            self.elements.append(Paragraph(f"{edu['degree']} {edu['year']}", self.subheading_style))
            self.elements.append(Paragraph(edu['institution'], self.body_style))
            self.elements.append(Spacer(1, 12))

    def projectExits(self):
        if len(data["projects"])>=1:
            return True
        else:
            return False

    def projects(self):
        if not self.projectExits():
            return None
        
        if len(self.data['projects'])>1:
            self.elements.append(Paragraph("PROJECTS", self.section_heading))
        else:
            self.elements.append(Paragraph("PROJECT", self.section_heading))

        for project in data['projects']:
            self.elements.append(Paragraph(f"{project['projectName']}", self.subheading_style))
            self.elements.append(Paragraph(f"""<a target="_blank" href="{project['projectLink']}">{project['projectLink']}</a>""", self.link_style))
            self.elements.append(Paragraph(project['projectDesc'], self.body_style))
        self.elements.append(Spacer(1, 20))


    def skills(self):
        # Section: Skills
        self.elements.append(Paragraph("SKILLS", self.section_heading))

        # Create rows of skills with 3 skills per row
        skills = data['skills']
        rows = [skills[i:i + 3] for i in range(0, len(skills), 3)]  # Grouping skills into rows of 3
        

        lis = []

        for p in rows:
            temp_lis = []
            for q in p:
                temp_lis.append(f" • {q}") 
            lis.append(temp_lis)
        rows = lis


        
        # Add empty cells if the last row has fewer than 3 skills
        if len(rows[-1]) < 3:
            rows[-1] += [''] * (3 - len(rows[-1]))  # Add empty strings to fill the row



        # Define table with skills and set column widths
        skills_table = Table(rows, colWidths=[190, 190, 190])  # Adjust widths as needed

        # Style the table
        skills_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Center-align all cells
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Use Helvetica font
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#333333")),  # Set text color
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Padding below text
        ]))

        # Add the table to the elements
        self.elements.append(skills_table)
        self.elements.append(Spacer(1, 20))
    

    def additionalExits(self):
        if len(data["additional_details"])>=1:
            return True
        else:
            return False
        
    def additional(self):
        if not self.additionalExits():
            return None
        # Section: Additional Details
        self.elements.append(Paragraph("ACHIEVEMENTS", self.section_heading))
        for detail in data['additional_details']:
            self.elements.append(Paragraph(detail, self.body_style, bulletText='-'))

data = {
    'name': 'Shivam Dhamejani',
    'email': 'dhamejanishivam@gmail.com',
    'phone': '+91 9644971120',
    'location': 'Raipur',
    'objective': (
        "Passionate web developer and programmer skilled in Python, PHP, HTML, CSS, and JavaScript. "
        "Seeking opportunities to apply my expertise in building innovative solutions while continuously "
        "learning and contributing to dynamic projects."
    ),
    'work_experience': [
        {
            'title': 'Web Developer • Internship',
            'company': 'Thought Applied Creation, Raipur',
            'duration': 'Jul 2024 - Aug 2024',
            'description': (
                "Built a responsive website linked to a database using React, HTML, CSS, JavaScript, PHP, "
                "and MySQL."
            ),
        }
    ],
    'education': [
        {'degree': 'B.Tech, Computer Science & Engineering', 'year': '2022 - 2026', 
         'institution': 'Shri Shankaracharya Institute Of Professional Management And Technology'},
        {'degree': 'Senior Secondary (XII), CBSE', 'year': '2022', 'institution': 'Krishna Public School'},
        {'degree': 'Secondary (X), CBSE', 'year': '2020', 'institution': 'Krishna Public School'}
    ],
    'projects': [
        {'projectName':'Heart Disease predictor',
        'projectLink':'youtube.com',
        'projectDesc':'I made a heart disease predictor which predicts the chances of you having a heart disease'},
        {'projectName':'Heart Disease predictor',
        'projectLink':'',
        'projectDesc':'I made a heart disease predictor which predicts the chances of you having a heart disease'},
        
    ],
    'skills': [
        'JavaScript', 'Python', 'Photography', 'HTML&CSS', 'C Programming',
        'C++ Programming', 'Linux', 'MS-Excel', 'Digital Marketing', 'SQL', 
        'Data Structures'
    ],
    'additional_details': [
        "Green Olympiad", "2nd position in Spell Bee Competition",
        "1st position in Best Out of Waste competition"
    ]
}


if __name__ == "__main__":
    a = Main(data1=data)
    print(a)