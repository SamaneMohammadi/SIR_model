##sir model and compare real model and theory model
## author : samane


import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy.integrate
import numpy as np


##load data Co-authoship of scientists in network theory & experiments % 379 379 914
f = open("/users/samanemohamadi/ca-netscience.txt","r")
file = f.readlines()

##create graph
G = nx.Graph()
data_fb =[]

##create list and add edge
for i in range(len(file)):
    data_fb.append((file[i].split(' ')))

for i in range(len(data_fb)):
    G.add_edge(int(data_fb[i][0]),int(data_fb[i][1]))


##label
labels_node = []
nx.set_node_attributes(G, labels_node ,'labels')
for i in range(1,len(G.nodes)+1):
    labels_node.append([i,'s'])

##generate random number for seed
for i in range(1,4):
    seed = random.randrange(1,379)
    labels_node[seed-1]=[seed,'i']


S0=0.99
I0=0.01
R0=0.0
beta=0.2
landa=0.1
S = []
I = []
R = []
###get neighbors for infected node
n = 100
while n >= 0:
    for x in labels_node:
        nbr = []
        if x[1] == 'i':
            nbr =list(G.neighbors(x[0]))
            for i in nbr:
                if labels_node[i-1]==[i,'s']:
                    rnd1 = np.random.random_sample()
                    if beta >= rnd1:
                        labels_node.insert(i-1,[i, 'i'])
                        del labels_node[i]

        if x[1] == 'i':
            rnd = np.random.random_sample()
            if landa >= rnd:
                labels_node.insert(x[0]-1, [x[0], 'r'])
                del labels_node[x[0]]

    I.append((sum(i.count('i') for i in labels_node)) / 379)
    R.append((sum(i.count('r') for i in labels_node)) / 379)
    S.append((sum(i.count('s') for i in labels_node)) / 379)
    n = n - 1

##sir model of theory
def SIR_model(y,t,beta,landa):
    S,I,R=y
    dS_dt=-beta*S*I
    dI_dt=beta*S*I-landa*I
    dR_dt=landa*I
    return([dS_dt,dI_dt,dR_dt])
t=np.linspace(0,100)
solution=scipy.integrate.odeint(SIR_model,[S0,I0,R0],t,args=(beta,landa))
solution=np.array(solution)



print ("persent of suscetible:",S)
print("persent of infected ",I)
print("persent of remove",R)


##show
x  = np.arange(1,102, 1)
x = np.array(x)
S = np.array(S)
I = np.array(I)
R = np.array(R)
plt.figure(figsize=[6,4])
plt.plot(x,S,label="S(t) real ")
plt.plot(x,I,label="I(t) real")
plt.plot(x,R,label="R(t)")
plt.plot(t,solution[:,0],label="S(t) theory")
plt.plot(t,solution[:,1],label="I(t) theory")
plt.plot(t,solution[:,2],label="R(t) theory")
plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("SIR model")

plt.show()







































