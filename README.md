# Typing Bad!
Welcome to **Typing Bad**. Immerse yourself in the world of [Breaking Bad](https://www.imdb.com/title/tt0903747/) and test your typing skills with iconic quotes from the series.  

&nbsp;  

## Quick Setup
1. Ensure you have `pip` installed.
2. Open your command prompt and run:
   - For Windows users: 
     ```sh
     pip install windows-curses
     python -m pip install windows-curses
     ```
   - For macOS and most Linux/Unix users, `curses` is preinstalled, so this step is not required.

**Side note:** For best results, run the program directly in your terminal/command prompt rather than an IDE's terminal.

&nbsp;  

## Features and Considerations
- **Live Updates**: Provides robust and live updates of WPM and accuracy.
- **Precision Timing**: Timer starts only when the user begins typing to ensure accurate measurement.
- **Dynamic Feedback**: End messages are customized based on performance to keep it engaging.
- **Special Key Handling**: Ignores special characters, function keys, and arrow keys to avoid errors.
- **Live Color Coding Update**: 
  - **Correct Input**: Displayed in green.
  - **Error Highlighting**: Incorrect characters are highlighted in red.
  - **Untyped Text**: Displayed in light grey.
- **Optimized Input**: Only accepts 'y' or 'n' during the replay prompt to optimize input handling, keeping things efficient and to the point.
- **JSON Storage**: Quotes and end messages are stored in separate JSON files.
- **Terminal Restoration**: Uses `curses.wrapper()` to restore the terminal to its previous state.
- **Performance Metrics**: Measures both typing speed (WPM) and accuracy.

&nbsp;  

## Working Process
1. **Initialize States**: Set up the initial game state, including terminal dimensions and color pairs.
2. **Display Start Screen**: Show a Breaking Bad themed welcome message and instructions to the user.
3. **Run Typing Test**:
   - Fetch a random quote from the JSON file.
   - Display the quote to be typed with the author for details.
   - Monitor user input, updating the current text, WPM, and accuracy in real-time.
   - Handle key presses, including correct typing, backspace, and special characters.
   - Calculate and display WPM and accuracy dynamically.
4. **Completion and Feedback**:
   - Evaluate your performance based on WPM and accuracy.
   - Display a performance evaluated end message and prompt for a replay.
5. **Replay or Exit**:
   - Restart the game on 'y' or 'Y' or 'KEY_ENTER' input.
   - Exit the program on 'n', 'N', or escape key input.

&nbsp;  

## Future Enhancements
- [ ] Fix detection of single quotes and double quotes? (using "do not" instead of "don't" for now)
- [ ] Implement ctrl+backspace to delete a whole word?
- [ ] Include corrected words in the accuracy calculation?
- [ ] Add different difficulty modes (easy/medium/hard) with varying text lengths and special characters?

&nbsp;  

## Contributing
Contributions of any kind are welcome and appreciated :)  

&nbsp;  

## Copyright Note  
All quotes used in this project are copyrighted by the respective owners of [Breaking Bad](https://www.imdb.com/title/tt0903747/). No claims of ownership are made over these quotes.  

---
