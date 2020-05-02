def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x/y

    print("enter operation: ")
    print("1) add")
    print("2) subtract")
    print("3) multiply")
    print("4) divide")

choice = input("enter choice (1/2/3/4): ")

if choice == '1':
    num_1 = int(input("enter 1st number: "))
    num_2 = int(input("enter 2nd number: "))
    print("num_1", "+", "num_2", "=", add(num_1, num_2))
elif choice == '2':
    num_1 = int(input("enter 1st number: "))
    num_2 = int(input("enter 2nd number: "))
    print("num_1", "-", "num_2", "=", subtract(num_1, num_2))
elif choice == '3':
    num_1 = int(input("enter 1st number: "))
    num_2 = int(input("enter 2nd number: "))
    print("num_1", "*", "num_2", "=", multiply(num_1, num_2))
elif choice == '4':
    num_1 = int(input("enter 1st number: "))
    num_2 = int(input("enter 2nd number: "))
    print("num_1", "/", "num_2", "=", divide(num_1,num_2))
else:
    print("invalid")