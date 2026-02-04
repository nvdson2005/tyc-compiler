"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser

# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"


def test_parser_case_11():
    """11. Empty struct"""
    source = "struct Empty { };"
    assert Parser(source).parse() == "success"


def test_parser_case_12():
    """12. Struct with members"""
    source = "struct Pair { int x; float y; string s; };"
    assert Parser(source).parse() == "success"


def test_parser_case_13():
    """13. Inferred return type function"""
    source = "add(int a, int b) { return a + b; }"
    assert Parser(source).parse() == "success"


def test_parser_case_14():
    """14. Explicit return type function"""
    source = "int add(int a, int b) { return a + b; }"
    assert Parser(source).parse() == "success"


def test_parser_case_15():
    """15. Nested blocks"""
    source = "void main() { { { } } }"
    assert Parser(source).parse() == "success"


def test_parser_case_16():
    """16. If-else with blocks"""
    source = "void main() { if (1) { auto x = 1; } else { auto y = 2; } }"
    assert Parser(source).parse() == "success"


def test_parser_case_17():
    """17. While with block"""
    source = "void main() { while (1) { auto x = 0; } }"
    assert Parser(source).parse() == "success"


def test_parser_case_18():
    """18. For with declaration init"""
    source = "void main() { for (auto i = 0; i < 10; ++i) { } }"
    assert Parser(source).parse() == "success"


def test_parser_case_19():
    """19. For with assignment init"""
    source = "void main() { for (i = 0; i < 10; i = i + 1) { } }"
    assert Parser(source).parse() == "success"


def test_parser_case_20():
    """20. For with empty parts"""
    source = "void main() { for (; ; ) { break; } }"
    assert Parser(source).parse() == "success"


def test_parser_case_21():
    """21. Switch with case and default"""
    source = "void main() { switch (1) { case 1: break; default: break; } }"
    assert Parser(source).parse() == "success"


def test_parser_case_22():
    """22. Switch with multiple cases"""
    source = "void main() { switch (1) { case 1: case 2: break; } }"
    assert Parser(source).parse() == "success"


def test_parser_case_23():
    """23. Return without expr"""
    source = "void main() { return; }"
    assert Parser(source).parse() == "success"


def test_parser_case_24():
    """24. Return with expr"""
    source = "int main() { return 1; }"
    assert Parser(source).parse() == "success"


def test_parser_case_25():
    """25. Break statement"""
    source = "void main() { break; }"
    assert Parser(source).parse() == "success"


def test_parser_case_26():
    """26. Continue statement"""
    source = "void main() { continue; }"
    assert Parser(source).parse() == "success"


def test_parser_case_27():
    """27. Expression statement call"""
    source = "void main() { printInt(1); }"
    assert Parser(source).parse() == "success"


def test_parser_case_28():
    """28. Assignment to member"""
    source = "void main() { a.b = 5; }"
    assert Parser(source).parse() == "success"


def test_parser_case_29():
    """29. Chained assignment"""
    source = "void main() { a = b = c; }"
    assert Parser(source).parse() == "success"


def test_parser_case_30():
    """30. Unary plus/minus"""
    source = "void main() { auto x = -1 + +2; }"
    assert Parser(source).parse() == "success"


def test_parser_case_31():
    """31. Prefix increment"""
    source = "void main() { auto x = ++i; }"
    assert Parser(source).parse() == "success"


def test_parser_case_32():
    """32. Postfix increment"""
    source = "void main() { auto x = i++; }"
    assert Parser(source).parse() == "success"


def test_parser_case_33():
    """33. Prefix decrement"""
    source = "void main() { auto x = --i; }"
    assert Parser(source).parse() == "success"


def test_parser_case_34():
    """34. Postfix decrement"""
    source = "void main() { auto x = i--; }"
    assert Parser(source).parse() == "success"


def test_parser_case_35():
    """35. Logical and/or precedence"""
    source = "void main() { auto x = 1 && 2 || 3; }"
    assert Parser(source).parse() == "success"


def test_parser_case_36():
    """36. Equality expression"""
    source = "void main() { auto x = 1 == 2; }"
    assert Parser(source).parse() == "success"


def test_parser_case_37():
    """37. Relational expression"""
    source = "void main() { auto x = 1 < 2; }"
    assert Parser(source).parse() == "success"


def test_parser_case_38():
    """38. Additive expression"""
    source = "void main() { auto x = 1 + 2 - 3; }"
    assert Parser(source).parse() == "success"


def test_parser_case_39():
    """39. Multiplicative expression"""
    source = "void main() { auto x = 1 * 2 / 3 % 4; }"
    assert Parser(source).parse() == "success"


