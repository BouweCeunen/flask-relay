from flask import Flask, g
from flask import render_template
from nocache import nocache
import sys
from relay_pi import Relay

app = Flask(__name__)
relays = []

@app.route('/static/styles/')
@nocache
def static_css(path):
	return app.send_static_file(path)

@app.route('/static/scripts/')
@nocache
def static_js(path):
	return app.send_static_file(path)

@app.route('/con<string:relay_id>/<string:state>')
@nocache
def relay_routing(relay_id,state):
	global relays
	relays[int(relay_id)-1].go(state)
	return 'ok'

@app.route("/")
@nocache
def index():
	global relays
	if len(sys.argv) < 2:
		msg = 'Usage: \n python relay.py (True|False) 7 Kitchenrelay 11 Livingroomrelay'
		print(msg)
		return msg
	else:
		inverse = sys.argv[1].lower()
		if inverse in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
			inverse = True
		else:
			inverse = False
		args = sys.argv[2:]
		ports = args[0::2]
		names = args[1::2]
		relays = [Relay(int(port),inverse) for port in ports]
		return render_template('template.html',args=True,ports=ports,names=names)

if __name__ == "__main__":
	app.run(
		host = "0.0.0.0",
		port = 5000,
		debug = False
	)
