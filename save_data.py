import mysql.connector
from mysql.connector import Error



class Main:
    def __init__(self):
        """
        Initialize connection details
        :param host: MySQL server hostname
        :param user: MySQL username
        :param password: MySQL password
        :param database: MySQL database name
        """
        # self.host="localhost",
        # self.user="root",
        # self.database="resumedata"
        # self.password="",
        # self.connect_to_database()

    def connect_to_database(self):
        """
        Establish a connection to the database
        :return: connection object or None if failed
        """
        try:
            connection = mysql.connector.connect(
                user="root",
                database="resumedata",
                password="",
            )
            if connection.is_connected():
                print("Successfully connected to the database")
                return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def insert_data(self, data, pdfpath):
        """
        Insert user data into MySQL database
        :param data: Dictionary containing user data
        :param pdfpath: Path to the user's PDF resume
        """
        # Connect to the database
        connection = self.connect_to_database()
        if not connection:
            return "Failed to connect to database"

        cursor = connection.cursor()

        # Insert user data into Users table
        insert_user_query = """
        INSERT INTO Users (name, phone, location, objective, pdfpath)
        VALUES (%s, %s, %s, %s, %s);
        """
        user_data = (
            data['name'], 
            data['phone'], 
            data['location'], 
            data['objective'], 
            pdfpath
        )

        try:
            cursor.execute(insert_user_query, user_data)
            connection.commit()
            print("User data inserted successfully.")
        except Error as e:
            print(f"Error inserting user data: {e}")
            connection.rollback()

        # Fetch the last inserted user ID
        user_id = cursor.lastrowid

        # Insert work experience
        for work in data['work_experience']:
            insert_work_query = """
            INSERT INTO WorkExperience (userid, title, company, duration, description)
            VALUES (%s, %s, %s, %s, %s);
            """
            work_data = (
                user_id,
                work['title'],
                work['company'],
                work['duration'],
                work['description']
            )
            try:
                cursor.execute(insert_work_query, work_data)
            except Error as e:
                print(f"Error inserting work experience: {e}")

        # Insert education
        for edu in data['education']:
            insert_edu_query = """
            INSERT INTO Education (userid, degree, year, institution)
            VALUES (%s, %s, %s, %s);
            """
            edu_data = (
                user_id,
                edu['degree'],
                edu['year'],
                edu['institution']
            )
            try:
                cursor.execute(insert_edu_query, edu_data)
            except Error as e:
                print(f"Error inserting education data: {e}")

        # Insert projects
        for project in data['projects']:
            insert_project_query = """
            INSERT INTO Projects (userid, projectName, projectLink, projectDesc)
            VALUES (%s, %s, %s, %s);
            """
            project_data = (
                user_id,
                project['projectName'],
                project['projectLink'],
                project['projectDesc']
            )
            try:
                cursor.execute(insert_project_query, project_data)
            except Error as e:
                print(f"Error inserting project data: {e}")

        # Insert skills
        for skill in data['skills']:
            insert_skill_query = """
            INSERT INTO Skills (userid, skill)
            VALUES (%s, %s);
            """
            skill_data = (user_id, skill)
            try:
                cursor.execute(insert_skill_query, skill_data)
            except Error as e:
                print(f"Error inserting skill data: {e}")

        # Insert additional details
        for detail in data['additional_details']:
            insert_detail_query = """
            INSERT INTO AdditionalDetails (userid, detail)
            VALUES (%s, %s);
            """
            detail_data = (user_id, detail)
            try:
                cursor.execute(insert_detail_query, detail_data)
            except Error as e:
                print(f"Error inserting additional details: {e}")

        # Commit changes and close connection
        connection.commit()
        cursor.close()
        connection.close()
        print("Data insertion complete.")

# Example usage of the Main class
if __name__ == "__main__":
    # Initialize the class with MySQL credentials
    main = Main()

    # Example data to insert (ensure to add valid PDF path)
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
    data = {
        'name': 'Shivam Dhamejani2',
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
                'title': '',
                'company': '',
                'duration': '',
                'description': (""),
            }
        ],
        'education': [
            {'degree': 'B.Tech, Computer Science & Engineering', 'year': '2022 - 2026', 
             'institution': 'Shri Shankaracharya Institute Of Professional Management And Technology'},
            {'degree': 'Senior Secondary (XII), CBSE', 'year': '2022', 'institution': 'Krishna Public School'},
            {'degree': 'Secondary (X), CBSE', 'year': '2020', 'institution': 'Krishna Public School'}
        ],
        'projects': [
            {'projectName':'',
            'projectLink':'',
            'projectDesc':''},
            
        ],
        'skills': [
            'JavaScript', 'Python', 'Photography', 'HTML&CSS', 'C Programming',
            'C++ Programming', 'Linux', 'MS-Excel', 'Digital Marketing', 'SQL', 
            'Data Structures'
        ],
        'additional_details': [
            ""
        ]
    }

    pdfpath = '/path/to/pdf_resume.pdf'  # Replace with actual PDF path

    # Insert data
    main.insert_data(data, pdfpath)
