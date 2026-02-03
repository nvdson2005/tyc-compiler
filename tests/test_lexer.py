"""
Lexer test cases for TyC compiler
"""

import pytest
from tests.utils import Tokenizer

def test_keyword_break():
    """Test 'break' keyword recognition"""
    tokenizer = Tokenizer("break")
    result = tokenizer.get_tokens_as_string()
    assert result == "break,<EOF>"


def test_keyword_case():
    """Test 'case' keyword recognition"""
    tokenizer = Tokenizer("case")
    result = tokenizer.get_tokens_as_string()
    assert result == "case,<EOF>"


def test_keyword_continue():
    """Test 'continue' keyword recognition"""
    tokenizer = Tokenizer("continue")
    result = tokenizer.get_tokens_as_string()
    assert result == "continue,<EOF>"


def test_keyword_default():
    """Test 'default' keyword recognition"""
    tokenizer = Tokenizer("default")
    result = tokenizer.get_tokens_as_string()
    assert result == "default,<EOF>"


def test_keyword_else():
    """Test 'else' keyword recognition"""
    tokenizer = Tokenizer("else")
    result = tokenizer.get_tokens_as_string()
    assert result == "else,<EOF>"


def test_keyword_float():
    """Test 'float' keyword recognition"""
    tokenizer = Tokenizer("float")
    result = tokenizer.get_tokens_as_string()
    assert result == "float,<EOF>"


def test_keyword_for():
    """Test 'for' keyword recognition"""
    tokenizer = Tokenizer("for")
    result = tokenizer.get_tokens_as_string()
    assert result == "for,<EOF>"


def test_keyword_if():
    """Test 'if' keyword recognition"""
    tokenizer = Tokenizer("if")
    result = tokenizer.get_tokens_as_string()
    assert result == "if,<EOF>"


def test_keyword_int():
    """Test 'int' keyword recognition"""
    tokenizer = Tokenizer("int")
    result = tokenizer.get_tokens_as_string()
    assert result == "int,<EOF>"


def test_keyword_return():
    """Test 'return' keyword recognition"""
    tokenizer = Tokenizer("return")
    result = tokenizer.get_tokens_as_string()
    assert result == "return,<EOF>"


def test_keyword_string():
    """Test 'string' keyword recognition"""
    tokenizer = Tokenizer("string")
    result = tokenizer.get_tokens_as_string()
    assert result == "string,<EOF>"


def test_keyword_struct():
    """Test 'struct' keyword recognition"""
    tokenizer = Tokenizer("struct")
    result = tokenizer.get_tokens_as_string()
    assert result == "struct,<EOF>"


def test_keyword_switch():
    """Test 'switch' keyword recognition"""
    tokenizer = Tokenizer("switch")
    result = tokenizer.get_tokens_as_string()
    assert result == "switch,<EOF>"


def test_keyword_void():
    """Test 'void' keyword recognition"""
    tokenizer = Tokenizer("void")
    result = tokenizer.get_tokens_as_string()
    assert result == "void,<EOF>"


def test_keyword_while():
    """Test 'while' keyword recognition"""
    tokenizer = Tokenizer("while")
    result = tokenizer.get_tokens_as_string()
    assert result == "while,<EOF>"


def test_operator_plus():
    """Test '+' operator"""
    tokenizer = Tokenizer("+")
    result = tokenizer.get_tokens_as_string()
    assert result == "+,<EOF>"


def test_operator_minus():
    """Test '-' operator"""
    tokenizer = Tokenizer("-")
    result = tokenizer.get_tokens_as_string()
    assert result == "-,<EOF>"


def test_operator_multiply():
    """Test '*' operator"""
    tokenizer = Tokenizer("*")
    result = tokenizer.get_tokens_as_string()
    assert result == "*,<EOF>"


def test_operator_divide():
    """Test '/' operator"""
    tokenizer = Tokenizer("/")
    result = tokenizer.get_tokens_as_string()
    assert result == "/,<EOF>"


