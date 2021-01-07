from mylib import Operators

def IsInRange(low_range,high_range,number):
 if number>=low_range and number<=high_range:
   return True
 else:
   return False

def Menu():

    print("Select Operation.")

    print("1.Addition")

    print("2.Subtraction")

    print("3.Multiply")

    print("4.Divide")

    print("5.scalc")

    print("6.All in one")

    print("7.Write to File")

    print("8.Read from the file")

    print("\n")

def main():

    obj = Operators()

    Menu()

    choice = input("Enter choice(1/2/3/4/5/6/7/8 or q):")

    try:

        low_range = int(input("lower range variable"))

        high_range= int(input("higher range variable"))

        var1 = int(input("first variable"))

        while not IsInRange(low_range, high_range, var1):

            var1=int(input("Re-Enter first variable"))

        var2=int(input("Enter your second variable"))

        while not IsInRange(low_range, high_range, var2):

            var2=int(input("Re-Enter your second variable in the range"))

    except ValueError:

        print('please use integers')

        return

    operation = str(input("Enter problem string like this, N1,N2,and Operator, "))

    try:

        if choice == '1':

            print("the sum of", var1, "+", var2, "=", obj.addition(var1, var2))

        elif choice == '2':

            print("the difference of:", var1, "-", var2, "=", obj.subtraction(var1, var2))

        elif choice == '3':

            print("the product of:", var1, "*", var2, "=", obj.multiplication(var1, var2))

        elif choice == '4':

            print("the quotient of:", var1, "/", var2, "=", obj.division(var1, var2))

        elif choice == '5':

            print(obj.scalc(operation))

        elif choice == '6':

            print(obj.allInOne(var1,var2))

        elif var1 >= low_range and var2 <= high_range:

            print("the sum of", var1, "+", var2, "=", obj.addition(var1, var2))

            print("the difference of", var1, "-", var2, "=", obj.subtraction(var1, var2))

            print("the product of", var1, "*", var2, "=", obj.multiplication(var1, var2))

            print("the quotient of", var1, "/", var2, "=", obj.division(var1, var2))

            print(obj.scalc(operation))

            print(obj.allInOne(var1,var2))


        elif menuChoice == 7:
                z=input("what do you want to write enter here: ")
                w=wrfile()
                w.write(z)

        elif menuChoice == 8:
            print("The file contents are: ")
            w=wrfile()
        for i in  w.read():
            print(i)

        else:

            print(IsInRange(low_range, high_range,int))

    except ZeroDivisionError:

        print("You cannot divide by zero!!")

    restart = input("Would like to try again? y for yes!")

    if restart == "y" :

        main()

    else:

        print("Thank you for using the calculator.")

    return

main()