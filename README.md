# SIR_model
The SIR Model for Spread of Disease - The Differential Equation Model
As the first step in the modeling process, we identify the independent and dependent variables. The independent variable is time  t,  measured in days. We consider two related sets of dependent variables.

The first set of dependent variables counts people in each of the groups, each as a function of time:

S = S(t) 	is the number of susceptible individuals,
I = I(t) 	is the number of infected individuals, and
R = R(t) 	is the number of recovered individuals.



The second set of dependent variables represents the fraction of the total population in each of the three categories. So, if  N  is the total population (7,900,000 in our example), we have

s(t) = S(t)/N, 	the susceptible fraction of the population,
i(t) = I(t)/N, 	the infected fraction of the population, and
r(t) = R(t)/N, 	the recovered fraction of the population.
It may seem more natural to work with population counts, but some of our calculations will be simpler if we use the fractions instead. The two sets of dependent variables are proportional to each other, so either set will give us the same information about the progress of the epidemic.
