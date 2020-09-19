def get_count(stack):
    countVar = 1
    flag = True
    while flag:
        flag = False
        for t in stack:
            if t[0][0] == "t":
                if countVar == int(t[0][1:]):
                    countVar += 1
                    flag = True
                    break
    return countVar
if __name__ == "__main__":
    inputOPZ = input().split()

    stack = []

    output = ""
    countVar = 1
    for token in inputOPZ:

        if token == "+":
            first = stack.pop()
            second = stack.pop()

            countVar = get_count(stack)

            stack.append(["t" + str(countVar), float(first[1]) + float(second[1])])
            output += "t" + str(countVar) + " = " + first[0] + " + " + second[0]  + "\n"

        elif token == "-":
            first = stack.pop()
            second = stack.pop()

            countVar = get_count(stack)

            stack.append(["t" + str(countVar), float(first[1]) - float(second[1])])
            output += "t" + str(countVar) + " = " + first[0] + " - " + second[0]  + "\n"
        elif token == "*":
            first = stack.pop()
            second = stack.pop()

            countVar = get_count(stack)

            stack.append(["t" + str(countVar), float(first[1]) * float(second[1])])
            output += "t" + str(countVar) + " = " + first[0] + " * " + second[0]  + "\n"
        elif token == "/":
            first = stack.pop()
            second = stack.pop()

            countVar = get_count(stack)

            stack.append(["t" + str(countVar), float(first[1]) / float(second[1])])
            output += "t" + str(countVar) + " = " + first[0] + " / " + second[0] + "\n"
        else:
            stack.append([token,int(token)])
            countVar -= 1
        print(stack)
        countVar += 1

    output += "print(t" + str(countVar - 1) + ")"
    with open("pr2.py", "w") as out:
        out.write(output)