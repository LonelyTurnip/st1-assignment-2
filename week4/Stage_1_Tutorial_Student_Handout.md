Stage 1 Tutorial Activity

\- Why Software Engineering Still Matters

Stage 1 | Introducing Software Technology Case Study with Python and Guided AI use

# Learning goals

- Explain why software engineering is broader than coding.
- Identify stakeholders in a simple software problem.
- Recognise missing requirements.
- Critically evaluate AI-generated feature suggestions.
- Explain why AI output should not automatically be treated as correct.

# Activity 1 - Think-Pair-Share (10 minutes)

If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?

1\. A software engineer will still need the knowledge to understand what is required of the software for the clients use case.

2\. A software engineer will still need the knowledge to read and understand code provided by AI to verify if the provided code completes the tasks or if there are any errors in the logic of the algorithm.

3\. A software engineer will still need the knowledge to create and configure the provided prompt for the AI to create the software.

# Activity 2 - Is This Software Engineering? (10 minutes)

Scenario A: A student writes a 50-line Python calculator.  
Scenario B: A team develops a payroll system used by 5,000 employees.  
Scenario C: An AI assistant generates a simple appointment application from one prompt.

| Scenario | Programming?              | Software engineering?               | Why?                                                                                                                                                                                                                                       |
| -------- | ------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A        | Scenario A is programming |                                     | Scenario is A is more programming than software engineering. This is because software engineering involves designing, testing, and creating the software package while this scenario the student only needs to program a basic calculator. |
| B        |                           | Scenario B is software engineering. | Scenario B is software engineering. This is because the team will need to design, test, and create the payroll system prior to writing the program.                                                                                        |
| C        | Scenario C is programming |                                     | Scenario C is programming. This is because the AI has only been instructed to create program based on a prompt and is not designing the application itself.                                                                                |

# Activity 3 - SmartCare Problem Analysis (20 minutes)

Client statement: SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants new software to improve these processes.

## Task 1 - Identify stakeholders

| Stakeholder  | What do they need?                                                                          |
| ------------ | ------------------------------------------------------------------------------------------- |
| Patients     | The ability to book and cancel appointments at the clinic.                                  |
| Admin Staff  | The ability to manage appointments and information about patients.                          |
| Clinic Staff | The ability to check information regarding appointments and information about the patients. |
| Owners       | A piece of software to help increase the efficiency of the clinic.                          |

## Task 2 - Identify current problems

1\. Information is not kept in a centralized area. This could potentially cause confusion regarding appointment time and information about the clients.

2\. The lack of information being centralized could lead to duplicate bookings being made.

3\. The ability to check if a practitioner is available for an appointment time is inconsistent and practitioners need to manually provide when they are available.

4\. Many small tasks will need to be completed manually instead of having a system in place to handle them. E.g. appointment cancelations and checking if a practitioner is available at the desired time.

## Task 3 - Ask client questions

1\. Does this software need to persistently store the information?

2\. Will this software also store other information about the patients? E.g. When was their last appointment?

3\. Will this software be used by practitioners to indicate when they are available?

4\. Who will be able to do what in this software? E.g. can practitioners cancel appointments? Or will it only be patients?

5\. Will patients have a login system or will they enter their information manually each time?

# Activity 4 - Critique an AI Response (15 minutes)

An AI assistant suggests: appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation.

| Suggestion                   | Client evidence? | In scope? | Decision |
| ---------------------------- | ---------------- | --------- | -------- |
| Appointment management       | Yes              | Yes       | Yes      |
| Facial recognition login     | No               | No        | No       |
| AI diagnosis recommendations | No               | No        | No       |
| Patient search               | Yes              | Yes       | Yes      |
| Online payment               | No               | No        | No       |
| Practitioner schedule view   | Yes              | Yes       | Yes      |
| Insurance processing         | No               | No        | No       |
| Treatment-plan generation    | No               | No        | No       |

# Exit question

Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.

One activity that a software engineer must perform that cannot be safely delegated entirely to an AI is communicating with the clients to understand what is required for the piece of software to complete its desired use case.