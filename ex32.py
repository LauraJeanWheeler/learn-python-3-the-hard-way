the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for i in the_count:
    print(f"The count is {i}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"We got {i}")

elements = []

for i in range(0,6):
    print(f"Addong {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")