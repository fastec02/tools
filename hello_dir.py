import os,sys
import datetime

now = datetime.date.today()

if(os.path.exists("work" + str(now.year)) == 0):
	os.mkdir("work" + str(now.year))


os.mkdir("work" + str(now.year) + "/" + str(now.month) + str(now.day) )
