def add_one(given_array):
    carry = 1
    result = [len(given_array)]
    result2 = [len(given_array)+1]
    for i in range(len(given_array)-1,0,-1):
       total = given_array[i] + carry
       print(i)
       if(total == 10):
          carry = 1
       else:
          carry = 0
       result[i] = total % 10
       result2[i+1] = total % 10
    if(carry == 1):
       result2[0] = 1
    return result

given_array = [1,2,3,4]
#given_array = [9,9,9,9]
print(given_array)
print(add_one(given_array))
