Elder Health Monitoring & SOS Alert System

 Introduction

•Caring for the elderly presents an increasing challenge globally. Due, to the 
emergence of nuclear family setups and longer lifespans numerous older 
adults reside by themselves. Face dangers during urgent situations. 
• This project offers an automated health surveillance system that mimics 
signs and notifies emergency responders when abnormalities are identified. 
• The system is developed using Python and demonstrates how fundamental 
programming concepts can solve real-world problems effectively.


 Real-World Problem

Many elders face difficulties such as: 
• Heart-related medical emergencies 
• High fever or infections 
• Low oxygen levels 
• Sudden falls or unconsciousness 
• No immediate caretaker response 
In most cases, the major issue is delay in medical attention. 
•A simple automated monitoring system helps reduce risk and can potentially 
saves the lifes         
------------------------------------------------------------------------

## 🥅 Objectives

-   Simulate heart rate & temperature\
-   Detect abnormal health conditions\
-   Trigger instant SOS alerts\
-   Demonstrate real-time monitoring\
-   Offer a beginner-friendly Python model

------------------------------------------------------------------------

## 📚 Concepts Used (From Coursework)

-   **Loops** -- continuous monitoring\
-   **Functions** -- modular approach\
-   **Conditional statements** -- threshold detection\
-   **Random module** -- simulated sensor data\
-   **Time module** -- real-time delay

------------------------------------------------------------------------

## 🛠️ Tools & Technologies

-   Python 3.x\
-   Libraries: `random`, `time`\
-   Console-based UI

------------------------------------------------------------------------

## 📝 Problem Definition

Elders need reliable monitoring, but manual supervision isn't
practical.\
This system automates vital checking and alerts during emergencies.

------------------------------------------------------------------------

## 🔍 Requirements Analysis

### ✔ Functional Requirements

-   Generate heart rate\
-   Generate body temperature\
-   Compare values with thresholds\
-   Display output\
-   Trigger SOS alerts

### ✔ Non-Functional Requirements

-   Easy to operate\
-   Readable\
-   Reliable\
-   Low resource usage

------------------------------------------------------------------------

## 🧩 Top-Down Design (Modules)

``` text
generate_vitals()   → Creates random health values  
check_thresholds()  → Evaluates vitals  
display_output()    → Prints current readings  
trigger_sos()       → Displays alert  
main_loop()         → Runs continuous monitoring  
```

------------------------------------------------------------------------

## 🧠 Step-Wise Algorithm

1.  Start\
2.  Generate vitals\
3.  Print values\
4.  Check thresholds\
5.  If abnormal → show SOS alert\
6.  Else → continue\
7.  Wait 1 second\
8.  Repeat

------------------------------------------------------------------------

## 🗂 Flowchart (Mermaid)

``` mermaid
flowchart TD
    A[Start] --> B[Generate Vitals]
    B --> C[Check Thresholds]
    C -->|Abnormal| D[SOS Alert]
    C -->|Normal| E[Continue Monitoring]
    D --> E
    E --> B
```

------------------------------------------------------------------------

## 🧪 Testing & Refinement

-   Tested multiple random ranges\
-   Verified threshold accuracy\
-   Continuous loop stability\
-   Improved warnings & readability

------------------------------------------------------------------------

## ⭐ Features

-   Real-time simulation\
-   Automated health checks\
-   Beginner-friendly\
-   Clean and modular code

------------------------------------------------------------------------

## 🔄 Detailed Workflow

``` mermaid
sequenceDiagram
    participant S as System
    participant V as Vital Generator
    participant C as Checker
    participant A as Alert Module

    S->>V: Generate vitals
    V->>S: Return HR & Temp
    S->>C: Evaluate thresholds
    C-->>S: Normal/Abnormal
    alt Abnormal
        S->>A: Trigger SOS
    end
```

------------------------------------------------------------------------

## 📁 Folder Structure

    project/
    │── project_report/
    │── screenshots/
    │── README.md
    └── src/
        └── main.py

------------------------------------------------------------------------

## ▶️ How to Operate the Program

### **Step 1 --** Download or clone the GitHub repository

### **Step 2 --** Open the project folder

### **Step 3 --** Go to the `src` directory

### **Step 4 --** Run the program:

``` bash
python main.py
```

### **Step 5 --** Observe real-time monitoring

You will see:\
- Heart rate\
- Temperature\
- Status (Normal / Warning / SOS)

### **Step 6 --** SOS Alerts

Displayed when vitals cross thresholds.

### **Step 7 --** Stop the program manually (Ctrl + C)

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Add oxygen monitoring\
-   Integrate real sensors\
-   SMS/Call API\
-   Mobile app\
-   Cloud database

------------------------------------------------------------------------

## 🌍 Real-World Applications

Useful for:\
- Elders living alone\
- Remote patient care\
- Home health IoT\
- Hospitals\
- Wearable devices

------------------------------------------------------------------------

## 🎓 Importance for Students

Students learn:\
- Real-world coding\
- Modular design\
- IoT basics\
- Proper documentation

------------------------------------------------------------------------

## 🏁 Conclusion

The Elder Health Monitoring & SOS Alert System demonstrates how simple
Python concepts can solve meaningful real-world problems.\
By simulating vitals and detecting abnormalities, the system provides
**automated, continuous monitoring** for elders, helping prevent medical
delays.\
This foundational model is highly expandable for IoT health technologies
and real sensor integration.

------------------------------------------------------------------------
