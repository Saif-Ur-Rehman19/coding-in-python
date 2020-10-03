def power(number1, number2):
    result = 1
    for go_through in range(number2):
        result = result*number1
    return result
print(pow(3,2))