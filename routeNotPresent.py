#This program will find routes which are in one file but not in other file

#This function will remove in between spaces of string
def removeSpaceInBetween(string):
	newStr=[]
	for ch in string:
		if not (ch == ' '):
			newStr.append(ch)
	return "".join(newStr)


finTrip=open('./routeWiseTT.csv')
finRoute=open('./routeIds.txt')

#Take data from file1 to list
finTrip.readline()
tokens=[]
listTrip=[]
routeIdPrev=''
cnt=0
for line in finTrip:
	tokens=line.split(',')
	tokens[2]=removeSpaceInBetween(tokens[2])
	if tokens[2][-1] == 'R':
		if tokens[2][-2] == '-':
			routeId=tokens[2][0:-1]+'R'
		else:
			routeId=tokens[2][0:-1]+'-R'
	else:
		routeId=tokens[2].strip()+"-"+tokens[1][0].upper()
	if not(routeIdPrev == routeId):
		listTrip.append(routeId)
		routeIdPrev=routeId
		cnt+=1
print('Number of elements in listTrip:'+str(cnt))

listRoute=[]

#Take data from file2 to list
finRoute.readline()
finRoute.readline()


cnt=0
for line in finRoute:
	listRoute.append(line[1:len(line)-1])
	cnt+=1
print('Number of routes in listRoute:'+str(cnt))

#for every element of list1 check if it is in list 2
#if not then save in list 3 and print also
print("List of stops which are in trips but not in route master")

cnt=0
for route in listTrip:
	if not (route in listRoute):
		print(route)
		cnt+=1

print("Non present stops:"+str(cnt))


print("List of stops which are in route Master  but not in trips")

cnt=0
for route in listRoute:
	if not (route in listTrip):
		print(route)
		cnt+=1

print("Non present stops:"+str(cnt))


