"""
Lexer test cases for TyC compiler
"""

import pytest
from tests.utils import Tokenizer

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


def test_lexer_case_11():
    """11. Keyword break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"


def test_lexer_case_12():
    """12. Keyword case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"


def test_lexer_case_13():
    """13. Keyword continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"


def test_lexer_case_14():
    """14. Keyword default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"


def test_lexer_case_15():
    """15. Keyword else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"


def test_lexer_case_16():
    """16. Keyword float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"


def test_lexer_case_17():
    """17. Keyword for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"


def test_lexer_case_18():
    """18. Keyword if"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"


def test_lexer_case_19():
    """19. Keyword int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"


def test_lexer_case_20():
    """20. Keyword return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"


def test_lexer_case_21():
    """21. Keyword string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"


def test_lexer_case_22():
    """22. Keyword struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"


def test_lexer_case_23():
    """23. Keyword switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"


def test_lexer_case_24():
    """24. Keyword void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"


def test_lexer_case_25():
    """25. Keyword while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"


def test_lexer_case_26():
    """26. Separator comma"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"


def test_lexer_case_27():
    """27. Separator left paren"""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"


def test_lexer_case_28():
    """28. Separator right paren"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"


def test_lexer_case_29():
    """29. Separator left brace"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"


def test_lexer_case_30():
    """30. Separator right brace"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"


def test_lexer_case_31():
    """31. Separator colon"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"


def test_lexer_case_32():
    """32. Operator increment"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"


def test_lexer_case_33():
    """33. Operator decrement"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"


def test_lexer_case_34():
    """34. Operator less than or equal"""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"


def test_lexer_case_35():
    """35. Operator greater than or equal"""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"


def test_lexer_case_36():
    """36. Operator equal"""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"


def test_lexer_case_37():
    """37. Operator not equal"""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"


def test_lexer_case_38():
    """38. Operator logical and"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"


def test_lexer_case_39():
    """39. Operator logical or"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"


def test_lexer_case_40():
    """40. Operator assign"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_lexer_case_41():
    """41. Operator plus"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"


def test_lexer_case_42():
    """42. Operator minus"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"


def test_lexer_case_43():
    """43. Operator multiply"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"


def test_lexer_case_44():
    """44. Operator divide"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"


def test_lexer_case_45():
    """45. Operator modulus"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"


def test_lexer_case_46():
    """46. Operator less than"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"


def test_lexer_case_47():
    """47. Operator greater than"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"


def test_lexer_case_48():
    """48. Operator logical not"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"


def test_lexer_case_49():
    """49. Operator member access"""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"


def test_lexer_case_50():
    """50. Identifier underscore"""
    tokenizer = Tokenizer("_id")
    assert tokenizer.get_tokens_as_string() == "_id,<EOF>"


def test_lexer_case_51():
    """51. Identifier mixed"""
    tokenizer = Tokenizer("a1_b2")
    assert tokenizer.get_tokens_as_string() == "a1_b2,<EOF>"


def test_lexer_case_52():
    """52. Integer leading zeros"""
    tokenizer = Tokenizer("007")
    assert tokenizer.get_tokens_as_string() == "007,<EOF>"


def test_lexer_case_53():
    """53. Float trailing dot"""
    tokenizer = Tokenizer("10.")
    assert tokenizer.get_tokens_as_string() == "10.,<EOF>"


def test_lexer_case_54():
    """54. Float leading dot"""
    tokenizer = Tokenizer(".25")
    assert tokenizer.get_tokens_as_string() == ".25,<EOF>"


def test_lexer_case_55():
    """55. Float exponent"""
    tokenizer = Tokenizer("1e10")
    assert tokenizer.get_tokens_as_string() == "1e10,<EOF>"


def test_lexer_case_56():
    """56. Float exponent sign"""
    tokenizer = Tokenizer("1E-2")
    assert tokenizer.get_tokens_as_string() == "1E-2,<EOF>"


def test_lexer_case_57():
    """57. Float decimal exponent"""
    tokenizer = Tokenizer("3.14e+2")
    assert tokenizer.get_tokens_as_string() == "3.14e+2,<EOF>"


def test_lexer_case_58():
    """58. Empty string literal"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"


def test_lexer_case_59():
    """59. String with space"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"


def test_lexer_case_60():
    """60. String with newline escape"""
    tokenizer = Tokenizer('"a\\n"')
    assert tokenizer.get_tokens_as_string() == "a\\n,<EOF>"


def test_lexer_case_61():
    """61. String with tab escape"""
    tokenizer = Tokenizer('"a\\t"')
    assert tokenizer.get_tokens_as_string() == "a\\t,<EOF>"


def test_lexer_case_62():
    """62. String with quote escape"""
    tokenizer = Tokenizer('"a\\\"b"')
    assert tokenizer.get_tokens_as_string() == "a\\\"b,<EOF>"


def test_lexer_case_63():
    """63. String with backslash escape"""
    tokenizer = Tokenizer('"a\\\\b"')
    assert tokenizer.get_tokens_as_string() == "a\\\\b,<EOF>"


def test_lexer_case_64():
    """64. Line comment only"""
    tokenizer = Tokenizer("// comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_lexer_case_65():
    """65. Block comment only"""
    tokenizer = Tokenizer("/* block */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_lexer_case_66():
    """66. Whitespace only"""
    tokenizer = Tokenizer(" \t\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_lexer_case_67():
    """67. Line comment then token"""
    tokenizer = Tokenizer("//c\nint")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"


def test_lexer_case_68():
    """68. Block comment then token"""
    tokenizer = Tokenizer("/*c*/int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"


def test_lexer_case_69():
    """69. Mixed expression tokens"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_lexer_case_70():
    """70. Member access tokens"""
    tokenizer = Tokenizer("a.b")
    assert tokenizer.get_tokens_as_string() == "a,.,b,<EOF>"


