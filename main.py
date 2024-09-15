import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "TYPING BAD: BREAKING LIMITS")
    stdscr.addstr("\nTime to cook… some serious WPM. Type fast and prove you’re the one who types!")
    stdscr.addstr("\n\nPress any key to continue… ")
    stdscr.refresh()
    stdscr.getkey() # waiting to press a key by the user


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(1, 0, target, curses.color_pair(3))
    stdscr.addstr(4, 0, f"WPM: {wpm}", curses.color_pair(4))
    stdscr.addstr(1, 0, "") # to keep the cursor in the beginnig of the line before typing
    
    for i, char in enumerate(current):
        correct_char=target[i]
        color=curses.color_pair(1)
        if char != correct_char:
            color=curses.color_pair(2)
        
        stdscr.addstr(1, i, char, color)


def wpm_test(stdscr):
    target_text="Hello world this is some test text for this app!"
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True) # makes sure the wpm doesnt get stuck when user doesnt type anything

    while True:
        time_elapsed=max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed/60)) / 5) # this assumes the avg word has 5 characters
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
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
        
        if ord(key)==27 or key in ("KEY_ENTER", '\n', '\r'): #ascii for escape key or the enter key
            break
        
        if key in ("KEY_BACKSPACE", '\b', "\x7f"): # different representation of backspaces in different OS
            if len(current_text)>0:
                current_text.pop()

        elif len(current_text)<len(target_text):
            current_text.append(key)

        # 13 for space


def main(stdscr): # stdscr == stand screen
    # creating color pair
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    if curses.can_change_color() and curses.COLORS >= 256:
        curses.init_pair(3, 8, curses.COLOR_BLACK)  # Dark grey (color 8)
    else:
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Fallback to whited
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.nodelay(False) # to wait for user's input after exitting with esc key
        stdscr.addstr(5, 0, "Test complete. Hit enter to give another try. ")
        key = stdscr.getkey()
        
        if key not in ("KEY_ENTER", '\n', '\r'):
            break   

wrapper(main) 
