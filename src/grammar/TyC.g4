grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

// TODO: Define grammar rules here
program: EOF;

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs

// Struct declaration
STRUCT: 'struct';

RESERVED_WORDS:
	| F_TYPE
	| 'break'
	| 'case'
	| 'continue'
	| 'default'
	| 'else'
	| 'for'
	| 'if'
	| 'return'
	| 'switch'
	| 'while';
TYPE: F_TYPE;

// Function declaration
fragment F_TYPE: 'int' | 'float' | 'string' | 'void' | 'auto';

// Comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Separators
COMMA: ',';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
SEMICOLON: ';';
LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;
fragment F_NUMBER: '-'? [0-9]+;
fragment F_FLOAT_NUMBER:
	'-'? [0-9]+ '.' [0-9]+ ('e' | 'E') ('+' | '-')? [0-9]+;
fragment F_STRING: '"' .*? '"';
fragment F_CHAR: '\\' .*? '\\';

// Operators
ASSIGN: '=';
EQUAL: '==';
NOT_EQUAL: '!=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULUS: '%';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';
INCREMENT: '++';
DECREMENT: '--';
MEMBER_ACCESS: '.';

// Literals
INTEGER_LITERAL: F_NUMBER;
FLOAT_LITERAL: F_FLOAT_NUMBER;
STRING_LITERAL: F_STRING;
CHAR_LITERAL: F_CHAR;

// Error tokens
ERROR_CHAR: .;
ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;
