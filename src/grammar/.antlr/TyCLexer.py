# Generated from /home/shon/PersonalWorkspace/Uni/PPL/assignment1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0156\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\3\2\6\2_\n\2\r\2\16\2`\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\u00a0\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u00ba\n\6\3\7\3\7\3\7\3\7\7\7\u00c0\n\7\f\7\16")
        buf.write("\7\u00c3\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b")
        buf.write("\u00ce\n\b\f\b\16\b\u00d1\13\b\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\7\21\u00e7\n\21\f\21\16\21\u00ea\13\21\3")
        buf.write("\22\5\22\u00ed\n\22\3\22\6\22\u00f0\n\22\r\22\16\22\u00f1")
        buf.write("\3\23\5\23\u00f5\n\23\3\23\6\23\u00f8\n\23\r\23\16\23")
        buf.write("\u00f9\3\23\3\23\6\23\u00fe\n\23\r\23\16\23\u00ff\3\23")
        buf.write("\3\23\5\23\u0104\n\23\3\23\6\23\u0107\n\23\r\23\16\23")
        buf.write("\u0108\3\24\3\24\7\24\u010d\n\24\f\24\16\24\u0110\13\24")
        buf.write("\3\24\3\24\3\25\3\25\7\25\u0116\n\25\f\25\16\25\u0119")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\5\u00c1\u010e\u0117\2/\3\3")
        buf.write("\5\4\7\5\t\6\13\2\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33")
        buf.write("\16\35\17\37\20!\21#\2%\2\'\2)\2+\22-\23/\24\61\25\63")
        buf.write("\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O")
        buf.write("$Q%S&U\'W(Y)[*\3\2\t\5\2\13\f\16\17\"\"\4\2\f\f\17\17")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\2\u016c")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\3^\3\2\2\2")
        buf.write("\5d\3\2\2\2\7\u009f\3\2\2\2\t\u00a1\3\2\2\2\13\u00b9\3")
        buf.write("\2\2\2\r\u00bb\3\2\2\2\17\u00c9\3\2\2\2\21\u00d4\3\2\2")
        buf.write("\2\23\u00d6\3\2\2\2\25\u00d8\3\2\2\2\27\u00da\3\2\2\2")
        buf.write("\31\u00dc\3\2\2\2\33\u00de\3\2\2\2\35\u00e0\3\2\2\2\37")
        buf.write("\u00e2\3\2\2\2!\u00e4\3\2\2\2#\u00ec\3\2\2\2%\u00f4\3")
        buf.write("\2\2\2\'\u010a\3\2\2\2)\u0113\3\2\2\2+\u011c\3\2\2\2-")
        buf.write("\u011e\3\2\2\2/\u0121\3\2\2\2\61\u0124\3\2\2\2\63\u0126")
        buf.write("\3\2\2\2\65\u0128\3\2\2\2\67\u012a\3\2\2\29\u012c\3\2")
        buf.write("\2\2;\u012e\3\2\2\2=\u0130\3\2\2\2?\u0132\3\2\2\2A\u0135")
        buf.write("\3\2\2\2C\u0138\3\2\2\2E\u013b\3\2\2\2G\u013e\3\2\2\2")
        buf.write("I\u0140\3\2\2\2K\u0143\3\2\2\2M\u0146\3\2\2\2O\u0148\3")
        buf.write("\2\2\2Q\u014a\3\2\2\2S\u014c\3\2\2\2U\u014e\3\2\2\2W\u0150")
        buf.write("\3\2\2\2Y\u0152\3\2\2\2[\u0154\3\2\2\2]_\t\2\2\2^]\3\2")
        buf.write("\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\2\2\2")
        buf.write("c\4\3\2\2\2de\7u\2\2ef\7v\2\2fg\7t\2\2gh\7w\2\2hi\7e\2")
        buf.write("\2ij\7v\2\2j\6\3\2\2\2k\u00a0\3\2\2\2l\u00a0\5\13\6\2")
        buf.write("mn\7d\2\2no\7t\2\2op\7g\2\2pq\7c\2\2q\u00a0\7m\2\2rs\7")
        buf.write("e\2\2st\7c\2\2tu\7u\2\2u\u00a0\7g\2\2vw\7e\2\2wx\7q\2")
        buf.write("\2xy\7p\2\2yz\7v\2\2z{\7k\2\2{|\7p\2\2|}\7w\2\2}\u00a0")
        buf.write("\7g\2\2~\177\7f\2\2\177\u0080\7g\2\2\u0080\u0081\7h\2")
        buf.write("\2\u0081\u0082\7c\2\2\u0082\u0083\7w\2\2\u0083\u0084\7")
        buf.write("n\2\2\u0084\u00a0\7v\2\2\u0085\u0086\7g\2\2\u0086\u0087")
        buf.write("\7n\2\2\u0087\u0088\7u\2\2\u0088\u00a0\7g\2\2\u0089\u008a")
        buf.write("\7h\2\2\u008a\u008b\7q\2\2\u008b\u00a0\7t\2\2\u008c\u008d")
        buf.write("\7k\2\2\u008d\u00a0\7h\2\2\u008e\u008f\7t\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\u0091\7v\2\2\u0091\u0092\7w\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\u00a0\7p\2\2\u0094\u0095\7u\2\2\u0095\u0096")
        buf.write("\7y\2\2\u0096\u0097\7k\2\2\u0097\u0098\7v\2\2\u0098\u0099")
        buf.write("\7e\2\2\u0099\u00a0\7j\2\2\u009a\u009b\7y\2\2\u009b\u009c")
        buf.write("\7j\2\2\u009c\u009d\7k\2\2\u009d\u009e\7n\2\2\u009e\u00a0")
        buf.write("\7g\2\2\u009fk\3\2\2\2\u009fl\3\2\2\2\u009fm\3\2\2\2\u009f")
        buf.write("r\3\2\2\2\u009fv\3\2\2\2\u009f~\3\2\2\2\u009f\u0085\3")
        buf.write("\2\2\2\u009f\u0089\3\2\2\2\u009f\u008c\3\2\2\2\u009f\u008e")
        buf.write("\3\2\2\2\u009f\u0094\3\2\2\2\u009f\u009a\3\2\2\2\u00a0")
        buf.write("\b\3\2\2\2\u00a1\u00a2\5\13\6\2\u00a2\n\3\2\2\2\u00a3")
        buf.write("\u00a4\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00ba\7v\2\2\u00a6")
        buf.write("\u00a7\7h\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7q\2\2\u00a9")
        buf.write("\u00aa\7c\2\2\u00aa\u00ba\7v\2\2\u00ab\u00ac\7u\2\2\u00ac")
        buf.write("\u00ad\7v\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7k\2\2\u00af")
        buf.write("\u00b0\7p\2\2\u00b0\u00ba\7i\2\2\u00b1\u00b2\7x\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7k\2\2\u00b4\u00ba\7f\2\2\u00b5")
        buf.write("\u00b6\7c\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7v\2\2\u00b8")
        buf.write("\u00ba\7q\2\2\u00b9\u00a3\3\2\2\2\u00b9\u00a6\3\2\2\2")
        buf.write("\u00b9\u00ab\3\2\2\2\u00b9\u00b1\3\2\2\2\u00b9\u00b5\3")
        buf.write("\2\2\2\u00ba\f\3\2\2\2\u00bb\u00bc\7\61\2\2\u00bc\u00bd")
        buf.write("\7,\2\2\u00bd\u00c1\3\2\2\2\u00be\u00c0\13\2\2\2\u00bf")
        buf.write("\u00be\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3")
        buf.write("\2\2\2\u00c4\u00c5\7,\2\2\u00c5\u00c6\7\61\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c8\b\7\2\2\u00c8\16\3\2\2\2\u00c9\u00ca")
        buf.write("\7\61\2\2\u00ca\u00cb\7\61\2\2\u00cb\u00cf\3\2\2\2\u00cc")
        buf.write("\u00ce\n\3\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d2\3")
        buf.write("\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\b\b\2\2\u00d3\20")
        buf.write("\3\2\2\2\u00d4\u00d5\7.\2\2\u00d5\22\3\2\2\2\u00d6\u00d7")
        buf.write("\7*\2\2\u00d7\24\3\2\2\2\u00d8\u00d9\7+\2\2\u00d9\26\3")
        buf.write("\2\2\2\u00da\u00db\7}\2\2\u00db\30\3\2\2\2\u00dc\u00dd")
        buf.write("\7\177\2\2\u00dd\32\3\2\2\2\u00de\u00df\7=\2\2\u00df\34")
        buf.write("\3\2\2\2\u00e0\u00e1\7]\2\2\u00e1\36\3\2\2\2\u00e2\u00e3")
        buf.write("\7_\2\2\u00e3 \3\2\2\2\u00e4\u00e8\t\4\2\2\u00e5\u00e7")
        buf.write("\t\5\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\"\3\2\2\2\u00ea")
        buf.write("\u00e8\3\2\2\2\u00eb\u00ed\7/\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00f0\t")
        buf.write("\6\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2$\3\2\2\2\u00f3\u00f5")
        buf.write("\7/\2\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f7\3\2\2\2\u00f6\u00f8\t\6\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3")
        buf.write("\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd\7\60\2\2\u00fc")
        buf.write("\u00fe\t\6\2\2\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3")
        buf.write("\2\2\2\u0101\u0103\t\7\2\2\u0102\u0104\t\b\2\2\u0103\u0102")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106\3\2\2\2\u0105")
        buf.write("\u0107\t\6\2\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109&\3\2\2")
        buf.write("\2\u010a\u010e\7$\2\2\u010b\u010d\13\2\2\2\u010c\u010b")
        buf.write("\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010f\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0111\u0112\7$\2\2\u0112(\3\2\2\2\u0113\u0117\7^\2\2")
        buf.write("\u0114\u0116\13\2\2\2\u0115\u0114\3\2\2\2\u0116\u0119")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118")
        buf.write("\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7^\2\2")
        buf.write("\u011b*\3\2\2\2\u011c\u011d\7?\2\2\u011d,\3\2\2\2\u011e")
        buf.write("\u011f\7?\2\2\u011f\u0120\7?\2\2\u0120.\3\2\2\2\u0121")
        buf.write("\u0122\7#\2\2\u0122\u0123\7?\2\2\u0123\60\3\2\2\2\u0124")
        buf.write("\u0125\7-\2\2\u0125\62\3\2\2\2\u0126\u0127\7/\2\2\u0127")
        buf.write("\64\3\2\2\2\u0128\u0129\7,\2\2\u0129\66\3\2\2\2\u012a")
        buf.write("\u012b\7\61\2\2\u012b8\3\2\2\2\u012c\u012d\7\'\2\2\u012d")
        buf.write(":\3\2\2\2\u012e\u012f\7>\2\2\u012f<\3\2\2\2\u0130\u0131")
        buf.write("\7@\2\2\u0131>\3\2\2\2\u0132\u0133\7>\2\2\u0133\u0134")
        buf.write("\7?\2\2\u0134@\3\2\2\2\u0135\u0136\7@\2\2\u0136\u0137")
        buf.write("\7?\2\2\u0137B\3\2\2\2\u0138\u0139\7(\2\2\u0139\u013a")
        buf.write("\7(\2\2\u013aD\3\2\2\2\u013b\u013c\7~\2\2\u013c\u013d")
        buf.write("\7~\2\2\u013dF\3\2\2\2\u013e\u013f\7#\2\2\u013fH\3\2\2")
        buf.write("\2\u0140\u0141\7-\2\2\u0141\u0142\7-\2\2\u0142J\3\2\2")
        buf.write("\2\u0143\u0144\7/\2\2\u0144\u0145\7/\2\2\u0145L\3\2\2")
        buf.write("\2\u0146\u0147\7\60\2\2\u0147N\3\2\2\2\u0148\u0149\5#")
        buf.write("\22\2\u0149P\3\2\2\2\u014a\u014b\5%\23\2\u014bR\3\2\2")
        buf.write("\2\u014c\u014d\5\'\24\2\u014dT\3\2\2\2\u014e\u014f\5)")
        buf.write("\25\2\u014fV\3\2\2\2\u0150\u0151\13\2\2\2\u0151X\3\2\2")
        buf.write("\2\u0152\u0153\13\2\2\2\u0153Z\3\2\2\2\u0154\u0155\13")
        buf.write("\2\2\2\u0155\\\3\2\2\2\22\2`\u009f\u00b9\u00c1\u00cf\u00e8")
        buf.write("\u00ec\u00f1\u00f4\u00f9\u00ff\u0103\u0108\u010e\u0117")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class TyCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    STRUCT = 2
    RESERVED_WORDS = 3
    TYPE = 4
    BLOCK_COMMENT = 5
    LINE_COMMENT = 6
    COMMA = 7
    LEFT_PAREN = 8
    RIGHT_PAREN = 9
    LEFT_BRACE = 10
    RIGHT_BRACE = 11
    SEMICOLON = 12
    LEFT_SQUARE_BRACKET = 13
    RIGHT_SQUARE_BRACKET = 14
    ID = 15
    ASSIGN = 16
    EQUAL = 17
    NOT_EQUAL = 18
    PLUS = 19
    MINUS = 20
    MULTIPLY = 21
    DIVIDE = 22
    MODULUS = 23
    LESS_THAN = 24
    GREATER_THAN = 25
    LESS_THAN_OR_EQUAL = 26
    GREATER_THAN_OR_EQUAL = 27
    LOGICAL_AND = 28
    LOGICAL_OR = 29
    LOGICAL_NOT = 30
    INCREMENT = 31
    DECREMENT = 32
    MEMBER_ACCESS = 33
    INTEGER_LITERAL = 34
    FLOAT_LITERAL = 35
    STRING_LITERAL = 36
    CHAR_LITERAL = 37
    ERROR_CHAR = 38
    ILLEGAL_ESCAPE = 39
    UNCLOSE_STRING = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'struct'", "','", "'('", "')'", "'{'", "'}'", "';'", "'['", 
            "']'", "'='", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", "'++'", 
            "'--'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "STRUCT", "RESERVED_WORDS", "TYPE", "BLOCK_COMMENT", "LINE_COMMENT", 
            "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE", 
            "SEMICOLON", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "ID", "ASSIGN", "EQUAL", "NOT_EQUAL", "PLUS", "MINUS", "MULTIPLY", 
            "DIVIDE", "MODULUS", "LESS_THAN", "GREATER_THAN", "LESS_THAN_OR_EQUAL", 
            "GREATER_THAN_OR_EQUAL", "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", 
            "INCREMENT", "DECREMENT", "MEMBER_ACCESS", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "STRING_LITERAL", "CHAR_LITERAL", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "WS", "STRUCT", "RESERVED_WORDS", "TYPE", "F_TYPE", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", 
                  "LEFT_BRACE", "RIGHT_BRACE", "SEMICOLON", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "ID", "F_NUMBER", "F_FLOAT_NUMBER", 
                  "F_STRING", "F_CHAR", "ASSIGN", "EQUAL", "NOT_EQUAL", 
                  "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULUS", "LESS_THAN", 
                  "GREATER_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
                  "LOGICAL_AND", "LOGICAL_OR", "LOGICAL_NOT", "INCREMENT", 
                  "DECREMENT", "MEMBER_ACCESS", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                  "STRING_LITERAL", "CHAR_LITERAL", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "TyC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


