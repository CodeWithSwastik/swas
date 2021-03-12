
from sly import Lexer

class SwasLexer(Lexer):
    tokens = { NAME, NUMBER, PLUS, TIMES, MINUS, DIVIDE, MOD, ARROW, LPAREN, RPAREN,
               IF, ELSE, WHILE, DO, STRING, PRINT, INC, DEC, JOIN, EQUALS, GT, GTE, LT, LTE, NE}
    ignore = ' \t'

    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    NAME['if'] = IF 
    NAME['else'] = ELSE
    NAME['while'] = WHILE
    NAME['do'] = DO
    NAME['upload'] = PRINT
    NAME['inc'] = INC
    NAME['dec'] = DEC


    # Operators
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ARROW = r'=>'
    LPAREN = r'\('
    RPAREN = r'\)'
    MOD = r'%'
    JOIN = r'&&&'
    EQUALS = r'=='
    GT = r'>'
    GTE = r'>='
    LT = r'<'
    LTE = r'<='
    NE = r'!='

    # Ignored pattern
    ignore_newline = r'\n+'

    # String
    @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    def STRING(self, t):
        t.value = self.remove_quotes(t.value)
        return t

    def remove_quotes(self, text: str):
        if text.startswith('\"') or text.startswith('\''):
            return text[1:-1]
        return text


    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
