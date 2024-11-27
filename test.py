import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="root",
    database="mychatapp"
)
cursor = conn.cursor()

# Insert PDF file into the database
# with open('example.pdf', 'rb') as file:
#     pdf_data = file.read()
# query = "INSERT INTO your_table (id, pdf_file) VALUES (%s, %s)"
# cursor.execute(query, (1, pdf_data))
query = "select * from users"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()
