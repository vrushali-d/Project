#A program to read csv file and come up with routeId and tripId
#also start time and end time for that trip

fin=open('./routeWiseTT.csv')
fout=open('./RouteTrips.csv','w')
fout.write("SrNo"+","+"RouteId"+","+"TripId"+","+"StartTime"+","+"End Time"+"\n")
fin.readline()
tokens=[];
cnt=0;
tripCnt=0;
routeIdPrev='' #route id of previous row
for line in fin:
	row=[];
	tripCnt+=1;
	cnt+=1
#	if cnt > 200:
#		break
	tokens=line.split(',');
	routeId=tokens[2].strip()+"-"+tokens[1][0].upper().strip()
	#If route id changes then start trip count from 1
	if not(routeIdPrev == routeId):
		tripCnt=1
		#print('Strings are different')
	tripId=str(routeId)+"-"+str(tripCnt)
	startTime=tokens[3]
	endTime=tokens[4]

	row.append(routeId)
	row.append(tripId)
	row.append(startTime)
	row.append(endTime)
	#Assign this route id as previuos route id
	routeIdPrev=routeId
	print(row)
	fout.write(str(cnt)+","+row[0]+","+row[1]+","+row[2]+","+row[3]+"\n")
	
	#print(routeId)
	#print(tokens)
	#print('\n')
