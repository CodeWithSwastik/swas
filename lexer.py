import string
from errors import *

KEYWORDS = {
    "upload": "print",
    "hi": "var",
    "its": "assign"
}

LETTERS = string.ascii_letters + "\"();\n"

class Lexer:
    def __init__(self, text):
        self.text = text   
        self.idx = -1
        self.current_char = None
        self.token = ""

        self.advance()

    def advance(self):
        self.idx += 1
        self.current_char = self.text[self.idx] if self.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in ";\n":
                tokens.append(Token("SCOLON"))
                self.advance()
            elif self.current_char == "\"":
                self.advance()
                tokens.append(self.make_str())
            elif self.current_char == "(":
                tokens.append(Token("LPAREN"))
                self.advance()

            elif self.current_char == ")":
                tokens.append(Token("RPAREN"))
                self.advance()

            elif self.current_char not in LETTERS:
                tokens.append(self.make_expr())
            else:
                tokens.append(self.find_token())

        return tokens, None

    def make_expr(self):
        expr_str = ''

        while self.current_char != None and self.current_char not in LETTERS:
            expr_str += self.current_char
            self.advance()


        return Token("EXPR", expr_str)

    def make_str(self):
        final_str = ''

        while self.current_char != None and self.current_char != "\"":
            final_str += self.current_char
            self.advance()

        self.advance()

        return Token("STRING", final_str)
        
    def find_token(self):
        cur_token = ''

        while self.current_char != None and not self.current_char in " (\n":
            cur_token += self.current_char
            self.advance()
        if self.current_char == " ": 
            self.advance()

 
        
        name = KEYWORDS.get(cur_token, None) 
        type_ = "KEYWORD" if name else "IDENTIFIER"
        name = name or cur_token
        return Token(type_, name)

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


