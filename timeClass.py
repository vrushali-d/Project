
class Time(object):
	"""This class will have hour minute and secs"""

def print_Time(t):
	print(str(t.hrs)+":"+str(t.min)+":"+str(t.sec))

def toString_Time(t):
	return str(t.hrs)+":"+str(t.min)+":"+str(t.sec)

def toMinutes_Time(t):
	return t.hrs*60+t.min;

def create_Time(string):
	if string == '':
		tokens="0:0:0"
	tokens=string.split(':')
	if len(tokens) == 1:
		tokens=string.split('.')
	t=Time()
	if tokens[0][-1]=='.':
		tokens[0]=tokens[0][0:-1]

	if tokens[1][-1]=='.':
		tokens[1]=tokens[1][0:-1]
	
	if tokens[2][-1]=='.':
		tokens[2]=tokens[2][0:-1]
	
	t.hrs=int(tokens[0],10)
	t.min=int(tokens[1],10)
	t.sec=int(tokens[2],10)

	return t

def subtract_Time(t1,t2):
	#t1-t2
	ans=Time()
	if t1.sec < t2.sec:
		t1.min-=1
		t1.sec+=60
		ans.sec=t1.sec-t2.sec
	else:
		ans.sec=t1.sec-t2.sec

	if t1.min < t2.min:
		t1.hrs-=1
		t1.min+=60
		ans.min=t1.min-t2.min
	else:
		ans.min=t1.min-t2.min

	if t1.hrs < t2.hrs:
		t1.hrs+=24
		ans.hrs=t1.hrs-t2.hrs
	else:
		ans.hrs=t1.hrs-t2.hrs
	return ans


def add_Time(t1,t2):
	ans=Time()
	s=0
	m=0
	h=0
	s=t1.sec+t2.sec
	if s >= 60:
		m=round(s/60)
		s=s%60
	ans.sec=s

	m=m+t1.min+t2.min
	if m >= 60:
		h=round(m/60)
		m=m%60
	ans.min=m

	h=h+t1.hrs+t2.hrs
	if h > 23:
		h=0
	ans.hrs=h
	return ans

#t1=Time()
#t1.hrs=2
#t1.min=10
#t1.sec=00

#time=toString_Time(t1)
#print(time)
#x=toMinutes_Time(t1)
#print(x)
#t2=Time()
#t2.hrs=23
#t2.min=60
#t2.sec=0

#print(t1)
#print_Time(t1)
#print_Time(t2)
#t3=add_Time(t1,t2)
#t4=subtract_Time(t1,t2)
#print_Time(t3)
#print_Time(t4)

#t=create_Time("3:45:21")
#print_Time(t)


fin=open('./routeTripsFilter.csv')
fout=open('./routeTripsFilterWithTime.csv','w')

line=fin.readline()#to ignore headers
line=line[0:-1]+",Duration\n"
fout.write(line)
cnt=0
for line in fin:
	cnt+=1
	#if cnt > 10:
	#	break
	tokens=line.split(',')
	print(tokens[4])
	print(tokens[3])
	t1=create_Time(tokens[4])
	print_Time(t1)
	t2=create_Time(tokens[3])
	print_Time(t2)
	t3=subtract_Time(t1,t2)
	diff=toMinutes_Time(t3)
	tokens.append(str(diff))
	#tokens.append="\n"
	#Problem at line 1295
	fout.write(tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]+","+tokens[4][0:-1]+","+tokens[5]+"\n")

	print(tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]+","+tokens[4]+","+tokens[5]+"\n")



