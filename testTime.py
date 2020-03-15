import datetime

string="1:33:35"

timeobj=datetime.strptime(string,'%H:%M:%S').time()

print(type(timeobj))
print(timeobj)

