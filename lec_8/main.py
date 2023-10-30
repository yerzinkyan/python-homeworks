#lekcia 8
class Matrix:
    def init(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def calculate_mean(self):
        total = sum(sum(row) for row in self.matrix)
        mean = total / (self.n * self.m)
        return mean

    def calculate_row_sum(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            return None

    def calculate_column_average(self, col_index):
        if 0 <= col_index < self.m:
            col = [row[col_index] for row in self.matrix]
            average = sum(col) / self.n
            return average
        else:
            return None

    def print_submatrix(self, col1, col2, row1, row2):
        if 0 <= row1 < row2 <= self.n and 0 <= col1 < col2 <= self.m:
            submatrix = [row[col1:col2] for row in self.matrix[row1:row2]]
            for row in submatrix:
                print(" ".join(map(str, row)))
        else:
            print("Invalid submatrix coordinates")

n = 4
m = 3
my_matrix = Matrix(n, m)

my_matrix.matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# 1) Print the matrix
print("Matrix:")
my_matrix.print_matrix()

# 2) Calculate the mean of the matrix
mean = my_matrix.calculate_mean()
print("Mean of the matrix:", mean)

# 3) Calculate the sum of a given row (e.g., row 2)
row_sum = my_matrix.calculate_row_sum(2)
print("Sum of row 2:", row_sum)

# 4) Calculate the average of a given column (e.g., column 1)
col_average = my_matrix.calculate_column_average(1)
print("Average of column 1:", col_average)

# 5) Print a submatrix (e.g., rows 1-3, columns 0-2)
print("Submatrix:")
my_matrix.print_submatrix(0, 3, 1, 4)