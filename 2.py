s1=input()
s2=input()
x=s2[len(s2)-1]
c=0
for i in range(len(s1)):
    if(s1[i]==x):
        c+=1

print(c)
