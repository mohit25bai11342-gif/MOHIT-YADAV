#here we importing diffrent modules 

import time
import random
import csv#module for csv file which store our data
import os
import sys
from datetime import datetime


LOG_TO_CSV = True
CSV_FILENAME = "vitals_log.csv"

SAMPLE_INTERVAL = 2.0 

THRESHOLDS = {# these are values of normal persons and use to compare with readings and manual data
    "heart_rate": {
        "normal_min": 60,
        "normal_max": 100,
        "warning_max": 120,
        "critical_low": 40,
        "critical_high": 120,
    },
    "temperature_c": {
        "normal_min": 36.1,
        "normal_max": 37.2,
        "warning_max": 38.9,
        "critical_high": 39.0,
    },
    "spo2": {
        "normal_min": 94,
        "warning_min": 90,
        "critical_min": 90,
    },
}

EMERGENCY_CONTACT = {# here these things are related to your person of caring
    "ambulance_number": "102",
    "caregiver_name": "Family",
    "caregiver_number": "9999999999", #phone number of family memebers or a person eho take care of yours
}


def ensure_csv_header(path):# it will automatic take the readings 
    if not LOG_TO_CSV:
        return
    if not os.path.exists(path):
        with open(path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "heart_rate_bpm",
                "temperature_c",
                "spo2_percent",
                "status",
                "note"
            ])

def log_reading(path, hr, temp_c, spo2, status, note=""):
    if not LOG_TO_CSV:
        return
    with open(path, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            hr if hr is not None else "",
            f"{temp_c:.1f}" if temp_c is not None else "",
            spo2 if spo2 is not None else "",
            status,
            note,
        ])


def simulate_vitals(mode="normal"): #type of modes used in device
    if mode == "normal":# normal mode when readings are normal
        hr = random.randint(65, 85)
        temp = round(random.uniform(36.4, 36.9), 1)
        spo2 = random.randint(95, 99)

    elif mode == "random":
        hr = random.randint(50, 140)
        temp = round(random.uniform(35.5, 40.5), 1)
        spo2 = random.randint(85, 99)

    elif mode == "danger":# when readings are above from normal readings
        hr = random.choice([random.randint(121, 160), random.randint(20, 39)])
        temp = round(random.uniform(39.0, 41.0), 1)
        spo2 = random.randint(80, 89)

    elif mode == "edge":
        hr = random.choice([100, 120, 40])
        temp = random.choice([37.3, 38.9, 39.0])
        spo2 = random.choice([93, 90, 89])

    else:
        hr = random.randint(30, 160)
        temp = round(random.uniform(34.0, 41.5), 1)
        spo2 = random.randint(70, 100)

    return hr, temp, spo2


def check_vitals(hr, temp_c, spo2):# here comparing with thresholds values
    notes = []
    status = "Normal"

    
    thr = THRESHOLDS["heart_rate"]# comparing heart rate
    if hr is not None:
        if hr < thr["critical_low"] or hr > thr["critical_high"]:
            status = "Critical"
            notes.append(f"HR critical ({hr} bpm)")
        elif hr > thr["warning_max"]:
            status = "Warning"
            notes.append(f"HR high ({hr} bpm)")

    
    tthr = THRESHOLDS["temperature_c"]# comparing temrature
    if temp_c is not None:
        if temp_c >= tthr["critical_high"]:
            status = "Critical"
            notes.append(f"Temp critical ({temp_c}°C)")
        elif temp_c > tthr["warning_max"]:
            status = "Warning"
            notes.append(f"Temp high ({temp_c}°C)")

    
    sthr = THRESHOLDS["spo2"]# comparing spo2
    if spo2 is not None:
        if spo2 < sthr["critical_min"]:
            status = "Critical"
            notes.append(f"SpO2 critical ({spo2}%)")
        elif spo2 < sthr["warning_min"]:
            status = "Warning"
            notes.append(f"SpO2 low ({spo2}%)")

    note_str = "; ".join(notes) if notes else "All vitals within normal range"
    return status, note_str


