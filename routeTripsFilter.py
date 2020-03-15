#This program will find routes which are in one file but not in other file and create filtered file

finTrip=open('./RouteTrips.csv')
finRoute=open('./routeIds.txt')

fout=open('routeTripsFilter.csv','w')
fout.write("SrNo"+","+"routeId"+","+"tripId"+","+"startTime"+","+"EndTime"+"\n")

listRoute=[]
#Take data from routeId to list
finRoute.readline()#header
finRoute.readline()#header
cnt=0
for line in finRoute:
	listRoute.append(line[1:len(line)-1])#ignore leading space and \n
	cnt+=1
print('Number of routes in listRoute:'+str(cnt))

#Take data from file1 to list
finTrip.readline()
tokens=[]
cnt=0
for line in finTrip:
	tokens=line.split(',')
	routeId=tokens[1]
	print(routeId)
	if routeId in listRoute:
		fout.write(tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]+","+tokens[4])
		cnt+=1
print("Lines written in file:"+str(cnt))

