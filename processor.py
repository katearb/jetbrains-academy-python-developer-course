def input_two_matrices():

    first_matrix_size = input('Enter size of first matrix: ').split()
    first_matrix = []
    print('Enter first matrix:\n')
    for row in range(int(first_matrix_size[0])):
        first_matrix.append(input().split())

    second_matrix_size = input('Enter size of second matrix: ').split()
    second_matrix = []
    print('Enter second matrix:\n')
    for row in range(int(second_matrix_size[0])):
        second_matrix.append(input().split())

    return first_matrix_size, second_matrix_size, first_matrix, second_matrix


def input_matrix():
    matrix_size = input('Enter size of matrix: ').split()

    matrix = []
    print('Enter matrix: ')
    for i in range(int(matrix_size[0])):
        matrix.append(input().split())

    return matrix_size, matrix


def addition():
    first_matrix_size, second_matrix_size, first_matrix, second_matrix = input_two_matrices()

    if first_matrix_size == second_matrix_size:
        result = []
        for ind_row, row in enumerate(first_matrix):
            el_addition = []
            for ind_el, el in enumerate(row):
                el_addition.append(str(float(el) + float(second_matrix[ind_row][ind_el])))
            result.append(el_addition)

        print('The result is:\n')
        for row in result:
            print(' '.join(row))
    else:
        print('The operation cannot be performed.')


def multiplication_by_number():
    matrix_size = input('Enter size of matrix: ').split()

    matrix = []
    print('Enter matrix: ')
    for i in range(int(matrix_size[0])):
        matrix.append(input().split())

    number = float(input('Enter constant: '))

    result = []
    for row in matrix:
        row_result = []
        for el in row:
            row_result.append(str(float(el) * number))
        result.append(row_result)

    print('The result is:\n')
    for row in result:
        print(' '.join(row))


def multiplication_matrices():
    first_matrix_size, second_matrix_size, first_matrix, second_matrix = input_two_matrices()

    if first_matrix_size[1] == second_matrix_size[0]:
        new_matrix = []
        for row in range(int(first_matrix_size[0])):
            new_matrix.append([])
            for column in range(int(second_matrix_size[1])):
                new_matrix[-1].append(0)

        for ind_row, row in enumerate(new_matrix):
            for ind_el, el in enumerate(row):
                first_m_row = first_matrix[ind_row]
                second_m_col = []
                for sec_m_row in second_matrix:
                    second_m_col.append(sec_m_row[ind_el])

                new_el = 0
                for i in range(len(first_m_row)):
                    new_el += float(first_m_row[i]) * float(second_m_col[i])

                new_matrix[ind_row][ind_el] = str(new_el)

        for row in new_matrix:
            print(' '.join(row))


def transpose():
    print('1. Main diagonal\n'
          '2. Side diagonal\n'
          '3. Vertical line\n'
          '4. Horizontal line')

    choice = input('Your choice: ')

    matrix_size, matrix = input_matrix()

    if choice == '1':
        new_matrix = []
        for i in range(int(matrix_size[1])):
            new_matrix.append([])

        for row in matrix:
            for ind_el, el in enumerate(row):
                new_matrix[ind_el].append(el)
    elif choice == '2':
        new_matrix = []
        for i in range(int(matrix_size[1])):
            new_matrix.append([])

        for row in matrix:
            for ind_el, el in enumerate(row):
                new_matrix[ind_el].append(el)

        for ind, row in enumerate(matrix):
            new_matrix[ind].reverse()

        new_matrix.reverse()
    elif choice == '3':
        new_matrix = []
        for row in matrix:
            new_matrix.append(row)
        for ind, row in enumerate(new_matrix):
            new_matrix[ind].reverse()
    elif choice == '4':
        new_matrix = matrix[::-1]
    else:
        print('Unknown command')
        return False

    for row in new_matrix:
        print(' '.join(row))


def calculate_determinant():
    matrix_size, matrix = input_matrix()

    if matrix_size == ['1', '1']:
        return matrix
    elif matrix_size == ['2', '2']:
        answer = int(matrix[0][0]) * int(matrix[1][1]) - int(matrix[0][1]) * int(matrix[1][0])
    else:
        m = int(matrix_size[0]) // 2
        pivot = matrix[m][m]

        pivot_row = matrix[m]
        pivot_col = []
        for ind, row in enumerate(matrix):
            pivot_col.append(matrix[ind][m])

        new_matrix = matrix
        new_matrix.remove(matrix[m])
        for ind, row in enumerate(matrix):
            new_matrix.append(matrix[ind][m])


while True:
    print('1. Add matrices\n'
          '2. Multiply matrix by a constant\n'
          '3. Multiply matrices\n'
          '4. Transpose matrix\n'
          '5. Calculate a determinant\n'
          '0. Exit')
    choice = input('Your choice: ')
    
    if choice == '1':
        addition()
    elif choice == '2':
        multiplication_by_number()
    elif choice == '3':
        multiplication_matrices()
    elif choice == '4':
        transpose()
    elif choice == '5':
        calculate_determinant()
    elif choice == '0':
        break
    else:
        print('Unknown command')
