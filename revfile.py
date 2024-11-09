f1=open("file1.txt","r")
f2=open("rev.txt","w")
data=f1.readlines()
for i in data:
    dd=data[::-1]
for i in dd:
    f2.write(i)
f1.close()
f2.close()
