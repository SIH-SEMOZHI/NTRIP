from Model import GNSSData
import random 
reference=[GNSSData(random.random()*0.1+11.01,random.random()*0.1+76.9,0) for i in range(10)]
client=[GNSSData(random.random()*0.1+11.01,random.random()*0.1+76.9,0) for i in range(10)]