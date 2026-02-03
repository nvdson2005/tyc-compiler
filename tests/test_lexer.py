"""
Lexer test cases for TyC compiler
"""

import pytest
from tests.utils import Tokenizer

def test_keyword_break():
    """Test 'break' keyword recognition"""
    tokenizer = Tokenizer("break")
    result = tokenizer.get_tokens_as_string()
    assert result == "BREAK,break,EOF"


def test_keyword_case():
    """Test 'case' keyword recognition"""
    tokenizer = Tokenizer("case")
    result = tokenizer.get_tokens_as_string()
    assert result == "CASE,case,EOF"


def test_keyword_continue():
    """Test 'continue' keyword recognition"""
    tokenizer = Tokenizer("continue")
    result = tokenizer.get_tokens_as_string()
    assert result == "CONTINUE,continue,EOF"


def test_keyword_default():
    """Test 'default' keyword recognition"""
    tokenizer = Tokenizer("default")
    result = tokenizer.get_tokens_as_string()
    assert result == "DEFAULT,default,EOF"


def test_keyword_else():
    """Test 'else' keyword recognition"""
    tokenizer = Tokenizer("else")
    result = tokenizer.get_tokens_as_string()
    assert result == "ELSE,else,EOF"


def test_keyword_float():
    """Test 'float' keyword recognition"""
    tokenizer = Tokenizer("float")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT,float,EOF"


def test_keyword_for():
    """Test 'for' keyword recognition"""
    tokenizer = Tokenizer("for")
    result = tokenizer.get_tokens_as_string()
    assert result == "FOR,for,EOF"


def test_keyword_if():
    """Test 'if' keyword recognition"""
    tokenizer = Tokenizer("if")
    result = tokenizer.get_tokens_as_string()
    assert result == "IF,if,EOF"


def test_keyword_int():
    """Test 'int' keyword recognition"""
    tokenizer = Tokenizer("int")
    result = tokenizer.get_tokens_as_string()
    assert result == "INT,int,EOF"


def test_keyword_return():
    """Test 'return' keyword recognition"""
    tokenizer = Tokenizer("return")
    result = tokenizer.get_tokens_as_string()
    assert result == "RETURN,return,EOF"


def test_keyword_string():
    """Test 'string' keyword recognition"""
    tokenizer = Tokenizer("string")
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING,string,EOF"


def test_keyword_struct():
    """Test 'struct' keyword recognition"""
    tokenizer = Tokenizer("struct")
    result = tokenizer.get_tokens_as_string()
    assert result == "STRUCT,struct,EOF"


def test_keyword_switch():
    """Test 'switch' keyword recognition"""
    tokenizer = Tokenizer("switch")
    result = tokenizer.get_tokens_as_string()
    assert result == "SWITCH,switch,EOF"


def test_keyword_void():
    """Test 'void' keyword recognition"""
    tokenizer = Tokenizer("void")
    result = tokenizer.get_tokens_as_string()
    assert result == "VOID,void,EOF"


def test_keyword_while():
    """Test 'while' keyword recognition"""
    tokenizer = Tokenizer("while")
    result = tokenizer.get_tokens_as_string()
    assert result == "WHILE,while,EOF"


def test_operator_plus():
    """Test '+' operator"""
    tokenizer = Tokenizer("+")
    result = tokenizer.get_tokens_as_string()
    assert result == "PLUS,+,EOF"


def test_operator_minus():
    """Test '-' operator"""
    tokenizer = Tokenizer("-")
    result = tokenizer.get_tokens_as_string()
    assert result == "MINUS,-,EOF"


def test_operator_multiply():
    """Test '*' operator"""
    tokenizer = Tokenizer("*")
    result = tokenizer.get_tokens_as_string()
    assert result == "MULTIPLY,*,EOF"


def test_operator_divide():
    """Test '/' operator"""
    tokenizer = Tokenizer("/")
    result = tokenizer.get_tokens_as_string()
    assert result == "DIVIDE,/,EOF"


def test_operator_modulus():
    """Test '%' operator"""
    tokenizer = Tokenizer("%")
    result = tokenizer.get_tokens_as_string()
    assert result == "MODULUS,%,EOF"


def test_operator_equal():
    """Test '==' operator"""
    tokenizer = Tokenizer("==")
    result = tokenizer.get_tokens_as_string()
    assert result == "EQUAL,==,EOF"


