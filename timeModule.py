
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


