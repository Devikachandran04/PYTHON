f=open("file1.txt","a")
f.write("apple")
f.close()

f=open("file1.txt","r")
print(f.read())
f.close()