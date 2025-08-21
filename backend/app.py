from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# --------------------------
# Database connection
# --------------------------
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",            # your MySQL username
        password="admin123",
        database="shacc_attendance",
        cursorclass=pymysql.cursors.DictCursor
    )

# --------------------------
# Home route
# --------------------------
@app.route('/')
def home():
    return "SHACC Attendance System Backend is running!"

# --------------------------
# Students endpoints
# --------------------------
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students)

# --------------------------
# Attendance endpoints
# --------------------------
@app.route('/attendance/<int:student_id>', methods=['GET'])
def get_attendance(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance WHERE student_id=%s", (student_id,))
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(records)

@app.route('/attendance', methods=['POST'])
def add_attendance():
    data = request.get_json()
    student_id = data.get('student_id')
    
    if not student_id:
        return jsonify({"error": "student_id is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id) VALUES (%s)", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": f"Attendance added for student_id {student_id}"}), 201

# --------------------------
# Run server
# --------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
