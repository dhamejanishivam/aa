from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os
from flask import render_template


import maker  # Ensure maker.py is in the same directory
import maker1
import maker2
import send_details
# import save_data



import json



dataPassword = 'IamIronMan_3000'


app = Flask(__name__)

# Allow CORS for specific origin or all origins (*)
CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:5500","http://localhost:5500", "https://dhamejanishivam.github.io"]}})

# CORS(app, resources={r"/api/*": {"origins": "*"}})










@app.route('/')
def index():
    return render_template("index.html")


@app.route("/maker/")
def makerfile():
    return render_template("maker/index.html")





# Serve the resumeFiles folder as a static directory
@app.route('/resumeFiles/<path:filename>')
def serve_resume(filename):
    return send_from_directory('resumeFiles', filename)

@app.route('/all')
def all():
    content = f""" <form action="/passwordCheck" method="post">
        <label for="password">Enter Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Submit</button>
    </form>"""
    return content

@app.route('/passwordCheck', methods=['POST'])
def checker():
    password = request.form.get("password")  # Get the password input
    if password==dataPassword:
        heading =  """<style>body{background:black;display:flex;align-items:center;justify-content:center;flex-direction: column;}h1{color:purple;}a{margin: 5px auto;}</style><h1>You are Authorized</h1> <br>"""
        code=''
        for i in os.listdir(r"resumeFiles"):
            heading += f"<a href='/resumeFiles/{i}' style='margin:5px auto'>{i}</a><br>"
        content = heading+code
        return heading
    


@app.route('/getData')
def getData():
    with open('resumeData.json',"r") as f:
        a = f.readlines()
    content = f""" <form action="/submit" method="post">
        <label for="password">Enter Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Submit</button>
    </form>"""
    return content

@app.route("/submit", methods=["POST"])
def submit():
    password = request.form.get("password")  # Get the password input
    if password==dataPassword:
        with open('resumeData.json',"r") as f:
            a = f.readlines()
        return f"<h1>Data : </h1> <br><br> <p>{a}</p>"
    else:
        return '<h1 style="color:red;">Wrong password</h1>'

















def makeResume(data):
    
    templateId = int(str(data['selectedTemplateId']))

    if templateId==1:
        obj = maker.Main(data1=data)

    elif templateId==2:
        obj = maker1.Main(data=data)

    elif templateId==3:
        obj = maker2.Main(data1=data)


    pdf_path = f"resumeFiles\\{data['name']}_resume.pdf"
    pdfName = f"{data['name']}_resume.pdf"
    return pdf_path  # Example path



def save_to_json(data):
    pdf_path = f"resumeFiles\\{data['name']}_resume.pdf"
    # obj = save_data.Main()
    # obj.insert_data(data,pdf_path)
    print("Data saved succesfully to mysql")

    # Define the filename for storing resumes
    # filename = 'resumeData.json'
    
    # # Check if the file exists
    # if os.path.exists(filename):
    #     # Read the existing data
    #     with open(filename, 'r') as f:
    #         try:
    #             # Load existing data
    #             existing_data = json.load(f)
    #         except json.JSONDecodeError:
    #             # If file is empty or has invalid JSON, start with an empty list
    #             existing_data = []
    # else:
    #     # If the file doesn't exist, start with an empty list
    #     existing_data = []

    # # Append the new data to the existing data
    # existing_data.append(data)

    # # Write the updated data back to the JSON file
    # with open(filename, 'w') as f:
    #     json.dump(existing_data, f, indent=4)  # Use indent for pretty printing


    # Sending details via message
    obj = send_details.Main(str(data))


@app.route('/api/resume', methods=['POST'])
def receive_resume():
    data = request.get_json()
    print("\nReceived Resume Data:", data)
    save_to_json(data)
    print("Data is saved successfully in resumesData.json\n")

    try:
        resumePath = makeResume(data)
        print("Sending resume file : ",resumePath)
        return send_file(resumePath, as_attachment=True, download_name=resumePath), 200
        # return "Done", 200
    except Exception as e:
        print("Error generating resume:", e)
        # return jsonify({"error": "Failed to generate resume"}), 500
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



