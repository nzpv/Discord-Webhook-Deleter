import os

try:
    from colorama import Fore, init
except ImportError:
    os.system("py -m pip install colorama")
    from colorama import Fore, init

try:
    import requests
except ImportError:
    os.system("py -m pip install requests")
    import requests

try:
    from pystyle import Center
except ImportError:
    os.system("py -m pip install pystyle")
    from pystyle import Center

init()

banner = (
    Fore.CYAN
    + """
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░   
                      ░                                  
"""
)

footer = (
    Fore.CYAN
    + "\n\n"
    + Center.XCenter("The fastest webhook deleter - sowqa 2024")
    + "\n"
)

print(Center.XCenter(banner) + footer)

webhook = input(Fore.WHITE + "[?] Webhook URL > " + Fore.CYAN)


def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(Fore.CYAN + "[+] Webhook succesfully deleted!")
        os.system("pause >nul")
    elif check.status_code == 200:
        print(Fore.WHITE + "[-] Failed to delete webhook!")
        os.system("pause >nul")


test = requests.get(webhook)
if test.status_code == 404:
    print(Fore.WHITE + "[-] Invalid webhook!")
    os.system("pause >nul")
elif test.status_code == 200:
    print(Fore.CYAN + "[+] Valid webhook!")
    delete()
