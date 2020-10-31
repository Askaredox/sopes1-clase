import pymysql
import pymysql.cursors

class Mysql:
	SQL = "select * from Usuario"	#COLOCAR CONSULTA AQUÍ

	def __init__(self):
		self.connection = pymysql.connect(
		# host="localhost", 
		host='34.72.187.239',
		user="admin", 
		passwd="admin", 
		db="Sopes1", 
		cursorclass=pymysql.cursors.DictCursor, 
		sql_mode=''
	)

	def consulta(self, num):
		with self.connection.cursor() as cursor:
			cursor.execute(self.SQL)
			res = cursor.fetchall()
		self.connection.close()
		return res

	def login(self,usr1,pasw):
		with self.connection.cursor() as cursor:
			cursor.execute('select * from Usuario where usuario=\''+usr1+'\' and contraseña=\''+pasw+'\'')
			res = cursor.fetchall()
		self.connection.close()
		return res

	def register(self,name,user,pasw):
		with self.connection.cursor() as cursor:
			cursor.execute('insert into Usuario(nombre,usuario,contraseña) values(\''+name+'\',\''+user+'\',\''+pasw+'\')')
			res = cursor.fetchall()
		self.connection.close()
		return res