# Generated from /home/shon/PersonalWorkspace/Uni/PPL/assignment1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u01b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\3\2\7\2S\n\2\f\2\16\2V\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3g\n\3\3\4\3\4\3\5\3\5\3\5\7\5n\n\5\f\5\16\5q\13\5")
        buf.write("\5\5s\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6}\n\6\3\7")
        buf.write("\3\7\3\7\7\7\u0082\n\7\f\7\16\7\u0085\13\7\5\7\u0087\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u0093\n")
        buf.write("\t\f\t\16\t\u0096\13\t\3\t\5\t\u0099\n\t\5\t\u009b\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a5\n\n\3\13\3")
        buf.write("\13\3\13\3\13\7\13\u00ab\n\13\f\13\16\13\u00ae\13\13\5")
        buf.write("\13\u00b0\n\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00b8\n\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00be\n\f\3\f\3\f\3\f\3\f\5\f\u00c4")
        buf.write("\n\f\3\f\3\f\3\f\3\f\5\f\u00ca\n\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00d1\n\f\5\f\u00d3\n\f\5\f\u00d5\n\f\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00de\n\16\3\17\3\17\3\17\7")
        buf.write("\17\u00e3\n\17\f\17\16\17\u00e6\13\17\3\20\3\20\3\20\7")
        buf.write("\20\u00eb\n\20\f\20\16\20\u00ee\13\20\3\21\3\21\3\21\7")
        buf.write("\21\u00f3\n\21\f\21\16\21\u00f6\13\21\3\22\3\22\3\22\7")
        buf.write("\22\u00fb\n\22\f\22\16\22\u00fe\13\22\3\23\3\23\3\23\7")
        buf.write("\23\u0103\n\23\f\23\16\23\u0106\13\23\3\24\3\24\3\24\7")
        buf.write("\24\u010b\n\24\f\24\16\24\u010e\13\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u011b\n\25")
        buf.write("\3\26\3\26\7\26\u011f\n\26\f\26\16\26\u0122\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u012c\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0136\n\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0149\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\7\33\u0152\n\33\f\33\16\33")
        buf.write("\u0155\13\33\3\34\3\34\3\35\3\35\7\35\u015b\n\35\f\35")
        buf.write("\16\35\u015e\13\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0169\n\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3 \5 \u0174\n \3 \3 \5 \u0178\n \3 \3 \5 \u017c")
        buf.write("\n \3 \3 \3 \3!\3!\5!\u0183\n!\3\"\3\"\5\"\u0187\n\"\3")
        buf.write("#\3#\3#\3#\3#\3#\7#\u018f\n#\f#\16#\u0192\13#\3#\5#\u0195")
        buf.write("\n#\3#\3#\3$\3$\3$\3$\7$\u019d\n$\f$\16$\u01a0\13$\3%")
        buf.write("\3%\3%\7%\u01a5\n%\f%\16%\u01a8\13%\3&\3&\5&\u01ac\n&")
        buf.write("\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\2\2)\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("N\2\7\7\2\f\f\17\17\21\21\24\24\61\61\3\2#$\4\2!\"-.\3")
        buf.write("\2()\3\2*,\2\u01d5\2T\3\2\2\2\4f\3\2\2\2\6h\3\2\2\2\b")
        buf.write("r\3\2\2\2\n|\3\2\2\2\f\u0086\3\2\2\2\16\u0088\3\2\2\2")
        buf.write("\20\u009a\3\2\2\2\22\u00a4\3\2\2\2\24\u00a6\3\2\2\2\26")
        buf.write("\u00d4\3\2\2\2\30\u00d6\3\2\2\2\32\u00dd\3\2\2\2\34\u00df")
        buf.write("\3\2\2\2\36\u00e7\3\2\2\2 \u00ef\3\2\2\2\"\u00f7\3\2\2")
        buf.write("\2$\u00ff\3\2\2\2&\u0107\3\2\2\2(\u011a\3\2\2\2*\u011c")
        buf.write("\3\2\2\2,\u012b\3\2\2\2.\u0135\3\2\2\2\60\u0148\3\2\2")
        buf.write("\2\62\u014a\3\2\2\2\64\u014e\3\2\2\2\66\u0156\3\2\2\2")
        buf.write("8\u0158\3\2\2\2:\u0161\3\2\2\2<\u016a\3\2\2\2>\u0170\3")
        buf.write("\2\2\2@\u0182\3\2\2\2B\u0186\3\2\2\2D\u0188\3\2\2\2F\u0198")
        buf.write("\3\2\2\2H\u01a1\3\2\2\2J\u01a9\3\2\2\2L\u01af\3\2\2\2")
        buf.write("N\u01b2\3\2\2\2PS\5\16\b\2QS\5\4\3\2RP\3\2\2\2RQ\3\2\2")
        buf.write("\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2W")
        buf.write("X\7\2\2\3X\3\3\2\2\2YZ\5\6\4\2Z[\7\61\2\2[\\\7\27\2\2")
        buf.write("\\]\5\b\5\2]^\7\30\2\2^_\58\35\2_g\3\2\2\2`a\7\61\2\2")
        buf.write("ab\7\27\2\2bc\5\b\5\2cd\7\30\2\2de\58\35\2eg\3\2\2\2f")
        buf.write("Y\3\2\2\2f`\3\2\2\2g\5\3\2\2\2hi\t\2\2\2i\7\3\2\2\2jo")
        buf.write("\5\n\6\2kl\7\26\2\2ln\5\n\6\2mk\3\2\2\2nq\3\2\2\2om\3")
        buf.write("\2\2\2op\3\2\2\2ps\3\2\2\2qo\3\2\2\2rj\3\2\2\2rs\3\2\2")
        buf.write("\2s\t\3\2\2\2tu\7\17\2\2u}\7\61\2\2vw\7\f\2\2w}\7\61\2")
        buf.write("\2xy\7\21\2\2y}\7\61\2\2z{\7\61\2\2{}\7\61\2\2|t\3\2\2")
        buf.write("\2|v\3\2\2\2|x\3\2\2\2|z\3\2\2\2}\13\3\2\2\2~\u0083\5")
        buf.write("\30\r\2\177\u0080\7\26\2\2\u0080\u0082\5\30\r\2\u0081")
        buf.write("\177\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2")
        buf.write("\u0086~\3\2\2\2\u0086\u0087\3\2\2\2\u0087\r\3\2\2\2\u0088")
        buf.write("\u0089\7\22\2\2\u0089\u008a\7\61\2\2\u008a\u008b\7\31")
        buf.write("\2\2\u008b\u008c\5\20\t\2\u008c\u008d\7\32\2\2\u008d\u008e")
        buf.write("\7\33\2\2\u008e\17\3\2\2\2\u008f\u0094\5\22\n\2\u0090")
        buf.write("\u0091\7\33\2\2\u0091\u0093\5\22\n\2\u0092\u0090\3\2\2")
        buf.write("\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0097")
        buf.write("\u0099\7\33\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2")
        buf.write("\2\u0099\u009b\3\2\2\2\u009a\u008f\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\21\3\2\2\2\u009c\u009d\7\17\2\2\u009d\u00a5")
        buf.write("\7\61\2\2\u009e\u009f\7\f\2\2\u009f\u00a5\7\61\2\2\u00a0")
        buf.write("\u00a1\7\21\2\2\u00a1\u00a5\7\61\2\2\u00a2\u00a3\7\61")
        buf.write("\2\2\u00a3\u00a5\7\61\2\2\u00a4\u009c\3\2\2\2\u00a4\u009e")
        buf.write("\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\23\3\2\2\2\u00a6\u00af\7\31\2\2\u00a7\u00ac\5\30\r\2")
        buf.write("\u00a8\u00a9\7\26\2\2\u00a9\u00ab\5\30\r\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00af\u00a7\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b2\7\32\2\2\u00b2\25\3\2\2\2\u00b3\u00b4")
        buf.write("\7\6\2\2\u00b4\u00b7\7\61\2\2\u00b5\u00b6\7\'\2\2\u00b6")
        buf.write("\u00b8\5\30\r\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2")
        buf.write("\2\u00b8\u00d5\3\2\2\2\u00b9\u00ba\7\17\2\2\u00ba\u00bd")
        buf.write("\7\61\2\2\u00bb\u00bc\7\'\2\2\u00bc\u00be\5\30\r\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00d5\3\2\2\2")
        buf.write("\u00bf\u00c0\7\f\2\2\u00c0\u00c3\7\61\2\2\u00c1\u00c2")
        buf.write("\7\'\2\2\u00c2\u00c4\5\30\r\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00d5\3\2\2\2\u00c5\u00c6\7\21\2")
        buf.write("\2\u00c6\u00c9\7\61\2\2\u00c7\u00c8\7\'\2\2\u00c8\u00ca")
        buf.write("\5\30\r\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00d5\3\2\2\2\u00cb\u00cc\7\61\2\2\u00cc\u00d2\7\61\2")
        buf.write("\2\u00cd\u00d0\7\'\2\2\u00ce\u00d1\5\30\r\2\u00cf\u00d1")
        buf.write("\5\24\13\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d3\3\2\2\2\u00d2\u00cd\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\u00d5\3\2\2\2\u00d4\u00b3\3\2\2\2\u00d4\u00b9\3")
        buf.write("\2\2\2\u00d4\u00bf\3\2\2\2\u00d4\u00c5\3\2\2\2\u00d4\u00cb")
        buf.write("\3\2\2\2\u00d5\27\3\2\2\2\u00d6\u00d7\5\32\16\2\u00d7")
        buf.write("\31\3\2\2\2\u00d8\u00d9\5\34\17\2\u00d9\u00da\7\'\2\2")
        buf.write("\u00da\u00db\5\32\16\2\u00db\u00de\3\2\2\2\u00dc\u00de")
        buf.write("\5\34\17\2\u00dd\u00d8\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\33\3\2\2\2\u00df\u00e4\5\36\20\2\u00e0\u00e1\7&\2\2\u00e1")
        buf.write("\u00e3\5\36\20\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2")
        buf.write("\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\35\3")
        buf.write("\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00ec\5 \21\2\u00e8\u00e9")
        buf.write("\7%\2\2\u00e9\u00eb\5 \21\2\u00ea\u00e8\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\37\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f4\5\"")
        buf.write("\22\2\u00f0\u00f1\t\3\2\2\u00f1\u00f3\5\"\22\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5!\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7")
        buf.write("\u00fc\5$\23\2\u00f8\u00f9\t\4\2\2\u00f9\u00fb\5$\23\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3")
        buf.write("\2\2\2\u00fc\u00fd\3\2\2\2\u00fd#\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\u0104\5&\24\2\u0100\u0101\t\5\2\2\u0101")
        buf.write("\u0103\5&\24\2\u0102\u0100\3\2\2\2\u0103\u0106\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105%\3\2\2")
        buf.write("\2\u0106\u0104\3\2\2\2\u0107\u010c\5(\25\2\u0108\u0109")
        buf.write("\t\6\2\2\u0109\u010b\5(\25\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\'\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\7\37")
        buf.write("\2\2\u0110\u011b\5(\25\2\u0111\u0112\7 \2\2\u0112\u011b")
        buf.write("\5(\25\2\u0113\u0114\7)\2\2\u0114\u011b\5(\25\2\u0115")
        buf.write("\u0116\7(\2\2\u0116\u011b\5(\25\2\u0117\u0118\7/\2\2\u0118")
        buf.write("\u011b\5(\25\2\u0119\u011b\5*\26\2\u011a\u010f\3\2\2\2")
        buf.write("\u011a\u0111\3\2\2\2\u011a\u0113\3\2\2\2\u011a\u0115\3")
        buf.write("\2\2\2\u011a\u0117\3\2\2\2\u011a\u0119\3\2\2\2\u011b)")
        buf.write("\3\2\2\2\u011c\u0120\5.\30\2\u011d\u011f\5,\27\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121+\3\2\2\2\u0122\u0120\3\2\2")
        buf.write("\2\u0123\u012c\7\37\2\2\u0124\u012c\7 \2\2\u0125\u0126")
        buf.write("\7\60\2\2\u0126\u012c\7\61\2\2\u0127\u0128\7\27\2\2\u0128")
        buf.write("\u0129\5\f\7\2\u0129\u012a\7\30\2\2\u012a\u012c\3\2\2")
        buf.write("\2\u012b\u0123\3\2\2\2\u012b\u0124\3\2\2\2\u012b\u0125")
        buf.write("\3\2\2\2\u012b\u0127\3\2\2\2\u012c-\3\2\2\2\u012d\u0136")
        buf.write("\7\61\2\2\u012e\u0136\7\62\2\2\u012f\u0136\7\63\2\2\u0130")
        buf.write("\u0136\7\64\2\2\u0131\u0132\7\27\2\2\u0132\u0133\5\30")
        buf.write("\r\2\u0133\u0134\7\30\2\2\u0134\u0136\3\2\2\2\u0135\u012d")
        buf.write("\3\2\2\2\u0135\u012e\3\2\2\2\u0135\u012f\3\2\2\2\u0135")
        buf.write("\u0130\3\2\2\2\u0135\u0131\3\2\2\2\u0136/\3\2\2\2\u0137")
        buf.write("\u0138\5\26\f\2\u0138\u0139\7\33\2\2\u0139\u0149\3\2\2")
        buf.write("\2\u013a\u013b\5\62\32\2\u013b\u013c\7\33\2\2\u013c\u0149")
        buf.write("\3\2\2\2\u013d\u013e\5\66\34\2\u013e\u013f\7\33\2\2\u013f")
        buf.write("\u0149\3\2\2\2\u0140\u0149\5:\36\2\u0141\u0149\5<\37\2")
        buf.write("\u0142\u0149\5> \2\u0143\u0149\5D#\2\u0144\u0149\5J&\2")
        buf.write("\u0145\u0149\5L\'\2\u0146\u0149\5N(\2\u0147\u0149\58\35")
        buf.write("\2\u0148\u0137\3\2\2\2\u0148\u013a\3\2\2\2\u0148\u013d")
        buf.write("\3\2\2\2\u0148\u0140\3\2\2\2\u0148\u0141\3\2\2\2\u0148")
        buf.write("\u0142\3\2\2\2\u0148\u0143\3\2\2\2\u0148\u0144\3\2\2\2")
        buf.write("\u0148\u0145\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0147\3")
        buf.write("\2\2\2\u0149\61\3\2\2\2\u014a\u014b\5\64\33\2\u014b\u014c")
        buf.write("\7\'\2\2\u014c\u014d\5\30\r\2\u014d\63\3\2\2\2\u014e\u0153")
        buf.write("\7\61\2\2\u014f\u0150\7\60\2\2\u0150\u0152\7\61\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154\65\3\2\2\2\u0155\u0153\3\2")
        buf.write("\2\2\u0156\u0157\5\30\r\2\u0157\67\3\2\2\2\u0158\u015c")
        buf.write("\7\31\2\2\u0159\u015b\5\60\31\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\7")
        buf.write("\32\2\2\u01609\3\2\2\2\u0161\u0162\7\16\2\2\u0162\u0163")
        buf.write("\7\27\2\2\u0163\u0164\5\30\r\2\u0164\u0165\7\30\2\2\u0165")
        buf.write("\u0168\5\60\31\2\u0166\u0167\7\13\2\2\u0167\u0169\5\60")
        buf.write("\31\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169;\3")
        buf.write("\2\2\2\u016a\u016b\7\25\2\2\u016b\u016c\7\27\2\2\u016c")
        buf.write("\u016d\5\30\r\2\u016d\u016e\7\30\2\2\u016e\u016f\5\60")
        buf.write("\31\2\u016f=\3\2\2\2\u0170\u0171\7\r\2\2\u0171\u0173\7")
        buf.write("\27\2\2\u0172\u0174\5@!\2\u0173\u0172\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\7\33\2\2\u0176")
        buf.write("\u0178\5\30\r\2\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2")
        buf.write("\2\u0178\u0179\3\2\2\2\u0179\u017b\7\33\2\2\u017a\u017c")
        buf.write("\5B\"\2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017e\7\30\2\2\u017e\u017f\5\60\31")
        buf.write("\2\u017f?\3\2\2\2\u0180\u0183\5\26\f\2\u0181\u0183\5\62")
        buf.write("\32\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183A\3")
        buf.write("\2\2\2\u0184\u0187\5\62\32\2\u0185\u0187\5\30\r\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187C\3\2\2\2\u0188")
        buf.write("\u0189\7\23\2\2\u0189\u018a\7\27\2\2\u018a\u018b\5\30")
        buf.write("\r\2\u018b\u018c\7\30\2\2\u018c\u0190\7\31\2\2\u018d\u018f")
        buf.write("\5F$\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0195\5H%\2\u0194\u0193\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\7\32\2")
        buf.write("\2\u0197E\3\2\2\2\u0198\u0199\7\b\2\2\u0199\u019a\5\30")
        buf.write("\r\2\u019a\u019e\7\36\2\2\u019b\u019d\5\60\31\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019fG\3\2\2\2\u01a0\u019e\3\2\2")
        buf.write("\2\u01a1\u01a2\7\n\2\2\u01a2\u01a6\7\36\2\2\u01a3\u01a5")
        buf.write("\5\60\31\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7I\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a9\u01ab\7\20\2\2\u01aa\u01ac\5\30\r")
        buf.write("\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\u01ae\7\33\2\2\u01aeK\3\2\2\2\u01af\u01b0")
        buf.write("\7\7\2\2\u01b0\u01b1\7\33\2\2\u01b1M\3\2\2\2\u01b2\u01b3")
        buf.write("\7\t\2\2\u01b3\u01b4\7\33\2\2\u01b4O\3\2\2\2\60RTfor|")
        buf.write("\u0083\u0086\u0094\u0098\u009a\u00a4\u00ac\u00af\u00b7")
        buf.write("\u00bd\u00c3\u00c9\u00d0\u00d2\u00d4\u00dd\u00e4\u00ec")
        buf.write("\u00f4\u00fc\u0104\u010c\u011a\u0120\u012b\u0135\u0148")
        buf.write("\u0153\u015c\u0168\u0173\u0177\u017b\u0182\u0186\u0190")
        buf.write("\u0194\u019e\u01a6\u01ab")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'case'", "'continue'", "'default'", 
                     "'else'", "'float'", "'for'", "'if'", "'int'", "'return'", 
                     "'string'", "'struct'", "'switch'", "'void'", "'while'", 
                     "','", "'('", "')'", "'{'", "'}'", "';'", "'['", "']'", 
                     "':'", "'++'", "'--'", "'<='", "'>='", "'=='", "'!='", 
                     "'&&'", "'||'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'<'", "'>'", "'!'", "'.'" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", 
                      "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                      "SWITCH", "VOID", "WHILE", "COMMA", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE", "SEMICOLON", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COLON", 
                      "INCREMENT", "DECREMENT", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
                      "EQUAL", "NOT_EQUAL", "LOGICAL_AND", "LOGICAL_OR", 
                      "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULUS", 
                      "LESS_THAN", "GREATER_THAN", "LOGICAL_NOT", "MEMBER_ACCESS", 
                      "ID", "INTEGER_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_functionDeclaration = 1
    RULE_returnType = 2
    RULE_parameterList = 3
    RULE_parameter = 4
    RULE_argumentList = 5
    RULE_structDeclaration = 6
    RULE_structMemberList = 7
    RULE_structMember = 8
    RULE_structInit = 9
    RULE_variableDeclaration = 10
    RULE_expression = 11
    RULE_assignmentExpression = 12
    RULE_orExpression = 13
    RULE_andExpression = 14
    RULE_equalityExpression = 15
    RULE_relationalExpression = 16
    RULE_additiveExpression = 17
    RULE_multiplicativeExpression = 18
    RULE_unaryExpression = 19
    RULE_postfixExpression = 20
    RULE_postfixOp = 21
    RULE_primaryExpression = 22
    RULE_statement = 23
    RULE_assignmentStatement = 24
    RULE_lvalue = 25
    RULE_expressionStatement = 26
    RULE_block = 27
    RULE_ifStatement = 28
    RULE_whileStatement = 29
    RULE_forStatement = 30
    RULE_forInit = 31
    RULE_forUpdate = 32
    RULE_switchStatement = 33
    RULE_caseClause = 34
    RULE_defaultClause = 35
    RULE_returnStatement = 36
    RULE_breakStatement = 37
    RULE_continueStatement = 38

    ruleNames =  [ "program", "functionDeclaration", "returnType", "parameterList", 
                   "parameter", "argumentList", "structDeclaration", "structMemberList", 
                   "structMember", "structInit", "variableDeclaration", 
                   "expression", "assignmentExpression", "orExpression", 
                   "andExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "postfixExpression", "postfixOp", "primaryExpression", 
                   "statement", "assignmentStatement", "lvalue", "expressionStatement", 
                   "block", "ifStatement", "whileStatement", "forStatement", 
                   "forInit", "forUpdate", "switchStatement", "caseClause", 
                   "defaultClause", "returnStatement", "breakStatement", 
                   "continueStatement" ]

    EOF = Token.EOF
    WS=1
    BLOCK_COMMENT=2
    LINE_COMMENT=3
    AUTO=4
    BREAK=5
    CASE=6
    CONTINUE=7
    DEFAULT=8
    ELSE=9
    FLOAT=10
    FOR=11
    IF=12
    INT=13
    RETURN=14
    STRING=15
    STRUCT=16
    SWITCH=17
    VOID=18
    WHILE=19
    COMMA=20
    LEFT_PAREN=21
    RIGHT_PAREN=22
    LEFT_BRACE=23
    RIGHT_BRACE=24
    SEMICOLON=25
    LEFT_SQUARE_BRACKET=26
    RIGHT_SQUARE_BRACKET=27
    COLON=28
    INCREMENT=29
    DECREMENT=30
    LESS_THAN_OR_EQUAL=31
    GREATER_THAN_OR_EQUAL=32
    EQUAL=33
    NOT_EQUAL=34
    LOGICAL_AND=35
    LOGICAL_OR=36
    ASSIGN=37
    PLUS=38
    MINUS=39
    MULTIPLY=40
    DIVIDE=41
    MODULUS=42
    LESS_THAN=43
    GREATER_THAN=44
    LOGICAL_NOT=45
    MEMBER_ACCESS=46
    ID=47
    INTEGER_LITERAL=48
    FLOAT_LITERAL=49
    STRING_LITERAL=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52
    ERROR_CHAR=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def structDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructDeclarationContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructDeclarationContext,i)


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(TyCParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.STRUCT) | (1 << TyCParser.VOID) | (1 << TyCParser.ID))) != 0):
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TyCParser.STRUCT]:
                    self.state = 78
                    self.structDeclaration()
                    pass
                elif token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.VOID, TyCParser.ID]:
                    self.state = 79
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(TyCParser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(TyCParser.ParameterListContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_functionDeclaration




    def functionDeclaration(self):

        localctx = TyCParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDeclaration)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.returnType()
                self.state = 88
                self.match(TyCParser.ID)
                self.state = 89
                self.match(TyCParser.LEFT_PAREN)
                self.state = 90
                self.parameterList()
                self.state = 91
                self.match(TyCParser.RIGHT_PAREN)
                self.state = 92
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(TyCParser.ID)
                self.state = 95
                self.match(TyCParser.LEFT_PAREN)
                self.state = 96
                self.parameterList()
                self.state = 97
                self.match(TyCParser.RIGHT_PAREN)
                self.state = 98
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_returnType




    def returnType(self):

        localctx = TyCParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.VOID) | (1 << TyCParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(TyCParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_parameterList




    def parameterList(self):

        localctx = TyCParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.ID))) != 0):
                self.state = 104
                self.parameter()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TyCParser.COMMA:
                    self.state = 105
                    self.match(TyCParser.COMMA)
                    self.state = 106
                    self.parameter()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_parameter




    def parameter(self):

        localctx = TyCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(TyCParser.INT)
                self.state = 115
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(TyCParser.FLOAT)
                self.state = 117
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(TyCParser.STRING)
                self.state = 119
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.match(TyCParser.ID)
                self.state = 121
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_argumentList




    def argumentList(self):

        localctx = TyCParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 124
                self.expression()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TyCParser.COMMA:
                    self.state = 125
                    self.match(TyCParser.COMMA)
                    self.state = 126
                    self.expression()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def structMemberList(self):
            return self.getTypedRuleContext(TyCParser.StructMemberListContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structDeclaration




    def structDeclaration(self):

        localctx = TyCParser.StructDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(TyCParser.STRUCT)
            self.state = 135
            self.match(TyCParser.ID)
            self.state = 136
            self.match(TyCParser.LEFT_BRACE)
            self.state = 137
            self.structMemberList()
            self.state = 138
            self.match(TyCParser.RIGHT_BRACE)
            self.state = 139
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructMemberContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMICOLON)
            else:
                return self.getToken(TyCParser.SEMICOLON, i)

        def getRuleIndex(self):
            return TyCParser.RULE_structMemberList




    def structMemberList(self):

        localctx = TyCParser.StructMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.ID))) != 0):
                self.state = 141
                self.structMember()
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 142
                        self.match(TyCParser.SEMICOLON)
                        self.state = 143
                        self.structMember() 
                    self.state = 148
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TyCParser.SEMICOLON:
                    self.state = 149
                    self.match(TyCParser.SEMICOLON)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structMember




    def structMember(self):

        localctx = TyCParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structMember)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(TyCParser.INT)
                self.state = 155
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(TyCParser.FLOAT)
                self.state = 157
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(TyCParser.STRING)
                self.state = 159
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.match(TyCParser.ID)
                self.state = 161
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_structInit




    def structInit(self):

        localctx = TyCParser.StructInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(TyCParser.LEFT_BRACE)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 165
                self.expression()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TyCParser.COMMA:
                    self.state = 166
                    self.match(TyCParser.COMMA)
                    self.state = 167
                    self.expression()
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 175
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def structInit(self):
            return self.getTypedRuleContext(TyCParser.StructInitContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_variableDeclaration




    def variableDeclaration(self):

        localctx = TyCParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(TyCParser.AUTO)
                self.state = 178
                self.match(TyCParser.ID)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TyCParser.ASSIGN:
                    self.state = 179
                    self.match(TyCParser.ASSIGN)
                    self.state = 180
                    self.expression()


                pass
            elif token in [TyCParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(TyCParser.INT)
                self.state = 184
                self.match(TyCParser.ID)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TyCParser.ASSIGN:
                    self.state = 185
                    self.match(TyCParser.ASSIGN)
                    self.state = 186
                    self.expression()


                pass
            elif token in [TyCParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.match(TyCParser.FLOAT)
                self.state = 190
                self.match(TyCParser.ID)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TyCParser.ASSIGN:
                    self.state = 191
                    self.match(TyCParser.ASSIGN)
                    self.state = 192
                    self.expression()


                pass
            elif token in [TyCParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.match(TyCParser.STRING)
                self.state = 196
                self.match(TyCParser.ID)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TyCParser.ASSIGN:
                    self.state = 197
                    self.match(TyCParser.ASSIGN)
                    self.state = 198
                    self.expression()


                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.match(TyCParser.ID)
                self.state = 202
                self.match(TyCParser.ID)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TyCParser.ASSIGN:
                    self.state = 203
                    self.match(TyCParser.ASSIGN)
                    self.state = 206
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [TyCParser.LEFT_PAREN, TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.PLUS, TyCParser.MINUS, TyCParser.LOGICAL_NOT, TyCParser.ID, TyCParser.INTEGER_LITERAL, TyCParser.FLOAT_LITERAL, TyCParser.STRING_LITERAL]:
                        self.state = 204
                        self.expression()
                        pass
                    elif token in [TyCParser.LEFT_BRACE]:
                        self.state = 205
                        self.structInit()
                        pass
                    else:
                        raise NoViableAltException(self)



                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(TyCParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expression




    def expression(self):

        localctx = TyCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpression(self):
            return self.getTypedRuleContext(TyCParser.OrExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def assignmentExpression(self):
            return self.getTypedRuleContext(TyCParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assignmentExpression




    def assignmentExpression(self):

        localctx = TyCParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignmentExpression)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.orExpression()
                self.state = 215
                self.match(TyCParser.ASSIGN)
                self.state = 216
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.orExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.AndExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.AndExpressionContext,i)


        def LOGICAL_OR(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LOGICAL_OR)
            else:
                return self.getToken(TyCParser.LOGICAL_OR, i)

        def getRuleIndex(self):
            return TyCParser.RULE_orExpression




    def orExpression(self):

        localctx = TyCParser.OrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.andExpression()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TyCParser.LOGICAL_OR:
                self.state = 222
                self.match(TyCParser.LOGICAL_OR)
                self.state = 223
                self.andExpression()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.EqualityExpressionContext,i)


        def LOGICAL_AND(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LOGICAL_AND)
            else:
                return self.getToken(TyCParser.LOGICAL_AND, i)

        def getRuleIndex(self):
            return TyCParser.RULE_andExpression




    def andExpression(self):

        localctx = TyCParser.AndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.equalityExpression()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TyCParser.LOGICAL_AND:
                self.state = 230
                self.match(TyCParser.LOGICAL_AND)
                self.state = 231
                self.equalityExpression()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.RelationalExpressionContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.EQUAL)
            else:
                return self.getToken(TyCParser.EQUAL, i)

        def NOT_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.NOT_EQUAL)
            else:
                return self.getToken(TyCParser.NOT_EQUAL, i)

        def getRuleIndex(self):
            return TyCParser.RULE_equalityExpression




    def equalityExpression(self):

        localctx = TyCParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.relationalExpression()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TyCParser.EQUAL or _la==TyCParser.NOT_EQUAL:
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==TyCParser.EQUAL or _la==TyCParser.NOT_EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.relationalExpression()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.AdditiveExpressionContext,i)


        def LESS_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LESS_THAN)
            else:
                return self.getToken(TyCParser.LESS_THAN, i)

        def LESS_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LESS_THAN_OR_EQUAL)
            else:
                return self.getToken(TyCParser.LESS_THAN_OR_EQUAL, i)

        def GREATER_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GREATER_THAN)
            else:
                return self.getToken(TyCParser.GREATER_THAN, i)

        def GREATER_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GREATER_THAN_OR_EQUAL)
            else:
                return self.getToken(TyCParser.GREATER_THAN_OR_EQUAL, i)

        def getRuleIndex(self):
            return TyCParser.RULE_relationalExpression




    def relationalExpression(self):

        localctx = TyCParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.additiveExpression()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LESS_THAN_OR_EQUAL) | (1 << TyCParser.GREATER_THAN_OR_EQUAL) | (1 << TyCParser.LESS_THAN) | (1 << TyCParser.GREATER_THAN))) != 0):
                self.state = 246
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LESS_THAN_OR_EQUAL) | (1 << TyCParser.GREATER_THAN_OR_EQUAL) | (1 << TyCParser.LESS_THAN) | (1 << TyCParser.GREATER_THAN))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.additiveExpression()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.PLUS)
            else:
                return self.getToken(TyCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MINUS)
            else:
                return self.getToken(TyCParser.MINUS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_additiveExpression




    def additiveExpression(self):

        localctx = TyCParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.multiplicativeExpression()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TyCParser.PLUS or _la==TyCParser.MINUS:
                self.state = 254
                _la = self._input.LA(1)
                if not(_la==TyCParser.PLUS or _la==TyCParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.multiplicativeExpression()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.UnaryExpressionContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MULTIPLY)
            else:
                return self.getToken(TyCParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DIVIDE)
            else:
                return self.getToken(TyCParser.DIVIDE, i)

        def MODULUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MODULUS)
            else:
                return self.getToken(TyCParser.MODULUS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_multiplicativeExpression




    def multiplicativeExpression(self):

        localctx = TyCParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.unaryExpression()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.MULTIPLY) | (1 << TyCParser.DIVIDE) | (1 << TyCParser.MODULUS))) != 0):
                self.state = 262
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.MULTIPLY) | (1 << TyCParser.DIVIDE) | (1 << TyCParser.MODULUS))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.unaryExpression()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(TyCParser.UnaryExpressionContext,0)


        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def MINUS(self):
            return self.getToken(TyCParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(TyCParser.PLUS, 0)

        def LOGICAL_NOT(self):
            return self.getToken(TyCParser.LOGICAL_NOT, 0)

        def postfixExpression(self):
            return self.getTypedRuleContext(TyCParser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unaryExpression




    def unaryExpression(self):

        localctx = TyCParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryExpression)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(TyCParser.INCREMENT)
                self.state = 270
                self.unaryExpression()
                pass
            elif token in [TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(TyCParser.DECREMENT)
                self.state = 272
                self.unaryExpression()
                pass
            elif token in [TyCParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.match(TyCParser.MINUS)
                self.state = 274
                self.unaryExpression()
                pass
            elif token in [TyCParser.PLUS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 275
                self.match(TyCParser.PLUS)
                self.state = 276
                self.unaryExpression()
                pass
            elif token in [TyCParser.LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 277
                self.match(TyCParser.LOGICAL_NOT)
                self.state = 278
                self.unaryExpression()
                pass
            elif token in [TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INTEGER_LITERAL, TyCParser.FLOAT_LITERAL, TyCParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.postfixExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(TyCParser.PrimaryExpressionContext,0)


        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(TyCParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_postfixExpression




    def postfixExpression(self):

        localctx = TyCParser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_postfixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.primaryExpression()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.MEMBER_ACCESS))) != 0):
                self.state = 283
                self.postfixOp()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def MEMBER_ACCESS(self):
            return self.getToken(TyCParser.MEMBER_ACCESS, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(TyCParser.ArgumentListContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_postfixOp




    def postfixOp(self):

        localctx = TyCParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_postfixOp)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(TyCParser.INCREMENT)
                pass
            elif token in [TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(TyCParser.DECREMENT)
                pass
            elif token in [TyCParser.MEMBER_ACCESS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 292
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.match(TyCParser.LEFT_PAREN)
                self.state = 294
                self.argumentList()
                self.state = 295
                self.match(TyCParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(TyCParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(TyCParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(TyCParser.STRING_LITERAL, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_primaryExpression




    def primaryExpression(self):

        localctx = TyCParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primaryExpression)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(TyCParser.ID)
                pass
            elif token in [TyCParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(TyCParser.INTEGER_LITERAL)
                pass
            elif token in [TyCParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(TyCParser.FLOAT_LITERAL)
                pass
            elif token in [TyCParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 302
                self.match(TyCParser.STRING_LITERAL)
                pass
            elif token in [TyCParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 303
                self.match(TyCParser.LEFT_PAREN)
                self.state = 304
                self.expression()
                self.state = 305
                self.match(TyCParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(TyCParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def assignmentStatement(self):
            return self.getTypedRuleContext(TyCParser.AssignmentStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(TyCParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(TyCParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(TyCParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(TyCParser.ForStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(TyCParser.SwitchStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(TyCParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(TyCParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(TyCParser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_statement




    def statement(self):

        localctx = TyCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.variableDeclaration()
                self.state = 310
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.assignmentStatement()
                self.state = 313
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.expressionStatement()
                self.state = 316
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 319
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 320
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 321
                self.switchStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 322
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 323
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 324
                self.continueStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 325
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(TyCParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assignmentStatement




    def assignmentStatement(self):

        localctx = TyCParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.lvalue()
            self.state = 329
            self.match(TyCParser.ASSIGN)
            self.state = 330
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def MEMBER_ACCESS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MEMBER_ACCESS)
            else:
                return self.getToken(TyCParser.MEMBER_ACCESS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_lvalue




    def lvalue(self):

        localctx = TyCParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(TyCParser.ID)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TyCParser.MEMBER_ACCESS:
                self.state = 333
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 334
                self.match(TyCParser.ID)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expressionStatement




    def expressionStatement(self):

        localctx = TyCParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_block




    def block(self):

        localctx = TyCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(TyCParser.LEFT_BRACE)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.AUTO) | (1 << TyCParser.BREAK) | (1 << TyCParser.CONTINUE) | (1 << TyCParser.FLOAT) | (1 << TyCParser.FOR) | (1 << TyCParser.IF) | (1 << TyCParser.INT) | (1 << TyCParser.RETURN) | (1 << TyCParser.STRING) | (1 << TyCParser.SWITCH) | (1 << TyCParser.WHILE) | (1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.LEFT_BRACE) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 343
                self.statement()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifStatement




    def ifStatement(self):

        localctx = TyCParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(TyCParser.IF)
            self.state = 352
            self.match(TyCParser.LEFT_PAREN)
            self.state = 353
            self.expression()
            self.state = 354
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 355
            self.statement()
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 356
                self.match(TyCParser.ELSE)
                self.state = 357
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whileStatement




    def whileStatement(self):

        localctx = TyCParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(TyCParser.WHILE)
            self.state = 361
            self.match(TyCParser.LEFT_PAREN)
            self.state = 362
            self.expression()
            self.state = 363
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 364
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMICOLON)
            else:
                return self.getToken(TyCParser.SEMICOLON, i)

        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def forInit(self):
            return self.getTypedRuleContext(TyCParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(TyCParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forStatement




    def forStatement(self):

        localctx = TyCParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(TyCParser.FOR)
            self.state = 367
            self.match(TyCParser.LEFT_PAREN)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.AUTO) | (1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING) | (1 << TyCParser.ID))) != 0):
                self.state = 368
                self.forInit()


            self.state = 371
            self.match(TyCParser.SEMICOLON)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 372
                self.expression()


            self.state = 375
            self.match(TyCParser.SEMICOLON)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 376
                self.forUpdate()


            self.state = 379
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 380
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(TyCParser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(TyCParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forInit




    def forInit(self):

        localctx = TyCParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forInit)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.assignmentStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(TyCParser.AssignmentStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forUpdate




    def forUpdate(self):

        localctx = TyCParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forUpdate)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(TyCParser.CaseClauseContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(TyCParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switchStatement




    def switchStatement(self):

        localctx = TyCParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(TyCParser.SWITCH)
            self.state = 391
            self.match(TyCParser.LEFT_PAREN)
            self.state = 392
            self.expression()
            self.state = 393
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 394
            self.match(TyCParser.LEFT_BRACE)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TyCParser.CASE:
                self.state = 395
                self.caseClause()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TyCParser.DEFAULT:
                self.state = 401
                self.defaultClause()


            self.state = 404
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_caseClause




    def caseClause(self):

        localctx = TyCParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(TyCParser.CASE)
            self.state = 407
            self.expression()
            self.state = 408
            self.match(TyCParser.COLON)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.AUTO) | (1 << TyCParser.BREAK) | (1 << TyCParser.CONTINUE) | (1 << TyCParser.FLOAT) | (1 << TyCParser.FOR) | (1 << TyCParser.IF) | (1 << TyCParser.INT) | (1 << TyCParser.RETURN) | (1 << TyCParser.STRING) | (1 << TyCParser.SWITCH) | (1 << TyCParser.WHILE) | (1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.LEFT_BRACE) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 409
                self.statement()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_defaultClause




    def defaultClause(self):

        localctx = TyCParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(TyCParser.DEFAULT)
            self.state = 416
            self.match(TyCParser.COLON)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.AUTO) | (1 << TyCParser.BREAK) | (1 << TyCParser.CONTINUE) | (1 << TyCParser.FLOAT) | (1 << TyCParser.FOR) | (1 << TyCParser.IF) | (1 << TyCParser.INT) | (1 << TyCParser.RETURN) | (1 << TyCParser.STRING) | (1 << TyCParser.SWITCH) | (1 << TyCParser.WHILE) | (1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.LEFT_BRACE) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 417
                self.statement()
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_returnStatement




    def returnStatement(self):

        localctx = TyCParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(TyCParser.RETURN)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LEFT_PAREN) | (1 << TyCParser.INCREMENT) | (1 << TyCParser.DECREMENT) | (1 << TyCParser.PLUS) | (1 << TyCParser.MINUS) | (1 << TyCParser.LOGICAL_NOT) | (1 << TyCParser.ID) | (1 << TyCParser.INTEGER_LITERAL) | (1 << TyCParser.FLOAT_LITERAL) | (1 << TyCParser.STRING_LITERAL))) != 0):
                self.state = 424
                self.expression()


            self.state = 427
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakStatement




    def breakStatement(self):

        localctx = TyCParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(TyCParser.BREAK)
            self.state = 430
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continueStatement




    def continueStatement(self):

        localctx = TyCParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(TyCParser.CONTINUE)
            self.state = 433
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





