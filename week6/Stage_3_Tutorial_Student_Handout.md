Assignment 2-Case Study

Stage 3 Tutorial Activities

From Requirements to Domain Models

Week 6 | 60 minutes

# Candidate Concepts

| Candidate    | Class?   | Reason                                                                                                                                       |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Patient      | Yes      | Using a class here is useful to easily store and access all information for patients.                                                        |
| Practitioner | Yes      | Using a class here is useful to easily store and access all information for practitioners.                                                   |
| Appointment  | Yes      | Using a class here is useful to create a template for the information needed for appointments and to access and modify that information.     |
| Name         | No       | A name is just a single value and does not need to be a class.                                                                               |
| Clinic       | Yes / No | Does not necessarily need to be a class. However, if the application was to be made for multiple clinics, then a clinic class could be made. |
| Database     | No       | A database stores all the data and does not need to be a class.                                                                              |
| Cancellation | No       | Cancellation would be a function and does not need to be a class. It could also be a value within the appointment class.                     |
| Status       | No       | Status would be a value in the appointment class and not a class itself.                                                                     |

# CRC Cards

## Patient

| Responsibilities                                                                     | Collaborators |
| ------------------------------------------------------------------------------------ | ------------- |
| Stores and can display information about the Patient. E.g. Name, Age, Date of Birth. | Practitioner  |
| Allows patients to update information.                                               | Appointment   |

## Practitioner

| Responsibilities                                                                            | Collaborators |
| ------------------------------------------------------------------------------------------- | ------------- |
| Stores and can display information about the Practitioner. E.g. Name, Age, and Availability | Appointment   |
| Allows the program to know when the Practitioner is available.                              | Patient       |

## Appointment

| Responsibilities                                                     | Collaborators |
| -------------------------------------------------------------------- | ------------- |
| Allows patients and staff to view available and booked appointments. | Patient       |
| Allows staff to change the appointment status                        | Practitioner  |

# Relationship Reasoning

Patient to Appointment: which relationship and why?

The patient to appointment relationship is an association relationship. This is because both are individual classes that don't derive from one another and don't have a shared main class but still have a reference to each other. The appointment class will need a reference to the patient class so that it is clear which patient that appointment is for.

Practitioner to Appointment: what multiplicity?

A practitioner could have multiple appointments assigned to them, but the specific appointment should only have one practitioner assigned to it at a time.

Should Appointment inherit from Patient?

No appointment should not inherit from patient. This is because appointments would store their own unique information and if they needed to access any information from the patient they can make a call from the patient class.

Does Clinic need to own every object?

Under the current scope, I see no reason for the Clinic to own every object. However, if this was to be scaled for use in other clinics then it would make sense to have clinics be given relationship to their patients, practitioners and appointments.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

PatientManager: This function would be useful for the application. This would help with the collection of information for the patient class. This function could also be useful for displaying information of the patient class.

PractitionerManager: This would be a useful function to help manage all the practitioners at the clinic.

AppointmentManager: This would be a useful function for managing all appointment information for the clinic. However, this should be broken down into smaller functions. These functions could include a function for booking appointments, a function for canceling appointments, and a function for changing the appointments status.

ClinicController: This function could be useful if the application will support multiple clinics.

NotificiationManager: If sending notifications to patients is an approved feature then having a system to manage the notifications would be important to the functionality of the program.

ScheduleEngine: A schedule engine would be an important part to help manage the time blocks that practitioners are available for.