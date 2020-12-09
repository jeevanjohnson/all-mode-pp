from flask import *
import os
from time import sleep 
from threading import Thread
import config
from get_users import main
import asyncio

def mins_to_seconds(mins):
	return mins * 60

lb = ''

def reset_lb():
	while True:
		sleep(mins_to_seconds(20))
		lb = asyncio.run(main())
	
lb = asyncio.run(main())
Thread(target=reset_lb).start()

app = Flask(__name__)
app.secret_key = 'balls'
url = config.url
global_message = config.global_message

@app.errorhandler(404)
def error(e):
	return redirect('lb')

@app.route('/lb')
def leaderboard():
	if request.args:
		method = request.args.get('name')
	else:
		method = 'none'
		session['n'] = 0
	file = lb.splitlines()
	_file = []
	if 'n' not in session:
		n = 0
	else:
		n = session['n']
	if n == 0 or n == -100:
		x = 0
	else:
		x = n - 50
	for f in file if n == 0 else file[n:]:
		if x == n + 50:
			break
		f = f.split('|')
		f[0] = f[0][6:]	
		f[1] = f[1][7:]
		f[2] = f[2][12:]
		f[3] = f[3][1:]
		_file.append(f)
		x += 1
	if 'n' not in session:
		if method == 'right':
			session['n'] = 50
		else:
			session['n'] = 0
	else:
		if method == 'right':
			session['n'] += 50
		else:
			session['n'] -= 50
	return render_template('index.html', 
	leaderboard = _file, 
	url = url,
	global_message = global_message
	)
	
app.run(threaded=True, port=5000)