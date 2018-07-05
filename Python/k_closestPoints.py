"""Problem:
   Given a set of n tupels find the k closest 
   points to the origin (0,0).
   Solution:
   First write a function that determines the 
   Euclidean distance (use Pythagoras' theorem)
   then implement a method to find the smallest k. 
"""
#  Note: A couple methods for finding smallest k are:
#  1.Using a sorting algorithm and returning the first k
#  2.Building a maxheap of the first k without sorting and
#  swaping the top element if smaller (faster than sorting)

from quickSort import sort #sort takes a list as argument
import math

def calc_distance(N):
   distance = []
   i = 0
   for a, b in N:
      distance.append(tuple((math.sqrt(a**2 + b**2),i))) 
      #will use index to hash a map when returning points
      i += 1
   return distance

def maxheap_kSort(N):

N_points = [(-2,-4),(0,-2),(-1,0),(3,-5),(-2,-2),(3,2)]
k = 3
print("The n points are: ",N_points)
N_dist = calc_distance(N_points)
#print("(Distance, index): ",N_dist)
hash_map = dict(N_dist) #dict is (key,value); D[key] returns value
#print("Our hash map: ",hash_map)
unzipped = list(zip(*N_dist)) #list1_2=zip(*list3) is the reverse of list3=zip(list1,list2) 
#print("(Distance),(indicies)",unzipped)
shortest_dist = sort(unzipped[0]) #This is solution 1 quicksort()
#print("Just distance: ",shortest_dist)
print(k,"closest points:")
for i in range(k):
   print(i+1,": ",N_points[hash_map[shortest_dist[i]]])