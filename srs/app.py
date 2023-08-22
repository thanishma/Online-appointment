from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage (replace with a database in production)
clinic_areas = [
    {"id": 1, "name": "General Clinic", "location": "City Center"},
    {"id": 2, "name": "Specialty Clinic", "location": "Suburb"},
    {"id": 3, "name": "Retail Clinic", "location": "Town"}
]

doctors = [
    {"id": 1, "name": "Dr. Smith", "specialization": "General Medicine", "clinic_area_id": 1},
    {"id": 2, "name": "Dr. Johnson", "specialization": "Dentistry", "clinic_area_id": 2},
    {"id": 3, "name": "Dr. Innian", "specialization": "Cardiologist", "clinic_area_id": 3}
]

appointments = []

logged_in = False

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in  
    if request.method == 'POST':
        logged_in = True
        return redirect('/')
    return render_template('login.html')

# Index route
@app.route('/')
def index():
    global logged_in  
    if not logged_in:
        return redirect('/login')
    return render_template('index.html', clinic_areas=clinic_areas, doctors=doctors)

# Book appointment route
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    doctor_id = int(request.form['doctor_id'])
    date = request.form['date']
    time = request.form['time']

    selected_doctor = next((doctor for doctor in doctors if doctor['id'] == doctor_id), None)
    if selected_doctor:
        global appointments
        appointment_id = len(appointments) + 1
        appointments.append({"id": appointment_id, "doctor": selected_doctor, "date": date, "time": time})

    return render_template('appointment_booked.html', appointment={"doctor": selected_doctor, "date": date, "time": time})

# Appointments route
@app.route('/appointments')
def view_appointments():
    return render_template('appointments.html', appointments=appointments)

# Cancel appointment route
@app.route('/cancel_appointment/<int:appointment_id>', methods=['POST'])
def cancel_appointment(appointment_id):
    # Find the appointment by its ID
    appointment_to_cancel = next((appointment for appointment in appointments if appointment['id'] == appointment_id), None)

    if appointment_to_cancel:
        # Remove the appointment from the list
        appointments.remove(appointment_to_cancel)
        message = "Appointment deleted successfully."
    else:
        message = "Appointment not found."

    return render_template('cancel_appointment_result.html', message=message)

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Your signup logic here
        # Redirect to login page after successful signup
        return redirect(url_for('login'))  # Redirect to login page after signup
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
