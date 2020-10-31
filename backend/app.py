from flask import Flask, request
from flask_cors import CORS
import json
from flask_mysqldb import MySQL



app = Flask(__name__)
app.config['MYSQL_HOST'] = '34.72.187.239'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'Sopes1'

mysql = MySQL(app)
CORS(app)

@app.route('/')
def check():
    return "¡Todo good!"


@app.route('/login',methods=['POST'])
def iniciarsesion():
    data = request.json
    user = data['user']
    pwd = data['pwd']
    cur = mysql.connection.cursor()
    cur.execute('select * from Usuario where usuario=\''+user+'\' and contraseña=\''+pwd+'\'')
    cur.execute('''SELECT * from Usuario''')
    rv = cur.fetchall()
    for x in rv:
        if x[2]== user and x[3]==pwd:
            return "+\""+x[1]+"\""
    return "false"

    


@app.route('/registro',methods=['POST'])
def registro():
    dato=request.json
    name=dato['name']
    user=dato['user']
    pasw=dato['pasw']
    cur = mysql.connection.cursor()
    cur.execute('insert into Usuario(nombre,usuario,contraseña) values(\''+name+'\',\''+user+'\',\''+pasw+'\')')
    mysql.connection.commit()
    cur.close()
    return "{\"data\":\"true\"}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)
    