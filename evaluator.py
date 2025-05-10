# COMP 340
# Albert Reyes
# github - a5reyes
def evaluate(rootNode):
    if rootNode.left is None and rootNode.right is None:
        return int(rootNode.value)
    else:
        result = 0
        leftResult = evaluate(rootNode.left) 
        rightResult = evaluate(rootNode.right) 
        if rootNode.token == "plus":
            result = leftResult + rightResult
            return result
        elif rootNode.token == "minus":
            result = leftResult - rightResult
            return result
        elif rootNode.token == "multiply":
            result = leftResult * rightResult
            return result
        elif rootNode.token == "divide":
            result = leftResult / rightResult
            return result