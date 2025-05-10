# COMP 340
# Albert Reyes
# github - a5reyes
def tokenizer(srccode):
    nString = ""
    List = []
    ops = {"+": "plus", "-": "minus", "*": "multiply", "/": "divide", "(": "leftPara", ")": "rightPara"}
    for i in srccode:
        if i == " ":
            continue
        if i not in ops:
            nString = nString + i
        elif nString == "":
            List.append([i, ops[i]])
        else:
            List.append([nString, "num"])
            nString = ""
            List.append([i, ops[i]])
    if nString != "":
        List.append([nString, "num"])
    return List