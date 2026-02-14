
import time
import numpy as np;
myList=[i for i in range(10000)]
startTime1=time.process_time();
myList=[i*2 for i in myList]
endTime1=time.process_time();
print(round(endTime1-startTime1,6))

a = np.array([[1, 2], [3, 4]]) 