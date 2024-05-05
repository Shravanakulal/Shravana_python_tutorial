for item in 'python':
    print(item)
print('fruits')
for items in ['apple','mango','grapes']:
    print(items)
print('numbers from 0 to 9')
for item in range(10):
    print(item)
print("skip 2's from 5 to 20")
for item in range(5,20,2):
    print(item)
print("CALCULATING TOTAL COST:")
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(f"TOTAL PRICE= {total}")
