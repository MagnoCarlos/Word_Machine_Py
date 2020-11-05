file = open("/Volumes/PC/ProjectsProgramming/LearningPython/Problems/Word_Machine/input.txt")

for sentence in file:
    print(" ")
    print("line: " + sentence)  # print line of command
    stack = []  # define empty stack
    for word in sentence.split():
        print("Operation => ", end="")
        print(word)

        # conditions for the operations
        if word.isdigit():
            num = int(word)
            stack.append(num)
            print("Current Stack after operation => ", end="")
            print(stack)
        if word == "POP":  # remove last stack value
            stack.pop()
            print("Current Stack after operation => ", end="")
            print(stack)
        elif word == "DUP":  # duplicate last stack value
            num2 = stack[-1]
            stack.append(num2)
            print("Current Stack after operation => ", end="")
            print(stack)
        elif word == "+":  # add last 2 stack values
            num3 = stack.pop()
            result = int(num3) + stack.pop()
            stack.append(result)
            print("Current Stack after operation => ", end="")
            print(stack)
        elif word == "-":  # subtract last 2 stack values
            num4 = stack.pop()
            result1 = int(num4) - stack.pop()
            stack.append(result1)
            print("Current Stack after operation => ", end="")
            print(stack)
