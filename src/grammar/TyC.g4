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
    elif tk == self.ERROR_TOKEN:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

/* ==========================
Parser rules
========================== */

// PROGRAM STRUCTURE
program: (structDeclaration | functionDeclaration)* EOF;

// FUNCTION SECTION
functionDeclaration
    : returnType ID LEFT_PAREN parameterList RIGHT_PAREN block    // explicit return type
    | ID LEFT_PAREN parameterList RIGHT_PAREN block               // inferred return type
    ;

returnType
    : INT
    | FLOAT
    | STRING
    | VOID
    | ID    // struct type name
    ;

parameterList: (parameter (COMMA parameter)*)?;

parameter
    : INT ID
    | FLOAT ID
    | STRING ID
    | ID ID     // struct type parameter
    ;

argumentList: (expression (COMMA expression)*)?;

// STRUCT SECTION
structDeclaration: STRUCT ID LEFT_BRACE structMemberList RIGHT_BRACE SEMICOLON;

structMemberList: (structMember (SEMICOLON structMember)* SEMICOLON?)?;

structMember
    : INT ID
    | FLOAT ID
    | STRING ID
    | ID ID     // struct type member
    ;

structInit: LEFT_BRACE (expression (COMMA expression)*)? RIGHT_BRACE;

// VARIABLE SECTION
variableDeclaration
    : AUTO ID (ASSIGN expression)?                          // auto with optional init
    | INT ID (ASSIGN expression)?                           // int with optional init
    | FLOAT ID (ASSIGN expression)?                         // float with optional init
    | STRING ID (ASSIGN expression)?                        // string with optional init
    | ID ID (ASSIGN (expression | structInit))?             // struct type with optional init
    ;

// EXPRESSION SECTION (proper precedence from lowest to highest)
expression: assignmentExpression;

assignmentExpression
    : orExpression ASSIGN assignmentExpression    // right associative
    | orExpression
    ;

orExpression: andExpression (LOGICAL_OR andExpression)*;

andExpression: equalityExpression (LOGICAL_AND equalityExpression)*;

equalityExpression: relationalExpression ((EQUAL | NOT_EQUAL) relationalExpression)*;

relationalExpression: additiveExpression ((LESS_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN | GREATER_THAN_OR_EQUAL) additiveExpression)*;

additiveExpression: multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression: unaryExpression ((MULTIPLY | DIVIDE | MODULUS) unaryExpression)*;

unaryExpression
    : INCREMENT unaryExpression
    | DECREMENT unaryExpression
    | MINUS unaryExpression
    | PLUS unaryExpression
    | LOGICAL_NOT unaryExpression
    | postfixExpression
    ;

postfixExpression
    : primaryExpression (postfixOp)*
    ;

postfixOp
    : INCREMENT
    | DECREMENT
    | MEMBER_ACCESS ID
    | LEFT_PAREN argumentList RIGHT_PAREN  // function call
    ;

primaryExpression
    : ID
    | INTEGER_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | LEFT_PAREN expression RIGHT_PAREN
    ;

// STATEMENT SECTION
statement
    : variableDeclaration SEMICOLON
    | assignmentStatement SEMICOLON
    | expressionStatement SEMICOLON
    | ifStatement
    | whileStatement
    | forStatement
    | switchStatement
    | returnStatement
    | breakStatement
    | continueStatement
    | block
    ;

assignmentStatement: lvalue ASSIGN expression;

lvalue
    : ID (MEMBER_ACCESS ID)*
    ;

expressionStatement: expression;

block: LEFT_BRACE statement* RIGHT_BRACE;

ifStatement: IF LEFT_PAREN expression RIGHT_PAREN statement (ELSE statement)?;

whileStatement: WHILE LEFT_PAREN expression RIGHT_PAREN statement;

forStatement: FOR LEFT_PAREN forInit? SEMICOLON expression? SEMICOLON forUpdate? RIGHT_PAREN statement;

forInit
    : variableDeclaration
    | assignmentStatement
    ;

forUpdate
    : assignmentStatement
    | expression
    ;

switchStatement: SWITCH LEFT_PAREN expression RIGHT_PAREN LEFT_BRACE caseClause* defaultClause? RIGHT_BRACE;

caseClause: CASE expression COLON statement*;

defaultClause: DEFAULT COLON statement*;

returnStatement: RETURN expression? SEMICOLON;

breakStatement: BREAK SEMICOLON;

continueStatement: CONTINUE SEMICOLON;

/* ==========================
Lexer rules
========================== */

// Whitespace and comments
WS: [ \t\r\n\f]+ -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Separators
COMMA: ',';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
SEMICOLON: ';';
LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';
COLON: ':';

// Operators (order matters - longer matches first)
INCREMENT: '++';
DECREMENT: '--';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
EQUAL: '==';
NOT_EQUAL: '!=';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULUS: '%';
LESS_THAN: '<';
GREATER_THAN: '>';
LOGICAL_NOT: '!';
MEMBER_ACCESS: '.';

// Identifiers (must come after keywords)
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
INTEGER_LITERAL: [0-9]+;

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]* EXPONENT?    // 123.456, 123., 123.456e10
    | '.' [0-9]+ EXPONENT?           // .456, .456e10
    | [0-9]+ EXPONENT                // 123e10
    ;

fragment EXPONENT: [eE] [+-]? [0-9]+;

STRING_LITERAL: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};

fragment STRING_CHAR
    : ~["\\\r\n]           // any char except ", \, newline
    | ESCAPE_SEQUENCE
    ;

fragment ESCAPE_SEQUENCE
    : '\\' [bfnrt"\\]      // valid escape sequences: \b \f \n \r \t \" \\
    ;

// Error handling tokens
UNCLOSE_STRING: '"' STRING_CHAR* ([\r\n] | EOF);

ILLEGAL_ESCAPE: '"' STRING_CHAR* '\\' ~[bfnrt"\\];

ERROR_TOKEN: . ;