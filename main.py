# COMP 340
# Albert Reyes
# github - a5reyes
import lexer, parser, evaluator, decipher


def main():
    print("\nHello baby language.\nEnter baby expression and see what you get.")
    while True:
        babyExp = input(">>> ")
        if babyExp == "poopoo":
            break
        # decipher
        srcCode = decipher.decipher(babyExp)
        print("Interpreted as: ", srcCode)
        # lexer
        srcList = lexer.tokenizer(srcCode)
        # parser
        rootNode = parser.parseEx(parser.preprocessTokens(srcList))
        # evaluator
        result = evaluator.evaluate(rootNode)
        print("The result is: ", result)
    print("Now it is time to go poo poo.")

main()    
