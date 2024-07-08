#<!-- YOGE ⚚𓆩(◣_◢)𓆪 --!>#               

import socket
import termcolor


def scan(target,ports):
	print('\n' + "Starting Scan For: " + str(target))
	for port in range(1,ports + 1):
		scanport(target,port)

def scanport(ipaddress,port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress,port))
		print((termcolor.colored(("[+] Port Open "), "green")) + str(port))
		sock.close()
	except:
		if choise == "y":
			print((termcolor.colored(("[-] Port Closed "), "red")) + str(port))
		else:
			pass

targets = input("[+] Enter targets to scan (split them by commas for many targets):")
ports = int(input("[+] Enter how many ports you want to scan:"))
choise = input("Do you wish to show all closed ports y/n:")

if ',' in targets:
	print("[+] Scanning Multiple ip addresses...")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)


	  