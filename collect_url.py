import requests
import json


class check:
	def __init__(self, domain):
		self.result = []
		self.wayback(domain)


	def wayback(self,domain):
		r = requests.get("http://web.archive.org/cdx/search/cdx?url=*."+domain+"/*&output=json&fl=original&collapse=urlkey").text
		j = json.loads(r)
		for i in j:
			self.result.append(i[0])