def test_operator_modulus():
    """Test '%' operator"""
    tokenizer = Tokenizer("%")
    result = tokenizer.get_tokens_as_string()
    assert result == "%,<EOF>"


def test_operator_equal():
    """Test '==' operator"""
    tokenizer = Tokenizer("==")
    result = tokenizer.get_tokens_as_string()
    assert result == "==,<EOF>"


def test_operator_not_equal():
    """Test '!=' operator"""
    tokenizer = Tokenizer("!=")
    result = tokenizer.get_tokens_as_string()
    assert result == "!=,<EOF>"


def test_operator_less_than():
    """Test '<' operator"""
    tokenizer = Tokenizer("<")
    result = tokenizer.get_tokens_as_string()
    assert result == "<,<EOF>"


def test_operator_greater_than():
    """Test '>' operator"""
    tokenizer = Tokenizer(">")
    result = tokenizer.get_tokens_as_string()
    assert result == ">,<EOF>"


def test_operator_less_than_or_equal():
    """Test '<=' operator"""
    tokenizer = Tokenizer("<=")
    result = tokenizer.get_tokens_as_string()
    assert result == "<=,<EOF>"


def test_operator_greater_than_or_equal():
    """Test '>=' operator"""
    tokenizer = Tokenizer(">=")
    result = tokenizer.get_tokens_as_string()
    assert result == ">=,<EOF>"


def test_operator_logical_and():
    """Test '&&' operator"""
    tokenizer = Tokenizer("&&")
    result = tokenizer.get_tokens_as_string()
    assert result == "&&,<EOF>"


def test_operator_logical_or():
    """Test '||' operator"""
    tokenizer = Tokenizer("||")
    result = tokenizer.get_tokens_as_string()
    assert result == "||,<EOF>"


def test_operator_logical_not():
    """Test '!' operator"""
    tokenizer = Tokenizer("!")
    result = tokenizer.get_tokens_as_string()
    assert result == "!,<EOF>"


def test_operator_increment():
    """Test '++' operator"""
    tokenizer = Tokenizer("++")
    result = tokenizer.get_tokens_as_string()
    assert result == "++,<EOF>"


def test_operator_decrement():
    """Test '--' operator"""
    tokenizer = Tokenizer("--")
    result = tokenizer.get_tokens_as_string()
    assert result == "--,<EOF>"


def test_operator_member_access():
    """Test '.' operator"""
    tokenizer = Tokenizer(".")
    result = tokenizer.get_tokens_as_string()
    assert result == ".,<EOF>"


# =============================================================================

def test_separator_comma():
    """Test ',' separator"""
    tokenizer = Tokenizer(",")
    result = tokenizer.get_tokens_as_string()
    assert result == ",,<EOF>"


def test_separator_left_paren():
    """Test '(' separator"""
    tokenizer = Tokenizer("(")
    result = tokenizer.get_tokens_as_string()
    assert result == "(,<EOF>"


def test_separator_right_paren():
    """Test ')' separator"""
    tokenizer = Tokenizer(")")
    result = tokenizer.get_tokens_as_string()
    assert result == "),<EOF>"


def test_separator_left_brace():
    """Test '{' separator"""
    tokenizer = Tokenizer("{")
    result = tokenizer.get_tokens_as_string()
    assert result == "{,<EOF>"


def test_separator_right_brace():
    """Test '}' separator"""
    tokenizer = Tokenizer("}")
    result = tokenizer.get_tokens_as_string()
    assert result == "},<EOF>"


def test_separator_semicolon():
    """Test ';' separator"""
    tokenizer = Tokenizer(";")
    result = tokenizer.get_tokens_as_string()
    assert result == ";,<EOF>"


def test_separator_left_square_bracket():
    """Test '[' separator"""
    tokenizer = Tokenizer("[")
    result = tokenizer.get_tokens_as_string()
    assert result == "[,<EOF>"


