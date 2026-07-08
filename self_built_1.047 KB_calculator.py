import math
while True:
    number=input("this is a calculator give me the first number:   ")
    operation=input("math operation:   ")
    second_number=input("second number (enter if sqrt):   ")
    if operation == 'quit' or number == 'quit' or second_number == 'quit':
        print("bye")
        break
    elif operation == '+':
        print("your answer is")
        print(int(number)+int(second_number))
    elif operation == '-':
        print("your answer is")
        print(int(number)-int(second_number))  
    elif operation == 'x' or operation == '*':
        print("your answer is")
        print(int(number)*int(second_number))
    elif operation == '/' or operation == '\\' or operation == '÷':
        print("your answer is")
        print(int(number)/int(second_number))
    elif operation == '^' or operation == '**':
        print("your answer is")
        print(int(number)**int(second_number))
    elif operation == 'sqrt':
        print("your answer is")
        print(math.sqrt(int(number)))
    
     
      
   
        