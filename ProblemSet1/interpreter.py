exp = input("expression")
exp = exp.split()
if exp[1] == "+":
        ans = int(exp[0])+ int(exp[2])
        print (float(ans))
elif exp[1] == "-":
        ans = int(exp[0]) - int(exp[2])
        print (float(ans))

elif exp[1] == "/":
        ans = int(exp[0]) / int(exp[2])
        print (float(ans))

elif exp[1] == "*":
        ans = int(exp[0]) * int(exp[2])
        print (float(ans))