def test_parser_case_40():
    """40. Parenthesized expression"""
    source = "void main() { auto x = (1 + 2) * 3; }"
    assert Parser(source).parse() == "success"


def test_parser_case_41():
    """41. Member access chain"""
    source = "void main() { auto x = a.b.c; }"
    assert Parser(source).parse() == "success"


def test_parser_case_42():
    """42. Call then member"""
    source = "void main() { auto x = a(1).b; }"
    assert Parser(source).parse() == "success"


def test_parser_case_43():
    """43. Chained calls"""
    source = "void main() { auto x = a(1)(2); }"
    assert Parser(source).parse() == "success"


def test_parser_case_44():
    """44. Struct init literal"""
    source = "void main() { auto x = {1, 2, 3}; }"
    assert Parser(source).parse() == "success"


def test_parser_case_45():
    """45. Struct type variable init"""
    source = "struct Point { int x; int y; }; void main() { Point p = {1,2}; }"
    assert Parser(source).parse() == "success"


def test_parser_case_46():
    """46. Nested struct init"""
    source = "void main() { auto p = { {1,2}, 3 }; }"
    assert Parser(source).parse() == "success"


def test_parser_case_47():
    """47. String literal expression"""
    source = "void main() { auto x = \"hello\"; }"
    assert Parser(source).parse() == "success"


def test_parser_case_48():
    """48. Float literal expression"""
    source = "void main() { auto x = 1e3; }"
    assert Parser(source).parse() == "success"


def test_parser_case_49():
    """49. Variable declaration without init"""
    source = "void main() { int x; float y; string s; }"
    assert Parser(source).parse() == "success"


def test_parser_case_50():
    """50. Multiple statements"""
    source = "void main() { int x; x = 1; x = x + 1; }"
    assert Parser(source).parse() == "success"


def test_parser_case_51():
    """51. If without else"""
    source = "void main() { if (1) return; }"
    assert Parser(source).parse() == "success"


def test_parser_case_52():
    """52. While with single statement"""
    source = "void main() { while (1) return; }"
    assert Parser(source).parse() == "success"


def test_parser_case_53():
    """53. For with update expression"""
    source = "void main() { for (auto i = 0; i < 10; i = i + 1) { } }"
    assert Parser(source).parse() == "success"


def test_parser_case_54():
    """54. Switch with empty body"""
    source = "void main() { switch (x) { } }"
    assert Parser(source).parse() == "success"


def test_parser_case_55():
    """55. Switch fallthrough"""
    source = "void main() { switch (x) { case 1: case 2: return; } }"
    assert Parser(source).parse() == "success"


def test_parser_case_56():
    """56. Logical not"""
    source = "void main() { auto x = !(!1); }"
    assert Parser(source).parse() == "success"


def test_parser_case_57():
    """57. Comparison chain"""
    source = "void main() { auto x = 1 < 2 == 3 != 4; }"
    assert Parser(source).parse() == "success"


def test_parser_case_58():
    """58. Modulus"""
    source = "void main() { auto x = 5 % 2; }"
    assert Parser(source).parse() == "success"


def test_parser_case_59():
    """59. Function call in expression"""
    source = "void main() { auto x = add(1,2); }"
    assert Parser(source).parse() == "success"


def test_parser_case_60():
    """60. Struct type variable decl"""
    source = "struct S { int x; }; void main() { S s; }"
    assert Parser(source).parse() == "success"


def test_parser_case_61():
    """61. Multiple functions"""
    source = "int f() { return 1; } void main() { auto x = f(); }"
    assert Parser(source).parse() == "success"


def test_parser_case_62():
    """62. Assignment expression in parens"""
    source = "void main() { auto x = (a = 1); }"
    assert Parser(source).parse() == "success"


def test_parser_case_63():
    """63. Complex expression"""
    source = "void main() { auto x = (a(1) + b(2)) * c(3); }"
    assert Parser(source).parse() == "success"


def test_parser_case_64():
    """64. Empty struct init"""
    source = "void main() { auto x = { }; }"
    assert Parser(source).parse() == "success"


def test_parser_case_65():
    """65. Single element struct init"""
    source = "void main() { auto x = {1}; }"
    assert Parser(source).parse() == "success"


def test_parser_case_66():
    """66. Nested struct init"""
    source = "void main() { auto x = {1, {2,3}}; }"
    assert Parser(source).parse() == "success"


def test_parser_case_67():
    """67. Multiple nested struct init"""
    source = "void main() { auto x = { {1}, {2} }; }"
    assert Parser(source).parse() == "success"


def test_parser_case_68():
    """68. Call with no args"""
    source = "void main() { foo(); }"
    assert Parser(source).parse() == "success"