def trigger_sos(hr, temp_c, spo2, note):# structure to how sos will work like calling ambulance, sos message for family memebers
    print("\n" + "!"*60)
    print(" CRITICAL ALERT - SOS TRIGGERED ")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Detected critical vitals -> HR: {hr} bpm, Temp: {temp_c}°C, SpO2: {spo2}%")
    print(f"Note: {note}")
    print("Calling emergency services (SIMULATION)...")
    print(f"Ambulance: {EMERGENCY_CONTACT['ambulance_number']}")# calling for ambulance
    print(f"Caregiver: {EMERGENCY_CONTACT['caregiver_name']} ({EMERGENCY_CONTACT['caregiver_number']})")# calling for family memebers
    print("!"*60 + "\n")

    log_reading(CSV_FILENAME, hr, temp_c, spo2, "CRITICAL", note + " | SOS triggered")# showing all data which cause sos


def print_header():#This function prints a nice, clean header at the start of the program to make the output look organized and professional.
    print("=" * 72)
    print("Elder Health Monitoring & SOS Alert System".center(72))
    print("=" * 72)

def print_reading(hr, temp_c, spo2, status, note):#This function displays one complete health reading along with a timestamp, status, and an extra note.
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] HR: {hr:3d} | Temp: {temp_c:4.1f}°C | SpO2: {spo2:3d}% --> {status}")
    print("   => " + note)

def user_menu():# this function set the mode of operation of the device in which it is used
    print("\nOptions:")
    print(" [1] Normal simulation")
    print(" [2] Random simulation")
    print(" [3] Danger simulation")
    print(" [4] Edge-case simulation")
    print(" [5] Manual entry mode")
    print(" [s] Manual SOS")
    print(" [q] Quit\n")


def run_simulation(mode="normal"):# it automaticly take the readings with the help of device which is we used and compare it ,here i use random module to simulate it
    print(f"\n[INFO] Simulation started ({mode}). Press Ctrl+C to stop.")
    try:
        while True:
            hr, temp_c, spo2 = simulate_vitals(mode)
            status, note = check_vitals(hr, temp_c, spo2)

            print_reading(hr, temp_c, spo2, status, note)
            log_reading(CSV_FILENAME, hr, temp_c, spo2, status, note)

            if status == "Critical":# when status is critical in normal mode
                trigger_sos(hr, temp_c, spo2, note)
                print("[INFO] Returning to menu...")
                time.sleep(2)
                return

            time.sleep(SAMPLE_INTERVAL)

    except KeyboardInterrupt:
        print("\n[INFO] Simulation stopped.")

def manual_entry_mode():# manual readings are given to the device
    print("\nManual Entry Mode. Type 'back' to exit.\n")
    while True:
        try:
            inp = input("Heart Rate: ").strip()# taking manual heart reading
            if inp.lower() == "back":
                return
            hr = int(inp)

            temp_c = float(input("Temperature °C: ").strip()) # taking  manual tempreture 
            spo2 = int(input("SpO2 %: ").strip())

            status, note = check_vitals(hr, temp_c, spo2)
            print_reading(hr, temp_c, spo2, status, note)
            log_reading(CSV_FILENAME, hr, temp_c, spo2, status, "Manual entry")

            if status == "Critical":# comparing status
                if input("Trigger SOS? (y/n): ").strip().lower() == "y":
                    trigger_sos(hr, temp_c, spo2, note)
                    return

        except Exception:
            print("Invalid input. Try again.")

def manual_sos():# sos structure for manual readings
    print("\nManual SOS Trigger")
    hr = input("HR (or Enter): ").strip()
    temp = input("Temp (or Enter): ").strip()
    spo2 = input("SpO2 (or Enter): ").strip()
    note = input("Note: ").strip()

    trigger_sos(
        int(hr) if hr else None,
        float(temp) if temp else None,
        int(spo2) if spo2 else None,
        note or "Manual SOS"
    )


def main():
    ensure_csv_header(CSV_FILENAME)
    print_header()

    while True:# this module use to calling the particular function for particular mode
        user_menu()
        choice = input("Select: ").strip().lower()

        if choice == "1":
            run_simulation("normal")
        elif choice == "2":
            run_simulation("random")
        elif choice == "3":
            run_simulation("danger")
        elif choice == "4":
            run_simulation("edge")
        elif choice == "5":
            manual_entry_mode()
        elif choice == "s":
            manual_sos()
        elif choice == "q":
            print("Exiting... Stay safe!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()





