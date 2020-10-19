import os 
import socket
import subprocess
import platform
import sys
from time import sleep
from socket import *


class ChameleonPY:


    def __init__(self):

        self.option_main = option_main = 0
        self.option_second = option_second = 0

        self.Start()


    def menu_one(self):

        try:

            print("""

                 1) Scan of ports

                 2) get-ip of domain

                 3) get information about system: 

                 0 BACK

                 -1 EXIT
                  
                  """)

            self.option_second = int(input("Option: "))

            if self.option_second == 1:

                #scan of ports
                import socket
                domain = str(input("Domain: "))
                ports = [21, 22, 25, 77, 80, 443, 8080, 8888]
                for List in ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    con = sock.connect_ex((domain, List))
                    if con == 0:
                        print(List, '\tOpen')
                    else:
                        print(List, "Closed")
                #;

            elif self.option_second == 2:

                #get IP
                D = gethostbyname(a)
                print("\n IP ===========> {}".format(D))
                #;

            elif self.option_second == 3:

                #get system informations
                System = platform.system()
                Version = platform.release()
                Data = platform.version()
                print("\nSystem: {}\nVersion: {}\nData: {}".format(System,Version,Data))
                #;
                
            elif self.option_second == 0:

                self.Start()

            elif self.option_second == -1:
                    
                self.exit()

            else:

                self.menu_one()
                    
        except Exception as error:
            print("Error: {}".format(error))
            self.menu_one()

        self.Start()


    def menu_two(self):

        try:
            
            print("""
            
                 1) Update repositories

                 2) Upgrade System

                 3) Dist-upgrade

                 4) ADD repositories in your sourcelist

                 5) Poweroff

                 6) Reboot

                 0 BACK

                 -1 EXIT
            
                 """)

            self.option_second = int(input("Option: "))

            if self.option_second == 1:

                os.system("sudo apt update")

            elif self.option_second == 2:

                os.system("sudo apt upgrade")

            elif self.option_second == 3:

                os.system("sudo apt dist-upgrade")

            elif self.option_second == 4:

                add = str(input("Repository: "))

            elif self.option_second == 5:

                os.system("sudo poweroff")

            elif self.option_second == 6:

                os.system("sudo reboot")

            elif self.option_second == 0:

                self.Start()

            elif self.option_second == -1:

                self.exit()

            else:

                print("Option no avaible")
                self.menu_two()
                    
        except Exception as error:

            print("Error: {}".format(error))
            self.menu_one()


        self.Start()


    def menu_three(self):

        try:
            
            print("""
            
            1) Install arpspoof

            2) Install crunch

            3) Install dig

            4) Install dnsenum

            5) Install dnsrecon

            6) Install dnsmap

            7) Install dnsspoof

            8) Install ettercap

            9) Install fierce

            10) Install hydra

            11) Install iptables

            12) Install maltego

            13) Install medusa

            14) Install metasploit

            15) Install mitmf

            16) Install netcat

            17) Install netdiscover

            18) Install nmap

            19) Install netcat

            20) Install sslsplit

            21) Install sslsplit

            22) Install tcpdump

            23) Install zenmap

            0 BACK

            -1 EXIT 
            
            """)

            self.option_second = int(input("Option: "))
                  
            if self.option_second == 1:

                os.system("apt install arpspoof")

            elif self.option_second == 2:

                os.system("apt upgrade crunch")

            elif self.option_second == 3:

                os.system("apt install dig")

            elif self.option_second == 4:

                os.system("apt install dnsenum")

            elif self.option_second == 5:

                os.system("apt install dnsrecon")

            if self.option_second == 6:

                os.system("apt install dnsmap")

            elif self.option_second == 7:

                os.system("apt upgrade dnsspoof")

            elif self.option_second == 8:

                os.system("apt install ettercap")

            elif self.option_second == 9:

                os.system("apt install fierce ")

            elif self.option_second == 10:

                os.system("apt install hydra")

            if self.option_second == 11:

                os.system("apt install iptables")

            elif self.option_second == 12:

                os.system("apt upgrade maltego")

            elif self.option_second == 13:

                os.system("apt install medusa")

            elif self.option_second == 14:

                os.system("apt install metasploit-framework")

            elif self.option_second == 15:

                os.system("apt install mitmf")

            if self.option_second == 16:

                os.system("apt install netcat")

            elif self.option_second == 17:

                os.system("apt upgrade netdiscover")

            elif self.option_second == 18:

                os.system("apt install nmap")

            elif self.option_second == 19:

                os.system("apt install netcat")

            elif self.option_second == 20:

                os.system("apt install sslsplit")

            if self.option_second == 21:

                os.system("apt install sslsplit")

            elif self.option_second == 22:

                os.system("apt upgrade tcpdump")

            elif self.option_second == 23:

                os.system("apt install zenmap")

            elif self.option_second == 0:

                self.Start()

            elif self.option_second == -1:

                self.exit()

            else:
                
                self.menu_three()
                    
        except Exception as error:

            self.menu_three()

        self.Start()


    def menu_four(self):

        try:

            key = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
            repositor = os.system("echo '# By chameleonPY\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
            os.sytem("apt update")

        except Exception as error:

            self.menu_four()

        self.Start()


    def exit(self):

        return exit()


    def Start(self):

        print(""" 
        
             ##===========================================##
             ##=============== chameleonPY ===============## 
             ##===========================================##

             1) chameleonPY tools

             2) Linux manager

             3) Install tools of pentest 

             4) Install kali repositors

             -1 EXIT 
        
             """)

        self.option_main = int(input("Option: "))

        if self.option_main == 1:

            os.system("clear")
            self.menu_one()

        elif self.option_main == 2:

            os.system("clear")
            self.menu_two()

        elif self.option_main == 3:

            os.system("clear")
            self.menu_three()

        elif self.option_main == 4:

            os.system("clear")
            self.menu_four()

        elif self.option_main == -1:

            os.system("clear")
            self.exit() 


root = ChameleonPY()