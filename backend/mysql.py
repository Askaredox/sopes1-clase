import pymysql
import pymysql.cursors

class Mysql:
	SQL = "CONSULTA"	#COLOCAR CONSULTA AQUÍ

	def __init__(self):
		self.connection = pymysql.connect(
		# host="localhost", 
		host='172.19.0.4',
		user="root", 
		passwd="12345678", 
		db="P2Bases", 
		cursorclass=pymysql.cursors.DictCursor, 
		sql_mode=''
	)

	def consulta(self, num):
		with self.connection.cursor() as cursor:
			cursor.execute(self.SQL)
			res = cursor.fetchall()
		self.connection.close()
		return res
