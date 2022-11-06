import json
import webbrowser
from os import chdir, getcwd
from os import path as os_path
from os import system
from subprocess import check_output
from sys import exit
from time import sleep

import animation
import keyboard
import oathtool
from genericpath import exists

art = """
	███████╗███████╗     ██████╗ ██████╗ ██╗████████╗██╗   ██╗███╗   ██╗██╗     
	██╔════╝╚══███╔╝     ██╔══██╗██╔══██╗██║╚══██╔══╝██║   ██║████╗  ██║██║     
	█████╗    ███╔╝█████╗██████╔╝██████╔╝██║   ██║   ██║   ██║██╔██╗ ██║██║     
	██╔══╝   ███╔╝ ╚════╝██╔═══╝ ██╔══██╗██║   ██║   ██║   ██║██║╚██╗██║██║     
	███████╗███████╗     ██║     ██║  ██║██║   ██║   ╚██████╔╝██║ ╚████║███████╗
	╚══════╝╚══════╝     ╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""

system(f'title EZ-Pritunl by Ary')
system(f'mode con:cols=125 lines=30')
print()
print (art)
file_data = exists("data.txt")
path = "C:\\Program Files (x86)\\Pritunl"
if os_path.exists(path) == False:
	print()
	print("[!] Pritunl client not installed [!]")
	webbrowser.open("https://client.pritunl.com/")
	sleep(10)
	exit()
if file_data == False:
	print()
	print("[!] data.txt file not found [!]")
	sleep(3)
	exit()

bdir = getcwd()
file_data = json.loads(open("data.txt").read())
secret = file_data["key"]
url = file_data["url"]

if secret == "":
	print()
	print("[!] data.txt file is empty [!]")
	sleep(3)
	exit()
elif secret == "Your Two-Step Authentication Key here":
	print()
	print("[!] Please put your Two-Step Authentication Key in data.txt [!]")
	webbrowser.open(url)
	sleep(10)
	exit()

chdir("C:\\Program Files (x86)\\Pritunl")

cek = check_output("pritunl-client.exe list", shell=True).decode("utf-8")
cek = len(cek.split("\n"))

if cek == 5:
	print()
	print("[!] No Pritunl Profile found [!]")
	print()
	webbrowser.open(url)
	print("Please enter Profile URI Link")
	print(f"Example: pritunl://{url}/ku/xxxxxxxx")
	print()
	addurl = input("Input Profile URI: ")

	while f"pritunl://{url}" not in addurl:
			print()
			print("[!] Invalid Profile URI [!]")
			sleep(3)
			system("cls")
			print()
			print("Please enter Profile URI Link")
			print(f"Example: pritunl://{url}/ku/xxxxxxxx")
			print()
			url = input("Input Profile URI: ")
	
	system(f"pritunl-client.exe add {addurl}")
	system("cls")

out = check_output("pritunl-client.exe list", shell=True).decode("utf-8")
out = out.split("\n")
vpn_list = {}
no = 1
for index, x in enumerate(out):
	split = x.split(' ')
	if len(split) > 1:
		if split[1] != "" and split[1] != "ID":
			system(f"pritunl-client.exe disable {split[1]}")
			vpn_list[no] = [split[1], split[4], index]
			no += 1

print()
system("pritunl-client.exe list")
print()
print("[1] => Connect")
print("[2] => Disconnect")
print("[3] => Exit")
print()
print("[?] Press Your Choice [?]")
pil = keyboard.read_key()
if pil in ["1","2","3","4","5","6","7","8","9","0"]:
	pil = int(pil)
else:
	pil = 99
while pil not in range(1,4):
	print()
	print("[!] Invalid Choice [!]")
	print()
	sleep(1)
	system("cls")
	print()
	print(art)
	system("pritunl-client.exe list")
	print()
	print("[1] => Connect")
	print("[2] => Disconnect")
	print("[3] => Exit")
	print()
	print("[?] Press Your Choice [?]")
	pil = keyboard.read_key()
	if pil in ["1","2","3","4","5","6","7","8","9","0"]:
		pil = int(pil)
	else:
		pil = 99

if pil == 1:
	print()
	for x in vpn_list:
		print(f"[{x}] = {vpn_list[x][1]}")
	print()
	if len(vpn_list) > 1:
		print(f"[?] Press Your Choice [1-{no-1}]: ")
		id = 99
		sleep(1)
		while id not in range(1,no):
			id = keyboard.read_key()
			if id in ["1","2","3","4","5","6","7","8","9","0"]:
				id = int(id)
			else:
				id = 99
	else:
		id = 1
	print()
	key = oathtool.generate_otp(secret)
	system(f"pritunl-client.exe start --password {key} {vpn_list[int(id)][0]}")
	sleep(2)
	cek = check_output("pritunl-client.exe list", shell=True).decode("utf-8")
	cek = cek.split("\n")
	cek_vpn = cek[vpn_list[id][2]]
	wait = animation.Wait(text="[!] Connecting", speed=0.1)
	wait.start()
	while "Connecting" in cek_vpn:
		cek = check_output("pritunl-client.exe list", shell=True).decode("utf-8")
		cek = cek.split("\n")
		cek_vpn = cek[vpn_list[id][2]]
		sleep(1)
	wait.stop()
	print("[!] VPN Connected")
	sleep(3)
	exit()
elif pil == 2:
	print()
	for x in vpn_list:
		print(f"[{x}] = {vpn_list[x][1]}")
	print()
	if len(vpn_list) > 1:
		print(f"[?] Press Your Choice [1-{no-1}]: ")
		id = 99
		sleep(1)
		while id not in range(1,no):
			id = keyboard.read_key()
			if id in ["1","2","3","4","5","6","7","8","9","0"]:
				id = int(id)
			else:
				id = 99
	else:
		id = 1
	print()
	system(f"pritunl-client.exe stop {vpn_list[int(id)][0]}")
	sleep(2)
	cek = check_output("pritunl-client.exe list", shell=True).decode("utf-8")
	cek = cek.split("\n")
	cek_vpn = cek[vpn_list[id][2]].split(' ')[11]
	wait = animation.Wait(text="[!] Disconnecting", speed=0.04)
	wait.start()
	while cek_vpn != "Disconnected":
		cek = check_output("pritunl-client.exe list", shell=True).decode("utf-8")
		cek = cek.split("\n")
		cek_vpn = cek[vpn_list[id][2]].split(' ')[11]
		sleep(1)
	wait.stop()
	print("[!] VPN Disconnected")
	sleep(3)
	exit()
elif pil == 3:
	exit()