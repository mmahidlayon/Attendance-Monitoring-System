from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Explicitly allow all origins

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",               # your MySQL username
    password="admin123",   # your MySQL password
    database="shacc_attendance",  # your DB name
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/students')
def get_students():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        return jsonify(students)
    except Exception as e:
        print("Error fetching students:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
