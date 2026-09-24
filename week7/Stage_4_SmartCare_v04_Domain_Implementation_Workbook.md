SmartCare v0.4 - Domain Implementation Workbook

Week 7 student resource

# 1\. UML-to-Code Trace

| UML element                         | Python element                               | Implemented? | Notes                                                                                                                                                                         |
| ----------------------------------- | -------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get / Set patient full name         | get_full_name()<br><br>set_full_name()       | Yes          | Has basic validation to make sure it is a string and is not an empty value                                                                                                    |
| Get / set patient email             | get_email()<br><br>set_email()               | Yes          | Has basic validation but does not check if it is a valid email.                                                                                                               |
| Get / set patient ID                | get_id()<br><br>set_id()                     | Yes          | Basic validation to ensure it is an integer                                                                                                                                   |
| Get patient details                 | get_details()                                | Yes          | Returns a list that contains all the patient details                                                                                                                          |
| Get / set patient phone number      | get_phone_number()<br><br>set_phone_number() | Yes          | Has basic validation to make sure the phone number is a valid string. Does not validate if the phone number is a valid phone number                                           |
| Get / set practitioner name         | get_name()<br><br>set_name()                 | Yes          | Has basic validation                                                                                                                                                          |
| Get / set practitioner specialty    | get_speciality()<br><br>set_speciality()     | Yes          | Has basic validation                                                                                                                                                          |
| Get / set practitioner id           | get_id()<br><br>set_id()                     | Yes          | Has basic validation                                                                                                                                                          |
| Get / set practitioner availability | get_availability()<br><br>set_availability() | Yes          | Has basic validation. Want to update so that when the set is called it just changes the value. E.g. if the practitioner is unavailable then it will just change to available. |

# 2\. Domain Invariants

| Class        | Invariant / rule                | How protected                          |
| ------------ | ------------------------------- | -------------------------------------- |
| Patient      | Patient has a name              | Private with validation                |
| Practitioner | Practitioner                    | Private with validation                |
| Appointment  | Appointment has a status        | Private with controlled status changes |
| Appointment  | Appointment has a date and time | Private with validation                |
| Appointment  | Appointment has a patient       | Private with a reference set           |
| Appointment  | Appointment has a practitioner  | Private with a reference set           |

# 3\. Composition / Inheritance Decisions

| Relationship               | Decision    | Rationale                                                                                                                                                                             |
| -------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patient - Appointment      | Association | These two classes do not inherit from each other, but appointment is aware of the patient, and a patient does store an appointment history, so they have an association relationship. |
| Practitioner - Appointment | Association | These two classed do not inherit from each other. Each appointment is given a practitioner that they are associated with.                                                             |

# 4\. AI Pair-Programming Record

| AI contribution                                          | Conforms? | Decision | Reason                                                            | Verification                                                                                                                                              |
| -------------------------------------------------------- | --------- | -------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Created AppointmentStatus Enum.                          | Yes       | Accept   | Helps ensure the appointment can only be set to specific statuses | Checked changing status. Currently does not have correct validation. E.g. you can change a cancelled appointment to a completed or scheduled appointment. |
| Added private attributes                                 | Yes       | Accept   | Matches approved UML attributes.                                  | Objects can successfully be created.                                                                                                                      |
| Implemented getter and setter methods for all attributes | Yes       | Accept   | Allows controlled access to appointment data.                     | Values can successfully be and set and retrieved.                                                                                                         |
| Created a method to change the status                    | Yes       | Accept   | Allows the status to be changed to a valid status value.          | Changed the appointment status value to each valid value and tried inputting an invalid value.                                                            |
| Added validation to prevent blank values                 | Yes       | Accept   | Ensures the values on an appointment has required values          | Provided both valid and invalid values.                                                                                                                   |

# 5\. Updated UML

Insert updated UML only if implementation revealed a justified design change. Explain every change.

| Class: Appointment                                                                                                                                                                                                             | Class: Patient                                                                                                                                                                                                                    | Class: Practitioner                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Appointment Date<br><br>Appointment Status<br><br>Booked<br><br>Practitioner Name<br><br>Patient Name                                                                                                                          | Patient Name<br><br>Patient ID<br><br>Patient Date of Birth<br><br>Patient Email<br><br>Patient Phone Number                                                                                                                      | Practitioner Name<br><br>Practitioner ID<br><br>Practitioner Specialty<br><br>Practitioner Availability                                                          |
| get_date()<br><br>get_status()<br><br>get_booked()<br><br>get_practitioner_name()<br><br>get_patient_name()<br><br>set_date()<br><br>set_status()<br><br>set_booked()<br><br>set_practitioner_name()<br><br>set_patient_name() | get_details()<br><br>get_name()<br><br>get_date_of_birth()<br><br>get_email()<br><br>get_phone_number()<br><br>get_id()<br><br>set_name()<br><br>set_date_of_birth()<br><br>set_email()<br><br>set_phone_number()<br><br>set_id() | get_name()<br><br>get_id()<br><br>get_speciality()<br><br>get_availability()<br><br>set_name()<br><br>set_id()<br><br>set_speciality()<br><br>set_availability() |