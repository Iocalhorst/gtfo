import sqlite

defaults={dbname="sqlite",filename="yalp.db"}

settings=default


def setup(settings=default):
	if settings.get(dbname)="sqlite":
			import sqlite
			try :
				connection=sqlite(settings.get(filename))
				return True,connection 
			except :
				return False,None



