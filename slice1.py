s="lbsitwpoojapura"
#print(s [: :-1])
#print(s[1:5])

v=" "
l=len(s)
for i in range (l):
    v=v+s[l-1: :-1]
print (v)