def test_operator_not_equal():
    """Test '!=' operator"""
    tokenizer = Tokenizer("!=")
    result = tokenizer.get_tokens_as_string()
    assert result == "NOT_EQUAL,!=,EOF"


def test_operator_less_than():
    """Test '<' operator"""
    tokenizer = Tokenizer("<")
    result = tokenizer.get_tokens_as_string()
    assert result == "LESS_THAN,<,EOF"


def test_operator_greater_than():
    """Test '>' operator"""
    tokenizer = Tokenizer(">")
    result = tokenizer.get_tokens_as_string()
    assert result == "GREATER_THAN,>,EOF"


def test_operator_less_than_or_equal():
    """Test '<=' operator"""
    tokenizer = Tokenizer("<=")
    result = tokenizer.get_tokens_as_string()
    assert result == "LESS_THAN_OR_EQUAL,<=,EOF"


def test_operator_greater_than_or_equal():
    """Test '>=' operator"""
    tokenizer = Tokenizer(">=")
    result = tokenizer.get_tokens_as_string()
    assert result == "GREATER_THAN_OR_EQUAL,>=,EOF"


def test_operator_logical_and():
    """Test '&&' operator"""
    tokenizer = Tokenizer("&&")
    result = tokenizer.get_tokens_as_string()
    assert result == "LOGICAL_AND,&&,EOF"


def test_operator_logical_or():
    """Test '||' operator"""
    tokenizer = Tokenizer("||")
    result = tokenizer.get_tokens_as_string()
    assert result == "LOGICAL_OR,||,EOF"


def test_operator_logical_not():
    """Test '!' operator"""
    tokenizer = Tokenizer("!")
    result = tokenizer.get_tokens_as_string()
    assert result == "LOGICAL_NOT,!,EOF"


def test_operator_increment():
    """Test '++' operator"""
    tokenizer = Tokenizer("++")
    result = tokenizer.get_tokens_as_string()
    assert result == "INCREMENT,++,EOF"


def test_operator_decrement():
    """Test '--' operator"""
    tokenizer = Tokenizer("--")
    result = tokenizer.get_tokens_as_string()
    assert result == "DECREMENT,--,EOF"


def test_operator_member_access():
    """Test '.' operator"""
    tokenizer = Tokenizer(".")
    result = tokenizer.get_tokens_as_string()
    assert result == "MEMBER_ACCESS,.,EOF"


# =============================================================================

def test_separator_comma():
    """Test ',' separator"""
    tokenizer = Tokenizer(",")
    result = tokenizer.get_tokens_as_string()
    assert result == "COMMA,,,EOF"


def test_separator_left_paren():
    """Test '(' separator"""
    tokenizer = Tokenizer("(")
    result = tokenizer.get_tokens_as_string()
    assert result == "LEFT_PAREN,(,EOF"


def test_separator_right_paren():
    """Test ')' separator"""
    tokenizer = Tokenizer(")")
    result = tokenizer.get_tokens_as_string()
    assert result == "RIGHT_PAREN,),EOF"


def test_separator_left_brace():
    """Test '{' separator"""
    tokenizer = Tokenizer("{")
    result = tokenizer.get_tokens_as_string()
    assert result == "LEFT_BRACE,{,EOF"


def test_separator_right_brace():
    """Test '}' separator"""
    tokenizer = Tokenizer("}")
    result = tokenizer.get_tokens_as_string()
    assert result == "RIGHT_BRACE,},EOF"


def test_separator_semicolon():
    """Test ';' separator"""
    tokenizer = Tokenizer(";")
    result = tokenizer.get_tokens_as_string()
    assert result == "SEMICOLON,;,EOF"


def test_separator_left_square_bracket():
    """Test '[' separator"""
    tokenizer = Tokenizer("[")
    result = tokenizer.get_tokens_as_string()
    assert result == "LEFT_SQUARE_BRACKET,[,EOF"


def test_separator_right_square_bracket():
    """Test ']' separator"""
    tokenizer = Tokenizer("]")
    result = tokenizer.get_tokens_as_string()
    assert result == "RIGHT_SQUARE_BRACKET,],EOF"


def test_separator_colon():
    """Test ':' separator"""
    tokenizer = Tokenizer(":")
    result = tokenizer.get_tokens_as_string()
    assert result == "COLON,:,EOF"



