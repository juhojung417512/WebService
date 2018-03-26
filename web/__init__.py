# default import library
from flask import Flask , render_template
import requests
import codecs
from bs4 import BeautifulSoup
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
import pdb
# module import
from parser import Crawler

app = Flask(__name__)

log_filepath = '/home/ubuntu/WebService/web/logs'

# logging
if not app.debug:
    err_f_handler = RotatingFileHandler('{0}/error.log'.format(log_filepath), maxBytes=1024*1024*1000, backupCount=20)
    err_f_handler.setLevel(logging.ERROR)
    err_f_handler.setFormatter(Formatter(
        '----------------------------------------------------------------------------------\n'
        '[%(asctime)s] [%(levelname)s]: %(message)s'
    ))
    app.logger.addHandler(err_f_handler)

@app.route('/')
def home():
	crawler = Crawler()
	data = crawler.body_filed_crawling('div','class','company')
	return render_template('home.html',data = data)

