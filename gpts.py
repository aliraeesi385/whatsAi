from WikiClient import Get
from colorama import Fore
import os,sys,subprocess

all_library = ["colorama", "WikiClient"]

for library in all_library:
    try:
        __import__(library)
    except ImportError:
        print(f"Library {library} not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        os.system('cls' if os.name == 'nt' else 'clear')

apis = Get.SyncAPI()
def gpt(message:str):
        datas = apis.request("apis-1/ChatGPT",{'q':message})
        return datas

fors = True
print(f"{Fore.MAGENTA}-------------------------\ncreator => aliraeesi385\ngithubs => https://github.com/aliraeesi385/whatsAi\n-------------------------")
messages = input(f"{Fore.MAGENTA}Ask your question to AI.\n\nSend the number 0 to finish.\n{Fore.WHITE}") 
while fors: 
    if messages == "0":
            print(f"{Fore.RED}The script was successfully closed.{Fore.RESET}") 
            fors = False
    else:
        gpts = gpt(messages)
        if gpts['status_code'] == 200:
            bodygpt = gpts['body']
            if bodygpt['status']:
                messages = input(f"{Fore.GREEN}{bodygpt['results']}{Fore.WHITE}\n")
            else:
                 messages = input(f"{Fore.RED}Error receiving the api{Fore.WHITE}\n")
        else:
             messages = input(f"{Fore.RED}Error receiving the api{Fore.WHITE}\n")
