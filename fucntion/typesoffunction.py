# 4 types of function in python
# 1.No argument, No return value
def sample():
    print("hello")
sample()
# 2.No argument, with return value
def sample1():
    a=10
    b=20
    sum = a + b
    return sum
result = sample1()
print(result)
# 3.with argument, no return value
def sample2(value):
    print("value is: " +str(value))
sample2(123)
# 3.with argument, with return value
def sample3(num1,num2):
    sum = num1 + num2
    return sum
result1 = sample3(12,24)
print(result1)

