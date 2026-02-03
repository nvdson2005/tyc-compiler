"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_program_with_comment_only():
    """Test program with only comment"""
    parser = Parser("// just a comment")
    result = parser.parse()
    assert result == "success"


def test_program_with_block_comment():
    """Test program with block comment"""
    parser = Parser("/* block comment */")
    result = parser.parse()
    assert result == "success"


def test_program_single_function():
    """Test program with single function"""
    parser = Parser("void main() {}")
    result = parser.parse()
    assert result == "success"


def test_program_multiple_functions():
    """Test program with multiple functions"""
    source = """
    int add(int x, int y) { return x + y; }
    void main() { int z = add(1, 2); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_void_no_params():
    """Test void function with no parameters"""
    parser = Parser("void main() {}")
    result = parser.parse()
    assert result == "success"


def test_function_int_return():
    """Test function with int return type"""
    parser = Parser("int getValue() { return 42; }")
    result = parser.parse()
    assert result == "success"


def test_function_float_return():
    """Test function with float return type"""
    parser = Parser("float getPI() { return 3.14; }")
    result = parser.parse()
    assert result == "success"


def test_function_string_return():
    """Test function with string return type"""
    parser = Parser('string getMessage() { return "hello"; }')
    result = parser.parse()
    assert result == "success"


def test_function_single_param():
    """Test function with single parameter"""
    parser = Parser("void print(int x) {}")
    result = parser.parse()
    assert result == "success"


def test_function_multiple_params():
    """Test function with multiple parameters"""
    parser = Parser("int add(int x, int y, int z) { return x + y + z; }")
    result = parser.parse()
    assert result == "success"


def test_function_mixed_param_types():
    """Test function with mixed parameter types"""
    parser = Parser("void process(int a, float b, string c) {}")
    result = parser.parse()
    assert result == "success"


def test_function_inferred_return():
    """Test function with inferred return type"""
    parser = Parser("add(int x, int y) { return x + y; }")
    result = parser.parse()
    assert result == "success"


def test_function_struct_return():
    """Test function with struct return type"""
    source = """
    struct Point { int x; int y; };
    Point getOrigin() { return p; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_struct_param():
    """Test function with struct parameter"""
    source = """
    struct Point { int x; int y; };
    void printPoint(Point p) {}
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_empty_body():
    """Test function with empty body"""
    parser = Parser("void doNothing() {}")
    result = parser.parse()
    assert result == "success"


def test_function_nested_blocks():
    """Test function with nested blocks"""
    source = """
    void test() {
        {
            { int x = 1; }
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_struct_single_member():
    """Test struct with single member"""
    parser = Parser("struct Point { int x; };")
    result = parser.parse()
    assert result == "success"


def test_struct_multiple_members():
    """Test struct with multiple members"""
    parser = Parser("struct Point { int x; int y; };")
    result = parser.parse()
    assert result == "success"


def test_struct_mixed_types():
    """Test struct with mixed member types"""
    parser = Parser("struct Person { string name; int age; float height; };")
    result = parser.parse()
    assert result == "success"


def test_struct_empty():
    """Test struct with no members"""
    parser = Parser("struct Empty { };")
    result = parser.parse()
    assert result == "success"


def test_struct_with_struct_member():
    """Test struct with another struct as member"""
    source = """
    struct Point { int x; int y; };
    struct Line { Point start; Point end; };
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_multiple_structs():
    """Test multiple struct declarations"""
    source = """
    struct Point { int x; int y; };
    struct Circle { Point center; int radius; };
    struct Rectangle { Point topLeft; Point bottomRight; };
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_struct_and_function():
    """Test struct and function together"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_struct_trailing_semicolon():
    """Test struct member list with trailing semicolon"""
    parser = Parser("struct Data { int a; int b; };")
    result = parser.parse()
    assert result == "success"


def test_var_auto_with_init():
    """Test auto variable with initialization"""
    parser = Parser("void main() { auto x = 10; }")
    result = parser.parse()
    assert result == "success"


def test_var_auto_without_init():
    """Test auto variable without initialization"""
    parser = Parser("void main() { auto x; }")
    result = parser.parse()
    assert result == "success"


def test_var_int_with_init():
    """Test int variable with initialization"""
    parser = Parser("void main() { int x = 42; }")
    result = parser.parse()
    assert result == "success"


def test_var_int_without_init():
    """Test int variable without initialization"""
    parser = Parser("void main() { int x; }")
    result = parser.parse()
    assert result == "success"


def test_var_float_with_init():
    """Test float variable with initialization"""
    parser = Parser("void main() { float pi = 3.14; }")
    result = parser.parse()
    assert result == "success"


def test_var_float_without_init():
    """Test float variable without initialization"""
    parser = Parser("void main() { float f; }")
    result = parser.parse()
    assert result == "success"


def test_var_string_with_init():
    """Test string variable with initialization"""
    parser = Parser('void main() { string msg = "hello"; }')
    result = parser.parse()
    assert result == "success"


def test_var_string_without_init():
    """Test string variable without initialization"""
    parser = Parser("void main() { string s; }")
    result = parser.parse()
    assert result == "success"


def test_var_struct_without_init():
    """Test struct variable without initialization"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_var_struct_with_init():
    """Test struct variable with initialization"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p = {10, 20}; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_var_multiple_declarations():
    """Test multiple variable declarations"""
    source = """
    void main() {
        int x = 1;
        int y = 2;
        float z = 3.0;
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_var_init_with_expression():
    """Test variable initialization with expression"""
    parser = Parser("void main() { int x = 1 + 2 * 3; }")
    result = parser.parse()
    assert result == "success"


# =============================================================================
# EXPRESSION TESTS (18 tests)
# =============================================================================

def test_expr_integer_literal():
    """Test integer literal expression"""
    parser = Parser("void main() { 42; }")
    result = parser.parse()
    assert result == "success"


def test_expr_float_literal():
    """Test float literal expression"""
    parser = Parser("void main() { 3.14; }")
    result = parser.parse()
    assert result == "success"


def test_expr_string_literal():
    """Test string literal expression"""
    parser = Parser('void main() { "hello"; }')
    result = parser.parse()
    assert result == "success"


def test_expr_identifier():
    """Test identifier expression"""
    parser = Parser("void main() { int x = 10; x; }")
    result = parser.parse()
    assert result == "success"


def test_expr_parenthesized():
    """Test parenthesized expression"""
    parser = Parser("void main() { (1 + 2); }")
    result = parser.parse()
    assert result == "success"


def test_expr_addition():
    """Test addition expression"""
    parser = Parser("void main() { 1 + 2; }")
    result = parser.parse()
    assert result == "success"


def test_expr_subtraction():
    """Test subtraction expression"""
    parser = Parser("void main() { 5 - 3; }")
    result = parser.parse()
    assert result == "success"


def test_expr_multiplication():
    """Test multiplication expression"""
    parser = Parser("void main() { 4 * 5; }")
    result = parser.parse()
    assert result == "success"


def test_expr_division():
    """Test division expression"""
    parser = Parser("void main() { 10 / 2; }")
    result = parser.parse()
    assert result == "success"


def test_expr_modulus():
    """Test modulus expression"""
    parser = Parser("void main() { 10 % 3; }")
    result = parser.parse()
    assert result == "success"


def test_expr_comparison():
    """Test comparison expressions"""
    parser = Parser("void main() { 1 < 2; 2 > 1; 1 <= 2; 2 >= 1; }")
    result = parser.parse()
    assert result == "success"


def test_expr_equality():
    """Test equality expressions"""
    parser = Parser("void main() { 1 == 1; 1 != 2; }")
    result = parser.parse()
    assert result == "success"


def test_expr_logical_and():
    """Test logical AND expression"""
    parser = Parser("void main() { 1 && 1; }")
    result = parser.parse()
    assert result == "success"


def test_expr_logical_or():
    """Test logical OR expression"""
    parser = Parser("void main() { 0 || 1; }")
    result = parser.parse()
    assert result == "success"


def test_expr_logical_not():
    """Test logical NOT expression"""
    parser = Parser("void main() { !0; }")
    result = parser.parse()
    assert result == "success"


def test_expr_unary_minus():
    """Test unary minus expression"""
    parser = Parser("void main() { -5; }")
    result = parser.parse()
    assert result == "success"


def test_expr_unary_plus():
    """Test unary plus expression"""
    parser = Parser("void main() { +5; }")
    result = parser.parse()
    assert result == "success"


def test_expr_complex():
    """Test complex expression with precedence"""
    parser = Parser("void main() { 1 + 2 * 3 - 4 / 2; }")
    result = parser.parse()
    assert result == "success"


# =============================================================================
# INCREMENT/DECREMENT TESTS (6 tests)
# =============================================================================

def test_prefix_increment():
    """Test prefix increment"""
    parser = Parser("void main() { int x = 0; ++x; }")
    result = parser.parse()
    assert result == "success"


def test_prefix_decrement():
    """Test prefix decrement"""
    parser = Parser("void main() { int x = 10; --x; }")
    result = parser.parse()
    assert result == "success"


def test_postfix_increment():
    """Test postfix increment"""
    parser = Parser("void main() { int x = 0; x++; }")
    result = parser.parse()
    assert result == "success"


def test_postfix_decrement():
    """Test postfix decrement"""
    parser = Parser("void main() { int x = 10; x--; }")
    result = parser.parse()
    assert result == "success"


def test_increment_in_expression():
    """Test increment in expression"""
    parser = Parser("void main() { int x = 0; int y = ++x + 1; }")
    result = parser.parse()
    assert result == "success"


def test_decrement_in_expression():
    """Test decrement in expression"""
    parser = Parser("void main() { int x = 10; int y = x-- - 1; }")
    result = parser.parse()
    assert result == "success"


# =============================================================================
# ASSIGNMENT TESTS (6 tests)
# =============================================================================

# def test_assignment_simple():
#     """Test simple assignment"""
#     parser = Parser("void main() { int x; x = 10; }")
#     result = parser.parse()
#     assert result == "success"


def test_assignment_expression():
    """Test assignment with expression"""
    parser = Parser("void main() { int x; x = 1 + 2 * 3; }")
    result = parser.parse()
    assert result == "success"


def test_assignment_chain():
    """Test chained assignment (right associative)"""
    parser = Parser("void main() { int x; int y; x = y = 10; }")
    result = parser.parse()
    assert result == "success"


def test_assignment_member():
    """Test member assignment"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; p.x = 10; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_assignment_nested_member():
    """Test nested member assignment"""
    source = """
    struct Point { int x; int y; };
    struct Line { Point start; Point end; };
    void main() { Line l; l.start.x = 10; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_assignment_from_function():
    """Test assignment from function call"""
    source = """
    int getValue() { return 42; }
    void main() { int x; x = getValue(); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


# =============================================================================
# IF STATEMENT TESTS (6 tests)
# =============================================================================

# def test_if_simple():
#     """Test simple if statement"""
#     parser = Parser("void main() { if (1) {} }")
#     result = parser.parse()
#     assert result == "success"


def test_if_with_block():
    """Test if with block body"""
    parser = Parser("void main() { if (x > 0) { int y = 1; } }")
    result = parser.parse()
    assert result == "success"


def test_if_else():
    """Test if-else statement"""
    parser = Parser("void main() { if (x > 0) { } else { } }")
    result = parser.parse()
    assert result == "success"


def test_if_else_nested():
    """Test nested if-else statements"""
    source = """
    void main() {
        if (x > 0) {
            if (y > 0) { }
        } else {
            if (z > 0) { } else { }
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_if_complex_condition():
    """Test if with complex condition"""
    parser = Parser("void main() { if (x > 0 && y < 10 || z == 5) { } }")
    result = parser.parse()
    assert result == "success"


def test_if_else_chain():
    """Test if-else chain (else if pattern)"""
    source = """
    void main() {
        if (x == 1) { }
        else { if (x == 2) { } else { } }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


# def test_while_simple():
#     """Test simple while statement"""
#     parser = Parser("void main() { while (1) {} }")
#     result = parser.parse()
#     assert result == "success"


def test_while_with_body():
    """Test while with body"""
    parser = Parser("void main() { int i = 0; while (i < 10) { ++i; } }")
    result = parser.parse()
    assert result == "success"


def test_while_nested():
    """Test nested while loops"""
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            int j = 0;
            while (j < 10) {
                ++j;
            }
            ++i;
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_while_with_break_continue():
    """Test while with break and continue"""
    source = """
    void main() {
        int i = 0;
        while (i < 100) {
            if (i == 50) { break; }
            if (i % 2 == 0) { continue; }
            ++i;
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


# def test_for_simple():
#     """Test simple for statement"""
#     parser = Parser("void main() { for (int i = 0; i < 10; ++i) {} }")
#     result = parser.parse()
#     assert result == "success"


def test_for_empty_parts():
    """Test for with empty parts"""
    parser = Parser("void main() { for (;;) { break; } }")
    result = parser.parse()
    assert result == "success"


def test_for_without_init():
    """Test for without init"""
    parser = Parser("void main() { int i = 0; for (; i < 10; ++i) {} }")
    result = parser.parse()
    assert result == "success"


def test_for_without_update():
    """Test for without update"""
    parser = Parser("void main() { for (int i = 0; i < 10;) { ++i; } }")
    result = parser.parse()
    assert result == "success"


def test_for_with_assignment_init():
    """Test for with assignment as init"""
    parser = Parser("void main() { int i; for (i = 0; i < 10; ++i) {} }")
    result = parser.parse()
    assert result == "success"


def test_for_nested():
    """Test nested for loops"""
    source = """
    void main() {
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
            }
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


# def test_switch_simple():
#     """Test simple switch statement"""
#     source = """
#     void main() {
#         int x = 1;
#         switch (x) {
#             case 1: break;
#         }
#     }
#     """
#     parser = Parser(source)
#     result = parser.parse()
#     assert result == "success"


def test_switch_multiple_cases():
    """Test switch with multiple cases"""
    source = """
    void main() {
        int x = 2;
        switch (x) {
            case 1: break;
            case 2: break;
            case 3: break;
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_switch_with_default():
    """Test switch with default"""
    source = """
    void main() {
        int x = 5;
        switch (x) {
            case 1: break;
            default: break;
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_switch_fallthrough():
    """Test switch with fallthrough (no break)"""
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
            case 2:
                break;
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_switch_case_with_statements():
    """Test switch case with multiple statements"""
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                int y = 10;
                y = y + 1;
                break;
        }
    }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_switch_empty():
    """Test empty switch statement"""
    parser = Parser("void main() { int x = 1; switch (x) {} }")
    result = parser.parse()
    assert result == "success"


def test_return_void():
    """Test return without value (void)"""
    parser = Parser("void main() { return; }")
    result = parser.parse()
    assert result == "success"


def test_return_value():
    """Test return with value"""
    parser = Parser("int getValue() { return 42; }")
    result = parser.parse()
    assert result == "success"


def test_return_expression():
    """Test return with expression"""
    parser = Parser("int compute() { return 1 + 2 * 3; }")
    result = parser.parse()
    assert result == "success"


def test_return_function_call():
    """Test return with function call"""
    source = """
    int getValue() { return 42; }
    int wrapper() { return getValue(); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_call_no_args():
    """Test function call with no arguments"""
    source = """
    void doSomething() {}
    void main() { doSomething(); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_call_single_arg():
    """Test function call with single argument"""
    source = """
    void print(int x) {}
    void main() { print(42); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_call_multiple_args():
    """Test function call with multiple arguments"""
    source = """
    int add(int x, int y, int z) { return x + y + z; }
    void main() { int result = add(1, 2, 3); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_call_expression_args():
    """Test function call with expression arguments"""
    source = """
    int add(int x, int y) { return x + y; }
    void main() { int result = add(1 + 2, 3 * 4); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_function_call_nested():
    """Test nested function calls"""
    source = """
    int f(int x) { return x + 1; }
    int g(int x) { return x * 2; }
    void main() { int result = f(g(5)); }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_member_access_simple():
    """Test simple member access"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; int val = p.x; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_member_access_chain():
    """Test chained member access"""
    source = """
    struct Point { int x; int y; };
    struct Line { Point start; Point end; };
    void main() { Line l; int val = l.start.x; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_member_access_in_expression():
    """Test member access in expression"""
    source = """
    struct Point { int x; int y; };
    void main() { Point p; int sum = p.x + p.y; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_member_increment():
    """Test member increment"""
    source = """
    struct Counter { int value; };
    void main() { Counter c; c.value++; ++c.value; }
    """
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"


def test_error_missing_semicolon():
    """Test syntax error: missing semicolon"""
    parser = Parser("void main() { int x = 10 }")
    result = parser.parse()
    assert result != "success"


def test_error_missing_brace():
    """Test syntax error: missing closing brace"""
    parser = Parser("void main() { int x = 10;")
    result = parser.parse()
    assert result != "success"


def test_error_missing_paren():
    """Test syntax error: missing parenthesis"""
    parser = Parser("void main( { }")
    result = parser.parse()
    assert result != "success"


def test_error_invalid_expression():
    """Test syntax error: invalid expression"""
    parser = Parser("void main() { int x = ; }")
    result = parser.parse()
    assert result != "success"


def test_error_invalid_statement():
    """Test syntax error: invalid statement"""
    parser = Parser("void main() { int; }")
    result = parser.parse()
    assert result != "success"


def test_error_missing_function_body():
    """Test syntax error: missing function body"""
    parser = Parser("void main()")
    result = parser.parse()
    assert result != "success"
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
