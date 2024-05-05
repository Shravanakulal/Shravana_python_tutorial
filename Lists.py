names=['annie','jose','luv','ajay','john']
print(names)
print(names[0])
print(names[-1])
print(names[0])
print(names[2:])
print(names[2:4])
print(names[:])
names[1]='joe'
print(names)
print("FIND LARGEST NUMBER IN A LIST")
numbers=[8,4,2,19,4,0]
max=numbers[0]
for num in numbers:
    if max<num:
        max=num
print(f"GREATEST NUMBER IN THE LIST IS {max}")