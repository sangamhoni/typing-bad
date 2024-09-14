import curses
from curses import wrapper

# COLOR_GREEN="fff"
# COLOR_WHITE="fff"
# COLOR_YELLOW="fff"

def main(stdscr): # stdscr == stand screen
    # creating color pair
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    # using those colors, positioniing them in the canvas
    stdscr.addstr(1, 5, "Hello world", curses.color_pair(1))
    stdscr.addstr(1, 0, "Hello world", curses.color_pair(2))
    stdscr.refresh()
    # grabbing what the user pressed
    key=stdscr.getkey()
    print(key)


wrapper(main) 
    