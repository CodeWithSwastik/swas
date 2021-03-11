from errors import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

        return self.current_tok

    def parse(self):
        pycode = ""

        while self.tok_idx < len(self.tokens):
            if self.current_tok.type == "EXPR":
                pycode += f"eval(\"{self.current_tok.value}\")"
            if self.current_tok.type == "KEYWORD":
                if self.current_tok.value == "print":
                    try:
                        next_tok = self.tokens[self.tok_idx + 1]
                    except:
                        return "", SyntaxError("print expects a value after it")

                    acceptable = ["EXPR", "STRING", "IDENTIFIER"]
                    if not next_tok.type in acceptable:
                        return "", SyntaxError("upload expects a string or an expression")
                    if next_tok.type == "STRING":
                        data = f"\"{next_tok.value}\""
                    elif next_tok.type == "EXPR":
                        data = f"eval('{next_tok.value}')"
                    elif next_tok.type == "IDENTIFIER":
                        data = f"{next_tok.value}"

                    pycode += f"print({data})"
                    self.advance()
                if self.current_tok.value == "var":
                    try:
                        varname = self.tokens[self.tok_idx + 1]
                        if varname.type != "IDENTIFIER":
                            raise Exception
                    except:
                        return "", SyntaxError("hi needs a varname after it")

                    try:
                        check_its = self.tokens[self.tok_idx + 2]
                        if check_its.value != "assign":
                            raise Exception
                    except:
                        return "", SyntaxError("no assignment operator found")

                    try:
                        value = self.tokens[self.tok_idx + 3]
                    except:
                        return "", SyntaxError("needed a value to assign to, found none")

                    acceptable = ["EXPR", "STRING", "IDENTIFIER"]
                    if not value.type in acceptable:
                        return "", SyntaxError("you can only assign a string/an expression or a variable")
                    if value.type == "STRING" or value.type == "IDENTIFIER":
                        data = f"\"{value.value}\""
                    elif value.type == "EXPR":
                        data = f"eval('{value.value}')"

                    pycode += f"{varname.value} = {data}"

                    for _ in range(3):
                        self.advance()

            if self.current_tok.type == "SCOLON":
                pycode += "\n"

            self.advance()


        #valid python code
        return pycode, None

