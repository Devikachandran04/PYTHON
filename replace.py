f1=open("file1.txt","r")
f2=open("fi3.txt","w")
#data=f1.readlines()
#for i in data:
 #   dd=i.replace("\n",".")
#    f2.write(dd)
data=f1.read()

data=data.replace("\n",".")
f2.write(data)
f1.close()
f2.close()