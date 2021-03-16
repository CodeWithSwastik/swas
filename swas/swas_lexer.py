
from sly import Lexer

class SwasLexer(Lexer):
    tokens = { NAME, NUMBER, PLUS, TIMES, MINUS, DIVIDE, MOD, POW, ARROW, LPAREN, RPAREN,
               IF, ELIF, ELSE, WHILE, DO, BREAK, STRING, PRINT, INPUT, INC, DEC, EQ, GT, GTE, LT, LTE, NE, PASS,
               LBRAC, RBRAC, OR, AND}
    
    # Ignored patterns
    ignore_newline = r'\n+'
    ignore_comment = r'//.*\n*'
    ignore = ' \t'
    
    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    NUMBER = r'\d+\.{0,1}\d*'

    NAME['if'] = IF 
    NAME['elif'] = ELIF
    NAME['else'] = ELSE
    NAME['while'] = WHILE
    NAME['do'] = DO
    NAME['break'] = BREAK
    NAME['output'] = PRINT
    NAME['input'] = INPUT
    NAME['inc'] = INC
    NAME['dec'] = DEC
    NAME['nothing'] = PASS
    NAME['and'] = AND
    NAME['or'] = OR

    # Operators
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRAC = r'\{'
    RBRAC = r'\}'
    MOD = r'%'
    POW = r'\^'
    EQ = r'=='
    GT = r'>'
    GTE = r'>='
    LT = r'<'
    LTE = r'<='
    NE = r'!='
    ARROW = r'='

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
