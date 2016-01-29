from random import randint
import time
avg=0
i=0
while i < 100:
    start= time.time()
    randint(0,100) + randint(0,100)
    end = time.time()
    avg = avg + (end -start)
    i += 1
print "The average time taken by my processor to perform an add is %s seconds " %avg   
