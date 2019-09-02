import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy.integrate
import numpy

def SIR_model(y,t,beta,landa):
    S,I,R=y
    dS_dt=-beta*S*I
    dI_dt=beta*S*I-landa*I
    dR_dt=landa*I
    return([dS_dt,dI_dt,dR_dt])

S0=0.99
I0=0.01
R0=0.0
beta=0.2
landa=0.08

t=numpy.linspace(0,100)

solution=scipy.integrate.odeint(SIR_model,[S0,I0,R0],t,args=(beta,landa))
solution=numpy.array(solution)

plt.figure(figsize=[6,4])
plt.plot(t,solution[:,0],label="S(t)")
plt.plot(t,solution[:,1],label="I(t)")
plt.plot(t,solution[:,2],label="R(t)")
plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("SIR model")
plt.show()
