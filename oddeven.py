def oddeven():
    num = int(input("Please enter a number: "))
    if num % 2 == 0 and 1000 > num > 0:
        return "偶數"
    elif 1000 > num > 0 :
        return "奇數"
    else:
        return "Invalid number"        

print(oddeven())
