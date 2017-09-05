import random, numpy, math
import matplotlib.pyplot as plt


print "Introduce betta parameter (range[0,1])"
betta=input()

print "Introduce alpha parameter (range[0,1])"
alpha=input()

print "Introduce initial temperature (T)"
t_inicial=input()

def sim_anneal():
	y=0
	t_anterior=t_inicial/alpha #Multiply by alpha to start at initial temperature
	p_actual=0
	while True:
		T=funcion_Temperatura(t_anterior)
		if T<=0.01 :
			return p_actual,y
		t_anterior=T	
		p_seguinte=funcion_vecinho(p_actual)
		custo=funcion_custo(p_seguinte)-funcion_custo(p_actual)
		if custo>0:
			p_actual=p_seguinte
		else:
			if (math.exp((custo)/T)>random.uniform(0,1)):
				p_actual=p_seguinte

		
		y=funcion_custo(p_actual)
		print y
		
		plt.plot(p_actual, y, 'b^')

def funcion_Temperatura(temp):
	t=betta*temp  #Change the formula
	return t

def funcion_vecinho(p_actual):
	vecinho=random.uniform((-alpha*40)+p_actual,(alpha*40)+p_actual)
	if vecinho<0 or vecinho >40:
		return funcion_vecinho(p_actual)
	return vecinho

def funcion_custo(x):
	y=numpy.sin(0.15*x)+numpy.cos(x)
	return y


print sim_anneal()

plt.show()