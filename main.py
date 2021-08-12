import find_max_number

if __name__ == '__main__':
    intLargest = find_max_number.FindMaximumNumber(10, 10, 10)
    floatLargest = find_max_number.FindMaximumNumber(10.5, 30.5, 20.5)
    print("The largest int number is: ", intLargest.find_max_int_num())
    print("the Largest float number is: ", floatLargest.find_max_float_num())
