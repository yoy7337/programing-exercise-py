# 6.2 - Write Your Own Functions
# Solutions to review exercises


# Exercise 1
def cube(num):
    """Return the cube of the input number."""
    cube_num = num**3  # Could also use pow(num, 3)
    return cube_num

a = cube(0)

print("0 cubed is " + a)
print(f"0 cubed is {a}" )
print(f"2 cubed is {cube(2)+cube(3)}")


# Exercise 2
def greet(name):
    """Display a greeting."""
    print(f"Hello {name}!")


greet("Guido")