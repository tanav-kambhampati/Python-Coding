import random
def generateProblem():
    problemTypeGenerator = random.randint(0,5)
    problemType = "undefined"
    if problemTypeGenerator == 0:
        problemType = "sin"
    elif problemTypeGenerator == 1:
        problemType = "cos"
    elif problemTypeGenerator == 2:
        problemType = "tan"
    elif problemTypeGenerator == 3:
        problemType = "sin^-1"
    elif problemTypeGenerator == 4:
        problemType = "cos^-1"
    elif problemTypeGenerator == 5:
        problemType = "tan^-1"
    problemArgument = 0
    if problemTypeGenerator <= 2:
        problemArgumentGenerator = random.randint(1,16)
        if problemArgumentGenerator == 5:
            problemArgument = '5π/6'
        elif problemArgumentGenerator == 7:
            problemArgument = '7π/6'
        elif problemArgumentGenerator == 11:
            problemArgument = '11π/6'
        elif problemArgumentGenerator == 1:
            problemArgument = str('π/6')
        elif problemArgumentGenerator == 2:
            problemArgument = 'π/4'
        elif problemArgumentGenerator == 3:
            problemArgument = 'π/3'
        elif problemArgumentGenerator == 4:
            problemArgument = 'π/2'
        elif problemArgumentGenerator == 6:
            problemArgument = '2π/3'
        elif problemArgumentGenerator == 8:
            problemArgument = '3π/4'
        elif problemArgumentGenerator == 9:
            problemArgument = 'π'
        elif problemArgumentGenerator == 10:
            problemArgument = '5π/4'
        elif problemArgumentGenerator == 16:
            problemArgument = '4π/3'
        elif problemArgumentGenerator == 12:
            problemArgument = '3π/2'
        elif problemArgumentGenerator == 13:
            problemArgument = '5π/3'
        elif problemArgumentGenerator == 14:
            problemArgument = '7π/4'
        elif problemArgumentGenerator == 15:
            problemArgument = '2π'
        del problemArgumentGenerator
    elif problemTypeGenerator == 3 or 4:
        problemArgumentGenerator = random.randint(0,8)
        if problemArgumentGenerator == 0:
            problemArgument = '-1'
        elif problemArgumentGenerator == 1:
            problemArgument = '-√3/2'
        elif problemArgumentGenerator == 2:
            problemArgument = '-√2/2'
        elif problemArgumentGenerator == 3:
            problemArgument = '-1/2'
        elif problemArgumentGenerator == 4:
            problemArgument = '0'
        elif problemArgumentGenerator == 5:
            problemArgument = '1/2'
        elif problemArgumentGenerator == 6:
            problemArgument = '√2/2'
        #this is line 69 (very important)
        elif problemArgumentGenerator == 7:
            problemArgument = '√3/2'
        elif problemArgumentGenerator == 8:
            problemArgument = '1'
        del problemArgumentGenerator
    elif problemTypeGenerator == 5:
        problemArgumentGenerator = random.randint(1,6)
        if problemArgumentGenerator == 1:
            problemArgument = '-√3'
        elif problemArgumentGenerator == 2:
            problemArgument = '-1'
        elif problemArgumentGenerator == 3:
            problemArgument = '-√3/3'
        elif problemArgumentGenerator == 4:
            problemArgument = '√3'
        elif problemArgumentGenerator == 4:
            problemArgument = '0'
        elif problemArgumentGenerator == 5:
            problemArgument = '√3/3'
        elif problemArgumentGenerator == 6:
            problemArgument = '1'
    problemFinal = str(problemType) + '(' + str(problemArgument) + ')'
    return problemFinal
def generateProblemList(quantity):
    for steps in range(quantity):
        printProblem = generateProblem()
        print(printProblem)
    