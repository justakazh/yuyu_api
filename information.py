from Wappalyzer import Wappalyzer, WebPage
from multiprocessing.dummy import Pool
import requests
import re



class check:
	def __init__(self, subdomain):
		self.result = []
		x = Pool(int(len(subdomain)))
		x.map(self.scan, subdomain)
	def scan(self,domain):
		try:
			site = "http://"+domain
			r = requests.get(site).text
			title = re.findall("<title>(.*?)</title>", r)[0]
			wappalyzer = Wappalyzer.latest()
			webpage = WebPage.new_from_url(site)
			wp = wappalyzer.analyze_with_versions(webpage)
			# print([domain,wp,title])
			self.result.append([domain, wp, title])
		except Exception as e:
			pass
			# print(e)