def test_parser_case_69():
    """69. If-else dangling"""
    source = "void main() { if (1) if (0) return; else return; }"
    assert Parser(source).parse() == "success"


def test_parser_case_70():
    """70. Switch case with block"""
    source = "void main() { switch (x) { case 1: { auto y = 2; } } }"
    assert Parser(source).parse() == "success"


def test_parser_case_71():
    """71. Missing semicolon"""
    source = "void main() { int x }"
    assert Parser(source).parse() != "success"


def test_parser_case_72():
    """72. Missing right paren"""
    source = "void main( { }"
    assert Parser(source).parse() != "success"


def test_parser_case_73():
    """73. Missing left paren"""
    source = "void main) { }"
    assert Parser(source).parse() != "success"


def test_parser_case_74():
    """74. Missing right brace"""
    source = "void main() {"
    assert Parser(source).parse() != "success"


def test_parser_case_75():
    """75. Var decl missing semicolon"""
    source = "void main() { auto x = 1 }"
    assert Parser(source).parse() != "success"


def test_parser_case_76():
    """76. Invalid parameter auto"""
    source = "void f(auto x) { }"
    assert Parser(source).parse() != "success"


def test_parser_case_77():
    """77. Invalid struct member auto"""
    source = "struct S { auto x; };"
    assert Parser(source).parse() != "success"


def test_parser_case_78():
    """78. Missing colon in case"""
    source = "void main() { switch (1) { case 1 break; } }"
    assert Parser(source).parse() != "success"


def test_parser_case_79():
    """79. Missing colon in default"""
    source = "void main() { switch (1) { default break; } }"
    assert Parser(source).parse() != "success"


def test_parser_case_80():
    """80. Return missing semicolon"""
    source = "void main() { return }"
    assert Parser(source).parse() != "success"


def test_parser_case_81():
    """81. Break missing semicolon"""
    source = "void main() { break }"
    assert Parser(source).parse() != "success"


def test_parser_case_82():
    """82. Continue missing semicolon"""
    source = "void main() { continue }"
    assert Parser(source).parse() != "success"


def test_parser_case_83():
    """83. For missing semicolons"""
    source = "void main() { for (auto i = 0 i < 10 i++) { } }"
    assert Parser(source).parse() != "success"


def test_parser_case_84():
    """84. For missing right paren"""
    source = "void main() { for (auto i = 0; i < 10; i++ { } }"
    assert Parser(source).parse() != "success"


def test_parser_case_85():
    """85. If missing right paren"""
    source = "void main() { if (1 return; }"
    assert Parser(source).parse() != "success"


def test_parser_case_86():
    """86. While missing right paren"""
    source = "void main() { while (1 return; }"
    assert Parser(source).parse() != "success"


def test_parser_case_87():
    """87. Switch missing right brace"""
    source = "void main() { switch (1) { case 1: break; }"
    assert Parser(source).parse() != "success"


def test_parser_case_88():
    """88. Assignment missing rhs"""
    source = "void main() { a = ; }"
    assert Parser(source).parse() != "success"


def test_parser_case_89():
    """89. Trailing operator"""
    source = "void main() { auto x = 1 + ; }"
    assert Parser(source).parse() != "success"


def test_parser_case_90():
    """90. Function missing block"""
    source = "void main();"
    assert Parser(source).parse() != "success"


def test_parser_case_91():
    """91. Struct missing semicolon"""
    source = "struct S { int x; }"
    assert Parser(source).parse() != "success"


def test_parser_case_92():
    """92. Struct missing closing brace"""
    source = "struct S { int x; "
    assert Parser(source).parse() != "success"


def test_parser_case_93():
    """93. Var decl missing id"""
    source = "void main() { int ; }"
    assert Parser(source).parse() != "success"


def test_parser_case_94():
    """94. Param missing id"""
    source = "void f(int) { }"
    assert Parser(source).parse() != "success"


def test_parser_case_95():
    """95. Missing right paren in params"""
    source = "void f(int a, int b { }"
    assert Parser(source).parse() != "success"


def test_parser_case_96():
    """96. Empty parameter with comma"""
    source = "void f(int a,) { }"
    assert Parser(source).parse() != "success"


def test_parser_case_97():
    """97. Case missing expression"""
    source = "void main() { switch (1) { case : break; } }"
    assert Parser(source).parse() != "success"


def test_parser_case_98():
    """98. Invalid token in program"""
    source = "@"
    assert Parser(source).parse() != "success"


def test_parser_case_99():
    """99. Else without if"""
    source = "void main() { else return; }"
    assert Parser(source).parse() != "success"


def test_parser_case_100():
    """100. Empty statement"""
    source = "void main() { ; }"
    assert Parser(source).parse() != "success"
