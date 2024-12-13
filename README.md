# Simple Keylogger

## Overview
The Simple Keylogger is a Python program that records keystrokes and logs them to a text file. Designed for educational purposes, it emphasises ethical usage and requires proper authorisation.

## Features

- **Keystroke Logging:** Captures all keystrokes, including special characters and function keys.
- **File Logging:** Saves keystrokes to a log file (`keylog.txt`) in the program directory.
- **Customisable File Name:** Change the log file name via the `log_file` parameter.
- **Stop Mechanism:** Stops logging when the `Esc` key is pressed, displaying a console message.
- **Cross-Platform Compatibility:** Uses `pynput` for compatibility with Windows, macOS, and Linux.

## Requirements
- Python 3.6 or later
- `pynput` library

## Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install the `pynput` library:
   ```bash
   pip install pynput
   ```

## Usage
1. Save the program as `Keylogger.py`.
2. Run the program:
   ```bash
   python Keylogger.py
   ```
3. Keystrokes are logged to `keylog.txt`.
4. Press the `Esc` key to stop the program.

## Ethical Considerations
Use this program responsibly and only with proper authorisation. Unauthorised use may violate laws and regulations. This project is intended for educational and authorised testing purposes only.

