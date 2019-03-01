# -*- coding: utf-8 -*-

def output_formatting(x):
    length = len(str(x))
    if length < 7:
        output = str(x)
    elif length >= 7 and length < 10:
        math = x/int(str(1)+(6)*str(0))
        output = str(math) + ' million'
    elif length >= 10 and length < 13:
        math = x/int(str(1)+(9)*str(0))
        output = str(math) + ' billion'
    elif length >= 13 and length < 16:
        math = x/int(str(1)+(12)*str(0))
        output = str(math) + ' trillion'
    return output

print("---------------------------------")
print("The Recall Co-Ordinator's Formula")
print("---------------------------------")
print("Take the number of vehicles in the field, A\nMultiply by the probable rate of failure, B\nMultiply by the average out-of-court settlement, C")
print("A x B x C = X")
print("If X is less than the cost of a recall, don't do one")
print("---------------------------------")
print("Applying the formula:")

a = int(input(" What is the number of vehicles in the field?: "))
b = int(input(" What is the probable rate of failure?: "))/100
c = int(input(" What is average out of court settlment?: "))
recall = int(input(" What is the cost of a recall?: "))

print("---------------------------------")
x = int(((a/1000000)*b)*(c/1000000)*1000000)
a_output = output_formatting(a)
c_output = output_formatting(c)
x_output = output_formatting(x)
recall_output = output_formatting(recall)

print("X =", a_output, "x", int(b*100), "% x", c_output, "=", x_output )
print("---------------------------------")
if x < recall:
    print(x_output, "is less than", recall_output)
    print("X is less than the cost of a recall. Don't do one")
else:
    print(x_output, "is more than",  recall_output)
    print("X is more than the cost of a recall. Do one")
print("---------------------------------")