import os

location = '/home/pi/pyobd-pi/log'
for filename in os.listdir(location):
    if filename == 'Datos_carro.log':
       f  = open(os.path.join(location, 'Datos_carro.log'), "r")

       lst = []
       for line in f:
           lst.append(line.strip())



#print(lst)

Time = []
RPM = []
mph = []
thr = []
load = []
fuel = []

lst.pop(0)

for i in lst:
    each = i.split(",")
    Time.append(each[0])
    RPM.append(float(each[1]))
    mph.append(float(each[2]))
    thr.append(float(each[3]))
    load.append(float(each[4]))
    #fuel.append(each[5])
    #print(each)

print(Time)
#print(RPM)
#print(mph)
#print(thr)
#print(load)
