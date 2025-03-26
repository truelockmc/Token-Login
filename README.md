# Discord Token-Login with Selenium

This Python script automates the process of logging into Discord using a user-provided token. It utilizes Selenium for browser automation and Tkinter for a simple graphical user interface (GUI) to input the Discord token.

> **Warning:**  
> Using this script may violate Discord's Terms of Service. It is intended for educational and testing purposes only. Use it at your own risk.

## Features

- **Token Input:**  
  A Tkinter-based GUI prompts the user to enter their Discord token securely.

- **Automated Browser Login:**  
  The script uses Selenium WebDriver with Firefox to navigate to Discord's website and inject the token into local storage to simulate a login.

- **Navigation to Direct Messages:**  
  After logging in, the script automatically redirects to the Direct Messages page.

## Dependencies

- **Python 3.x**  
  Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
- **Python Modules**
  - selenium
  - webdriver-manager

- **Firefox Browser**  
  The script uses Firefox for automation. Download it from the [official Firefox website](https://www.mozilla.org/firefox/).
  If you prefer to use chrome change line 17 from ```options = webdriver.FirefoxOptions()``` to ```options = webdriver.ChromeOptions()```

- **Webdriver:**  
  Managed automatically by `webdriver-manager`, so no manual installation is required.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/discord-auto-login.git
   cd discord-auto-login
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script:**
   ```bash
   python discord_auto_login.py
   ```

2. **Enter Discord Token:**
   - A dialog box will appear prompting you to enter your Discord token. The input is hidden for security.
   - After entering the token, the script will launch Firefox and perform the login process.

3. **Post-Login:**
   - The browser will navigate to your Direct Messages page.
   - Monitor the terminal for status updates and any potential errors.

## Security Considerations

- **Token Safety:**  
  Your Discord token grants full access to your account. Handle it with care and avoid sharing it.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