def test_lexer_case_71():
    """71. Function call tokens"""
    tokenizer = Tokenizer("f(1,2)")
    assert tokenizer.get_tokens_as_string() == "f,(,1,,,2,),<EOF>"


def test_lexer_case_72():
    """72. Postfix increment tokens"""
    tokenizer = Tokenizer("a++")
    assert tokenizer.get_tokens_as_string() == "a,++,<EOF>"


def test_lexer_case_73():
    """73. Postfix decrement tokens"""
    tokenizer = Tokenizer("a--")
    assert tokenizer.get_tokens_as_string() == "a,--,<EOF>"


def test_lexer_case_74():
    """74. Logical and tokens"""
    tokenizer = Tokenizer("1&&2")
    assert tokenizer.get_tokens_as_string() == "1,&&,2,<EOF>"


def test_lexer_case_75():
    """75. Logical or tokens"""
    tokenizer = Tokenizer("1||2")
    assert tokenizer.get_tokens_as_string() == "1,||,2,<EOF>"


def test_lexer_case_76():
    """76. Relational tokens"""
    tokenizer = Tokenizer("1<=2")
    assert tokenizer.get_tokens_as_string() == "1,<=,2,<EOF>"


def test_lexer_case_77():
    """77. Equality tokens"""
    tokenizer = Tokenizer("1!=2")
    assert tokenizer.get_tokens_as_string() == "1,!=,2,<EOF>"


def test_lexer_case_78():
    """78. Arithmetic mix tokens"""
    tokenizer = Tokenizer("1+-2")
    assert tokenizer.get_tokens_as_string() == "1,+,-,2,<EOF>"


def test_lexer_case_79():
    """79. Unary not token"""
    tokenizer = Tokenizer("!1")
    assert tokenizer.get_tokens_as_string() == "!,1,<EOF>"


def test_lexer_case_80():
    """80. Auto declaration tokens"""
    tokenizer = Tokenizer("auto x=5;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,;,<EOF>"


def test_lexer_case_81():
    """81. String with carriage return escape"""
    tokenizer = Tokenizer('"a\\r"')
    assert tokenizer.get_tokens_as_string() == "a\\r,<EOF>"


def test_lexer_case_82():
    """82. String with form feed escape"""
    tokenizer = Tokenizer('"a\\f"')
    assert tokenizer.get_tokens_as_string() == "a\\f,<EOF>"


def test_lexer_case_83():
    """83. String with backspace escape"""
    tokenizer = Tokenizer('"a\\b"')
    assert tokenizer.get_tokens_as_string() == "a\\b,<EOF>"


def test_lexer_case_84():
    """84. String with multiple escapes"""
    tokenizer = Tokenizer('"a\\n\\t"')
    assert tokenizer.get_tokens_as_string() == "a\\n\\t,<EOF>"


def test_lexer_case_85():
    """85. Identifier keyword-like"""
    tokenizer = Tokenizer("for1")
    assert tokenizer.get_tokens_as_string() == "for1,<EOF>"


def test_lexer_case_86():
    """86. Identifier with keyword prefix"""
    tokenizer = Tokenizer("intx")
    assert tokenizer.get_tokens_as_string() == "intx,<EOF>"


def test_lexer_case_87():
    """87. Identifier underscore only"""
    tokenizer = Tokenizer("_")
    assert tokenizer.get_tokens_as_string() == "_,<EOF>"


def test_lexer_case_88():
    """88. Float .0"""
    tokenizer = Tokenizer(".0")
    assert tokenizer.get_tokens_as_string() == ".0,<EOF>"


def test_lexer_case_89():
    """89. Float 0."""
    tokenizer = Tokenizer("0.")
    assert tokenizer.get_tokens_as_string() == "0.,<EOF>"


def test_lexer_case_90():
    """90. Float exponent zero"""
    tokenizer = Tokenizer("0e0")
    assert tokenizer.get_tokens_as_string() == "0e0,<EOF>"


def test_lexer_case_91():
    """91. Float decimal exponent zero"""
    tokenizer = Tokenizer("0.0e0")
    assert tokenizer.get_tokens_as_string() == "0.0e0,<EOF>"


def test_lexer_case_92():
    """92. Error token at symbol"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"


def test_lexer_case_93():
    """93. Error token dollar"""
    tokenizer = Tokenizer("$")
    assert tokenizer.get_tokens_as_string() == "Error Token $"


def test_lexer_case_94():
    """94. Unclosed string"""
    tokenizer = Tokenizer('"abc')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: abc"


def test_lexer_case_95():
    """95. Unclosed empty string"""
    tokenizer = Tokenizer('"')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: "


def test_lexer_case_96():
    """96. Illegal escape q"""
    tokenizer = Tokenizer('"a\\q"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: a\\q"


def test_lexer_case_97():
    """97. Illegal escape x"""
    tokenizer = Tokenizer('"\\x"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\x"


def test_lexer_case_98():
    """98. Token then error token"""
    tokenizer = Tokenizer("auto @")
    assert tokenizer.get_tokens_as_string() == "auto,Error Token @"


def test_lexer_case_99():
    """99. Token then illegal escape"""
    tokenizer = Tokenizer('x "a\\q"')
    assert tokenizer.get_tokens_as_string() == "x,Illegal Escape In String: a\\q"


def test_lexer_case_100():
    """100. Block comment then token"""
    tokenizer = Tokenizer("/* comment */int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"
