
# # Simple python file with basic input and output statements
# # Prints the welcome message
print("Welcome to SmartCare: Community Clinic Book System!")
# # Collects the patient's name
patients_name = input("Please enter your name:")
# # Collects the name of the practitioner and adds 'Dr.' to the front
practitioners_name = "Dr. " + input("Please enter the name of the practitioner you wish to visit:")
# # Collects the date of the appointment 
appointment_date = input("Please enter the date you want to book an appointment for (YYYY-MM-DD):")
# # Collects the time of the appointment
appointment_time = input("Please enter the time you want to book an appointment for (XX:XX AM/PM)")
# # Combines the date and time to create the full appointment booking 
appointment_booking = appointment_date + " " + appointment_time

print(f"Patient: {patients_name} | Practitioner: {practitioners_name} | Time: {appointment_booking}")

# Python program that uses lists to store appointment information

# Creates the list to store appointment information
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if (not patient_name):   
        raise ValueError("Patient name cannot be empty")
    if (not practitioner_name):
        raise ValueError("Practitioner name cannot be empty")
    if (not appointment_time):
        raise ValueError("Appointment time cannot be empty")
    appointment = {
        'patient': patient_name,
        'practitioner': practitioner_name,
        'time': appointment_time,
    }
    appointments.append(appointment)

def display_appointments():
    if(not appointments):
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: Community Clinic Book System!")

# Usual inputs for testing
book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr Jane Roe", "2024-07-20 11:00 AM")

# Unusual inputs for testing
book_appointment("", "Dr Jane Roe", "2024-07-20 11:00 AM")
book_appointment("Bob Johnson", "Dr Jane Roe", "")
book_appointment("", "", "M")

# Function being used in combination with the collected information.
book_appointment(f"{patients_name}", f"{practitioners_name}", f"{appointment_booking}")

display_appointments()