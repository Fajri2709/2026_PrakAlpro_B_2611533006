height = int(input("Enter the height of the triangle: "))
for rows in range(height, 0, -1):
    for columns in range(1, rows + 1):
        print("*", end=" ")
    print()