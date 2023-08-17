from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage (replace with a database in production)
clinic_areas = [
    {"id": 1, "name": "General Clinic", "location": "City Center"},
    {"id": 2, "name": "Specialty Clinic", "location": "Suburb"}
]

doctors = [
    {"id": 1, "name": "Dr. Smith", "specialization": "General Medicine", "clinic_area_id": 1},
    {"id": 2, "name": "Dr. Johnson", "specialization": "Dentistry", "clinic_area_id": 2}
]

appointments = []

# Routes
@app.route('/')
def index():
    return render_template('index.html', clinic_areas=clinic_areas, doctors=doctors)

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    doctor_id = int(request.form['doctor_id'])
    date = request.form['date']
    time = request.form['time']

    selected_doctor = next((doctor for doctor in doctors if doctor['id'] == doctor_id), None)
    if selected_doctor:
        appointments.append({"doctor": selected_doctor, "date": date, "time": time})

    return render_template('appointment_booked.html', appointment={"doctor": selected_doctor, "date": date, "time": time})

@app.route('/appointments')
def view_appointments():
    return render_template('appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

