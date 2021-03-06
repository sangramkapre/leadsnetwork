import os, sys, inspect
import ConfigParser
import MySQLdb as mdb

# get Conf file
cfgfile=os.path.dirname(os.path.abspath(__file__))+'/../conf/app.conf'

config = ConfigParser.ConfigParser()
config.read(cfgfile)

domain = config.get('MySql','domain')
user = config.get('MySql','user')
password = config.get('MySql','password')
db = config.get('MySql','db')

print domain, user, password, db

try:
	connection = mdb.connect(domain, user, password, db)
	cursor = connection.cursor()

	try:
		print 'drop INVITATIONS if exists'
		cursor.execute("""DROP TABLE invitations""")
	except Exception as e:
		print e

	try:
		print 'create INVITATIONS'
		cursor.execute("CREATE TABLE `invitations` (`id` int(10) unsigned NOT NULL AUTO_INCREMENT,`email` varchar(50) DEFAULT NULL, `random_string` varchar(64) DEFAULT NULL,`used` BOOL DEFAULT '0',`create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,`modified_ts` timestamp NULL DEFAULT NULL,PRIMARY KEY (`id`))")
	except Exception as e:
		print e
		
except Exception as e:
	print e

connection.close()
