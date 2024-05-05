is_hot = True
is_cold = False
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It is a lovely day")
print("Enjoy your day")


price = 1000000
has_god_credit1 = True
if has_god_credit1:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
