import pdb

class g_companyData :
	def __init__(self) : 
		self.company_name = '' 
		self.href_url = ''
		self.img_src = ''
		self.incruit_cases = ''
	def converter(self, soup_data):
		pdb.set_trace()
		try :
			self.company_name = data.find('img')['alt']
		except : 
			self.comapny_name = '...'
		try :
			self.href_url = data.find('a')['href']
		except : 
			self.href_url = '/'
		try :
			self.img_src = data.find('img')['src']
		except : 
			self.img_src = '/default.img'
		try :
			self.incruit_cases = data.find('span').contents[0]
		except : 
			self.incruit_cases = '...'
