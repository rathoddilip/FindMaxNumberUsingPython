class FindMaximumNumber:
    num1 = 0
    num2 = 0
    num3 = 0

    # parameterized constructor
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def find_max_num(self):

        if (self.num1 > self.num2) and (self.num1 > self.num3):
            return self.num1
        elif (self.num2 > self.num1) and (self.num2 > self.num3):
            return self.num2
        elif (self.num3 > self.num1) and (self.num1 > self.num2):
            return self.num3
        else:
            print("All number are same")


if __name__ == '__main__':
    print("Welcome to max number program")
    intLargest = FindMaximumNumber(10, 30, 20)
    print("The largest number is", intLargest.find_max_num())