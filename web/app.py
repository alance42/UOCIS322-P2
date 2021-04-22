"""
Avi Lance's Flask API.
"""
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<path:pathstr>")
def pages(pathstr):
	forbiddenChar = ("//", "..", "~")

	pages = os.path.join(os.path.dirname( __file__ ), 'templates')
	pagelist = os.listdir(pages)

	if any(ele in pathstr for ele in forbiddenChar):
		abort(403)
	elif not pathstr in pagelist:
		abort(404)
	elif pathstr in pagelist:
		return render_template(pathstr), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def file_forbidden(e):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
