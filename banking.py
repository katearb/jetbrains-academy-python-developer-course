import random


def luhn_algorithm(card_number: list):

    number_int = list(map(int, card_number))

    double_num = []  # step 2
    for ind, num in enumerate(number_int):
        if ind % 2 == 0:
            double_num.append(num * 2)
        else:
            double_num.append(num)

    subtract_over_9 = []  # step 3
    for num in double_num:
        if num > 9:
            subtract_over_9.append(num - 9)
        else:
            subtract_over_9.append(num)

    check_sum = subtract_over_9  # step 4
    sum = 0
    for num in check_sum:
        sum += int(num)

    if sum % 10 != 0:
        last_digit = str(10 - sum % 10)
    else:
        last_digit = '0'
    return ''.join(card_number) + last_digit


def create_card_number():
    account_number = ''
    for i in range(9):
        account_number += (str(random.randint(0, 9)))

    card_number = list('400000' + account_number)

    full_number = luhn_algorithm(card_number)

    if full_number not in account_base:
        return full_number
    else:
        create_card_number()


def create_pin():
    pin = ''

    for i in range(4):
        pin += str(random.randint(0, 9))
    return pin


class Account:

    def __init__(self):
        self.card_number = create_card_number()
        self.pin = create_pin()
        account_base[self.card_number] = self.pin

    def print_card_number(self):
        print('Your card number:\n'+self.card_number)

    def print_pin(self):
        print('Your card PIN:\n'+self.pin)


account_base = {}
while True:
    print('1. Create an account\n'
          '2. Log into account\n'
          '0. Exit')

    choice = input()

    if choice == '1':
        new_acc = Account()

        print('Your card has been created')
        new_acc.print_card_number()
        new_acc.print_pin()

    elif choice == '2':
        check_card = input('Enter your card number:\n')

        if check_card in account_base:
            check_pin = input('Enter your PIN:\n')
            if account_base[check_card] == check_pin:
                print('You have successfully logged in!')
            else:
                print('Wrong card number or PIN!')
        else:
            print('Wrong card number.')
    elif choice == '0':
        break
