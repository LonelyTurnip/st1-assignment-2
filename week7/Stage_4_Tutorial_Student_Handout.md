Assignment 2 – Case Study

Stage 4 Tutorial Activities

Object-Oriented Design Decisions

Week 7 | 60 minutes

# Activity 1 - Encapsulation Review

| Class        | Protected state / invariant                                                                                                                              | Public operations                                                                                                                       |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Patient      | Name<br><br>Date of Birth<br><br>Email<br><br>Phone Number<br><br>Name can't be blank<br><br>Date of Birth must be in the past<br><br>Patient must exist | Return Details<br><br>Change Appointment status<br><br>Get appointment History                                                          |
| Practitioner | Name<br><br>Availability<br><br>Email<br><br>Name can't be blank<br><br>Availability must be true or false<br><br>Practitioner must exist                | Return details<br><br>Check availability                                                                                                |
| Appointment  | Date<br><br>Status<br><br>Practitioner<br><br>Patient<br><br>Date must exist<br><br>Practitioner must not be blank<br><br>Patient must not be blank      | Check appointment status<br><br>Return appointment details<br><br>Book appointment<br><br>Cancel appointment<br><br>Change practitioner |

# Activity 2 - Composition or Inheritance?

Appointment and Patient -> Composition/association Reason: These two would associate with each other. An appointment would need a patient association to indicate which patient the appointment belongs to. This would not be inheritance because they could exist without each other.

Appointment and Practitioner -> Composition/association Reason: Appointment and practitioner have a composition/association relationship. This is because they don't share an 'is a' relationship so they don't inherit but they do need to be able to communicate with each other.

Doctor and Practitioner (hypothetical) -> Inheritance Reason: This relationship would be inheritance as doctors and Practitioners share similar information. The doctor class could inherit from the practitioner class.

Clinic and Appointment -> □ Composition/association Reason: Clinic and Appointment do not share an 'is a' relationship but clinic does need to know how many appointments it has. This means that clinic and appointment share a Composition/association relationship.

# Activity 3 - Responsibility Allocation

Who decides whether SCHEDULED can become CANCELLED?

- Practitioners and patients should decide whether scheduled can become cancelled. This is because these two classes would be the ones that have something effect the status of the appointment.

Who validates a patient name?

- The patient class would validate the patient's name. It will check if the patient exists within the database. If a patient is found with matching details, then it will return that the patient's name is valid. If no patient is found within the database with those details, it will return invalid.

Should Appointment execute SQL? Why?

- Yes, appointment should execute SQL. This is because once the appointment is created it should tell the database to add a new appointment.

Should the UI decide whether a status transition is legal?

- No, the UI should not decide whether a status transition is legal. This is because UI should just reflect the status of the program. Instead, status transitions should be handle by a backend logic.

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

1. This would create too many responsibilities within the appointment class. Instead the appointment class should just focus on storing data about an appointment and having the ability to change the status of the appointment.
2. The appointment should not inherit from PatientRecord. This is because appointment is not a type of PatientRecord and instead they should have an association relationship.
3. Having SQL inside of the cancel() function should be decoupled from the appointment class. Instead there should be a separate function to handle all the SQL.
4. The status mutation should not be public. Instead there should be functions that allows the status to be changed but it should not be possible for manual assignment of status.
5. A dependency to a NotificationManager will couple the appointment class to NotificationManager. These should be decoupled so that appointment does not become dependent on the logic of the NotificationManager.

# Exit question

Why can code be object-oriented syntactically but still have poor object-oriented design?

Code can be written syntactically through an object-orientated design but still be considered poorly designed. This can happen through incorrect use of object-orientated principles. An example of this would be creating a class that inherits elements from another class where no shared inheritance can be found.