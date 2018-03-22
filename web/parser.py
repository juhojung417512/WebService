#-*- coding: utf-8 -*-
# 파서 부분 
# bs4 사용하여 crawling
import requests
from bs4 import BeautifulSoup
import pdb
class Crawler :
	def __init__(self):
		self.req = requests.get('http://www.devkorea.co.kr/')
		self.html = self.req.text
		self.status = self.req.status_code
		self.is_ok = self.req.ok
		self.soup = BeautifulSoup(self.html, 'html.parser')
		self.html_start = '<html lang="ko">'
     		
		self.html_end = "</html>"
		self.data = [] 
	def body_filed_crawling(self,html_type,find_type,value):
		result = self.soup.find(html_type,{find_type : value})
		if result :
			print(result)
			self.data.append(result)
		else :
			print('cant find')
	def login_filed_crawling(self):
		self.soup.find('form',{'id' :''})

