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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u018b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\6")
        buf.write("\2u\n\2\r\2\16\2v\3\2\3\2\3\3\3\3\3\3\3\3\7\3\177\n\3")
        buf.write("\f\3\16\3\u0082\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u008d\n\4\f\4\16\4\u0090\13\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\7\60\u0132\n\60\f\60\16\60\u0135\13\60")
        buf.write("\3\61\6\61\u0138\n\61\r\61\16\61\u0139\3\62\6\62\u013d")
        buf.write("\n\62\r\62\16\62\u013e\3\62\3\62\7\62\u0143\n\62\f\62")
        buf.write("\16\62\u0146\13\62\3\62\5\62\u0149\n\62\3\62\3\62\6\62")
        buf.write("\u014d\n\62\r\62\16\62\u014e\3\62\5\62\u0152\n\62\3\62")
        buf.write("\6\62\u0155\n\62\r\62\16\62\u0156\3\62\5\62\u015a\n\62")
        buf.write("\3\63\3\63\5\63\u015e\n\63\3\63\6\63\u0161\n\63\r\63\16")
        buf.write("\63\u0162\3\64\3\64\7\64\u0167\n\64\f\64\16\64\u016a\13")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\5\65\u0171\n\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\7\67\u0178\n\67\f\67\16\67\u017b\13\67")
        buf.write("\3\67\5\67\u017e\n\67\38\38\78\u0182\n8\f8\168\u0185\13")
        buf.write("8\38\38\38\39\39\3\u0080\2:\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\2g\64i\2k\2m\65o\66q\67\3\2\f\5\2\13\f\16\17\"\"\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\17\17$$^^\t\2$$^^ddhhppttvv\4\3\f\f\17")
        buf.write("\17\2\u019a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2g")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3t\3\2\2\2\5")
        buf.write("z\3\2\2\2\7\u0088\3\2\2\2\t\u0093\3\2\2\2\13\u0098\3\2")
        buf.write("\2\2\r\u009e\3\2\2\2\17\u00a3\3\2\2\2\21\u00ac\3\2\2\2")
        buf.write("\23\u00b4\3\2\2\2\25\u00b9\3\2\2\2\27\u00bf\3\2\2\2\31")
        buf.write("\u00c3\3\2\2\2\33\u00c6\3\2\2\2\35\u00ca\3\2\2\2\37\u00d1")
        buf.write("\3\2\2\2!\u00d8\3\2\2\2#\u00df\3\2\2\2%\u00e6\3\2\2\2")
        buf.write("\'\u00eb\3\2\2\2)\u00f1\3\2\2\2+\u00f3\3\2\2\2-\u00f5")
        buf.write("\3\2\2\2/\u00f7\3\2\2\2\61\u00f9\3\2\2\2\63\u00fb\3\2")
        buf.write("\2\2\65\u00fd\3\2\2\2\67\u00ff\3\2\2\29\u0101\3\2\2\2")
        buf.write(";\u0103\3\2\2\2=\u0106\3\2\2\2?\u0109\3\2\2\2A\u010c\3")
        buf.write("\2\2\2C\u010f\3\2\2\2E\u0112\3\2\2\2G\u0115\3\2\2\2I\u0118")
        buf.write("\3\2\2\2K\u011b\3\2\2\2M\u011d\3\2\2\2O\u011f\3\2\2\2")
        buf.write("Q\u0121\3\2\2\2S\u0123\3\2\2\2U\u0125\3\2\2\2W\u0127\3")
        buf.write("\2\2\2Y\u0129\3\2\2\2[\u012b\3\2\2\2]\u012d\3\2\2\2_\u012f")
        buf.write("\3\2\2\2a\u0137\3\2\2\2c\u0159\3\2\2\2e\u015b\3\2\2\2")
        buf.write("g\u0164\3\2\2\2i\u0170\3\2\2\2k\u0172\3\2\2\2m\u0175\3")
        buf.write("\2\2\2o\u017f\3\2\2\2q\u0189\3\2\2\2su\t\2\2\2ts\3\2\2")
        buf.write("\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\b\2\2\2y")
        buf.write("\4\3\2\2\2z{\7\61\2\2{|\7,\2\2|\u0080\3\2\2\2}\177\13")
        buf.write("\2\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080\u0081\3\2\2\2")
        buf.write("\u0080~\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2")
        buf.write("\2\u0083\u0084\7,\2\2\u0084\u0085\7\61\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\u0087\b\3\2\2\u0087\6\3\2\2\2\u0088\u0089")
        buf.write("\7\61\2\2\u0089\u008a\7\61\2\2\u008a\u008e\3\2\2\2\u008b")
        buf.write("\u008d\n\3\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3")
        buf.write("\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\b\4\2\2\u0092\b")
        buf.write("\3\2\2\2\u0093\u0094\7c\2\2\u0094\u0095\7w\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7q\2\2\u0097\n\3\2\2\2\u0098\u0099")
        buf.write("\7d\2\2\u0099\u009a\7t\2\2\u009a\u009b\7g\2\2\u009b\u009c")
        buf.write("\7c\2\2\u009c\u009d\7m\2\2\u009d\f\3\2\2\2\u009e\u009f")
        buf.write("\7e\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7u\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\16\3\2\2\2\u00a3\u00a4\7e\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7g\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7f\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7w\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3\7v\2\2\u00b3\22")
        buf.write("\3\2\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7")
        buf.write("\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\24\3\2\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7c\2\2\u00bd\u00be\7v\2\2\u00be\26\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\30")
        buf.write("\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7h\2\2\u00c5\32")
        buf.write("\3\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\34\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7p\2\2\u00d0\36\3\2\2\2\u00d1\u00d2")
        buf.write("\7u\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7i\2\2\u00d7 \3")
        buf.write("\2\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\"\3\2\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7y\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7j\2\2\u00e5$\3\2\2\2\u00e6\u00e7")
        buf.write("\7x\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7f\2\2\u00ea&\3\2\2\2\u00eb\u00ec\7y\2\2\u00ec\u00ed")
        buf.write("\7j\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0(\3\2\2\2\u00f1\u00f2\7.\2\2\u00f2*\3\2\2")
        buf.write("\2\u00f3\u00f4\7*\2\2\u00f4,\3\2\2\2\u00f5\u00f6\7+\2")
        buf.write("\2\u00f6.\3\2\2\2\u00f7\u00f8\7}\2\2\u00f8\60\3\2\2\2")
        buf.write("\u00f9\u00fa\7\177\2\2\u00fa\62\3\2\2\2\u00fb\u00fc\7")
        buf.write("=\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7]\2\2\u00fe\66\3\2")
        buf.write("\2\2\u00ff\u0100\7_\2\2\u01008\3\2\2\2\u0101\u0102\7<")
        buf.write("\2\2\u0102:\3\2\2\2\u0103\u0104\7-\2\2\u0104\u0105\7-")
        buf.write("\2\2\u0105<\3\2\2\2\u0106\u0107\7/\2\2\u0107\u0108\7/")
        buf.write("\2\2\u0108>\3\2\2\2\u0109\u010a\7>\2\2\u010a\u010b\7?")
        buf.write("\2\2\u010b@\3\2\2\2\u010c\u010d\7@\2\2\u010d\u010e\7?")
        buf.write("\2\2\u010eB\3\2\2\2\u010f\u0110\7?\2\2\u0110\u0111\7?")
        buf.write("\2\2\u0111D\3\2\2\2\u0112\u0113\7#\2\2\u0113\u0114\7?")
        buf.write("\2\2\u0114F\3\2\2\2\u0115\u0116\7(\2\2\u0116\u0117\7(")
        buf.write("\2\2\u0117H\3\2\2\2\u0118\u0119\7~\2\2\u0119\u011a\7~")
        buf.write("\2\2\u011aJ\3\2\2\2\u011b\u011c\7?\2\2\u011cL\3\2\2\2")
        buf.write("\u011d\u011e\7-\2\2\u011eN\3\2\2\2\u011f\u0120\7/\2\2")
        buf.write("\u0120P\3\2\2\2\u0121\u0122\7,\2\2\u0122R\3\2\2\2\u0123")
        buf.write("\u0124\7\61\2\2\u0124T\3\2\2\2\u0125\u0126\7\'\2\2\u0126")
        buf.write("V\3\2\2\2\u0127\u0128\7>\2\2\u0128X\3\2\2\2\u0129\u012a")
        buf.write("\7@\2\2\u012aZ\3\2\2\2\u012b\u012c\7#\2\2\u012c\\\3\2")
        buf.write("\2\2\u012d\u012e\7\60\2\2\u012e^\3\2\2\2\u012f\u0133\t")
        buf.write("\4\2\2\u0130\u0132\t\5\2\2\u0131\u0130\3\2\2\2\u0132\u0135")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("`\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0138\t\6\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013ab\3\2\2\2\u013b\u013d\t\6\2")
        buf.write("\2\u013c\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0144\7\60\2\2\u0141\u0143\t\6\2\2\u0142\u0141\3\2\2")
        buf.write("\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0147")
        buf.write("\u0149\5e\63\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u015a\3\2\2\2\u014a\u014c\7\60\2\2\u014b\u014d")
        buf.write("\t\6\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2")
        buf.write("\u0150\u0152\5e\63\2\u0151\u0150\3\2\2\2\u0151\u0152\3")
        buf.write("\2\2\2\u0152\u015a\3\2\2\2\u0153\u0155\t\6\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015a\5e\63\2")
        buf.write("\u0159\u013c\3\2\2\2\u0159\u014a\3\2\2\2\u0159\u0154\3")
        buf.write("\2\2\2\u015ad\3\2\2\2\u015b\u015d\t\7\2\2\u015c\u015e")
        buf.write("\t\b\2\2\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u0160\3\2\2\2\u015f\u0161\t\6\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163f\3\2\2\2\u0164\u0168\7$\2\2\u0165\u0167\5")
        buf.write("i\65\2\u0166\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016b\u016c\7$\2\2\u016c\u016d\b\64\3\2")
        buf.write("\u016dh\3\2\2\2\u016e\u0171\n\t\2\2\u016f\u0171\5k\66")
        buf.write("\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171j\3\2")
        buf.write("\2\2\u0172\u0173\7^\2\2\u0173\u0174\t\n\2\2\u0174l\3\2")
        buf.write("\2\2\u0175\u0179\7$\2\2\u0176\u0178\5i\65\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017c\u017e\t\13\2\2\u017d\u017c\3\2\2\2\u017en\3\2\2")
        buf.write("\2\u017f\u0183\7$\2\2\u0180\u0182\5i\65\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0183\3\2\2\2")
        buf.write("\u0186\u0187\7^\2\2\u0187\u0188\n\n\2\2\u0188p\3\2\2\2")
        buf.write("\u0189\u018a\13\2\2\2\u018ar\3\2\2\2\26\2v\u0080\u008e")
        buf.write("\u0133\u0139\u013e\u0144\u0148\u014e\u0151\u0156\u0159")
        buf.write("\u015d\u0162\u0168\u0170\u0179\u017d\u0183\4\b\2\2\3\64")
        buf.write("\2")
        return buf.getvalue()


class TyCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_COMMENT = 2
    LINE_COMMENT = 3
    AUTO = 4
    BREAK = 5
    CASE = 6
    CONTINUE = 7
    DEFAULT = 8
    ELSE = 9
    FLOAT = 10
    FOR = 11
    IF = 12
    INT = 13
    RETURN = 14
    STRING = 15
    STRUCT = 16
    SWITCH = 17
    VOID = 18
    WHILE = 19
    COMMA = 20
    LEFT_PAREN = 21
    RIGHT_PAREN = 22
    LEFT_BRACE = 23
    RIGHT_BRACE = 24
    SEMICOLON = 25
    LEFT_SQUARE_BRACKET = 26
    RIGHT_SQUARE_BRACKET = 27
    COLON = 28
    INCREMENT = 29
    DECREMENT = 30
    LESS_THAN_OR_EQUAL = 31
    GREATER_THAN_OR_EQUAL = 32
    EQUAL = 33
    NOT_EQUAL = 34
    LOGICAL_AND = 35
    LOGICAL_OR = 36
    ASSIGN = 37
    PLUS = 38
    MINUS = 39
    MULTIPLY = 40
    DIVIDE = 41
    MODULUS = 42
    LESS_THAN = 43
    GREATER_THAN = 44
    LOGICAL_NOT = 45
    MEMBER_ACCESS = 46
    ID = 47
    INTEGER_LITERAL = 48
    FLOAT_LITERAL = 49
    STRING_LITERAL = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    ERROR_TOKEN = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'case'", "'continue'", "'default'", "'else'", 
            "'float'", "'for'", "'if'", "'int'", "'return'", "'string'", 
            "'struct'", "'switch'", "'void'", "'while'", "','", "'('", "')'", 
            "'{'", "'}'", "';'", "'['", "']'", "':'", "'++'", "'--'", "'<='", 
            "'>='", "'=='", "'!='", "'&&'", "'||'", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'<'", "'>'", "'!'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "BREAK", "CASE", 
            "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", 
            "RETURN", "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "COMMA", 
            "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE", "SEMICOLON", 
            "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COLON", "INCREMENT", 
            "DECREMENT", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
            "EQUAL", "NOT_EQUAL", "LOGICAL_AND", "LOGICAL_OR", "ASSIGN", 
            "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULUS", "LESS_THAN", 
            "GREATER_THAN", "LOGICAL_NOT", "MEMBER_ACCESS", "ID", "INTEGER_LITERAL", 
            "FLOAT_LITERAL", "STRING_LITERAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

    ruleNames = [ "WS", "BLOCK_COMMENT", "LINE_COMMENT", "AUTO", "BREAK", 
                  "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", 
                  "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", "VOID", 
                  "WHILE", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACE", 
                  "RIGHT_BRACE", "SEMICOLON", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "COLON", "INCREMENT", "DECREMENT", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN_OR_EQUAL", "EQUAL", "NOT_EQUAL", "LOGICAL_AND", 
                  "LOGICAL_OR", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MODULUS", "LESS_THAN", "GREATER_THAN", "LOGICAL_NOT", 
                  "MEMBER_ACCESS", "ID", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                  "EXPONENT", "STRING_LITERAL", "STRING_CHAR", "ESCAPE_SEQUENCE", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.STRING_LITERAL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


