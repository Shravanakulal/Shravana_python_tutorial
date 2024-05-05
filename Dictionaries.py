customer={
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))
customer["name"]="jack"
print(customer["name"])
print("PRINT PHONE NUMBER IN WORDS")
Nnum={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":'seven',
    "8":"eight",
    "9":"nine"
}
ph=input('phone: ')
output=""
for p in ph:
    output+=(Nnum.get(p,"!"))+ " "
print(output)
