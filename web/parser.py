import requests
from bs4 import BeautifulSoup

class parser :
	def __init__(self):
		req = requests.get('http://gamejob.co.kr/main/home')
		html = req.text
		header = req.headers
		status = req.status_code
		is_ok = req.ok
		soup = BeautifulSoup(html, 'html.parser')
		data = {}
	def input_filed_crawling(self):
		input_data = soup.find('input',{'':''})
		for d in input_data : 
			data[d.text] = d.get('input')

