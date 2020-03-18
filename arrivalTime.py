import timeModule as T
import psycopg2

#This program  will take each line from routeTripsFilter.csv and for each 
#trip it will give arrival time for eact stop

fin=open('./routeTripsFilterWithTime.csv')
fout=open('./arrivalTime.csv','w')
fin.readline()#Skip header of file
fout.write("SrNo,routeId,tripId,stopSequence,stopId,arrivalTime\n")
conn = psycopg2.connect("dbname=pmpml user=vrushali password=openpsql")
cur=conn.cursor()
cnt=0
rowCnt=0
seqCnt=0
routeIdPrev=''
for line in fin:
	#cnt+=1
	#if cnt > 20:
	#	break
	tokens=line.split(',')
	#print(line)
	routeId=tokens[1]
	#type(routeId)
	startTime=T.create_Time(tokens[3])
	totalTime=tokens[5]
	if not (routeIdPrev==routeId):
		#startTime=T.create_Time(tokens[3])
		#totalTime=tokens[5]
		query="select count(*) from bus_routes group by route_id having route_id="+"'"+routeId+"'"
		cur.execute(query)
		numberOfStops=cur.fetchone()
		avgTime=round(int(totalTime)/(numberOfStops[0]-1))
		intervalTime=T.create_Time("0:"+str(avgTime)+":0")
		#print(str(totalTime)+"/"+str(numberOfStops)+"="+str(avgTime))
	query="select stop_seq,stop_id from bus_routes WHERE route_id="+"'"+routeId+"'"+" order by stop_seq "
	cur.execute(query)
	result=cur.fetchall()
	arrivalTime=startTime
	seqCnt=0
	for row in result:
		rowCnt+=1
		stopSeq,stopId=row
		#print(str(rowCnt)+","+routeId+","+tokens[2]+","+str(stopSeq)+","+str(stopId)+","+T.toString_Time(arrivalTime))
		#fout.write(str(rowCnt)+","+routeId+","+tokens[2]+","+str(stopSeq)+","+str(stopId)+","+T.toString_Time(arrivalTime)+"\n")
		print(str(rowCnt)+","+routeId+","+tokens[2]+","+str(seqCnt)+","+str(stopId)+","+T.toString_Time(arrivalTime))
		fout.write(str(rowCnt)+","+routeId+","+tokens[2]+","+str(seqCnt)+","+str(stopId)+","+T.toString_Time(arrivalTime)+"\n")
		arrivalTime=T.add_Time(arrivalTime,intervalTime)
		seqCnt+=1
