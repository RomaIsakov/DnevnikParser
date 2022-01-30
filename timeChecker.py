import time
t = time.localtime()
nowTime = time.strftime("%D", t)
with open ("lastTime.txt", "r") as Time:
    lastTime=Time.read()
month=nowTime[0:2]
day=nowTime[3:5]
lastMonth=lastTime[0:2]
lastDay=lastTime[3:5]


days=int(month)*30.5+day
lastDays=int(lastMonth)*30.5+lastDay

print()
#dayDif=nowTime-lastTime
