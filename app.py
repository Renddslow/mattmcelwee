import json

import requests
from flask import Flask, render_template, request
from flaskext.markdown import Markdown

application = Flask(__name__)
Markdown(application)


api_base_url = "http://api.mattmcelwee.com/v1"


@application.route("/thoughts")
def blog():
	page_param = request.args.get('page')
	page = page_param if page_param else 1
	params = {"page": page}

	posts = requests.get(api_base_url + "/blog", params=params).json()
	pagination_meta = posts['pagination']['meta']

	page_title = "Regular Musings on Scripture, God, and Spritituality"
	
	return render_template("blog.html", posts=posts['posts'],
							pagination_meta=pagination_meta, 
							page_title=page_title,
							pagination=posts['pagination']['pages'])


@application.route("/thoughts/<permalink>")
def post():
	return render_template("blog-post.html")


@application.route("/resume")
def resume():
	data = open('resume.json')
	resume = json.load(data)
	return render_template("resume.html", resume=resume)


if __name__ == "__main__":
	application.run(host='0.0.0.0')
