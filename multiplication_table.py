# multiplication_table.py

# Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
Enter a number to see its multiplication table: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

