#-*- coding: utf-8 -*-
# 파서 부분 
# bs4 사용하여 crawling
import requests
from bs4 import BeautifulSoup
import pdb
from selenium import webdriver 
from pyvirtualdisplay import Display
class Crawler :
	def __init__(self):
		#chrome browser를 열기위한 display 실행
		display = Display(visible=0, size=(800, 800))  
		display.start()
		# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
		self.driver = webdriver.Chrome('/usr/bin/chromedriver')
		self.driver.implicitly_wait(3)# 암묵적으로 웹 자원을 최대 3초 기다림
		self.driver.get('http://www.gamejob.co.kr/main/home')# 로그인 페이지 이동
		self.html = self.driver.page_source
		self.soup = BeautifulSoup(self.html, 'html.parser')
		self.data = [] 
		self.driver.quit()
	def body_filed_crawling(self,html_type,find_type,value):
		result = self.soup.find(html_type,{find_type : value})
		if result :
			print(result)
			self.data.append(result)
		else :
			print('cant find')
	def login_page_crawling(self):
		driver.find_element_by_name('M_ID').send_keys('kevin7274')
		driver.find_element_by_name('M_PWD').send_keys('j1247324')
