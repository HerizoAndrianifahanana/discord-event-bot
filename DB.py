import sqlite3

conn = sqlite3.connect('event.db')

def newActivity(title):
	conn.execute("INSERT INTO Activity VALUES('%s')" % title)
	conn.commit()
	
def getAllActivities():
	return conn.execute('SELECT * FROM Activity')

conn.execute('DROP TABLE IF EXISTS Activity')
conn.execute('CREATE TABLE Activity (title VARCHAR(255))')

for res in getAllActivities() :
	print(res)