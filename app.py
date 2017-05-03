import json

from flask import Flask

application = Flask(__name__)


@application.route("/resume")
def resume():
	data = open('resume.json')
	resume = json.load(data)
	return render_template("resume.html", resume=resume)


if __name__ == "__main__":
	application.run(host='0.0.0.0')
