import os
import time

RATELIMIT = 45

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    os.system('pause' if os.name == 'nt' else 'pause')
os.system("title syphoncore company - roblox group shout spam")

try:
    import requests
except ImportError:
    print("'requests' module was not found, installing requests...")
    os.system("pip install requests")
    print(" ")
    print(f"Installed 'requests' module, restart this software for changes to take affect.")
    pause()
    exit()
    
try:
    from colorama import Fore, Style, init
except ImportError:
    print("'colorama' module was not found, installing colorama...")
    os.system("pip install colorama")
    print(" ")
    print("Installed 'colorama' module, restart this software for changes to take affect.")
    pause()
    exit()

init()

STATEMENT = '''
[2025] syphoncore company

Syphoncore company software does NOT log cookies, or information of anykind.
Syphoncore does NOT permit the resale of this software or any other redistribution other than the offical GitHub page.

We are not responsible if anything happens to your Roblox account during, or after the use of our software.
------
This script does NOT work best with threading.
'''

BANNER = '''                                                                                                                
███████ ██   ██  ██████  ██    ██ ████████ 
██      ██   ██ ██    ██ ██    ██    ██    
███████ ███████ ██    ██ ██    ██    ██    
     ██ ██   ██ ██    ██ ██    ██    ██    
███████ ██   ██  ██████   ██████     ██    
 - Roblox group shout spammer created by syphoncore company                                         
'''

print(STATEMENT)
time.sleep(5)
cls()

print(Fore.RED + BANNER)
print(" ")
ROBLOX_SECURITY_COOKIE = input(Fore.WHITE + "[INPUT] Enter your ROBLOX .ROBLOSECURITY cookie >>> ")
GROUP_ID = int(input("[INPUT] Enter the group ID >>> "))
SHOUT_MESSAGE = input("[INPUT] Enter the message to shout >>> ")
SHOUT_SPAM = int(input("[INPUT] Enter the number of times to spam >>> "))
cls()


HEADERS = {
    'Cookie': f'.ROBLOSECURITY={ROBLOX_SECURITY_COOKIE}',
    'Content-Type': 'application/json',
    'X-CSRF-TOKEN': ''
}


def get_csrf_token():
    response = requests.post('https://auth.roblox.com/v2/logout', headers=HEADERS)
    if response.status_code == 403:
        return response.headers['x-csrf-token']
    raise Exception(Fore.RED + "[ERROR] Unable to fetch CSRF token.")

def send_shout(message):
    url = f"https://groups.roblox.com/v1/groups/{GROUP_ID}/status"
    payload = {"message": message}
    
    try:
        response = requests.patch(url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"[SUCCESS] Shouted message: {message}")
        elif response.status_code == 429:
            print(Fore.YELLOW + f"[WARNING] Rate limit hit. Retrying after cooldown...")
            time.sleep(RATELIMIT)
            send_shout(message)
        else:
            print(Fore.RED + f"[ERROR] Failed to send shout. Response: {response.text}")
    except requests.RequestException as e:
        print(Fore.RED + f"[ERROR] An error occurred while sending the shout: {e}")

try:
    HEADERS['X-CSRF-TOKEN'] = get_csrf_token()
    for i in range(SHOUT_SPAM):
        print(Fore.WHITE + f"[INFO] Sending shout {i + 1} of {SHOUT_SPAM}...")
        send_shout(SHOUT_MESSAGE)
except Exception as e:
    print(Fore.RED + f"[ERROR] {e}")
    pause()
    exit()

print("")
print(Fore.WHITE + "Completed shout spam!")
pause()
