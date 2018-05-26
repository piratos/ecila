from flask import Flask, send_from_directory, render_template

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=BASE_DIR)
WEB_PORT = int(os.environ.get('WEB_PORT', '5000'))

@app.route('/<path:path>')
def serve(path):
	return send_from_directory(BASE_DIR, path)

@app.route('/')
def root():
	HOST_IP = os.environ.get('HOST_IP', '127.0.0.1')
	MAIN_PORT = int(os.environ.get('MAIN_PORT', '5000'))
	WEB_PORT = int(os.environ.get('WEB_PORT', '5000'))
	return render_template('index.html', **locals())


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=WEB_PORT)
