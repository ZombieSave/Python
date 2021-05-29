class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix

    @property
    def matrix(self):
        return self._matrix

    def __str__(self):
        for i in self._matrix:
            for j in i:
                print(j, end="  ")
            print()

        return str()

    def __add__(self, other):
        result = []

        for i, item in enumerate(self._matrix):
            result.append([x+y for x, y in zip(item, other.matrix[i])])

        return Matrix(result)


matrix_1 = [[31, 22],
           [37, 43],
           [51, 86]]
matrix_2 = [[31, 22],
           [37, 43],
           [51, 86]]
m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)
m_3 = m_1 + m_2 + m_1

print(f"Результат сложения матриц:")
print(m_3)





