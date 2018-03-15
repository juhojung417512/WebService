from flask import Flask , render_template
import requests
import codecs
from bs4 import BeautifulSoup
import parser


app = Flask(__name__)

@application.route('/')
def home():
	crawler = parser.Crawler()
	print(crawler.data)
	f = codecs.open('templates/home.html','r',encoding='utf-8')
	if f.readlines() != None : 
		f.close()
	        f = codecs.open('templates/home.html','w',encoding='utf-8')
		f.close()	
	f = codecs.open('templates/home.html','w',encoding='utf-8')
	f.write(crawler.html)
	f.close()
	return render_template('home.html')

