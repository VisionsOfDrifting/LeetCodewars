"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the 
new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
def allButi(array):
   retVal = []
   for i in range(len(array)):
      product = 1
      for j in range(len(array)):
         if array[i] != array[j]:
            product *= array[j]
      retVal.append(product)
   return retVal

#array = [1,2,3,4,5]
#[120, 60, 40, 30, 24]
array = [3,2,1]
#[2, 3, 6]
print(allButi(array))

#Time 9 min 30 sec. That includes the no division.
#Would've failed though, there is an O(N) time/space solution
#and an O(N) time O(1) space solution
"""
int a[N] # This is the input
int products_below[N];
p=1;
for(int i=0;i<N;++i) {
  products_below[i]=p;
  p*=a[i];
}

int products_above[N];
p=1;
for(int i=N-1;i>=0;--i) {
  products_above[i]=p;
  p*=a[i];
}

int products[N]; # This is the result
for(int i=0;i<N;++i) {
  products[i]=products_below[i]*products_above[i];
}
"""
"""
#If you need to be O(1) in space too you can do this

int a[N] // This is the input
int products[N];

# Get the products below the current index
p=1;
for(int i=0;i<N;++i) {
  products[i]=p;
  p*=a[i];
}

# Get the products above the curent index
p=1;
for(int i=N-1;i>=0;--i) {
  products[i]*=p;
  p*=a[i];
}
"""