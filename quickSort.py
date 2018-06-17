#QuickSort

def sort(array):
   less = []
   equal = []
   greater = []
   if len(array) > 1:
      pivot = array[0]
      for x in array:
         if x < pivot:
            less.append(x)
         if x == pivot:
            equal.append(x)
         if x > pivot:
            greater.append(x)
      return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
   # Note that you want equal ^^^^^ not pivot because mutable type
   else:  
      return array

#array = [12,4,5,6,7,3,1,15]
array = [-1, 0, 1, 2, -1, -4]
print(array)
print(sort(array))