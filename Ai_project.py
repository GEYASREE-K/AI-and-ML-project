import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

P=np.array([2,2])
Q=np.array([6,-1])
R=np.array([7,3])
S=(Q+R)*0.5 #since s is median S=(Q+R)/2
dvec=np.array([-1,1])
omat=np.array([[0,1],[-1,0]])
PS=np.vstack((P,S)).T

#solving for equation of line
def dir_vec(PS):
   return np.matmul(PS,dvec)
def norm_vec(PS):
   return np.matmul(omat,np.matmul(PS,dvec))

A=(norm_vec(PS)).T   
print(str(A)+str("(x-")+str(dvec)+str(")=0"))      #printing equation of parallel line passing through (-1,1)

#drawing graphs
len=10
lam_1=np.linspace(0,1,len)
x_PQ =np.zeros((2,len)) #2x10 matrix of zeros with x values in first row and y values in second row
x_QR =np.zeros((2,len))
x_RP =np.zeros((2,len))
x_PS=np.zeros((2,len))
x_xd=np.zeros((2,len))

for i in range(len):
  temp1=P+lam_1[i]*(Q-P)
  x_PQ[:,i]=temp1.T #takes ith coloumn and T is self transpose
  temp2=Q+lam_1[i]*(R-Q)
  x_QR[:,i]=temp2.T
  temp3=R+lam_1[i]*(P-R)
  x_RP[:,i]=temp3.T
  temp4=P+lam_1[i]*(S-P)
  x_PS[:,i]=temp4.T

plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')  
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')  
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')  
plt.plot(x_PS[0,:],x_PS[1,:],label='$PS$') 


plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.05),P[1]*(1-0.05),'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1-0.03),Q[1]*(1-0.05),'Q')
plt.plot(R[0],R[1],'o')
plt.text(R[0]*(1),R[1]*(1),'R')
plt.plot(S[0],S[1],'o')
plt.text(S[0]*(1+0.01),S[1],'S')

#plotting parallel line
lam_2=np.linspace(-2,2,len)
for i in range(len):
 temp5=dvec+lam_2[i]*(dir_vec(PS))
 x_xd[:,i]=temp5.T
plt.plot(x_xd[0,:],x_xd[1,:])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.show()

   
