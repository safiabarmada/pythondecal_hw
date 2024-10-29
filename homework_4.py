list = []
for i in range (0,21):
    list.append(i)
    i = i+1
print(list)

square_list = []
for number in list:
    square_list.append(number**2)
print(square_list)

def first_fifteen(list):
    return list[0:16]

print(first_fifteen(square_list))

def every_five(list):
    return list[::5]

print(every_five(square_list))

def fancy(list):
    return list[-1:-30:-3]
print(fancy(square_list))

m = []
def create2Dlist():
    for i in range(5):
        row = []
        for j in range(5):
            row.append((5*i)+j+1)
        m.append(row)
    return m

matrix = create2Dlist()
print(matrix)


for i in range(len(matrix)):
     for j in range(len(matrix)):
         if matrix[i][j] %3 == 0:
            matrix[i][j] = "?"
print(matrix)


def sum_non_question(matrix):
    sum = 0
    for row in matrix:
        for element in row:
            if element != "?":
                sum = sum + element
    return sum

print(sum_non_question(matrix))