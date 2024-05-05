#functions, parameters, key word argument
def greet_user(firstname, lastname):
    print(f'Hi {firstname} {lastname}!')
    print('welcome aboard')
print("Start")
greet_user(firstname = "John", lastname= "Smith")
greet_user("Mary" , "Smith")
print("Finish")

#return statement
def square(number):
    return number * number
result = square(3)
print(result)
print(square(3))

#recreating the reusable function
def emoji_converter(message1):
    words=message1.split(' ')
    emojis={
        ":)" : "😊",
        ":(" : "😢",
    }
    output=""
    for word in words:
        output+= emojis.get(word,word)+ " "
    return output

message1=input(">")
print(emoji_converter(message1))
