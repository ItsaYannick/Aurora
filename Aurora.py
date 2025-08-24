#!/usr/bin/python


import subprocess
import random
from rich import print
import responses
import os
import datetime

sas_mode = True

#Defining max and min packages for the different stages

stage0_threshold = 0

normal_threshold  = 10

moderate_threshold  = 15
high_threshold  = 20
critical_threshold  = 30

result = subprocess.run(["pacman", "-Qu"], capture_output = True, text = True)
lines = result.stdout.splitlines()

updateable_packages = len(lines)

script_dir = os.path.dirname(os.path.abspath(__file__))
flag_file = os.path.join(script_dir, ".aurora_update_question_check")

def should_ask_today():
    today = datetime.date.today().isoformat()

    if(os.path.exists(flag_file)):
        with open(flag_file, "r") as f:
            last_date = f.read().strip()
        if last_date == today:
            return False
    
    with open(flag_file, "w") as f:
        f.write(today)
    return True


# stage 0: 0 packages
# Stage 2 — Moderate updates (10–15)
# Stage 3 — Major updates (16–19)
# Stage 4 — Critical updates (20–49)
# Stage 5 — Overload (50+)

def update():
    subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
    

def update_handler():
    sas_response()
    if(updateable_packages < moderate_threshold):
        #Minimal load, no update required
        return
    elif(updateable_packages < critical_threshold):
        #Moderate to high load
        

        valid_responses = ["y", "n"]
        while(True):
            inpt = input(">").strip().lower()
            if(inpt in valid_responses):
                if(inpt == "y"):
                    update()
                break
            else:
                print("Aurora: I said 'y' or [red]'n'[/red]. Try again.")
                
    else:
        #forced update
        print("Aurora:", random.choice(responses.aurora_auto_update_responses))
        runUpdate()


def package_count():
    if updateable_packages < normal_threshold:
        print(f"[green]{updateable_packages}[/green] packages require attention.")
    elif updateable_packages < moderate_threshold:
        print(f"[yellow]{updateable_packages}[/yellow] packages require attention.")
    elif updateable_packages < high_threshold:
        print(f"[red]{updateable_packages}[/red] packages require attention.")
    else:
        print(f"[dark_red]{updateable_packages}[/dark_red] packages require attention.")
        


def sas_response():
    if should_ask_today():
        if updateable_packages == 0:
            print("Aurora:", random.choice(responses.stage_0))
        elif updateable_packages < normal_threshold:
            print("Aurora:", random.choice(responses.stage_1_update))
        elif updateable_packages < moderate_threshold:
            print("Aurora:", random.choice(responses.stage_2_update))
        elif updateable_packages < high_threshold:
            print("Aurora:", random.choice(responses.stage_3_update))
        elif updateable_packages < critical_threshold:
            print("Aurora:", random.choice(responses.stage_4_update))
        else:
            print("Aurora:", random.choice(responses.stage_5))
    else:       
        if updateable_packages == 0:
            print("Aurora:", random.choice(responses.stage_0))
        elif updateable_packages < normal_threshold:
            print("Aurora:", random.choice(responses.stage_1))
        elif updateable_packages < moderate_threshold:
            print("Aurora:", random.choice(responses.stage_2))
        elif updateable_packages < high_threshold:
            print("Aurora:", random.choice(responses.stage_3))
        elif updateable_packages < critical_threshold:
            print("Aurora:", random.choice(responses.stage_4))
        else:
            print("Aurora:", random.choice(responses.stage_5))

def regular_response():
    if updateable_packages == 0:
        print("Aurora: All systems optimal. No updates required.")
    elif updateable_packages < 10:
        print("Aurora: Minor updates detected. Routine maintenance advised.")
    elif updateable_packages < 15:
        print("Aurora: Moderate updates available. Schedule maintenance soon.")
    elif updateable_packages <= 20:
        print("Aurora: Major updates pending. Consider immediate system checks.")
    elif updateable_packages < 100:
        print("Aurora: Critical updates detected. System integrity at risk.")
    else:
        print("Aurora: WARNING! Over 100 updates pending. Initiate full system overhaul immediately.")


package_count()
update_handler()
    

