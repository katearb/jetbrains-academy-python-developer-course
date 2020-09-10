from decimal import Decimal


def create_matrix(num):
    rows, columns = input(f'Enter size of the {num} matrix: ').split()
    matrix_list = []
    print('Enter matrix: ')
    for i in range(int(rows)):
        matrix_list.append(input().split())

    return Matrix(matrix_list)


class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix = matrix_list

    def m_float(self):
        matrix_float = []
        for row in self.matrix:
            matrix_float.append([float(el) for el in row])

        return Matrix(matrix_float)

    def add(self, matrix2):
        if len(self.matrix) == len(matrix2.matrix) and len(self.matrix[0]) == len(matrix2.matrix[0]):
            result = []

            for ind_row, row in enumerate(self.matrix):
                el_addition = []
                for ind_el, el in enumerate(row):
                    el_addition.append(float(el) + float(matrix2.matrix[ind_row][ind_el]))
                result.append(el_addition)

            return Matrix(result)
        else:
            return []

    def multiply(self, constant):
        result = []
        for row in self.matrix:
            row_result = []
            for el in row:
                row_result.append(str(float(el) * constant))
            result.append(row_result)

        return Matrix(result)

    def multiply_matrices(self, matrix2):
        if len(self.matrix[1]) == len(matrix2.matrix):
            new_matrix = []
            for row in range(int(self.matrix[0][0])):
                new_matrix.append([])
                for column in range(len(matrix2.matrix[1][0])):
                    new_matrix[-1].append(0)

            for ind_row, row in enumerate(new_matrix):
                for ind_el, el in enumerate(row):
                    first_m_row = self.matrix[ind_row]
                    second_m_col = []
                    for sec_m_row in matrix2:
                        second_m_col.append(sec_m_row[ind_el])

                    new_el = 0
                    for i in range(len(first_m_row)):
                        new_el += float(first_m_row[i]) * float(second_m_col[i])

                    new_matrix[ind_row][ind_el] = str(new_el)

            return Matrix(new_matrix)
        else:
            return []

    def transpose(self, choice):
        if choice == '1':
            result = []
            for i in range(len(self.matrix)):
                result.append([])

            for row in self.matrix:
                for ind_el, el in enumerate(row):
                    result[ind_el].append(el)
            return Matrix(result)

        elif choice == '2':
            result_main = self.transpose('1')
            main_reverse = []
            for row in result_main.matrix:
                main_reverse.append(row[::-1])
            result = main_reverse[::-1]

            return Matrix(result)

        elif choice == '3':
            result = []
            for row in self.matrix:
                result.append(row)
            for ind, row in enumerate(result):
                result[ind].reverse()
            return Matrix(result)

        elif choice == '4':
            return Matrix(self.matrix[::-1])

        else:
            print('Unknown command')
            return []

    def calculate_det(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        else:
            result = 0
            indices = list(range(len(self.matrix)))
            if len(self.matrix) == 2 and len(self.matrix[0]) == 2:
                result = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
                return result

            for fc in indices:
                As = self.matrix[:]
                As = As[1:]
                height = len(As)
                for i in range(height):
                    As[i] = As[i][0:fc] + As[i][fc + 1:]
                sign = (-1) ** (fc % 2)
                sub_det = Matrix(As).calculate_det()
                result += sign * self.matrix[0][fc] * sub_det
            return result

    def inverse(self):
        det = self.calculate_det()
        if det != 0:
            ct = self.transpose('1')
            inverse_matrix = ct.multiply(1/det)
            result = []
            for i, row in enumerate(inverse_matrix.matrix):
                result.append([round(float(el), 2) for el in row])
            return Matrix(result)
        else:
            return []

    def print_matrix(self):
        if not self.matrix:
            print('The operation cannot be performed.')
        else:
            print('The result is: ')
            for row in self.matrix:
                print(' '.join(list(map(str, row))))


while True:
    print('1. Add matrices\n'
          '2. Multiply matrix by a constant\n'
          '3. Multiply matrices\n'
          '4. Transpose matrix\n'
          '5. Calculate a determinant\n'
          '6. Inverse matrix\n'
          '0. Exit')
    choice = input('Your choice: ')

    if choice == '1':
        matrix1 = create_matrix('first')
        matrix2 = create_matrix('second')

        result = matrix1.add(matrix2)
        result.print_matrix()

    elif choice == '2':
        matrix = create_matrix('')
        const = float(input('Enter the number: '))

        result = matrix.multiply(const)
        result.print_matrix()

    elif choice == '3':
        matrix1 = create_matrix('first')
        matrix2 = create_matrix('second')
        result = matrix1.multiply_matrices(matrix2)
        result.print_matrix()

    elif choice == '4':
        print('1. Main diagonal\n'
              '2. Side diagonal\n'
              '3. Vertical line\n'
              '4. Horizontal line')

        choice = input('Your choice: ')
        matrix = create_matrix('')
        result = matrix.transpose(choice)
        result.print_matrix()

    elif choice == '5':
        matrix = create_matrix('')
        matrix_float = matrix.m_float()
        print('The result is:\n', matrix_float.calculate_det())

    elif choice == '6':
        matrix = create_matrix('')
        matrix_float = matrix.m_float()
        result = matrix_float.inverse()
        if not result:
            print('This matrix doesn\'t have an inverse')
        result.print_matrix()

    elif choice == '0':
        break

    else:
        print('Unknown command')
