// Adjust if backend is running on another device
const API_BASE = "http://127.0.0.1:5000";

async function loadStudents() {
  try {
    let res = await fetch(`${API_BASE}/students`);
    let students = await res.json();

    let tableBody = document.querySelector("#studentsTable tbody");
    tableBody.innerHTML = "";

    students.forEach(student => {
      let row = `
        <tr>
          <td>${student.id}</td>
          <td>${student.name}</td>
          <td>${student.rank}</td>
          <td>
            <button class="btn btn-sm btn-primary" onclick="markAttendance(${student.id})">Mark Attendance</button>
          </td>
        </tr>
      `;
      tableBody.innerHTML += row;
    });
  } catch (err) {
    console.error("Error loading students:", err);
  }
}

async function markAttendance(studentId) {
  try {
    await fetch(`${API_BASE}/attendance`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ student_id: studentId })
    });
    alert("Attendance marked for student " + studentId);
  } catch (err) {
    console.error("Error marking attendance:", err);
  }
}

// Load students on page load
window.onload = loadStudents;
