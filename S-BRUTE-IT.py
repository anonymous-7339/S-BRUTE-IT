import requests

#colours used
red = ''

print()
print (red+"""
                   _             _ _               
 | |__  _ __ _   _| |_ ___      (_) |_ 
 | '_ \| '__| | | | __/ _ \_____| | __|
 | |_) | |  | |_| | ||  __/_____| | |_ 
 |_.__/|_|   \__,_|\__\___|     |_|\__|
 """+red)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
print("             ミ★ S-BRUTE-IT ★彡		    ")  
print("              SUB-DOMAIN FINDER                 ")	
print(">>DEVLOPED BY : KRISHNA_7339:HACKER	       ") 	
print(">>INSTA :krishna_7339_			       ") 
print(">>twitter:krishnanandivelugu		       ") 
print(">>special thanks to @mahesh @raghava	       ") 
print(">>#supraja_technologies		               ") 	
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
domain = input("Enter domain: ")
file = open('wordlist.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"            
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f"Discovered URL: {url1}")
		requests.get(url2)
		print(f"Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
