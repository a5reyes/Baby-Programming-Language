# COMP 340
# Albert Reyes
# github - a5reyes
class TreeNode:
    def __init__(self, srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None

def getPrecedence(operator):
    if operator == "neg": 
        return 3
    elif operator in ["multiply", "divide"]:
        return 2
    elif operator in ["plus", "minus"]:
        return 1
    else:
        return 0

def preprocessTokens(srcList):
    newList = []
    i = 0
    while i < len(srcList):
        token = srcList[i]
        if token[1] == "minus":
            # If the minus is unary (start or after an operator)
            if i == 0 or srcList[i - 1][1] in ["plus", "minus", "multiply", "divide"]:
                nextToken = srcList[i + 1]
                if nextToken[1] == "num":
                    newList.append([f"-{nextToken[0]}", "num"])  # Combine unary minus with number
                    i += 2
                    continue
        newList.append(token)
        i += 1
    return newList

def parseEx(srcList):
    # recursive fun. to parse expressions with mini. precedence level
    def parse_expr(i, min_precedence):
        left = TreeNode(srcList[i])
        i += 1
        while i < len(srcList):
            op = srcList[i]
            # if curr_op's precedence is less than min_precedence, then break
            if getPrecedence(op[1]) < min_precedence:
                break
            # store curr_op's precedence, move on to right side and make it a more higher-precedence ops side
            precedence = getPrecedence(op[1])
            i += 1
            right, i = parse_expr(i, precedence + 1)
            opNode = TreeNode(op)
            opNode.left = left
            opNode.right = right
            # whole subtree as the new left to chain ops
            left = opNode
        return left, i
    
    # handle parenthesis preference
    if ["(", "leftPara"] in srcList:
        if srcList[0] == ["(", "leftPara"] and srcList[-1] == [")", "rightPara"]:
            del srcList[0]
            del srcList[-1]
        leftPara = srcList.index(["(", "leftPara"])
        rightPara = srcList.index([")", "rightPara"])
        within_Para = srcList[leftPara+1:rightPara+1]
        out_Para = srcList[:leftPara] + srcList[rightPara+1:]
        within_Parsed = parseEx(within_Para)
        for part in out_Para:
            if part[1] != "num":
                op_token = part
        op = TreeNode(op_token)
        for part in out_Para:
            if part[1] == "num":
                right_Tree = TreeNode(part)
        left_Tree = within_Parsed
        op.left = left_Tree
        op.right = right_Tree
        return op
    else:
        tree, _ = parse_expr(0,1)
        return tree

def printTree(treeRoot):
    if treeRoot.token == "num":
        print(treeRoot.value, end="")
    elif treeRoot.token == "neg":
        print("(0-", end="")
        printTree(treeRoot.right)
        print(")", end="")
    else:
        print("(", end="")
        printTree(treeRoot.left)
        print(treeRoot.value, end="")
        printTree(treeRoot.right)
        print(")", end="")