Elder Health Monitoring & SOS Alert System
Introduction

As the number of elderly people living alone continues to rise—mainly due to nuclear families and longer life expectancy—the risk during medical emergencies also increases. Many seniors are unable to call for help in time, which often leads to serious consequences.

This project presents a simple automated health monitoring system that keeps track of basic vitals and raises an SOS alert whenever abnormal readings are detected. It is built using Python and shows how basic programming concepts can be used to address real-life problems effectively.

Real-World Problem

Elderly individuals commonly face issues such as:

Sudden heart-related complications

High fever due to infections

Low oxygen levels

Unexpected falls or unconsciousness

No caretaker available during emergencies

The biggest risk in all these situations is delay in medical attention.
An automated monitoring system helps reduce this delay and can potentially save lives.

Objectives

Simulate heart rate and temperature readings

Detect abnormal conditions instantly

Trigger SOS alerts when needed

Demonstrate a simple real-time monitoring loop

Provide a beginner-friendly Python implementation

Concepts Used (From Coursework)

Loops — for continuous health monitoring

Functions — to keep the program modular

Conditional statements — to check thresholds

random module — for generating sensor-like data

time module — for adding delay between readings

Tools & Technologies

Python 3.x

Libraries: random, time

Console-based output

Problem Definition

Many elders require round-the-clock monitoring, but manual supervision is not always possible. This system automates the monitoring of basic vitals and alerts whenever something seems off.

Requirements Analysis
Functional Requirements

Generate random heart rate

Generate random body temperature

Compare readings with safe ranges

Display vitals on screen

Trigger an SOS alert if needed

Non-Functional Requirements

Should be simple to operate

Easy to read output

Should run reliably in a loop

Must use minimal system resources

Top-Down Design (Modules)

generate_vitals() – Creates random health data

check_thresholds() – Evaluates whether readings are normal

display_output() – Shows current vitals

trigger_sos() – Prints emergency alert

main_loop() – Runs the monitoring cycle

Step-Wise Algorithm

Start the program

Generate vital readings

Display the values

Check if readings are normal or abnormal

If abnormal → Show SOS alert

If normal → Continue monitoring

Wait for 1 second

Repeat the cycle

Flowchart (Mermaid)
flowchart TD
    A[Start] --> B[Generate Vitals]
    B --> C[Check Thresholds]
    C -->|Abnormal| D[SOS Alert]
    C -->|Normal| E[Continue Monitoring]
    D --> E
    E --> B

Testing & Refinement

Tested with multiple random ranges

Checked threshold conditions for accuracy

Observed stability of continuous loop

Improved warning visibility and print formatting

Features

Real-time vital simulation

Automated checks every second

Beginner-friendly structure

Clean, modular code

Detailed Workflow
sequenceDiagram
    participant S as System
    participant V as Vital Generator
    participant C as Checker
    participant A as Alert Module

    S->>V: Generate vitals
    V->>S: Return heart rate & temperature
    S->>C: Check thresholds
    C-->>S: Normal or Abnormal
    alt Abnormal
        S->>A: Trigger SOS Alert
    end

Folder Structure
project/
│── project_report/
│── screenshots/
│── README.md
└── src/
    └── main.py

How to Operate the Program

Step 1: Download or clone the GitHub repository
Step 2: Open the project folder
Step 3: Navigate to the src directory
Step 4: Run the program:

python main.py


Step 5: Watch the real-time monitoring output, including:

Heart Rate

Temperature

Status (Normal / Warning / SOS)

Step 6: SOS alerts appear automatically when thresholds are crossed.

Step 7: Stop the program manually anytime using:

Ctrl + C

Future Enhancements

Add oxygen saturation monitoring

Integrate real IoT sensors

SMS or call API for real alerts

Android/iOS app

Cloud database for storing health logs

Real-World Applications

This system can be useful for:

Elders living alone

Remote patient monitoring

Home healthcare IoT setups

Hospitals (preliminary screening)

Wearable devices

Importance for Students

By building this project, students learn:

How to apply programming basics to real problems

Modular code design

Simple IoT principles

Writing proper documentation

Building a complete working program

Conclusion

The Elder Health Monitoring & SOS Alert System is a simple yet meaningful project that shows how basic Python programming can contribute to real-world healthcare needs. By simulating vital signs and detecting abnormal conditions, the system provides an automated way to monitor elders and reduce delays in receiving help. This foundational version can easily be expanded into a more advanced IoT-based health monitoring solution with real sensors and communication features.
