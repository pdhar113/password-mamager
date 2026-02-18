# 🔐 Password Manager

A simple desktop password manager built with Python and Tkinter, allowing you to generate secure passwords and save your credentials locally.

## Features

- **Secure Password Generation**: Automatically create strong, randomized passwords containing a mix of uppercase letters, lowercase letters, numbers, and symbols.
- **Local Credential Storage**: Save website names, email/usernames, and passwords to a local `data.json` file in JSON format.
- **Search Functionality**: Quickly look up saved credentials by website name.
- **User-Friendly GUI**: A clean and intuitive interface built with Tkinter makes it easy to manage your information.
- **Input Validation**: Prevents saving empty fields to ensure data integrity.
- **Clipboard Integration**: Generated passwords are automatically copied to the clipboard using pyperclip.
- **Default Email**: Automatically populates the email field to save time.

## How to Use

1.  **Clone the repository or download the source code.**

2.  **Ensure you have Python 3 installed.**

3.  **Install dependencies:**
    ```bash
    pip install pyperclip
    ```

4.  **Navigate to the project directory and run the application:**
    ```bash
    python main.py
    ```

5.  **Using the App:**
    - Enter the website you want to save credentials for.
    - Your default email is pre-filled, but you can change it.
    - Click **"Generate Password"** to create a new password (auto-copied to clipboard), or type your own.
    - Click **"Add"** to save the information to `data.json`.
    - Click **"Search"** to look up saved credentials for a website.