def test_separator_right_square_bracket():
    """Test ']' separator"""
    tokenizer = Tokenizer("]")
    result = tokenizer.get_tokens_as_string()
    assert result == "],<EOF>"


def test_separator_colon():
    """Test ':' separator"""
    tokenizer = Tokenizer(":")
    result = tokenizer.get_tokens_as_string()
    assert result == ":,<EOF>"



def test_identifier_underscore_start():
    """Test identifier starting with underscore"""
    tokenizer = Tokenizer("_private")
    result = tokenizer.get_tokens_as_string()
    assert result == "_private,<EOF>"


def test_identifier_with_numbers():
    """Test identifier with numbers"""
    tokenizer = Tokenizer("var123")
    result = tokenizer.get_tokens_as_string()
    assert result == "var123,<EOF>"


def test_identifier_uppercase():
    """Test uppercase identifier"""
    tokenizer = Tokenizer("CONSTANT")
    result = tokenizer.get_tokens_as_string()
    assert result == "CONSTANT,<EOF>"


def test_identifier_mixed_case():
    """Test mixed case identifier"""
    tokenizer = Tokenizer("myVariable123")
    result = tokenizer.get_tokens_as_string()
    assert result == "myVariable123,<EOF>"


def test_identifier_single_char():
    """Test single character identifier"""
    tokenizer = Tokenizer("x")
    result = tokenizer.get_tokens_as_string()
    assert result == "x,<EOF>"


def test_identifier_all_underscores():
    """Test identifier with multiple underscores"""
    tokenizer = Tokenizer("__init__")
    result = tokenizer.get_tokens_as_string()
    assert result == "__init__,<EOF>"


def test_identifier_keyword_prefix():
    """Test identifier that starts like a keyword"""
    tokenizer = Tokenizer("integer")
    result = tokenizer.get_tokens_as_string()
    assert result == "integer,<EOF>"


def test_identifier_camelCase():
    """Test camelCase identifier"""
    tokenizer = Tokenizer("myVariableName")
    result = tokenizer.get_tokens_as_string()
    assert result == "myVariableName,<EOF>"


def test_identifier_snake_case():
    """Test snake_case identifier"""
    tokenizer = Tokenizer("my_variable_name")
    result = tokenizer.get_tokens_as_string()
    assert result == "my_variable_name,<EOF>"



def test_integer_zero():
    """Test integer literal zero"""
    tokenizer = Tokenizer("0")
    result = tokenizer.get_tokens_as_string()
    assert result == "0,<EOF>"


def test_integer_positive():
    """Test positive integer literal"""
    tokenizer = Tokenizer("123")
    result = tokenizer.get_tokens_as_string()
    assert result == "123,<EOF>"


def test_integer_large():
    """Test large integer literal"""
    tokenizer = Tokenizer("9999999")
    result = tokenizer.get_tokens_as_string()
    assert result == "9999999,<EOF>"


def test_integer_leading_zeros():
    """Test integer with leading zeros (treated as separate tokens or one)"""
    tokenizer = Tokenizer("007")
    result = tokenizer.get_tokens_as_string()
    assert result == "007,<EOF>"


def test_integer_sequence():
    """Test multiple integers"""
    tokenizer = Tokenizer("1 2 3")
    result = tokenizer.get_tokens_as_string()
    assert result == "1,2,3,<EOF>"


def test_integer_negative_sign_separate():
    """Test negative number (minus is separate token)"""
    tokenizer = Tokenizer("-42")
    result = tokenizer.get_tokens_as_string()
    assert result == "-,42,<EOF>"


# =============================================================================
# FLOAT LITERAL TESTS (10 tests)
# =============================================================================

def test_float_simple():
    """Test simple float literal"""
    tokenizer = Tokenizer("3.14")
    result = tokenizer.get_tokens_as_string()
    assert result == "3.14,<EOF>"


