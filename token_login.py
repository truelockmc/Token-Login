from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import tkinter as tk
from tkinter import simpledialog
import json

def get_token_from_input():
    root = tk.Tk()
    root.withdraw()  # Verstecke Hauptfenster
    token = simpledialog.askstring("Token Eingabe", "Bitte Discord Token eingeben:", show='*')
    return token.strip() if token else None  # Entferne Leerzeichen und Zeilenumbrüche

def open_discord_and_login(token):
    print("Starte Firefox WebDriver...")
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webdriver.enabled", False)
    
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    print("Navigiere zu Discord...")
    driver.get("https://discord.com/")
    
    time.sleep(5)  # Warten, bis die Seite geladen ist
    print("Führe Login-Skript aus...")
    
    safe_token = json.dumps(token)  # Sicheres Einfügen des Tokens in JavaScript
    script = f'''
    function login(token) {{
        setInterval(() => {{
            document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"${{token}}"`;
        }}, 50);
        setTimeout(() => {{ location.reload(); }}, 2500);
    }}
    login({safe_token});
    '''
    
    # Ausgabe des Skripts in der Konsole
    print("Auszuführendes Skript:")
    print(script)
    
    driver.execute_script(script)
    print("Login-Skript ausgeführt, warte 10 Sekunden...")
    
    time.sleep(10)  # Warten nach Login
    
    print("Erzwinge manuelle Navigation zu Direktnachrichten...")
    driver.get("https://discord.com/channels/@me")
    
    # Warten, um sicherzustellen, dass die Seite geladen wird
    time.sleep(5)
    
    # Überprüfen, ob die Weiterleitung erfolgreich war
    if "login" in driver.current_url:
        print("Weiterleitung zu Login-Seite festgestellt. Login möglicherweise fehlgeschlagen.")
    else:
        print("Login abgeschlossen und auf Direktnachrichten-Seite navigiert!")
    
    return driver

# Token über Eingabeaufforderung erhalten
print("Bitte Token eingeben...")
discord_token = get_token_from_input()
if discord_token:
    print("Token erhalten, starte Login-Prozess...")
    driver = open_discord_and_login(discord_token)
else:
    print("Kein Token eingegeben. Beende das Programm.")