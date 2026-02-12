# 🔐 Password Manager

A simple desktop password manager built with Python and Tkinter, allowing you to generate secure passwords and save your credentials locally.

## Features

- **Secure Password Generation**: Automatically create strong, randomized passwords containing a mix of uppercase letters, lowercase letters, numbers, and symbols.
- **Local Credential Storage**: Save website names, email/usernames, and passwords to a local `data.txt` file for easy access.
- **User-Friendly GUI**: A clean and intuitive interface built with Tkinter makes it easy to manage your information.
- **Input Validation**: Prevents saving empty fields to ensure data integrity.
- **Clipboard Integration**: (Future feature) Copy passwords directly to the clipboard.
- **Default Email**: Automatically populates the email field to save time.

## How to Use

1.  **Clone the repository or download the source code.**

2.  **Ensure you have Python 3 installed.**

3.  **Navigate to the project directory and run the application:**
    ```bash
    python main.py
    ```

4.  **Using the App:**
    - Enter the website you want to save credentials for.
    - Your default email is pre-filled, but you can change it.
    - Click **"Generate Password"** to create a new password, or type your own.
    - Click **"Add"** to save the information. You will be asked to confirm before it saves to `data.txt`.

