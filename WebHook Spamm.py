import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import *

colorama.init()

print(f'''{Fore.BLUE} 











                                        ___ _  _ _____ __  __   ___ ___  _   __  __ __  __ 
                                      / __| || |_   _|  \/  | / __| _ \/_\ |  \/  |  \/  |
                                      \__ \ __ | | | | |\/| | \__ \  _/ _ \| |\/| | |\/| |
                                      |___/_||_| |_| |_|  |_|_|___/_|/_/ \_\_|  |_|_|  |_|
                                                           |___|                          


                                                                                                             




                                                                                                            


                                                                                                                       
                                    By SAIHTAM
                                    Appuis sur ENTRER pour ne plus spammer!{Style.RESET_ALL}
''')

def sbammah():
    webhook = input(Fore.BLUE + "[>] Entrer le webhook: ")
    message = input(Fore.YELLOW + "[>] Entrer le message : ")    
    delay = float(input(Fore.RED + "[>] entrer le delai (EX: 0.1): "))
    print(Fore.BLUE + 'Début de l’envoi d’un messages')

    while True:

        print(Fore.CYAN + "Envoie... -> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent -> " + message) 
        except:
            print("Quelque chose s’est passé! | Webhook probablement incorrect ! -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    sbammah()
