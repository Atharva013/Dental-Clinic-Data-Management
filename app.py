from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import date

app = Flask(__name__)

# Database connection
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clinicDB'
    )

# ---------------------- Index/Home Route ----------------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- PATIENTS ----------------
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        age = request.form['age']
        gender = request.form['gender']
        cursor.execute("INSERT INTO Patients (name, phone, age, gender) VALUES (%s, %s, %s, %s)",
                       (name, phone, age, gender))
        conn.commit()

    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    conn.close()
    return render_template('patients.html', patients=patients)

# ---------------- APPOINTMENTS ----------------
@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT patient_id, name FROM Patients")
    patient_list = cursor.fetchall()

    if request.method == 'POST':
        patient_id = request.form['patient_id']
        appointment_date = request.form['appointment_date']
        treatment_type = request.form['treatment_type']
        doctor_name = request.form['doctor_name']
        status = request.form['status']
        cursor.execute("""
            INSERT INTO Appointments (patient_id, appointment_date, treatment_type, doctor_name, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (patient_id, appointment_date, treatment_type, doctor_name, status))
        conn.commit()

    cursor.execute("""
        SELECT a.*, p.name FROM Appointments a
        JOIN Patients p ON a.patient_id = p.patient_id
        ORDER BY appointment_date DESC
    """)
    appointments = cursor.fetchall()
    conn.close()
    return render_template('appointments.html', appointments=appointments, patient_list=patient_list)

# ---------------- BILLING ----------------
@app.route('/billing', methods=['GET', 'POST'])
def billing():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT patient_id, name FROM Patients")
    patient_list = cursor.fetchall()

    if request.method == 'POST':
        patient_id = request.form['patient_id']
        treatment_type = request.form['treatment_type']
        treatment_date = request.form['treatment_date']
        cost = request.form['cost']
        payment_status = request.form['payment_status']
        cursor.execute("""
            INSERT INTO Billing (patient_id, treatment_type, treatment_date, cost, payment_status)
            VALUES (%s, %s, %s, %s, %s)
        """, (patient_id, treatment_type, treatment_date, cost, payment_status))
        conn.commit()

    cursor.execute("""
        SELECT b.*, p.name FROM Billing b
        JOIN Patients p ON b.patient_id = p.patient_id
        ORDER BY treatment_date DESC
    """)
    billing = cursor.fetchall()
    conn.close()
    return render_template('billing.html', billing=billing, patient_list=patient_list)



if __name__ == '__main__':
    app.run(debug=True)
