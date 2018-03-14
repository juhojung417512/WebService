from flask import Flask , render_template
from parser import parser

app = Flask(__name__)

@app.route('/')
def home():
	print(parser.soup)
	f = open('templates/home.html','w')
	f.write(parser.html)
	f.close()
	return render_template('home.html')

if __name__ == '__main__' : 
	app.run(debug=True)

