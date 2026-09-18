class Patient:
    def __init__(self, first_name, last_name, date_of_birth, age, last_appointment, next_appointment, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.last_appointment = last_appointment
        self.next_appointment = next_appointment
        self.email = email
        self.phone_number = phone_number

    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def set_age(self, age):
        self.age = age
    def set_last_appointment(self, last_appointment):
        self.last_appointment = last_appointment
    def set_next_appointment(self, next_appointment):
        self.next_appointment = next_appointment
    def set_email(self, email):
        self.email = email
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_age(self):
        return self.age
    def get_last_appointment(self):
        return self.last_appointment
    def get_next_appointment(self):
        return self.next_appointment
    def get_phone_number(self):
        return self.phone_number
    def get_email(self):
        return self.email
        


class Practitioner: 
    def __init__(self, first_name, last_name, age, available):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.available = available

    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_age(self, age):
        self.age = age
    def set_available(self, available):
        self.available = available
    
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_age(self):
        return self.age
    def get_available(self):
        return self.available


class Appointment:
    def __init__(self, appointment_date, appointment_time, patient_name, practitioner_name, appointment_status, booked):
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.patient_name = patient_name
        self.practitioner_name = practitioner_name
        self.appointment_status = appointment_status
        self.booked = booked 
    
    def set_appointment_date(self, appointment_date):
        self.appointment_date = appointment_date
    def set_appointment_time(self, appointment_time):
        self.appointment_time = appointment_time
    def set_patient_name(self, patient_name):
        self.patient_name = patient_name
    def set_practitioner_name(self, practitoner_name):
        self.practitioner_name = practitoner_name
    def set_appointment_status(self, appointment_status):
        self.appointment_status = appointment_status
    def set_booked(self, booked):
        self.booked = booked
    
    def get_appointment_date(self):
        return self.appointment_date
    def get_appointment_time(self):
        return self.appointment_time
    def get_patient_name(self):
        return self.patient_name
    def get_practitioner_name(self):
        return self.practitioner_name
    def get_appointment_status(self):
        return self.appointment_status
    def get_booked(self):
        return self.booked
    
