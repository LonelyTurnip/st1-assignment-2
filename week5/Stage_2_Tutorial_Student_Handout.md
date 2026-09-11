Assignment 2 Case Study

Stage 2 Tutorial From Problems to Requirements

Week 5 | 60 minutes

# Learning goals

- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder   | Need                                                                 | Potential conflict                                                                                     |
| ------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Patients      | The ability to manage personal information and appointment bookings. | Patients booking the same appointment at the same time.                                                |
| Practitioners | The ability to manage timetables and view upcoming appointments.     | Patients booking an appointment at the same time as a practitioner changing their availability status. |
| Admin Staff   | The ability to manage patient information and booking appointments.  | Patients and admin staff both interfacing with the same features at the same time.                     |
| Clinic Staff  | The ability to view patient information.                             | N/A                                                                                                    |

# Activity 2 - Functional or Non-Functional?

□ Functional □ Non-functional The system shall allow staff to cancel an appointment -> functional

□ Functional □ Non-functional The system should remain responsive for the course-scale dataset -> non-functional

□ Functional □ Non-functional The system shall retain cancelled appointments -> functional

□ Functional □ Non-functional Core business logic should be independently testable -> non-functional

□ Functional □ Non-functional The system shall search for a patient by ID. -> functional

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem: Describing the system as easy to use is ambiguous. Depending on the target user, what is considered easy to use can be interpreted in different ways.

Clarification question: What does the requirement classify as easy to use? And who would it be defined easy for? E.g. a tech literate individual or someone who struggles with technology use.

Patient search should be fast.

Problem: Unclear what client means by fast.

Clarification question: Do you mean fast as in fast to physically search up a patient or fast in processing the patient search?

The system should securely manage data.

Problem: unclear what data needs to be managed securely Clarification question: What data will be securely managed? And which parties will be able to access what data?

Appointments should normally be easy to cancel.

Problem: Unclear what normally means.

Clarification question: What scenarios would cause the appointment to not easily be canceled?

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion                             | Classification                                | Evidence / reason                                                                                                                                                                                                          |
| ----------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patients receive SMS reminders.           | Assumption requiring validation.              | SMS reminders would be an important feature to help users with both reminding them for their appointments and act as a confirmation for appointments being booked.                                                         |
| Facial recognition login.                 | Assumption requiring validation / Unsupported | This feature could help improve the ease of use for the user but is not necessary for the functionality of the program.                                                                                                    |
| Receptionists create appointments.        | Confirmed                                     | One of the main purposes of this application is to help manage appointments. This feature would be an essential part of the application.                                                                                   |
| Online payment.                           | Unsupported                                   | Typically, at a health clinic, payment is not taken until after the appointment has finished.                                                                                                                              |
| Practitioners view schedules.             | Confirmed                                     | This feature would be an essential part for the functionality of this application. This function would be needed to help practitioners manage their schedules which would then influence when patients can place bookings. |
| AI recommends treatments.                 | Out of scope                                  | The brief claims that this application would just be a small management application. This means that AI recommended treatments would fall out of scope.                                                                    |
| Cancelled appointments remain in history. | Assumption requiring validation.              | Currently unsure if this is a necessary feature for the functionally of the program but can see the potential use of this information.                                                                                     |

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

'AI suggested it' is not sufficient evidence for a requirement. This is because AI would not be directly interfacing directly with the clients and would make suggestions that could potentially be considered out of scope. Another reason would be that currently AI still tends to misinterpret information at times.