def test_float_zero():
    """Test float zero"""
    tokenizer = Tokenizer("0.0")
    result = tokenizer.get_tokens_as_string()
    assert result == "0.0,<EOF>"


def test_float_trailing_dot():
    """Test float with trailing dot (e.g., 1.)"""
    tokenizer = Tokenizer("1.")
    result = tokenizer.get_tokens_as_string()
    assert result == "1.,<EOF>"


def test_float_leading_dot():
    """Test float with leading dot (e.g., .5)"""
    tokenizer = Tokenizer(".5")
    result = tokenizer.get_tokens_as_string()
    assert result == ".5,<EOF>"


def test_float_scientific_notation():
    """Test float with scientific notation"""
    tokenizer = Tokenizer("1.23e4")
    result = tokenizer.get_tokens_as_string()
    assert result == "1.23e4,<EOF>"


def test_float_scientific_uppercase():
    """Test float with uppercase E"""
    tokenizer = Tokenizer("5.67E2")
    result = tokenizer.get_tokens_as_string()
    assert result == "5.67E2,<EOF>"


def test_float_scientific_negative_exp():
    """Test float with negative exponent"""
    tokenizer = Tokenizer("1.5e-3")
    result = tokenizer.get_tokens_as_string()
    assert result == "1.5e-3,<EOF>"


def test_float_scientific_positive_exp():
    """Test float with positive exponent"""
    tokenizer = Tokenizer("2.0e+10")
    result = tokenizer.get_tokens_as_string()
    assert result == "2.0e+10,<EOF>"


def test_float_integer_with_exponent():
    """Test integer with exponent (becomes float)"""
    tokenizer = Tokenizer("5e3")
    result = tokenizer.get_tokens_as_string()
    assert result == "5e3,<EOF>"


def test_float_multiple():
    """Test multiple float literals"""
    tokenizer = Tokenizer("1.0 2.5 3.14")
    result = tokenizer.get_tokens_as_string()
    assert result == "1.0,2.5,3.14,<EOF>"


# =============================================================================
# STRING LITERAL TESTS (10 tests)
# =============================================================================

def test_string_empty():
    """Test empty string literal"""
    tokenizer = Tokenizer('""')
    result = tokenizer.get_tokens_as_string()
    assert result == ",<EOF>"


def test_string_with_spaces():
    """Test string with spaces"""
    tokenizer = Tokenizer('"hello world"')
    result = tokenizer.get_tokens_as_string()
    assert result == "hello world,<EOF>"


def test_string_escape_newline():
    """Test string with newline escape"""
    tokenizer = Tokenizer('"hello\\nworld"')
    result = tokenizer.get_tokens_as_string()
    assert result == "hello\\nworld,<EOF>"


def test_string_escape_tab():
    """Test string with tab escape"""
    tokenizer = Tokenizer('"hello\\tworld"')
    result = tokenizer.get_tokens_as_string()
    assert result == "hello\\tworld,<EOF>"


def test_string_escape_quote():
    """Test string with escaped quote"""
    tokenizer = Tokenizer('"say \\"hello\\""')
    result = tokenizer.get_tokens_as_string()
    assert result == 'say \\"hello\\",<EOF>'


def test_string_escape_backslash():
    """Test string with escaped backslash"""
    tokenizer = Tokenizer('"path\\\\file"')
    result = tokenizer.get_tokens_as_string()
    assert result == "path\\\\file,<EOF>"


def test_string_escape_carriage_return():
    """Test string with carriage return escape"""
    tokenizer = Tokenizer('"line1\\rline2"')
    result = tokenizer.get_tokens_as_string()
    assert result == "line1\\rline2,<EOF>"


def test_string_escape_backspace():
    """Test string with backspace escape"""
    tokenizer = Tokenizer('"back\\bspace"')
    result = tokenizer.get_tokens_as_string()
    assert result == "back\\bspace,<EOF>"


