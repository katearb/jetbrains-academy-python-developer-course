import random
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor


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
    sum_16 = 0
    for num in check_sum:
        sum_16 += int(num)

    if sum_16 % 10 != 0:
        last_digit = str(10 - sum_16 % 10)
    else:
        last_digit = '0'
    return ''.join(card_number) + last_digit


def create_pin():
    pin = ''
    for i in range(4):
        pin += str(random.randint(0, 9))
    return pin


def check_balance(card):
    balance = cur.execute(f"SELECT balance FROM card WHERE number = '{card}'")
    balance = cur.fetchone()[0]
    return balance


def transfer_money(card, balance, amount, trnsfr_acc):
    new_balance = float(balance) - float(amount)
    cur.execute(f'UPDATE card SET balance = "{new_balance}" WHERE number = "{card}"')
    conn.commit()

    trnsfr_crd_balance = cur.execute(f'SELECT balance FROM card WHERE number = "{trnsfr_acc}"')
    trnsfr_crd_balance = cur.fetchone()[0]

    new_trnsfr_card_balance = int(trnsfr_crd_balance) + int(amount)
    cur.execute(f'UPDATE card SET balance = "{new_trnsfr_card_balance}" WHERE number = "{trnsfr_acc}"')
    conn.commit()


class Account:

    def __init__(self):
        self.card_number = self.create_card_number()
        self.pin = create_pin()

    def print_card_number(self):
        print('Your card number:\n' + self.card_number)

    def print_pin(self):
        print('Your card PIN:\n' + self.pin)

    def create_card_number(self):

        account_number = ''
        for i in range(9):
            account_number += (str(random.randint(0, 9)))

        card_number = list('400000' + account_number)

        full_number = luhn_algorithm(card_number)

        check_unique = cur.execute(f'SELECT number FROM card WHERE number = "{full_number}"')
        conn.commit()
        if check_unique != full_number:
            return full_number
        else:
            self.create_card_number()


conn: Connection = sqlite3.connect('card.s3db')
cur: Cursor = conn.cursor()


cur.execute('CREATE TABLE IF NOT EXISTS card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()

ids = 0
flag = False
while True:
    if flag:
        break

    choice = input('1. Create an account\n'
                   '2. Log into account\n'
                   '0. Exit\n')

    if choice == '1':
        new_acc = Account()
        print('Your card has been created')
        new_acc.print_card_number()
        new_acc.print_pin()

        number = new_acc.card_number
        pin = new_acc.pin
        ids += 1
        cur.execute(f'INSERT INTO card(id, number, pin) VALUES ({int(ids)}, {number}, {pin})')
        conn.commit()

    elif choice == '2':
        card = input('Enter your card number:\n')
        check_pin = str(input('Enter your PIN: '))

        find_pin = cur.execute(f"SELECT pin FROM card WHERE number = '{card}'")
        find_pin = cur.fetchone()

        if find_pin and find_pin[0] != check_pin:
            print('Wrong card number or PIN!')
            continue

        print('You have successfully logged in!')

        while True:
            choice2 = input('1. Balance\n'
                            '2. Add income\n'
                            '3. Do transfer\n'
                            '4.Close account\n'
                            '5.Log out\n'
                            '0. Exit\n')

            if choice2 == '1':
                print('Balance:', check_balance(card))

            elif choice2 == '2':
                add_income = input('Enter income: ')
                new_balance = float(check_balance(card)) + float(add_income)
                cur.execute(f'UPDATE card SET balance = "{new_balance}" WHERE number = "{card}"')
                conn.commit()
                print('Income was added.')

            elif choice2 == '3':
                print('-----TRANSFER-----')
                trnsfr_acc = input('Enter card number:\n')
                check_existence = cur.execute(f'SELECT number FROM card WHERE number = "{trnsfr_acc}"')
                check_existence = cur.fetchone()

                if luhn_algorithm(trnsfr_acc[:-1]) != trnsfr_acc:
                    print('Probably you have made a mistake')
                    continue

                if not check_existence:
                    print('Such a card does not exist.')
                    continue

                if trnsfr_acc == card:
                    print('You cannot transfer money to the same card')
                    continue

                trnsfr_acc_check = cur.execute(f'SELECT number FROM card WHERE number = "{number}"')
                trnsfr_acc_check = cur.fetchone()[0]

                if not trnsfr_acc_check:
                    print('There are no such card')
                    continue

                amount = input('Enter amount of money you want to transfer')
                balance = cur.execute(f'SELECT balance FROM card WHERE number = "{card}"')
                balance = cur.fetchone()[0]

                if float(balance) >= float(amount):
                    transfer_money(card, balance, amount, trnsfr_acc)
                    print('Success!')
                else:
                    print('Not enough money.')

            elif choice2 == '4':
                cur.execute(f'DELETE FROM card WHERE number = "{card}"')
                conn.commit()
                print('The account has been closed.')

            elif choice2 == '5':
                print('You have successfully logged out!')
                break

            else:
                flag = True
                break
    else:
        break