def test_identifier_underscore_start():
    """Test identifier starting with underscore"""
    tokenizer = Tokenizer("_private")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,_private,EOF"


def test_identifier_with_numbers():
    """Test identifier with numbers"""
    tokenizer = Tokenizer("var123")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,var123,EOF"


def test_identifier_uppercase():
    """Test uppercase identifier"""
    tokenizer = Tokenizer("CONSTANT")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,CONSTANT,EOF"


def test_identifier_mixed_case():
    """Test mixed case identifier"""
    tokenizer = Tokenizer("myVariable123")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,myVariable123,EOF"


def test_identifier_single_char():
    """Test single character identifier"""
    tokenizer = Tokenizer("x")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,x,EOF"


def test_identifier_all_underscores():
    """Test identifier with multiple underscores"""
    tokenizer = Tokenizer("__init__")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,__init__,EOF"


def test_identifier_keyword_prefix():
    """Test identifier that starts like a keyword"""
    tokenizer = Tokenizer("integer")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,integer,EOF"


def test_identifier_camelCase():
    """Test camelCase identifier"""
    tokenizer = Tokenizer("myVariableName")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,myVariableName,EOF"


def test_identifier_snake_case():
    """Test snake_case identifier"""
    tokenizer = Tokenizer("my_variable_name")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,my_variable_name,EOF"



def test_integer_zero():
    """Test integer literal zero"""
    tokenizer = Tokenizer("0")
    result = tokenizer.get_tokens_as_string()
    assert result == "INTEGER_LITERAL,0,EOF"


def test_integer_positive():
    """Test positive integer literal"""
    tokenizer = Tokenizer("123")
    result = tokenizer.get_tokens_as_string()
    assert result == "INTEGER_LITERAL,123,EOF"


def test_integer_large():
    """Test large integer literal"""
    tokenizer = Tokenizer("9999999")
    result = tokenizer.get_tokens_as_string()
    assert result == "INTEGER_LITERAL,9999999,EOF"


def test_integer_leading_zeros():
    """Test integer with leading zeros (treated as separate tokens or one)"""
    tokenizer = Tokenizer("007")
    result = tokenizer.get_tokens_as_string()
    assert result == "INTEGER_LITERAL,007,EOF"


def test_integer_sequence():
    """Test multiple integers"""
    tokenizer = Tokenizer("1 2 3")
    result = tokenizer.get_tokens_as_string()
    assert result == "INTEGER_LITERAL,1,INTEGER_LITERAL,2,INTEGER_LITERAL,3,EOF"


def test_integer_negative_sign_separate():
    """Test negative number (minus is separate token)"""
    tokenizer = Tokenizer("-42")
    result = tokenizer.get_tokens_as_string()
    assert result == "MINUS,-,INTEGER_LITERAL,42,EOF"


# =============================================================================
# FLOAT LITERAL TESTS (10 tests)
# =============================================================================

def test_float_simple():
    """Test simple float literal"""
    tokenizer = Tokenizer("3.14")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,3.14,EOF"


def test_float_zero():
    """Test float zero"""
    tokenizer = Tokenizer("0.0")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,0.0,EOF"


def test_float_trailing_dot():
    """Test float with trailing dot (e.g., 1.)"""
    tokenizer = Tokenizer("1.")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,1.,EOF"


def test_float_leading_dot():
    """Test float with leading dot (e.g., .5)"""
    tokenizer = Tokenizer(".5")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,.5,EOF"


def test_float_scientific_notation():
    """Test float with scientific notation"""
    tokenizer = Tokenizer("1.23e4")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,1.23e4,EOF"


def test_float_scientific_uppercase():
    """Test float with uppercase E"""
    tokenizer = Tokenizer("5.67E2")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,5.67E2,EOF"


def test_float_scientific_negative_exp():
    """Test float with negative exponent"""
    tokenizer = Tokenizer("1.5e-3")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,1.5e-3,EOF"


def test_float_scientific_positive_exp():
    """Test float with positive exponent"""
    tokenizer = Tokenizer("2.0e+10")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,2.0e+10,EOF"


def test_float_integer_with_exponent():
    """Test integer with exponent (becomes float)"""
    tokenizer = Tokenizer("5e3")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,5e3,EOF"


def test_float_multiple():
    """Test multiple float literals"""
    tokenizer = Tokenizer("1.0 2.5 3.14")
    result = tokenizer.get_tokens_as_string()
    assert result == "FLOAT_LITERAL,1.0,FLOAT_LITERAL,2.5,FLOAT_LITERAL,3.14,EOF"


