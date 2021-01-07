class operators:

    def addition(self, var1, var2):
        return var1 + var2

    def subtraction(self, var1, var2):
        return var1 - var2

    def division(self, var1, var2):
        if var1 == 0 or var2 == 0:
            raise ZeroDivisionError
        return var1 / var2

    def multiplication(self, var1, var2):
        return var1 * var2

    def scalc(self, p1):
        istring = p1.split(",")
        res = 0

        if istring[2] == "+":
            res = self.addition(int(istring[0]), int(istring[1]))

        elif istring[2] == "-":
            res = self.subtraction(int(istring[0]), int(istring[1]))

        elif istring[2] == "*":
            res = self.multiplication(int(istring[0]), int(istring[1]))

        elif istring[2] == "/":
            res = self.division(int(istring[0]), int(istring[1]))

        return res

    def allInOne(self, var1, var2):
        result1 = self.addition(var1, var2)
        print("{0}+{1}={2}".format(var1, var2, result1))

        result2 = self.subtraction(var1, var2)
        print("{0}-{1}={2}".format(var1, var2, result2))

        result3 = self.multiplication(var1, var2)
        print("{0}*{1}={2}".format(var1, var2, result3))

        result4 = self.division(var1, var2)
        print("{0}/{1}={2}".format(var1, var2, result4))

        return {
            "addition": result1,
            "subtraction": result2,
            "multiplication": result3,
            "division": result4,
        }

class wrfile():
    def __init__(self):
        self.filename = 'output.txt'

    def read(self):
        try:
            file = open(self.filename, 'r')
        except:
            print('File does not exist')
            return
        print(file.read())

    def write(self, output):
        file = open(self.filename, 'a')
        file.write(str(output) + "\n")
        print('Output Written to the file')