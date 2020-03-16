import datetime

string="1:33:35"
y="2:0:0"
timeobj1=datetime.datetime.strptime(string,'%H:%M:%S')

timeobj2=datetime.datetime.strptime(y,'%H:%M:%S')
#print(type(timeobj))
print(timeobj1.time()+timeobj2.time())

