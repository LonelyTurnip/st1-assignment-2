class Practitioner:
    _practitioner_id : int = 0
    _name : str = ""
    _speciality : str = ""
    _available : bool = True

    def get_id(self):
        return self._practitioner_id
    def get_name(self):
        return self._name
    def get_speciaility(self):
        return self._speciality
    def get_availability(self):
        return self._available
    
    def set_id(self, practitioner_id):
        if not isinstance(practitioner_id, int):
            print("Practitioner ID must be an integer")
            return
        if practitioner_id < 0:
            print("Practitioner ID must be above 0")
            return
        self._practitioner_id = practitioner_id

    def set_name(self, name):
        if not isinstance(name, str):
            print("Name must be a string")
            return
        if not name.strip():
            print("Name can not be blank")
            return
        
        self._name = name
    
    def set_speciality(self, speciality):
        if not isinstance(speciality, str):
            print("Specialty must be a string")
            return
        if not speciality.strip():
            print("Specialty can not be blank")
            return
        
        self._speciality = speciality 
    
    def set_availability(self, availability):
        if not isinstance(availability, bool):
            print("Availability must be a boolean value")
            return
        self._available = availability
