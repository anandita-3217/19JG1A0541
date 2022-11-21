matrix=[]
for i in range(256):         
    a =[]
    for j in range(256):     
         a.append(int(input()))
    matrix.append(a)
for i in range(256):
    for j in range(256):
        if matrix[i][j]==0:
            x,y=i,j
        print(x,y)