# =============================================================================
# STRING LITERAL TESTS (10 tests)
# =============================================================================

def test_string_empty():
    """Test empty string literal"""
    tokenizer = Tokenizer('""')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,,EOF"


def test_string_with_spaces():
    """Test string with spaces"""
    tokenizer = Tokenizer('"hello world"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,hello world,EOF"


def test_string_escape_newline():
    """Test string with newline escape"""
    tokenizer = Tokenizer('"hello\\nworld"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,hello\\nworld,EOF"


def test_string_escape_tab():
    """Test string with tab escape"""
    tokenizer = Tokenizer('"hello\\tworld"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,hello\\tworld,EOF"


def test_string_escape_quote():
    """Test string with escaped quote"""
    tokenizer = Tokenizer('"say \\"hello\\""')
    result = tokenizer.get_tokens_as_string()
    assert result == 'STRING_LITERAL,say \\"hello\\",EOF'


def test_string_escape_backslash():
    """Test string with escaped backslash"""
    tokenizer = Tokenizer('"path\\\\file"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,path\\\\file,EOF"


def test_string_escape_carriage_return():
    """Test string with carriage return escape"""
    tokenizer = Tokenizer('"line1\\rline2"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,line1\\rline2,EOF"


def test_string_escape_backspace():
    """Test string with backspace escape"""
    tokenizer = Tokenizer('"back\\bspace"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,back\\bspace,EOF"


def test_string_escape_formfeed():
    """Test string with formfeed escape"""
    tokenizer = Tokenizer('"form\\ffeed"')
    result = tokenizer.get_tokens_as_string()
    assert result == "STRING_LITERAL,form\\ffeed,EOF"


# =============================================================================
# COMMENT TESTS (6 tests)
# =============================================================================

def test_line_comment_simple():
    """Test simple line comment"""
    tokenizer = Tokenizer("// this is a comment")
    result = tokenizer.get_tokens_as_string()
    assert result == "EOF"


def test_line_comment_with_code():
    """Test line comment after code"""
    tokenizer = Tokenizer("int x // comment")
    result = tokenizer.get_tokens_as_string()
    assert result == "INT,int,ID,x,EOF"


def test_block_comment_simple():
    """Test simple block comment"""
    tokenizer = Tokenizer("/* this is a block comment */")
    result = tokenizer.get_tokens_as_string()
    assert result == "EOF"


def test_block_comment_multiline():
    """Test multiline block comment"""
    tokenizer = Tokenizer("/* line1\nline2\nline3 */")
    result = tokenizer.get_tokens_as_string()
    assert result == "EOF"


def test_block_comment_with_code():
    """Test block comment between code"""
    tokenizer = Tokenizer("int /* comment */ x")
    result = tokenizer.get_tokens_as_string()
    assert result == "INT,int,ID,x,EOF"


def test_comment_in_comment():
    """Test // inside block comment (should be ignored)"""
    tokenizer = Tokenizer("/* // not a line comment */")
    result = tokenizer.get_tokens_as_string()
    assert result == "EOF"


# =============================================================================
# ERROR HANDLING TESTS (13 tests)
# =============================================================================

def test_error_unrecognized_char():
    """Test unrecognized character error"""
    tokenizer = Tokenizer("@")
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Error Token @" in str(excinfo.value)


def test_error_unrecognized_hash():
    """Test unrecognized # character"""
    tokenizer = Tokenizer("#")
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Error Token #" in str(excinfo.value)


def test_error_unrecognized_dollar():
    """Test unrecognized $ character"""
    tokenizer = Tokenizer("$")
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Error Token $" in str(excinfo.value)


def test_error_unrecognized_backtick():
    """Test unrecognized ` character"""
    tokenizer = Tokenizer("`")
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Error Token `" in str(excinfo.value)


def test_error_unclosed_string():
    """Test unclosed string error"""
    tokenizer = Tokenizer('"hello')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Unclosed String" in str(excinfo.value)


def test_error_unclosed_string_newline():
    """Test unclosed string with newline"""
    tokenizer = Tokenizer('"hello\nworld"')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Unclosed String" in str(excinfo.value)


def test_error_unclosed_string_partial():
    """Test unclosed string with partial content"""
    tokenizer = Tokenizer('"unclosed string')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Unclosed String" in str(excinfo.value)


def test_error_illegal_escape():
    """Test illegal escape sequence"""
    tokenizer = Tokenizer('"hello\\xworld"')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in str(excinfo.value)


def test_error_illegal_escape_number():
    """Test illegal escape with number"""
    tokenizer = Tokenizer('"test\\1"')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in str(excinfo.value)


def test_error_illegal_escape_lowercase_a():
    """Test illegal escape \\a (not supported)"""
    tokenizer = Tokenizer('"test\\a"')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in str(excinfo.value)


def test_error_illegal_escape_space():
    """Test illegal escape with space"""
    tokenizer = Tokenizer('"test\\ space"')
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Illegal Escape" in str(excinfo.value)


def test_error_char_in_expression():
    """Test error character in expression"""
    tokenizer = Tokenizer("x @ y")
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Error Token @" in str(excinfo.value)


def test_error_tilde():
    """Test unrecognized ~ character"""
    tokenizer = Tokenizer("~")
    with pytest.raises(Exception) as excinfo:
        tokenizer.get_tokens_as_string()
    assert "Error Token ~" in str(excinfo.value)


def test_variable_declaration_tokens():
    """Test tokenizing a variable declaration"""
    tokenizer = Tokenizer("int x = 10;")
    result = tokenizer.get_tokens_as_string()
    assert result == "INT,int,ID,x,ASSIGN,=,INTEGER_LITERAL,10,SEMICOLON,;,EOF"


def test_function_header_tokens():
    """Test tokenizing function header"""
    tokenizer = Tokenizer("void main()")
    result = tokenizer.get_tokens_as_string()
    assert result == "VOID,void,ID,main,LEFT_PAREN,(,RIGHT_PAREN,),EOF"


def test_expression_tokens():
    """Test tokenizing arithmetic expression"""
    tokenizer = Tokenizer("a + b * c")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,a,PLUS,+,ID,b,MULTIPLY,*,ID,c,EOF"


def test_comparison_tokens():
    """Test tokenizing comparison expression"""
    tokenizer = Tokenizer("x >= 10 && y <= 20")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,x,GREATER_THAN_OR_EQUAL,>=,INTEGER_LITERAL,10,LOGICAL_AND,&&,ID,y,LESS_THAN_OR_EQUAL,<=,INTEGER_LITERAL,20,EOF"


def test_increment_decrement_tokens():
    """Test tokenizing increment and decrement"""
    tokenizer = Tokenizer("++i--")
    result = tokenizer.get_tokens_as_string()
    assert result == "INCREMENT,++,ID,i,DECREMENT,--,EOF"


def test_struct_declaration_tokens():
    """Test tokenizing struct declaration"""
    tokenizer = Tokenizer("struct Point { int x; }")
    result = tokenizer.get_tokens_as_string()
    assert result == "STRUCT,struct,ID,Point,LEFT_BRACE,{,INT,int,ID,x,SEMICOLON,;,RIGHT_BRACE,},EOF"


def test_member_access_tokens():
    """Test tokenizing member access"""
    tokenizer = Tokenizer("point.x")
    result = tokenizer.get_tokens_as_string()
    assert result == "ID,point,MEMBER_ACCESS,.,ID,x,EOF"


def test_switch_case_tokens():
    """Test tokenizing switch case keywords"""
    tokenizer = Tokenizer("switch case default break")
    result = tokenizer.get_tokens_as_string()
    assert result == "SWITCH,switch,CASE,case,DEFAULT,default,BREAK,break,EOF"


def test_control_flow_tokens():
    """Test tokenizing control flow keywords"""
    tokenizer = Tokenizer("if else while for continue")
    result = tokenizer.get_tokens_as_string()
    assert result == "IF,if,ELSE,else,WHILE,while,FOR,for,CONTINUE,continue,EOF"


def test_all_separators():
    """Test all separators together"""
    tokenizer = Tokenizer("( ) { } [ ] ; , :")
    result = tokenizer.get_tokens_as_string()
    assert result == "LEFT_PAREN,(,RIGHT_PAREN,),LEFT_BRACE,{,RIGHT_BRACE,},LEFT_SQUARE_BRACKET,[,RIGHT_SQUARE_BRACKET,],SEMICOLON,;,COMMA,,,COLON,:,EOF"
# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"
