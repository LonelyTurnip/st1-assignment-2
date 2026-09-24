class Patient:  
    def __init__(self):
        self._full_name = ""
        self._email = ""
        self._phone_number = ""
        self._patient_id = ""

    def get_full_name(self):
        return self._full_name
    def get_id(self):
        return self._patient_id
    def get_email(self):
        return self._email
    def get_phone_number(self):
        return self._phone_number
    
    def get_details(self):
        return self._full_name, self._patient_id, self._email, self._phone_number
    
    def set_name(self, name: str):
        if not isinstance(name, str):
            print("Name must be a string")
            return
        if not name.strip():
            print("Name can not be blank")
            return
        
        self._full_name = name
    
    def set_email(self, email: str):
        if not isinstance(email, str):
            print("Email must be a string")
            return
        if not email.strip():
            print("Email can not be blank")
            return
        self._email = email

    def set_phone_number(self, phone_number: str):
        if not isinstance(phone_number, str):
            print("Phone number must be a string")
            return
        if not phone_number.strip():
            print("Phone number can not be blank")
            return
        self._phone_number = phone_number
        
    def set_id(self, patient_id:int):
        if not isinstance(patient_id, int):
            print("Patient ID must be an integer")
            return
        if patient_id < 0:
            print("Patient ID must be above 0")
            return
        self._patient_id = patient_id

patient1 = Patient()

patient1.set_name("Steve")
patient1.set_email("Steve@email.com")
patient1.set_id(52)
patient1.set_phone_number("040404040404")

print(patient1.get_details())
    


