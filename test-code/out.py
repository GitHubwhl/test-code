import inspect
def retrieve_name_ex(var):
    stacks = inspect.stack()
    try:
        callFunc = stacks[1].function
        contentCode = stacks[2].code_context[0]
        startIndex = contentCode.index(callFunc)
        headerLen = len(callFunc)
        startIndex = contentCode.index("(", startIndex + headerLen) + 1
        codeArray = contentCode.split('#')
        ClearCode = codeArray[0]
        endIndex = ClearCode.rindex(")", 0)
        result = ClearCode[startIndex:endIndex].strip()
        return result
    except Exception as e:
        print(str(e))
def out(var):
    print("{} = {}".format(retrieve_name_ex(var),var))
y=2
x=[2,3,y];
print(x)
out(x)
