import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "TYPING BAD: BREAKING LIMITS")
    stdscr.addstr("\nTime to cook… some serious WPM. Type fast and prove you’re the one who types!")
    stdscr.addstr("\n\nPress any key to continue..")
    stdscr.refresh()
    stdscr.getkey() # waiting to press a key by the user

def wpm_test(stdscr):
    target_text="Hello world this is some test text for this app!"
    current_text=[]

    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.refresh()
        
        key=stdscr.getkey()
        
        if ord(key)==27: #ascii for Return key
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"): # different representation of backspaces in different OS
            if len(current_text)>0:
                current_text.pop()
        else:
            current_text.append(key)



def main(stdscr): # stdscr == stand screen
    # creating color pair
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)




wrapper(main) 
    