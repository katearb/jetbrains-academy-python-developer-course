print(
    'Hi, welcome to my calculator.\n If you need some help, type /help.\n If you want to close the calculator, type /exit')


def addition(first_num, second_num):
    return int(first_num) + int(second_num)


def substraction(first_num, second_num):
    return int(first_num) - int(second_num)


def multi_operations(list_numbers):
    result = list_numbers[0]
    check_len = 2
    while check_len <= len(list_numbers):
        minus_count = list_numbers[check_len - 1].count('-')
        if minus_count % 2 == 0:
            result = int(addition(result, list_numbers[check_len]))
        else:
            result = int(substraction(result, list_numbers[check_len]))
        check_len += 2

    print(result)


while True:
    numbers = input()
    if len(numbers) == 0 or numbers == ' ':
        continue
    elif numbers == '/exit':
        print('bye!')
        break
    elif numbers == '/help':
        print('This calculator is able to add and subtract many numbers (both positive and negative).'
              '\nJust type your expression'
              '\nIf you want to close the calculator, type /exit')
    elif len(numbers.split()) == 1:
        print(numbers)
    else:
        numbers = numbers.split(' ')
        while '' in numbers:
            numbers.remove('')
        multi_operations(numbers)
