numbers=[5,2,1,7,4]
print("add element at end")
numbers.append(20)
print(numbers)
print("add element at any position")
numbers.insert(36,4)
print(numbers)
print("remove element at end")
numbers.remove(6)
print(numbers)

print("remove element at end")
numbers.pop()
print(numbers)
print("to know index")
print(numbers.index(20))
print("check existence of an element in the list")
print(10 in numbers)
print("sort in ascending")
numbers.sort()
print(numbers)
print("delete all elements")
numbers.clear()
print(numbers)
print("remove duplicate elements in list")
nums=[2,2,4,6,3,4,6,1]
unique=[]
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)

