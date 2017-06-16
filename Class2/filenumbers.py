fileName=input("what file are the numbers in?")
infile=open(fileName,'r')
sum=0.0
count= 0
line=infile.readline()
while line != "":
    for xStr in line.split(","):
        sum=sum + eval(xStr)
        count=count + 1
    line=infile.readline()
print("\n The average of the numbemyfrs is",sum / count)