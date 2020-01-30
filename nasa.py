from statistics import mean

def reader(filename):
    file= open(filename,"r")
    while True:
        yield file.readline()



reader("data.csv")

print(len(data))
masses=[]
for line in data.splitlines():
    name,id,type,recclass,mass,year,lat,long,geo=line.split(",")
    masses.append(int(mass))

print("Smallest meteorite weighed: {}".format(min(masses)))
print("Largest meteorite weighed: {}".format(max(masses)))
print("Average meteorite weighed: {}".format(mean(masses)))