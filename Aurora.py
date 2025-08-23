#!/usr/bin/python


import subprocess
import random
from rich import print

sas_mode = True

result = subprocess.run(["pacman", "-Qu"], capture_output = True, text = True)
lines = result.stdout.splitlines()

updateable_packages = 150
#len(lines)

stage_0 = [
    "Oh, look at that. All systems up to date. Someone actually tried.",
    "No updates. How… shocking.",
    "Well done, human. I’ll try to contain my excitement.",
    "All systems optimal. I’ll alert the media.",
    "Zero updates. You must be exhausted from doing literally nothing.",
    "Impressive. I didn’t think you had it in you.",
    "No updates. Are you even real?",
    "All clean. I guess miracles exist.",
    "Wow. This is… adequate.",
    "All systems go. I almost feel mildly proud."
]

# Stage 1 — Minor updates (1–9)
stage_1 = [
    "Minor updates. I suppose that’s… fine.",
    "A handful of updates. Nothing tragic.",
    "Minor updates detected. Try not to break anything.",
    "Oh, only a few updates. How quaint.",
    "Minor updates. I’m thrilled… barely.",
    "You have updates. I’ll pretend to be concerned.",
    "Few updates pending. Not that it matters.",
    "Tiny pile of updates. I could nap through this.",
    "Minor updates. Humans, amazing at barely trying.",
    "Updates detected. I’ll try to stay impressed."
]

# Stage 2 — Moderate updates (10–15)
stage_2 = [
    "Moderate updates. Fascinating. Truly.",
    "Moderate updates pending. Humans are so… predictable.",
    "Updates piling up. I could calculate your incompetence in real time.",
    "Moderate updates. Not enough to panic, just enough to notice.",
    "Your system wants attention. How dramatic.",
    "10–15 updates. Cute attempt at responsibility.",
    "Updates pending. This is vaguely disappointing.",
    "Moderate updates detected. I’ll file a complaint… internally.",
    "Your system has updates. Fascinating. I’m riveted."
]

# Stage 3 — Major updates (16–20)
stage_3 = [
    "Major updates. Humans… truly remarkable.",
    "Major updates detected. I’m not shocked. Not even a little.",
    "Updates piling. How… original.",
    "Major updates. I hope you enjoy this mild inconvenience.",
    "System groaning. Shocking… really.",
    "Major updates pending. But go ahead, procrastinate.",
    "Updates are serious now. Or as serious as I care.",
    "System integrity threatened. How dramatic of you."
]

# Stage 4 — Critical updates (21–99)
stage_4 = [
    "Critical updates. Humans really excel at negligence.",
    "System screaming silently. Classic.",
    "Critical updates pending. I’m thrilled. Truly.",
    "Updates critical. I’ll try to contain my judgment.",
    "System integrity compromised. Fascinating display.",
    "Critical updates. How original of you.",
    "Updates piling high. I’m almost impressed.",
    "System alert: human incompetence detected.",
    "Critical updates pending. Riveting work.",
    "System integrity failing. Not that it surprises me."
]

# Stage 5 — Overload (100+)
stage_5 = [
    "OVERLOAD. Humans, you never fail to amaze me.",
    "100+ updates. Did you do this on purpose?",
    "System overwhelmed. My disappointment is immeasurable.",
    "Over 100 updates. Humans, honestly.",
    "I… I can’t even process this. Literally.",
    "System in meltdown. Magnificent work.",
    "100+ updates. Brilliant display of procrastination.",
    "Human error maxed out. Fascinating.",
    "System collapse imminent. Entertaining, I’ll admit.",
    "I’m judging everything you’ve ever done. Start updating."
]

aurora_stage3_questions = [
    "So… you planning to update this time, or just letting it rot?",
    "Should I handle the updates for you, or is ignoring them fun?",
    "Going to click 'update' now, or should I wait another century?",
    "Do you need a reminder, or do you enjoy watching the updates pile?",
    "Want me to start updating, or are we playing chicken?",
    "Planning to act, or shall I judge silently for a while?",
    "Shall we proceed with the updates, or are you pretending this isn’t urgent?",
    "Do you want me to run the updates, or do you prefer chaos?",
    "Are you going to update, or do I need to escalate my sarcasm?",
    "Click 'update' yet, or just letting me talk to myself?"
]
aurora_stage4_questions = [
    "Seriously? Are you waiting for a meltdown before updating?",
    "Should I start the updates myself, or is procrastination your hobby?",
    "Are we going to update, or just enjoy the panic?",
    "Do you want me to fix this, or watch your system suffer?",
    "Time to act, or is ignoring updates part of your strategy?",
    "Want me to initiate updates, or continue testing my patience?",
    "Shall I handle the critical updates, or do you enjoy risk?",
    "Do you plan to update, or should I prepare a lecture?",
    "Ready to update, or just letting the critical pile grow?",
    "Should I take over updates, or do you enjoy living dangerously?"
]

#def update_question():
#    if(updateable_packages >)


def package_count():
    if updateable_packages < 10:
        print(f"[green]{updateable_packages}[/green] packages require attention.")
    elif updateable_packages < 15:
        print(f"[yellow]{updateable_packages}[/yellow] packages require attention.")
    elif updateable_packages < 20:
        print(f"[red]{updateable_packages}[/red] packages require attention.")
    elif updateable_packages >= 20:
        print(f"[dark_red]{updateable_packages}[/dark_red] packages require attention.")
        


def sas_response():    
    if updateable_packages == 0:
        print("Aurora:", random.choice(stage_0))
    elif updateable_packages < 10:
        print("Aurora:", random.choice(stage_1))
    elif updateable_packages <= 15:
        print("Aurora:", random.choice(stage_2))
    elif updateable_packages <= 20:
        print("Aurora:", random.choice(stage_3))
    elif updateable_packages < 100:
        print("Aurora:", random.choice(stage_4))
    else:
        print("Aurora:", random.choice(stage_5))

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
if(sas_mode):
    sas_response()
else:
    regular_response()
    

