"""
def quadrado(num):
	x=num**2
	return x

def quadrado(num):
	return num**2

def quadrado(num):return num**2 
"""
import time

x = 4
z = list(range(1,6))

quadrado = lambda num: num*num
par = lambda x: x%2==0
index0 = lambda x: x[0]
inverter = lambda x: x[::-1]



print(quadrado(x),par(x),index0(z),inverter(z))
time.sleep(6)

