# def max_num(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
       
# print(max_num(6,3,4))        



def max_num():
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    num3 = int(input("Please enter third number: "))
    if num1 >= num2 and num1 >= num3:
        return "Max is " + str(num1)
    elif num2 >= num1 and num2 >= num3:
        return "Max is " + str(num2)
    else:    
        return "Max is " + str(num3)      

print(max_num())               
