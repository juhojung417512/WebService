from flask import Flask , render_template
import requests
import codecs
from bs4 import BeautifulSoup
from parser import Crawler
import pdb

app = Flask(__name__)

@app.route('/')
def home():
	crawler = Crawler()
	crawler.body_filed_crawling('div','class','company')
	return render_template('home.html',data = ''.join(crawler.data))

