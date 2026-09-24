from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(self):
        self._date_time = ""
        self._patient_name = ""
        self._practitioner_name = ""
        self._appointment_status = AppointmentStatus.SCHEDULED
        self._booked = False

    # Date and Time
    def get_date_time(self):
        return self._date_time

    def set_date_time(self, date_time):
        if not isinstance(date_time, str) or not date_time.strip():
            print("Date and time cannot be blank")
            return

        self._date_time = date_time

    # Patient Name
    def get_patient_name(self):
        return self._patient_name

    def set_patient_name(self, patient_name):
        if not isinstance(patient_name, str) or not patient_name.strip():
            print("Patient name cannot be blank")
            return

        self._patient_name = patient_name

    # Practitioner Name
    def get_practitioner_name(self):
        return self._practitioner_name

    def set_practitioner_name(self, practitioner_name):
        if not isinstance(practitioner_name, str) or not practitioner_name.strip():
            print("Practitioner name cannot be blank")
            return

        self._practitioner_name = practitioner_name

    # Appointment Status
    def get_appointment_status(self):
        return self._appointment_status

    def set_appointment_status(self, status):
        if not isinstance(status, AppointmentStatus):
            print("Invalid appointment status")
            return

        self._appointment_status = status

    # Booked
    def get_booked(self):
        return self._booked

    def set_booked(self, booked):
        if not isinstance(booked, bool):
            print("Booked must be True or False")
            return

        self._booked = booked

    # Change Status
    def change_status(self, status):
        try:
            if isinstance(status, AppointmentStatus):
                self._appointment_status = status

            elif isinstance(status, str):
                self._appointment_status = AppointmentStatus[status.upper()]

            else:
                raise ValueError

        except (KeyError, ValueError):
            print("Invalid appointment status. Valid options are:")
            for valid_status in AppointmentStatus:
                print(f"- {valid_status.value}")




# Test cases

#Appointment 1 - Valid input
appointment1 = Appointment()
appointment1.set_date_time("12/07/2027 10:00")
appointment1.set_practitioner_name("Dr House")
appointment1.set_patient_name("Adam Smith")
appointment1.set_booked(True)
appointment1.change_status("scheduled")

print(f"Patient Name: {appointment1.get_patient_name()}, Practitioner Name: {appointment1.get_practitioner_name()}, Date: {appointment1.get_date_time()}, Status: {appointment1.get_appointment_status()}, Booked: {appointment1.get_booked()} ")

#Appointment 2 - Invalid input
appointment2 = Appointment()
appointment2.set_date_time("18/07/2027 10:00")
appointment2.set_practitioner_name("Dr Stevenson")
appointment2.set_patient_name("Rick Rick")
appointment2.set_booked(True)
appointment2.change_status("scheduled")

print(f"Patient Name: {appointment2.get_patient_name()}, Practitioner Name: {appointment2.get_practitioner_name()}, Date: {appointment2.get_date_time()}, Status: {appointment2.get_appointment_status()}, Booked: {appointment2.get_booked()} ")

appointment2.change_status("No Show")

print(f"Patient Name: {appointment2.get_patient_name()}, Practitioner Name: {appointment2.get_practitioner_name()}, Date: {appointment2.get_date_time()}, Status: {appointment2.get_appointment_status()}, Booked: {appointment2.get_booked()} ")

#Appointment 3 - Cancel a scheduled appointment
appointment3 = Appointment()
appointment3.set_date_time("9/07/2027 15:00")
appointment3.set_practitioner_name("Dr Mansion")
appointment3.set_patient_name("Paul Allen")
appointment3.set_booked(True)
appointment3.change_status("scheduled")

print(f"Patient Name: {appointment3.get_patient_name()}, Practitioner Name: {appointment3.get_practitioner_name()}, Date: {appointment3.get_date_time()}, Status: {appointment3.get_appointment_status()}, Booked: {appointment3.get_booked()} ")

appointment3.change_status("cancelled")

print(f"Patient Name: {appointment3.get_patient_name()}, Practitioner Name: {appointment3.get_practitioner_name()}, Date: {appointment3.get_date_time()}, Status: {appointment3.get_appointment_status()}, Booked: {appointment3.get_booked()} ")

#Appointment 4 - Illegal repeated transition
appointment4 = Appointment()
appointment4.set_date_time("10/02/2027 12:00")
appointment4.set_practitioner_name("Dr Creator")
appointment4.set_patient_name("Tyler, The")
appointment4.set_booked(True)
appointment4.change_status("scheduled")

print(f"Patient Name: {appointment4.get_patient_name()}, Practitioner Name: {appointment4.get_practitioner_name()}, Date: {appointment4.get_date_time()}, Status: {appointment4.get_appointment_status()}, Booked: {appointment4.get_booked()} ")

appointment4.change_status("cancelled")

print(f"Patient Name: {appointment4.get_patient_name()}, Practitioner Name: {appointment4.get_practitioner_name()}, Date: {appointment4.get_date_time()}, Status: {appointment4.get_appointment_status()}, Booked: {appointment4.get_booked()} ")

appointment4.change_status("completed")

print(f"Patient Name: {appointment4.get_patient_name()}, Practitioner Name: {appointment4.get_practitioner_name()}, Date: {appointment4.get_date_time()}, Status: {appointment4.get_appointment_status()}, Booked: {appointment4.get_booked()} ")