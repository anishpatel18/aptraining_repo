from flask import Flask, jsonify, request
import json
import mysql.connector

app = Flask(__name__)

# Establish a global connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="flaskapptable"
)

#### Python MySQL Create Table ####
@app.route("/create_table")
def create_table():
    cursor = mydb.cursor()
    create_table1 = '''
        CREATE TABLE IF NOT EXISTS Flask_App_Table (
            Username VARCHAR(20),
            Password VARCHAR(20),
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Email_Address VARCHAR(50),
            First_Name VARCHAR(20),
            Last_Name VARCHAR(20),
            Age INT,
            House_Address VARCHAR(100),
            State VARCHAR(20),
            City VARCHAR(20),
            Zip_Code VARCHAR(10),
            Country VARCHAR(50)
        )
    '''
    cursor.execute(create_table1)
    mydb.commit()
    cursor.close()
    return "Successful", 200

#### Python MySQL Insert Into Table ####
@app.route("/insert_table", methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        data = request.json
        Insert_Into_Table = [
            'Username', 'Password', 'ID', 'Email_Address', 'First_Name', 
            'Last_Name', 'Age', 'House_Address', 'State', 'City', 'Zip_Code', 'Country'
        ]
        for insertt in Insert_Into_Table:
            print(f"{insertt}: {data.get(insertt)}")

        print(request.method)
        print(request.headers)
        return jsonify({'status': "Insert Table Success"})
    else:
        return jsonify({'status': "Insert Table Success"})
    

@app.route("/")
def entry():
    return "<p>Welcome to Flask App</p>"

@app.route("/home")
def home():
    data = {
        'Username': 'anishpatel',
        'Password': 'anishpatel1000',
        'ID': 1,
        'Email Address': 'anishpatel@atlanta.com',
        'First Name': 'Anish',
        'Last Name': 'Patel',
        'Age': 24,
        'House Address': '1234 Welcome to Flask App St',
        'State': 'GA',
        'City': 'Atlanta',
        'Zip Code': '12345',
        'Country': 'United States of America'
    }
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
