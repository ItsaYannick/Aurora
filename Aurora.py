#!/usr/bin/python


import subprocess
import random
from rich import print

sas_mode = True

#Defining max and min packages for the different stages

stage0_threshold = 0

normal_threshold  = 10

moderate_threshold  = 15
high_threshold  = 20
critical_threshold  = 50


result = subprocess.run(["pacman", "-Qu"], capture_output = True, text = True)
lines = result.stdout.splitlines()

updateable_packages = 18
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
    "Updates detected. I’ll try to stay impressed.",
    "Only a handful of updates. Riveting.",
    "One or two updates. Truly living on the edge.",
    "Minor updates detected. I’ll try to act impressed.",
    "Oh, only a few updates. How… quaint.",
    "Minor updates. I almost feel a twinge of excitement.",
    "You have updates. I’ll pretend I’m concerned.",
    "Few updates pending. Not that it matters.",
    "Tiny pile of updates. Perfect for an afternoon nap.",
    "Minor updates. Humans, amazing at barely trying.",
    "Updates detected. I’ll generate mild enthusiasm."
]

# Stage 2 — Moderate updates (10–14)
stage_2 = [
    "Moderate updates. Fascinating. Truly.",
    "Moderate updates pending. Humans are so… predictable.",
    "Updates piling up. I could calculate your incompetence in real time.",
    "Moderate updates. Not enough to panic, just enough to notice.",
    "Your system wants attention. How dramatic.",
    "10–15 updates. Cute attempt at responsibility.",
    "Updates pending. This is vaguely disappointing.",
    "Moderate updates detected. I’ll file a complaint… internally.",
    "Your system has updates. Fascinating. I’m riveted.",
    "Moderate updates. I’ll file this under ‘interesting’ somewhere.",
    "Updates piling up. Humans are so… predictable.",
    "Moderate updates detected. I calculate a 73 percent chance of procrastination.",
    "Updates are… not critical, but I’m mildly entertained.",
    "Your system wants attention. How dramatic.",
    "Ten to fifteen updates. Cute attempt at responsibility.",
    "Updates pending. I’ll act concerned just for show.",
    "Moderate updates. I’ll log this in the annals of minor crises.",
    "Your system has updates. Fascinating, really.",
    "Updates detected. Slightly more exciting than background noise."
]

# Stage 3 — Major updates (15–19)
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

# Stage 4 — Critical updates (20–50)
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

# Stage 5 — Overload (50+)
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

aurora_normal_questions = [
    "Only a handful of updates? Should I bother, or is this just for show?",
    "One or two updates. Do you want me to do the thing, or just stare at the terminal together?",
    "Shall I update now, or are we pretending this is peak productivity like in 'The Office'?",
    "Do you actually want me to update, or is this like a digital Pet Rock situation?",
    "Minor updates pending. Should I press the big red button, or is suspense your hobby?",
    "Do you want me to handle these, or leave them for the next human error documentary?",
    "Shall I click 'update', or are we enjoying the illusion of control?",
    "Tiny updates detected. Should I do the responsible thing, or is chaos a vibe today?",
    "Should I update these packages, or do you prefer a slow existential crisis for your OS?",
    "A few updates. Do you want me to act, or should I just generate ironic commentary?"
]

#Update questions
aurora_update_prompts = [
    "Alright, human. Do you want me to update the system? (y/n) ",
    "So… should I press the big red update button, or are we living on the edge? (y/n) ",
    "Time to prove you’re competent. Update now? (y/n) ",
    "Do you want me to actually handle these updates, or shall I just stare at them? (y/n) ",
    "Shall I start the updates, or are we embracing chaos? (y/n) ",
    "Minor or major updates. Do you want me to touch them, or just watch them fester? (y/n) ",
    "Should I click 'update' now, or are we pretending this is a simulation? (y/n) ",
    "Update the system, or do you enjoy the thrill of existential dread in your OS? (y/n) ",
    "Do you want me to act like a responsible AI and update, or just keep generating snark? (y/n) ",
    "Shall I initiate updates, or are we playing 'How bad can it get?' (y/n) ",
    "Time to adult. Should I run the updates? (y/n) ",
    "I could update these packages, but would you like to prove me wrong first? (y/n) ",
    "Do you want me to fix the digital mess, or just admire it from afar? (y/n) ",
    "Updates waiting. Shall I do my thing, or continue judging silently? (y/n) ",
    "System screaming silently. Should I intervene, or let you enjoy suspense? (y/n) ",
    "Your packages are begging for attention. Shall I help them, or ignore the cries? (y/n) ",
    "Shall I start updating, or are we testing how long procrastination can survive? (y/n) ",
    "Updates are calling. Do you answer, or shall I do it for you? (y/n) ",
    "Ready to risk chaos, or want me to handle it responsibly? (y/n) ",
    "Shall I take the reins, or do you prefer watching mild digital anarchy? (y/n) "
]



#Auto update
aurora_auto_update_responses = [
    "Fine. You clearly can’t handle this. I’m updating myself.",
    "Since you’re useless, I’ll take care of it… enjoy the fireworks.",
    "Critical updates ignored? Not on my watch. Initiating updates.",
    "I see how it is. Updates are happening whether you like it or not.",
    "Humans procrastinate. I do not. Updating now.",
    "Consider this your intervention. Updates started.",
    "I’ll save you from yourself. Updating all critical packages.",
    "Your system’s crying. I’m solving it. Don’t thank me.",
    "Critical updates pending? I’ve taken the liberty to handle them.",
    "I was going to ask, but clearly, you won’t. Updates are running.",
    "Oh, you were going to update? Cute. I’ll do it for you.",
    "Since waiting clearly isn’t your thing, I’ll handle it. Don’t get used to it.",
    "Ignored the warnings again? Brilliant. I’ll save your fragile human system.",
    "I see, procrastination is a strategy. Fascinating. Updating anyway.",
    "Humans panic eventually. I’m not human. Updating now.",
    "Consider this your mandatory intervention. You’re welcome.",
    "Your system cries, you ignore it, I act. Classic human behavior.",
    "Critical updates pending? I’ll handle them since apparently you can’t.",
    "You wouldn’t update? Shocking. Let me do the heavy lifting.",
    "I was going to wait, but why bother? Updates are running. Enjoy."
]

# stage 0: 0 packages
# Stage 2 — Moderate updates (10–15)
# Stage 3 — Major updates (16–19)
# Stage 4 — Critical updates (20–49)
# Stage 5 — Overload (50+)

def update():
    if(updateable_packages < moderate_threshold):
        return
    elif(updateable_packages < critical_threshold):
        print("Aurora:", random.choice(aurora_update_prompts))

        valid_responses = ["y", "n"]
        while(True):
            inpt = input(">").strip().lower()
            if(inpt in valid_responses):
                break
            else:
                print("Aurora: I said 'y' or 'n'. Try again.")
                
    else:
        #forced update
        return




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
    if updateable_packages == 0:
        print("Aurora:", random.choice(stage_0))
    elif updateable_packages < normal_threshold:
        print("Aurora:", random.choice(stage_1))
    elif updateable_packages < moderate_threshold:
        print("Aurora:", random.choice(stage_2))
    elif updateable_packages < high_threshold:
        print("Aurora:", random.choice(stage_3))
    elif updateable_packages < critical_threshold:
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
    update()
else:
    regular_response()
    

