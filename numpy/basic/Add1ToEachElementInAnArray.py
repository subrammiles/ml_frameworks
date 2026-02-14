import numpy as np;

A=[1,1,1,0]
R=[]
for i in A:
    R.append(i+2)
print(R)

A2=np.array(A);
print(A2+2);