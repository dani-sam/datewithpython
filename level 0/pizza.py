print("welcome to Python pizza deliveries!")
bill = 0
want_pizza = input("Do want pizza? Y & N:")
if want_pizza == 'Y':
    p_size = input("What size pizza do ur want? S,M,L: ")
    if p_size == 'S':
        bill = 15
        print('Your select small size & billamount is $15')
    elif p_size == 'M':
        bill = 20
        print('Your select medium size & billamount is $20')
    elif p_size == 'L':
        bill = 25
        print('Your select large size & billamount is $25')
    else:
        print('Your select size value is invalid!!!')

    add_pepperoni = input('Do you want pepperoni? Y & N: ')
    if add_pepperoni == 'Y' and p_size == 'S':
        bill += 2
    elif add_pepperoni == 'Y'and p_size == 'M ' or 'L':
        bill += 3
    add_extrachesse =input('Do you want extra chesse Y & N: ')
    if add_extrachesse == 'Y':
        bill += 1
    print(f"final bill amount is ${bill}") 
else:
    print('!!THANK YOU & VISIT AGAIN!!')

    



