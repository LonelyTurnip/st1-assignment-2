Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype

# Learning objectives

- Create and run a simple Python file with basic input,output and processing statements
- Use lists, dictionaries and functions to enhance the Python file
- Build a small SmartCare appointment prototype.
- Use AI as a tutor rather than a replacement.
- Compare human-written and AI-generated code.
- Verify AI-generated code through execution and test inputs.
- Document a short AI-use reflection.

# Files to create and commit in GitHub

stage01/  
smartcare_v01.py  
comparison.md  
reflection.md  
ai_usage.md

# Part A - Understand the Problem: AI OFF

SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each appointment records patient name, practitioner name and appointment time.

What data must be stored?

What functions might be useful?

What could go wrong?

What requirements are unclear?

For the SmartCare prototype, the data that must be stored is the patients name, practitioners name, and time of appointment. Functions that might be useful for the prototype are a function to store information about a patient, a function to check what times a practitioner is available, a function to return patient information, a function to book the appointment, and a function to return all information about the appointment. Limitations for the current prototype could be confirming if a practitioner is available, if the patient does not enter their correct information, and if two patients book the same appointment. Currently, it is unclear what kind of error handling needs to be implemented for the moment or if the prototype only needs to fulfill the basic task without worrying about errors.

# Part B - Build a Human-Written Prototype: AI OFF

**#task 1**

```
# Create and run a simple Python file with basic input,output statements
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")
#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file
appointments = []
def book_appointment(patient_name, practitioner_name, appointment_time):
        if not patient_name:
                raise ValueError("Patient name cannot be empty")
        appointment = {
                "patient": patient_name,
                "practitioner": practitioner_name,
                "time": appointment_time
        }
        appointments.append(appointment)
def display_appointments():
        if not appointments:
                print("No appointments recorded.")
                return
        for appointment in appointments:
                print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")
print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()
```

^ Now, run both programs , and identify at least five limitations.

Program Limitations

1. In the book_appointment() function, it only checks for if patient_name is empty. This would allow the user to leave appointment_time and practitioner_name to be empty, and the program will still run.
2. This program does not check if it is receiving the correct inputs. This means that users could enter incorrect information. E.g. provide a date for the practitioner's name.
3. In the programs current iteration, there is no way of checking if both the practitioner is available at the time of the booking or if the appointment time has already been booked.
4. The program has no pre-determined date or time range. This allows users to enter dates or times that have passed or are unavailable. E.g. they can book an appointment for years prior to the current year.
5. The display appointments function returns all appointments and currently has no way of searching for a specific appointment.

# Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot)

Suggested prompt structure:  
Act as a Python tutor.  
I am learning introductory software technology.  
Here is a small appointment-booking function.  
1\. Explain what the code does.  
2\. Identify three limitations.  
3\. Suggest improvements.  
4\. Do not rewrite the whole application.  
5\. Ask me two questions to test my understanding.

# Part D - Generate an Alternative: AI ON

Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI.

# Part E - Compare Human and AI Versions

| Question                     | Human version | AI version |
| ---------------------------- | ------------- | ---------- |
| Easy to understand?          | Yes           | Yes        |
| Runs successfully?           | Yes           | Yes        |
| Uses only required features? | Yes           | Yes        |
| Adds assumptions?            | Yes           | Yes        |
| Handles errors?              | Partially     | Partially  |
| Could I explain it?          | Yes           | Yes        |

# Part F - Verify Behaviour

- Normal appointment
- Blank patient name
- Two appointments for the same practitioner/time
- Strange input such as patient_name=None or appointment_time=None

# Part G - Improve One Thing

Choose exactly one controlled improvement, for example: if not patient_name: raise ValueError("Patient name cannot be empty")

The controlled improved that I chose was to add checks to ensure that both practitioner_name and appointment_time cannot be entered as null.

# Part H - Reflection (150-250 words)

What did you build before using AI?

What did AI help you understand?

Did AI make assumptions?

How did you verify the AI output?

What engineering work remained for you?

Before using AI, I created a basic input system that collects information about the patient and their appointment booking. This was then used with a function to store that information in a list as a dictionary which could be accessed by using a function that would display appointments. This was made using the template provided in this document. AI helped me understand more about what specifically is happening on certain lines of code. For example, AI helped me understand what the ValueError function does. Prior to AI I thought it would just send an error message saying "Patient name cannot be empty" however, AI has taught me that not only does it do that but also stops the function creating and storing the invalid appointment. The assumptions that AI made was how the information was collected. When creating the function, Copilot would just manually input the information instead of creating a system to collect the information. This meant that I still would need to create how the user inputs were collected. AI output was verified by manually providing test cases that would test how the function would respond to missing information.

# Submission checklist \[GitHub Commit\]

- Python file runs.
- Comparison table completed.
- Normal and unusual inputs tested.
- AI assistance documented.
- Reflection completed.
- I can explain my code.