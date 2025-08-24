#!/usr/bin/python

import subprocess
import random
from rich import print
import responses
import os
import datetime

# ---------------- CONFIG ----------------
sas_mode = True

# Thresholds for update stages
stage0_threshold = 0
normal_threshold = 10
moderate_threshold = 15
high_threshold = 20
critical_threshold = 30

# ---------------- FILE & STATE ----------------
script_dir = os.path.dirname(os.path.abspath(__file__))
flag_file = os.path.join(script_dir, ".aurora_update_question_check")
should_ask_today = False

# ---------------- GET UPDATABLE PACKAGES ----------------
result = subprocess.run(["pacman", "-Qu"], capture_output=True, text=True)
updateable_packages = len(result.stdout.splitlines())

# ---------------- FUNCTIONS ----------------

def should_ask_today_function():
    """Check if we have already asked the user today."""
    global should_ask_today
    today = datetime.date.today().isoformat()

    if os.path.exists(flag_file):
        with open(flag_file, "r") as f:
            last_date = f.read().strip()
        if last_date == today:
            should_ask_today = False
            return

    with open(flag_file, "w") as f:
        f.write(today)
    should_ask_today = True


def update():
    """Run system update via pacman."""
    subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])


def package_count():
    """Print package count with color according to severity."""
    if updateable_packages < normal_threshold:
        color = "green"
    elif updateable_packages < moderate_threshold:
        color = "yellow"
    elif updateable_packages < high_threshold:
        color = "red"
    else:
        color = "dark_red"

    print(f"[{color}]{updateable_packages}[/{color}] packages require attention.")


def sas_response():
    """Print sassy response according to update stage and whether we ask today."""
    if should_ask_today:
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
        # Regular sassy responses when not prompting
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


def update_handler():
    """Handle user prompts or forced updates based on load and stage."""
    sas_response()

    if updateable_packages < moderate_threshold:
        # Minimal load, no update required
        return

    elif updateable_packages < critical_threshold and should_ask_today:
        # Moderate to high load, ask user
        valid_responses = ["y", "n"]
        while True:
            print("Aurora: Do you want me to update? (y/n)")
            inpt = input("> ").strip().lower()
            if inpt in valid_responses:
                if inpt == "y":
                    update()
                break
            else:
                print("Aurora: I said 'y' or [red]'n'[/red]. Try again.")

    elif updateable_packages >= critical_threshold:
        # Forced auto-update
        print("Aurora:", random.choice(responses.aurora_auto_update_responses))
        update()


# ---------------- MAIN ----------------
should_ask_today_function()
package_count()
update_handler()
