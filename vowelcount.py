V= input('Enter the proverb :')
c = 0
v= V.lower()
for j in v:
    if j == 'a'or j == 'e' or j == 'i' or j == 'o' or j == 'u' :
        c=c+1
if c== 0:
    print('No vowels found')
else:
    print(c)