# Code provided by Microsoft Copilot

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        print("Patient name cannot be empty.")
        return

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

    print("Appointment booked successfully.")

# Input examples provided by Microsoft Copilot 
book_appointment("Alice", "Dr Smith", "10:00")
book_appointment("Bob", "Dr Jones", "11:00")

# Unusual inputs for testing 
book_appointment("Bob", "Dr Jones", "11:00")
book_appointment("11:00", "", "Dan")
book_appointment("", "", "")

print(appointments)