import socket
import subprocess
import xml.etree.ElementTree as ET
import string
import random
import os
import socket
import nmap

class check:
	def __init__(self, lists = []):
		self.result = []
		for target in lists:
			self.scan(target)

	def scan(self, target):
		p_open = []
		nm = nmap.PortScanner()
		data = nm.scan(target, arguments="--open -sS -p 21,22,23,25,53,80,110,115,135,139,143,194,443,445,1433,3306,3389,5632,5900,25565")
		for i in data['scan']:
			for tcp in data['scan'][i]['tcp']:
				p_open.append(str(tcp)+"/"+data['scan'][i]['tcp'][tcp]['name'])

		self.result.append([target, p_open])