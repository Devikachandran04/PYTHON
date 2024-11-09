length=len("thrikkarthika")
#print(length)

#below statement will lead to type error as except length all are str
#print("Your name has"+length +"characters") 

#to convert it to str for concatenate we use str()
print("Your name has "+str(length) +" characters")  
# it will concatenate

#it will not its permanent data type
print(type(length))  
# shows int



#unless we can do by conversion by declaring that to new variable &its datatype changes
n_length=str(length)
print("Your name has "+ n_length +" characters")
print(type(n_length))

#same can be done for other data types also
#int()
#float()
#bool()
print(10+10)  #20
print("10"+"10")  #1010 as these are string to convert it
print(int("10")+int("10") ) #20

#int and float
#print(10+"10") #type error
print(10+float("10"))


#value error
n="devu"
#print(10+int(n)) #--------------value error---------
n="125"
print(10+int(n))




##assignment to add 2 num by input function
a=input("enter a")
b=input("enter b")
#print(a+b)   # shows ab if a=1 ,b=2 =>12
#change it 
print(int(a)+int(b))