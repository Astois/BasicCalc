def main():
    while True:
        Action = input("Do you want to use calc? (yes or no) ")
        if Action == "no":
            break
        elif Action == "yes":
            InputChoice = input("What operation do you want to use?(+, -, /, *)  ")
            if  InputChoice == "+":
                def add():
                    AddNum1 = int(input("what is the first number?" ))
                    AddNum2 = int(input("what is the second number?" ))
                    print("the sum is... ",AddNum1 + AddNum2)
                add()    
            if   InputChoice == "-":
                def sub():
                    SubNum1 = int(input("what is the first number? "))
                    SubNum2 = int(input("what is the second number? "))
                    print("The difference is... ",SubNum1 - SubNum2)
                sub()
            if InputChoice == "/":
                def div():
                    DivNum1 = int(input("what is the first number? "))
                    DivNum2 = int(input("what is the second number? "))
                    print("The result is... ", DivNum1 / DivNum2)
                div()    
            if InputChoice == "*":
                def mul():
                    MulNum1 = int(input("What is the first number?  "))
                    MulNum2 = int(input("What is the second number? "))        
                    print("The product is..",MulNum1 * MulNum2)
                mul()
main()            