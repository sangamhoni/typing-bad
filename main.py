import curses
from curses import wrapper
import math
import time
import json
import random

# quotes = [
#     "Who are you talking to right now? Who is it you think you see? Do you know how much I make a year? I mean, even if I told you, you wouldn’t believe it. Do you know what would happen if I suddenly decided to stop going into work?",
#     "No, you clearly don’t know who you’re talking to, so let me clue you in. I am not in danger, Skyler. I am the danger.",
#     "A guy opens his door and gets shot and you think that of me? No. I am the one who knocks!"
# ]

global TERMINAL_HEIGHT, TERMINAL_WIDTH

# Load the quotes from the JSON file

with open('quotes.json', 'r') as file:
    quotes = json.load(file)

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "TYPING BAD: BREAKING LIMITS")
    stdscr.addstr("\nTime to cook… some serious WPM. Type fast and prove you’re the one who types!")
    stdscr.addstr("\n\nPress any key to continue… ")
    stdscr.refresh()
    stdscr.getkey() # waiting to press a key by the user


def typing_accuracy(current_text, target_text):
    total_characters = min(len(current_text), len(target_text))
    if total_characters == 0:
        return 0.0  # If there are no characters, consider accuracy as 100%

    matching_characters = 0
    for current_char, target_char in zip(current_text, target_text):
        if current_char == target_char:
            matching_characters += 1
    
    matching_percentage = (matching_characters / total_characters) * 100
    return matching_percentage


def display_text(stdscr, target, target_author, current, wpm=0, accuracy=100):
    global WPM_YCOR
    WPM_YCOR=max(math.ceil(len(target)/TERMINAL_WIDTH), 1) + 3
    
    stdscr.addstr(1, 0, target, curses.color_pair(3))
    stdscr.addstr(WPM_YCOR-2, 5, f"— {target_author}")
    stdscr.addstr(WPM_YCOR, 0, f"WPM: {wpm}", curses.color_pair(4))
    stdscr.addstr(f"     Accuracy: {accuracy}%", curses.color_pair(4))
    stdscr.addstr(1, 0, "") # to keep the cursor in the beginnig of the line before typing
    
    for i, char in enumerate(current):
        correct_char=target[i]
        color=curses.color_pair(1)
        if char != correct_char:
            color=curses.color_pair(2)
        
        xcor=(i%TERMINAL_WIDTH) # here i is the index of the character
        ycor=max(math.ceil((i+1)/TERMINAL_WIDTH), 1)
        stdscr.addstr(ycor, xcor, char, color)


def wpm_test(stdscr):
    # select random quote from json file loaded into quotes
    quote_json=random.choice(quotes)
    target_text=quote_json['quote']
    target_text_author=quote_json['character']
    
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True) # makes sure the wpm doesnt get stuck when user doesnt type anything

    while True:
        if current_text == []:
            start_time = time.time()
        time_elapsed=max(time.time() - start_time, 1)
        
        # calculates WPM
        wpm = round((len(current_text) / (time_elapsed/60)) / 5) # this assumes the avg word has 5 characters
        
        # calculates Accuracy
        total_characters = min(len(current_text), len(target_text))
        if (total_characters==0):
            accuracy_score=100
        else:
            matching_characters = 0
            for current_char, target_char in zip(current_text, target_text):
                if current_char == target_char:
                    matching_characters += 1
            accuracy_score = round((matching_characters / total_characters) * 100)
        
        stdscr.clear()
        display_text(stdscr, target_text, target_text_author, current_text, wpm, accuracy_score)
        stdscr.refresh()
        
        # detect the end of line
        if len(current_text)==len(target_text):
            break
        
        # converting to a string for comparison 
        if ("".join(current_text)==target_text):
            stdscr.nodelay(False) #now pause the live wpm update
            break
        
        # to make sure we dont get error because of stdscr.nodelay(True)
        try: 
            key=stdscr.getkey()
        except:
            continue
            
        if current_text == []:
            start_time = time.time()
        
        if ord(key)==27 or key in ("KEY_ENTER", '\n', '\r'): #ascii for escape key or the enter key
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"): # different representation of backspaces in different OS
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)


def main(stdscr): # stdscr == stand screen
    # creating color pair
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    if curses.can_change_color() and curses.COLORS >= 256:
        curses.init_pair(3, 8, curses.COLOR_BLACK)  # Dark grey (color 8)
    else:
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Fallback to whited
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # getting terminal height and width for positioning
    global TERMINAL_HEIGHT, TERMINAL_WIDTH
    TERMINAL_HEIGHT, TERMINAL_WIDTH=stdscr.getmaxyx()

    start_screen(stdscr)
    wpm_test(stdscr)
    
    stdscr.addstr(WPM_YCOR+1, 0, "Test complete. Hit enter to give another try. ")
    
    while True:
        stdscr.nodelay(False) # to wait for user's input after exitting with esc key
        key = stdscr.getkey()
        if key in ("KEY_ENTER", '\n', '\r', 'y', 'Y'):
            wrapper(main)
        elif key=="N" or key=="n" or ord(key)==27:
            break  


wrapper(main) 
