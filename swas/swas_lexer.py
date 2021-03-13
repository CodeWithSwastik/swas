
from sly import Lexer

class SwasLexer(Lexer):
    tokens = { NAME, NUMBER, PLUS, TIMES, MINUS, DIVIDE, MOD, ARROW, LPAREN, RPAREN,
               IF, ELSE, WHILE, DO, STRING, PRINT, INC, DEC, JOIN, EQ, GT, GTE, LT, LTE, NE, PASS}
    
    # Ignored patterns
    ignore_newline = r'\n+'
    ignore_comment = r'ignore.*\n*'
    ignore = ' \t'
    
    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    NAME['if'] = IF 
    NAME['else'] = ELSE
    NAME['while'] = WHILE
    NAME['do'] = DO
    NAME['output'] = PRINT
    NAME['inc'] = INC
    NAME['dec'] = DEC
    NAME['nothing'] = PASS
    
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
    EQ = r'=='
    GT = r'>'
    GTE = r'>='
    LT = r'<'
    LTE = r'<='
    NE = r'!='


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
