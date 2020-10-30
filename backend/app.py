from flask import Flask, request
from flask_cors import CORS
from mysql import Mysql
import simplejson as json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origin": "*"}})

@app.route('/')
def check():
    return "¡Todo good!"

@app.route('/api/login', methods=['GET'])
def login():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    return mysql.login(user, pwd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)
    