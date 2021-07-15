import requests

#colours used
red = ''

print()
print (red+"""
▌│█║▌║▌║ S-ＢＲＵＴＥ-ＩＴ ║▌║▌║█│▌                                                     
"""+red)

print(" Coded By - krishna_7339:Hacker")
print(" Instagram: https://instagram.com/krishna_7339_ ")
print(" Twitter https://twitter.com/krishnannandvelugu ")
print(" special Thanks to : @mahesh @raghava @suprajatechnologies ")
print()
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