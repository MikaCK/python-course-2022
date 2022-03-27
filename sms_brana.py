import random

def is_valid_lenght_tel_number(number: str):
    number_no_spaces =number.replace(" ", "")
    number_of_digits = len(number_no_spaces)
    
    if number_of_digits == 9:
        return True
    elif number_of_digits == 13 and number_no_spaces[0:4] == "+420":
        return True
    else:
        return False

def calc_price(message: str):
    sms = (len(message) // 180)
    
    if len(message) % 180 != 0:
        sms = sms + 1
    return sms * 3
    


tel_number = input("Phone number: ")
is_valid_number = is_valid_lenght_tel_number(tel_number)

if is_valid_number:
    text_message = input("Type message: ")
    message_price = calc_price(text_message)
    print(f'Total price:  {message_price} CZK')
else:
    print('invalid number')

