#!/usr/bin/python
# Aurora - A Arch Linux update assistant
# Copyright (C) 2025 Yannick Winkler
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys
import os
sys.path.append("/usr/lib/aurora")
import responses

import subprocess
import random
from rich import print
import os
import datetime
import time

# ---------------- CONFIG ----------------
auto_update = True
# Thresholds for update stages
stage0_threshold = 0
normal_threshold = 20
moderate_threshold = 60
high_threshold = 120
critical_threshold = 200
atomic_threshold = 500
nuclear_threshold = 1000

# ---------------- FILE & STATE ----------------
script_dir = os.getenv("HOME")+"/.config"
flag_file = os.path.join(script_dir, ".aurora_update_flag")
time_flag_file = os.path.join(script_dir, ".aurora_time_flag")
result_storage_file = os.path.join(script_dir, ".aurora_result_storage_file")
should_ask_today = False

# ---------------- GET UPDATABLE PACKAGES ----------------


# ---------------- FUNCTIONS ----------------

def should_sync():
    """Check if we have synced in the last hour"""
    current_time = str(time.localtime().tm_hour)
    if os.path.exists(time_flag_file):
        with open(time_flag_file, "r") as f:
            last_hour = f.read().strip()
        if last_hour == current_time:
            return False
    with open(time_flag_file, "w") as f:
        f.write(current_time)
    return True


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
            print("Aurora:", random.choice(responses.stage_1))
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
        elif updateable_packages < atomic_threshold:
            print("Aurora:", random.choice(responses.stage_5))
        elif updateable_packages < nuclear_threshold:
            print("Aurora:", random.choice(responses.stage_6))
        else:
            print("Aurora:", random.choice(responses.stage_7))


def update_handler():
    """Handle user prompts or forced updates based on load and stage."""
    sas_response()

    if updateable_packages < moderate_threshold:
        # Minimal load, no update required
        return

    elif updateable_packages < high_threshold and should_ask_today:
        # Moderate to high load, ask user
        valid_responses = ["y", "n"]
        while True:
            print("Aurora: Do you want me to update? (y/n)")
            inpt = input("> ").strip().lower()
            if inpt in valid_responses:
                if inpt == "y":
                    update()
                    with open(result_storage_file, "w") as f:
                        f.write("0")
                break
            else:
                print("Aurora:", random.choice(responses.invalid_input_responses))

    elif updateable_packages >= high_threshold and auto_update:
        # Forced auto-update
        print("Aurora:", random.choice(responses.aurora_auto_update_responses))
        update()
        with open(result_storage_file, "w") as f:
            f.write("0")


# ---------------- MAIN ----------------
#Check if pacman-contrib is installed
check = subprocess.run(["pacman", "-Q", "pacman-contrib"], capture_output=True, text=True)


if check.returncode != 0:
    print("Aurora:", random.choice(responses.missing_contrib))
else:
    if should_sync():
        result = subprocess.run(["checkupdates"], capture_output=True, text=True)
        updateable_packages = len(result.stdout.splitlines())
        with open(result_storage_file, "w") as f:
            f.write(str(updateable_packages))

    else:
       with open(result_storage_file, "r") as f:
            updateable_packages = int(f.read().strip())

    should_ask_today_function()
    package_count()
    update_handler()

