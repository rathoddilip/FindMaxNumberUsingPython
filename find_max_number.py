from custom_exception import CustomError


class FindMaximumNumber:

    # parameterized constructor
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def find_max_int_num(self):

        if (self.num1 > self.num2) and (self.num1 > self.num3):
            return self.num1
        elif self.num2 > self.num3:
            return self.num2
        elif self.num3 > self.num1:
            return self.num3
        else:
            raise CustomError("All number are same")

    def find_max_float_num(self):
        try:
            if (self.num1 > self.num2) and (self.num1 > self.num3):
                return self.num1
            elif self.num2 > self.num3:
                return self.num2
            elif self.num3 > self.num1:
                return self.num3
            else:
                raise CustomError

        except CustomError:
            print("Custom Exception All number are same")

            ''''
            docs string 
            list and dictionary
            lambda, filter and reduce'''
