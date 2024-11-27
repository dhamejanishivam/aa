from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

class Main:
    def __init__(self, data):
        self.data = data
        self.elements = []

        # Ensure the "resumeFiles" directory exists
        if not os.path.exists("resumeFiles"):
            os.makedirs("resumeFiles")

        # PDF output path
        self.pdf_path = f"resumeFiles/{self.data['name']}_resume.pdf"
        self.doc = SimpleDocTemplate(
            self.pdf_path,
            pagesize=letter,
            leftMargin=40,
            rightMargin=40,
            topMargin=20,
            bottomMargin=30
        )

        # Define styles
        self.styles = getSampleStyleSheet()
        self.define_styles()

        # Create the PDF layout
        self.build_pdf()

    def define_styles(self):
        # Define various text styles
        self.name_style = ParagraphStyle(
            'Name', fontSize=26, fontName="Helvetica-Bold", textColor=colors.HexColor("#2E4053"), alignment=1, spaceAfter=6
        )
        self.title_style = ParagraphStyle(
            'Title', fontSize=14, fontName="Helvetica-Oblique", textColor=colors.HexColor("#555555"), alignment=1, spaceAfter=15
        )
        self.contact_style = ParagraphStyle(
            'Contact', fontSize=10, fontName="Helvetica", textColor=colors.HexColor("#555555"), alignment=1, spaceBefore=10, leading=12
        )
        self.section_heading = ParagraphStyle(
            'SectionHeading', fontSize=12, fontName="Helvetica-Bold", textColor=colors.HexColor("#2E4053"), spaceBefore=20, spaceAfter=12
        )
        self.body_text = ParagraphStyle(
            'Body', fontSize=10, fontName="Helvetica", textColor=colors.HexColor("#333333"), leading=12
        )
        self.subheading_style = ParagraphStyle(
            'Subheading', fontSize=11, fontName="Helvetica-Bold", textColor=colors.HexColor("#333333"), spaceAfter=4
        )
        self.bullet_text = ParagraphStyle(
            'Bullet', fontSize=10, fontName="Helvetica", textColor=colors.HexColor("#2E4053"), leftIndent=15
        )
        self.link_style = ParagraphStyle(
            'Body', parent=self.styles['Heading6'], fontSize=9.8, leading=15, textColor=colors.HexColor("#5555BB"), alignment=0,spaceAfter=0
        )
        self.body_style = ParagraphStyle(
            'Body', parent=self.styles['Normal'], fontSize=9, leading=15, textColor=colors.HexColor("#444444")
        )

    def build_pdf(self):
        # Add content to the PDF
        self.build_header()
        self.build_objective()
        self.build_section("Experience", self.data['work_experience'])
        # self.build_section("Education", self.data['education'])
        self.build_education_section()
        self.build_skills_section()
        # self.build_additional_details_section()
        self.build_projects_section()

        # Build the PDF
        self.doc.build(self.elements)

    def build_header(self):
        # Name and title centered at the top
        self.elements.append(Paragraph(self.data['name'], self.name_style))
        # self.elements.append(Paragraph("Graphic Designer", self.title_style))
        self.elements.append(Spacer(1, 10))  # Add some space before the next section

        # Contact information as centered text
        contact_info = f"{self.data['phone']} | {self.data['email']} | {self.data['location']}"
        self.elements.append(Paragraph(contact_info, self.contact_style))
        self.elements.append(Spacer(1, 20))  # Add some space before the next section

    def build_objective(self):
        # Add objective section with a horizontal line divider
        self.elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2E4053")))
        self.elements.append(Spacer(1, 8))
        self.elements.append(Paragraph("Objective", self.section_heading))
        self.elements.append(Paragraph(self.data['objective'], self.body_text))
        self.elements.append(Spacer(1, 20))

    def build_section(self, title, items):
        # Section title with underline
        self.elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2E4053")))
        self.elements.append(Spacer(1, 8))
        self.elements.append(Paragraph(title, self.section_heading))

        # List experience or education items
        for item in items:
            item_title = f"{item.get('title', item.get('degree'))} - {item.get('company', item.get('institution', ''))}"
            self.elements.append(Paragraph(item_title, self.subheading_style))
            
            # Add duration if present
            if 'duration' in item:
                self.elements.append(Paragraph(item['duration'], ParagraphStyle(
                    'Duration', fontSize=9, fontName="Helvetica-Oblique", textColor=colors.HexColor("#777777")
                )))
            
            # Add description if it exists
            if 'description' in item:
                self.elements.append(Paragraph(item['description'], self.body_text))
            self.elements.append(Spacer(1, 10))

        # Spacer before the next section
        self.elements.append(Spacer(1, 10))

        

    def build_education_section(self):
        # Section: Education
        self.elements.append(Paragraph("EDUCATION", self.section_heading))
        for edu in self.data['education']:
            # Create a table with two columns: one for degree (left) and one for year (right)
            education_row = [
                [Paragraph(f"{edu['degree']}", self.subheading_style), 
                Paragraph(f"{edu['year']}", ParagraphStyle(
                    'edu', fontSize=9, fontName="Helvetica-Oblique", textColor=colors.HexColor("#777777"), alignment=2
                ))]
            ]

            # Define a table for each education entry
            education_table = Table(education_row, colWidths=[460, 70])  # Adjust widths as needed

            # Style the table
            education_table.setStyle(TableStyle([
                ('ALIGN', (1, 0), (1, 0), 'RIGHT'),  # Right align the year in the second column
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Vertically align text to the top
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),  # Padding below the text
            ]))

            # Add the table and institution name below it
            self.elements.append(education_table)
            self.elements.append(Paragraph(edu['institution'], self.body_text))
            self.elements.append(Spacer(1, 9))  # Spacer after each education entry


    def build_skills_section(self):
        # Section: Skills
        self.elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2E4053")))
        self.elements.append(Paragraph("Skills",  self.section_heading))

        # Group skills into rows of 3
        skills = self.data['skills']
        rows = [skills[i:i + 3] for i in range(0, len(skills), 3)]  # Grouping skills into rows of 3

        # Format each skill with a bullet point
        formatted_rows = []
        for row in rows:
            formatted_row = [f"• {skill}" for skill in row]  # Add bullet to each skill
            # Add empty cells if the last row has fewer than 3 skills
            if len(formatted_row) < 3:
                formatted_row += [''] * (3 - len(formatted_row))  # Fill row with empty strings
            formatted_rows.append(formatted_row)

        # Define table with skills and set column widths
        skills_table = Table(formatted_rows, colWidths=[110, 190, 190])  # Adjust column widths if needed

        # Style the table
        skills_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align all cells to the left
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Use Helvetica font
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#333333")),  # Set text color
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Padding below text
        ]))

        # Add the table to the elements
        self.elements.append(skills_table)
        self.elements.append(Spacer(1, 20))  # Spacer after the skills section


    # def build_additional_details_section(self):
    def build_projects_section(self):
        # Additional details section with custom bullets
        self.elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#2E4053")))
        self.elements.append(Spacer(1, 8))
        if len(self.data['projects'])>1:
            self.elements.append(Paragraph("Projects", self.section_heading))
        else:
            self.elements.append(Paragraph("Project", self.section_heading))


        # for interest in self.data['projects']:
        #     self.elements.append(Paragraph(f"• {interest}", self.bullet_text))
        ## self.elements.append(Spacer(1, 15))
        for project in self.data['projects']:
            self.elements.append(Paragraph(f"{project['projectName']}", self.subheading_style))
            self.elements.append(Paragraph(f"""<a target="_blank" href="{project['projectLink']}">{project['projectLink']}</a>""", self.link_style))
            self.elements.append(Paragraph(project['projectDesc'], self.body_style))
        # self.elements.append(Spacer(1, 20))

# Data for the resume

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
        'projectLink':'https://github.com/dhamejanishivam/Heart-Disease-Predictor',
        'projectDesc':'I made a heart disease predictor using Machine Learning which predicts the chances of you having a heart disease, just by entering a few symptomps, '},
        
    ],
    'skills': [
        'JavaScript', 'Python', 'Photography', 'HTML&CSS', 'C Programming',
        'C++ Programming', 'Linux', 'MS-Excel', 'SQL', 
        'Data Structures'
    ],
    'additional_details': [
        "Green Olympiad", "2nd position in Spell Bee Competition",
        "1st position in Best Out of Waste competition"
    ]
}

if __name__ == "__main__":
    resume = Main(data)
    print(f"Resume saved at: {resume.pdf_path}")
