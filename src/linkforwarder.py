import base64
import flask
from flask import redirect, request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<p>This service can only redirect.</p>
</br>
<p>call /redirect/{path}</p>
<p>{path} - a base64 encoded onenote link!</p>'''


@app.route('/redirect/<path>', methods=['GET'])
def redirectToPath(path):
    return redirect(base64.b64decode(path), code=302)

app.run(debug=False, host='0.0.0.0')