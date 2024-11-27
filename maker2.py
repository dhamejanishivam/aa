from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

class Main:
    def __init__(self, data1):
        self.data = data1
        self.template = r"C:\Users\Admin\Documents\New folder\resumeAi\pythonServer\resumedesigntemplates\htmlDesign1.html"
        self.pdfPath = f"resumeFiles/{self.data['name']}_resume.pdf"
        self.main()

    def main(self):
        # Specify the folder containing your templates
        env = Environment(loader=FileSystemLoader('resumedesigntemplates'))
        
        # Provide the actual template name
        self.template = env.get_template('htmlDesign1.html')

        # Render the template with data
        html_content = self.template.render(self.data)

        # Convert HTML to PDF
        output_pdf = self.pdfPath
        HTML(string=html_content).write_pdf(output_pdf)


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


# Example usage
if __name__ == "__main__":
    a = Main(data1=data)
    print(f"PDF generated: resumeFiles/{data['name']}_resume.pdf")
