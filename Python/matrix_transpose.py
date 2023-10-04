import time
list1 = []
rows = int(input("Enter the dimension of the square matrice: "))
time.sleep(0.5)
columns = rows

print("\nEnter the elements of the matrix: \n")
time.sleep(0.5)

for i in range(rows):
    row1 = []
    for j in range(columns):
        a = int(input("\tPosition " + str(i) + "," + str(j) + ": "))
        row1.append(a)
        time.sleep(0.5)
    list1.append(row1)

print("\nAll elements are inserted successfully")
time.sleep(0.5)
print("Displaying the given matrix...")
time.sleep(0.5)

for i in range(rows):
    print("\t[", end=" ")
    for j in range(columns):
        print(list1[i][j], end=" ")
    print("]")

for i in range(rows):
    for j in range(i+1, rows):
        list1[i][j], list1[j][i] = list1[j][i], list1[i][j]

time.sleep(0.5)
print("\nDisplaying the transpose matrix...")
time.sleep(0.5)

for i in range(rows):
    print("\t[", end=" ")
    for j in range(columns):
        print(list1[i][j], end=" ")
    print("]")
