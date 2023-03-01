import addition, division, multiplication, subtraction


def __main__():
    while True:
        inp = int(input("""\n\nChoose Operation:    1. Addition    2. Subtraction    3. Multiplication    4. Division    5. Exit\n> """))

        if inp == 5:
            print("\nProgram exited.")
            break

        else:
            a, b = [int(i) for i in input("Enter two numbers separated by spaces: ").split(" ")]

            if inp == 1:
                print(addition.add(a, b))
            elif inp == 2:
                print(subtraction.subtract(a, b))
            elif inp == 3:
                print(multiplication.multiply(a, b))
            elif inp == 4:
                print(division.divide(a, b))
        
        
__main__()