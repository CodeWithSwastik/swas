from lexer import Lexer
from swasparser import Parser

def execute(data):
    lexer = Lexer(data)
    tokens, error = lexer.make_tokens()
    if not error:
        parser = Parser(tokens)
        res, err = parser.parse()

        # Debug
        #print(tokens)
        #print(res)
        
        if err:
            print(err.as_string())                
        else:
            exec(res)
    else:
        print(error.as_string())

def run():
    while True:
        data = ""
        user_input = input("swas >>> ")
        if user_input == "end":
            continue
        data += user_input + "\n"

        while True:
            user_input = input("     ... ")
            if user_input == "end":
                break
            data += user_input + "\n"
        
        execute(data)