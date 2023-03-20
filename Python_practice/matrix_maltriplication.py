#Naive method :Multiply two matics using nested loop
X = [[1,2],[2,3]]
Y = [[2,3],[3,4]]

#2x2 matrix of o which added to our answer ,gives the answer
result = [[0,0],[0,0]]

# m xn
#iterate through the rows of x
for i in range(len(X)):
    #iterate through the column of Y
    for j in range(len(Y[0])):
        #iterate through the row of Y
        for k in range(len(Y)):
            result [i][j] += X[i][k] + Y[k][j]

for end in result:
    print(end)            
