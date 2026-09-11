SmartCare v0.2 - Requirements Specification Template

# 1\. Problem and Scope

Currently, SmartCare's use of spreadsheets and paper records is believed to be causing major issues with managing patients and their appointments. These issues include duplicate bookings, difficulty finding patient information, inconsistent appointment status, and limited appointment history. In response to this, management wants a small, maintainable patient, practitioner, and appointment system.

Functions that would be useful for this application are the ability to input and retrieve patient information, the ability for patients and admin staff to place appointments, the ability to view and manage practitioner timetables, and the ability for practitioners and clinic staff to view information about the patients.

As described by the brief, the scope of this application will be quite small. An example of an in-scope feature that is not confirmed could be SMS reminder messages for when patients have appointments. An example of a feature that would be out of scope is AI integration to help provide patients further assist treatment.

Some provisional features could include, SMS message capability, facial recognition / pass key to log in, a system to remember their login, the ability to add the appointment booking straight to a Calander app, a way to access sick notes for employers / schools, and personal notes section for practitioners.

# 2\. Stakeholders

| Stakeholder   | Need                                                                                                                                        | Evidence                                                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patients      | The ability to book appointments, review appointment information, and update personal information.                                          | This would be an essential part of the application and most functionality would be built around this.                                                 |
| Practitioners | The ability to change their availability status and view upcoming appointments.                                                             | The practitioners will need a way to be able to know when their appointments are and be able to update the application for when they are unavailable. |
| Admin Staff   | The ability to book appointments, view and manage patient information, update appointment information, and check practitioner availability. | The admin staff would be the biggest user base outside of patients and the ability to do all these functions would tie in with their work.            |
| Clinic Staff  | The ability to view patient information and appointment information.                                                                        | This function would help clinic staff outside of practitioners help assist in the treatment of patients.                                              |

# 3\. Functional Requirements

FR-01: Store patient information.

FR-02: Display patient information

FR-03: Store practitioner information

FR-04: Display practitioner information

FR-05: Display available appointment bookings

FR-06: Place appointment booking

FR-07: Store appointment booking information

FR-08: Display appointment booking information

FR-09: Cancel appointment/s

# 4\. Non-Functional Requirements

NFR-01: The ability to look up patient information is simple.

NFR-02: The process to book an appointment is simple.

NFR-03: The process to cancel an appointment is simple.

NFR-04: Practitioner availability is instantly updated when a change is made.

# 5\. User Stories

US-01: As a Practitioner, I want the ability to change my availability, so that if something happens, I can change my availability status.

US-02: As a nurse, I want the ability to access patient information, so that I can effectively do my job.

US-03: As a new patient, I want to learn about the practitioners available at the clinic, so that I can find the best practitioner for me.

US-04: As a receptionist, I want the ability to manage appointments and information, so that I can help people who visit the clinic.

US-05: As an elderly patient, I want the ability to still call up the clinic, so that I do not need to worry about being confused using new technology.

US-06: As a young parent, I want ability to manage my children's information, so that I can ensure the clinic knows all the required information and so the clinic knows my relationship my child.

# 6\. Acceptance Criteria

GIVEN: A practitioner manages their availability time  
WHEN: they change their availability times  
THEN: the program is updated to reflect those changes

GIVEN a patient booking an appointment  
WHEN they pick an unavailable appointment  
THEN a message tells them the appointment time is unavailable

GIVEN a receptionist updates an appointment  
WHEN the practitioner has changed availability  
THEN the patient is informed of the change in the appointment

# 7\. Assumptions and Open Questions

Assumptions:  
There will be a log in system for patients and practitioners.

Each patient and practitioner would have a personal profile.

Every staff member would access this application. E.g. nurses checking for patient information.

Questions:

What data about patients would need to be stored?

How tech literate would the expected average user be?

Could you provide more details on what you mean by "small" in context to the size of the program?

# 8\. AI Requirements Review Record

| AI suggestion                                               | Evidence?                       | Decision   | Reason                                                   | Verification                                                                               |
| ----------------------------------------------------------- | ------------------------------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| System should allow staff to search for patient information | Yes                             | Accepted   | Staff report difficulty finding information              | Demonstrate that patient information matches recorded information.                         |
| System stores a status for each appointment                 | Yes                             | Accepted   | Staff report inconsistent appointment status information | Create an appointment and verify that it can be stored and updated                         |
| System should prevent duplicate bookings                    | Yes                             | Accepted   | Staff report duplicate bookings                          | Test appointment booking to determine if duplicates are unable to be created               |
| System should provide appointment history                   | Yes                             | Accepted   | Staff report limited appointment history                 | Create a test patient and provide a history of appointments and then retrieve the history. |
| System allows staff to update appointment information       | Assumption needing verification | Unverified | This requirement is not stated in the brief.             | Confirm with client and then test if accepted.                                             |

# 9\. Reflection

The main thing that AI was able to notice was more features that were not outlined in the brief that would help improve the overall quality of the application. My AI agent didn't invent many new functions. but it did provide questions that would help with clarifying information about the needs of the application. No requirements significantly changed after using AI. This could be from the prompt not being investigated further but AI mainly backed up previously existing requirements. Requirements must have evidence to help effectively meet the needs of the clients. Without evidence, requirements become what the software engineer personally thinks the application need. This can lead to the software engineer adding elements that do not actually help the users in practice. This can then lead to development time that was not necessary to complete the task to the clients' specifications.