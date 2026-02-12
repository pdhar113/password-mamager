# Password Manager

A simple GUI-based password manager application built with Python and Tkinter.

## Features

- **Generate Password:** Creates a secure, random password using a mix of letters, numbers, and symbols.
- **Save Data:** Stores website credentials (website name, email/username, and password) in a local text file (`data.txt`).
- **Input Validation:** Ensures no fields are left empty before saving.
- **Auto-fill:** Pre-fills the email field with a default email address for convenience.

## Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How to Use

1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. Enter the website name and your email/username.
3. Generate a password or enter your own.
4. Click "Add" to save the credentials to `data.txt`.

## Project Structure

- `main.py`: The main application code handling UI and logic.
- `logo.png`: Application logo used in the GUI.
- `data.txt`: (Generated upon first save) Stores your saved passwords.

## Preview

The application uses a clean grid layout with a canvas for the logo and specific fields for organized data entry.