def test_string_escape_formfeed():
    """Test string with formfeed escape"""
    tokenizer = Tokenizer('"form\\ffeed"')
    result = tokenizer.get_tokens_as_string()
    assert result == "form\\ffeed,<EOF>"


# =============================================================================
# COMMENT TESTS (6 tests)
# =============================================================================

def test_line_comment_simple():
    """Test simple line comment"""
    tokenizer = Tokenizer("// this is a comment")
    result = tokenizer.get_tokens_as_string()
    assert result == "<EOF>"


def test_line_comment_with_code():
    """Test line comment after code"""
    tokenizer = Tokenizer("int x // comment")
    result = tokenizer.get_tokens_as_string()
    assert result == "int,x,<EOF>"


def test_block_comment_simple():
    """Test simple block comment"""
    tokenizer = Tokenizer("/* this is a block comment */")
    result = tokenizer.get_tokens_as_string()
    assert result == "<EOF>"


def test_block_comment_multiline():
    """Test multiline block comment"""
    tokenizer = Tokenizer("/* line1\nline2\nline3 */")
    result = tokenizer.get_tokens_as_string()
    assert result == "<EOF>"


def test_block_comment_with_code():
    """Test block comment between code"""
    tokenizer = Tokenizer("int /* comment */ x")
    result = tokenizer.get_tokens_as_string()
    assert result == "int,x,<EOF>"


def test_comment_in_comment():
    """Test // inside block comment (should be ignored)"""
    tokenizer = Tokenizer("/* // not a line comment */")
    result = tokenizer.get_tokens_as_string()
    assert result == "<EOF>"


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
    assert result == "int,x,=,10,;,<EOF>"


def test_function_header_tokens():
    """Test tokenizing function header"""
    tokenizer = Tokenizer("void main()")
    result = tokenizer.get_tokens_as_string()
    assert result == "void,main,(,),<EOF>"


def test_expression_tokens():
    """Test tokenizing arithmetic expression"""
    tokenizer = Tokenizer("a + b * c")
    result = tokenizer.get_tokens_as_string()
    assert result == "a,+,b,*,c,<EOF>"


def test_comparison_tokens():
    """Test tokenizing comparison expression"""
    tokenizer = Tokenizer("x >= 10 && y <= 20")
    result = tokenizer.get_tokens_as_string()
    assert result == "x,>=,10,&&,y,<=,20,<EOF>"


def test_increment_decrement_tokens():
    """Test tokenizing increment and decrement"""
    tokenizer = Tokenizer("++i--")
    result = tokenizer.get_tokens_as_string()
    assert result == "++,i,--,<EOF>"


def test_struct_declaration_tokens():
    """Test tokenizing struct declaration"""
    tokenizer = Tokenizer("struct Point { int x; }")
    result = tokenizer.get_tokens_as_string()
    assert result == "struct,Point,{,int,x,;,},<EOF>"


def test_member_access_tokens():
    """Test tokenizing member access"""
    tokenizer = Tokenizer("point.x")
    result = tokenizer.get_tokens_as_string()
    assert result == "point,.,x,<EOF>"


def test_switch_case_tokens():
    """Test tokenizing switch case keywords"""
    tokenizer = Tokenizer("switch case default break")
    result = tokenizer.get_tokens_as_string()
    assert result == "switch,case,default,break,<EOF>"


def test_control_flow_tokens():
    """Test tokenizing control flow keywords"""
    tokenizer = Tokenizer("if else while for continue")
    result = tokenizer.get_tokens_as_string()
    assert result == "if,else,while,for,continue,<EOF>"


def test_all_separators():
    """Test all separators together"""
    tokenizer = Tokenizer("( ) { } [ ] ; , :")
    result = tokenizer.get_tokens_as_string()
    assert result == "(,),{,},[,],;,,,,:,<EOF>"
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
