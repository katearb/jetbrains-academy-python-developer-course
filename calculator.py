from collections import deque

print('Hi, welcome to my calculator.'
      '\n If you need some help, type /help.'
      '\n If you want to close the calculator, type /exit')


def prepare_data(input_data):
    data = []
    number: str = ''
    for s in input_data:
        if s in var_dict.keys():
            data.append(var_dict[s])
        else:
            try:
                int(s)
            except ValueError:
                if number != '':
                    data.append(number)
                    number = ''
                data.append(s)

            else:
                number += s
    if len(number) > 0:
        data.append(number)

    if ('(' in data and ')' not in data) or (')' in data and '(' not in data):
        print('Invalid expression')
        return False
    else:
        new_data = []
        for item in data:
            item = str(item)

            if len(new_data) and item in new_data[-1] and (item == '-' or item == '+'):
                new_data[-1] += item
            else:
                new_data.append(item)

        for i, item in enumerate(new_data):
            if '-' in item:
                minus_count = item.count('-')
                if minus_count % 2 == 0:
                    new_data[i] = '+'
                else:
                    new_data[i] = '-'
            elif '+' in item:
                new_data[i] = '+'

        return deque(new_data)


def postfix(data):
    nums = deque()
    operators = deque()
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for item in data:
        if str(item) not in '+-*/()':
            nums.append(int(item))
        else:
            if len(operators) == 0:
                operators.append(item)
            elif item == '(':
                operators.append('(')
            elif item == ')':
                operators.append(')')
                while len(operators):
                    check = operators.pop()
                    operators.append(check)
                    if check == ')':
                        operators.pop()
                    elif check != '(':
                        nums.append(operators.pop())
                    else:
                        operators.pop()
                        break
            else:
                check = operators.pop()
                operators.append(check)
                if check == '(':
                    operators.append(item)
                elif priority[item] > priority[check]:
                    operators.append(item)
                elif priority[item] <= priority[check]:

                    for i in range(len(operators)):
                        nums.append(operators.pop())
                    operators.append(item)

    while len(operators) > 0:
        nums.append(operators.pop())
    return nums


def multi_operations(data):
    stack = deque()
    try:
        stack.append(data.popleft())
    except (TypeError, AttributeError):
        return None
    else:
        stack.append(data.popleft())

    for item in data:
        try:
            int(item)
        except ValueError:
            if item in var_dict:
                stack.append(var_dict[item])
            else:

                try:
                    second_num = int(stack.pop())
                    first_num = int(stack.pop())
                except ValueError:
                    print('Invalid expression')
                    break
                if '-' == item:
                    stack.append(first_num - second_num)
                elif '+' == item:
                    stack.append(first_num + second_num)
                elif '*' == item:
                    stack.append(first_num * second_num)
                elif '/' == item:
                    stack.append(first_num / second_num)
                else:
                    stack.append(first_num ** second_num)

        else:
            stack.append(item)
    return stack[0]


def variables_store(data_list):
    if data_list.count('=') == 1:
        data_list = data_list.split('=')
        identifier = data_list[0]
        variable = data_list[1]
        if not identifier.isalpha():
            print('Invalid identifier')
        else:
            try:
                variable = int(variable)
            except ValueError:
                if variable in var_dict.keys():
                    var_dict[identifier] = var_dict[variable]
                elif variable.isalpha():
                    print('Unknown variable')
                else:
                    print('Invalid assignment')
            else:
                var_dict[identifier] = variable

    else:
        print('Invalid assignment')


var_dict = {}

while True:
    input_data = input().replace(' ', '')
    if input_data.isdigit() or input_data in var_dict.keys() or input_data.startswith('-') or len(input_data) == 1 or input_data.isalpha():
        try:
            int(input_data)
        except ValueError:
            if input_data[0] in var_dict.keys():
                print(var_dict[input_data[0]])
                continue
            else:
                print('Unknown variable')
                continue
        else:
            print(input_data)
            continue

    if '=' in input_data:
        variables_store(input_data)
        continue
    elif input_data.startswith('/'):
        if input_data[1:] == 'exit':
            print('bye!')
            break
        elif input_data[1:] == 'help':
            print('This calculator is able to add and subtract many numbers (both positive and negative) '
                  'and save the result of the operations into variables.'
                  '\nJust type your expression'
                  '\nIf you want to close the calculator, type /exit')
            continue
        else:
            print('Unknown command')
            continue
    elif input_data == ' ' or input_data == '':
        continue

    data = prepare_data(input_data)  # deque
    if data:
        postfix_data = postfix(data)  # deque
        result = multi_operations(postfix_data)
        if result is not None:
            print(result)
    else:
        continue
