"""Problem:
   Given a staircase with N stairs and a set X of steps 
   that you can take at a time i.e. {1,2} write an algorithm 
   that determines the number of possible paths to reach the 
   top of the staircase.
   Note: There are multiple solutions, however, the dynamic
   programming solution is preferable to the others. """
#It would take minimal effort to modify this to output the 
#actual paths i.e. N=4, X=[1,3,5], Paths=[[4,3,2,1,0],[4,1,0],[4,3,0]]

def num_ways(N,X,current_stair):
   ways = 0
   if current_stair == N:
      return 1; #The trivial case, only one way to get from step 4 to step 4
   for i in range(len(X)): #Walk through all the cases on the current step
      if X[i] + current_stair <= N:
         ways += num_ways(N,X,X[i] + current_stair) #if we've found a possible case take the step
   return ways

def num_ways_bottomup(N,X):
   if 0 == N:
      return 1;
   ways = list(range(N+1))
   ways[0] = 1 #Trival Solution
   for i in range(1,N+1,1):
      total = 0
      #print(i)
      for j in range(len(X)):
         #print(X[j])
         if i - X[j] >= 0:
            #print(i,"-",X[j],">=",0)
            total += ways[i-X[j]]
      ways[i] = total
      #print("ways to ",i," = ",ways[i])
   return ways[N]

N=4
#N=3
#N=2
X=[1,3,5] #Should be 3 for N = 4
#X=[1,2]    #Should be 5 for N = 4, 3 for N = 3, 2 for N = 2
x=[[1,2],[1,3,5]]
for n in range(N+1): #Use the for loops to test multiple cases.
   for i in range(len(x)):
      print("The staircase is: ",n," steps.")
      print("We can take: ",x[i]," steps at a time.")
      #print("There are: ",num_ways(n,x[i],0)," ways to the top.")
      print("There are: ",num_ways_bottomup(n,x[i])," way(s) to the top.")
      print(' ')
"""print("The staircase is: ",N," steps.")
print("We can take: ",X," steps at a time.")
#print("There are: ",num_ways(N,X,0)," way(s) to the top.")
print("There are: ",num_ways_bottomup(N,X)," ways to the top.")"""