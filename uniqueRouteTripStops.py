#A program to read csv file and come up with routeId and tripId
#also start time and end time for that trip

fin=open('./routeWiseTT.csv')
fin.readline()
tokens=[];
cnt=0;

routeCnt=0;
routeIdPrev='' #route id of previous row
for line in fin:
	row=[];
	cnt+=1
	tokens=line.split(',');
	routeId=tokens[2]+"-"+tokens[1][0]
	#If route id changes then start trip count from 1
	if not(routeIdPrev == routeId):
		routeCnt+=1
		#print('Strings are different')
	#Assign this route id as previuos route id
	routeIdPrev=routeId
print('Total number of unique routes are:'+str(routeCnt))
