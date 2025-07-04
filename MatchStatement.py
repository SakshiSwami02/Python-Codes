#basic calculator using python

print("Enter two numbers")
val1=int(input())
val2=int(input())
print("Choose one of the following options. \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power")
x=int(input())
match x:
    case 1:
        sum=val1+val2
        print("The sum of ",val1," and ", val2, " is", sum)
    case 2:
        diff=val1-val2
        print("The difference of ",val1," and ",val2," is", diff)
    case 3:
        mul=val1*val2
        print("The multiplication of ",val1, " and", val2, " is", mul)
    case 3:
        div=val1/val2
        print("The division of ",val1, " and", val2, " is", div)
    case 3:
        mod=val1%val2
        print("The value of ",val1, " modulus", val2, " is", mod)
    case 6:
        pow=val1**val2
        print("The value of ",val1, " to the power", val2, " is", pow)
    case _:
        print("Not a valid option!")