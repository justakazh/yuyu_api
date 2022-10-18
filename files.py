from multiprocessing.dummy import Pool
import requests
import re



class check:
	def __init__(self, subdomain, timeout=4):
		self.timeout = timeout
		file_list = [
			"/.git/HEAD",
			"/.git/config",
			"/.env",
			"/.env.bak",
			"/.svn",
			"/xmlrpc.php",
			"/robots.txt",
		]
		self.file_match = [
			"APP_KEY",
			"SQLite",
			"refs/heads",
			"logs/HEAD",
			"Disallow:",
			"XML-RPC server accepts POST requests only."
		]
		self.result = []
		fullpath = []
		for domain in subdomain:
			for path in file_list:
				fullpath.append(domain+path)
		x = Pool(100)
		x.map(self.scan, fullpath)
	def scan(self,domain):
		try:
			# print("checking for "+domain+" with timeout "+str(self.timeout))
			r = requests.get("http://"+domain, verify=False, headers={"user-agent": "yuyu scanner"}, timeout=self.timeout)
			if r.status_code != 200:
				r = requests.get("https://"+domain, verify=False,headers={"user-agent": "yuyu scanner"}, timeout=self.timeout)
			if self.checking(r.text):
				self.result.append(domain)

		except Exception as e:
			pass

	def checking(self, text):
		for delimiter in self.file_match:
			if delimiter in text:
				return True
				break
			else:
				pass
