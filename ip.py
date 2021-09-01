#!usr/bin/python
# author by angga kurniawan

import os, json, requests

def __main__():
	os.system("clear")
	with requests.Session() as ses:
		try:
			j = ses.get("https://ipapi.co/json/").json()
			print("  [+] IP Anda     : %s"%(j["ip"]))
			print(" +--------------------------------------+")
			print("  [+] Negara      : %s"%(j["country_name"]))
			print("  [+] Kota        : %s"%(j["city"]))
			print("  [+] Provinsi    : %s"%(j["region"]))
			print(" +--------------------------------------+")
			print("  [+] Kode Negara : %s"%(j["country_calling_code"]))
			print("  [+] Mata Uang   : %s"%(j["currency_name"]))
			print("  [+] Bahasa      : %s"%(j["languages"]))
			print(" +--------------------------------------+")
			print("  [+] Populasi    : %s"%(j["country_population"]))
			print("  [+] Organisasi  : %s"%(j["org"]))
			print("  [+] Time Zone   : %s"%(j["timezone"]))
			print(" +--------------------------------------+")
			exit("  [*] Website     : https://ipapi.co")
		except Exception as e:
			exit("\n  [!] Error : "+str(e)) 

__main__()