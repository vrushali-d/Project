#This program will find routes which are in one file but not in other file
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
	routeId=tokens[2].strip()+"-"+tokens[1][0].upper()
	if not(routeIdPrev == routeId):
		listTrip.append(routeId)
		routeIdPrev=routeId
		cnt+=1
print('Number of elements in list1:'+str(cnt))


listRoute=[]

#Take data from file2 to list
finRoute.readline()
finRoute.readline()


cnt=0
for line in finRoute:
	listRoute.append(line[1:len(line)-1])
	#print(line[0:len(line)-1])
	cnt+=1
#print(listRoute)
print('Number of routes in list2:'+str(cnt))

#for every element of list1 check if it is in list 2
#if not then save in list 3 and print also

cnt=0
for route in listRoute:
	if not (route in listTrip):
		print(route)
		cnt+=1

print("Non present stops:"+str(cnt))






