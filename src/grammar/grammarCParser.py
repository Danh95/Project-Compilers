# Generated from ./src/grammar/grammarC.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u0229\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7\u0089\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\5\t\u0095\n\t\3\t\3\t\7\t\u0099")
        buf.write("\n\t\f\t\16\t\u009c\13\t\3\t\3\t\5\t\u00a0\n\t\3\t\5\t")
        buf.write("\u00a3\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\7\13\u00b2\n\13\f\13\16\13\u00b5\13\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00bb\n\13\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00c1\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00ce\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00e0\n")
        buf.write("\16\3\17\3\17\3\17\7\17\u00e5\n\17\f\17\16\17\u00e8\13")
        buf.write("\17\3\17\3\17\5\17\u00ec\n\17\3\20\5\20\u00ef\n\20\3\20")
        buf.write("\3\20\7\20\u00f3\n\20\f\20\16\20\u00f6\13\20\3\20\7\20")
        buf.write("\u00f9\n\20\f\20\16\20\u00fc\13\20\5\20\u00fe\n\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u0104\n\20\3\21\5\21\u0107\n\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\5\22\u0111\n\22")
        buf.write("\3\22\3\22\7\22\u0115\n\22\f\22\16\22\u0118\13\22\3\22")
        buf.write("\7\22\u011b\n\22\f\22\16\22\u011e\13\22\5\22\u0120\n\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5\24")
        buf.write("\u012c\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\5\25\u013c\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u014a\n\27\f\27\16\27\u014d\13\27\3\27\5\27\u0150\n\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0156\n\27\3\30\3\30\7\30\u015a")
        buf.write("\n\30\f\30\16\30\u015d\13\30\3\30\5\30\u0160\n\30\3\30")
        buf.write("\3\30\5\30\u0164\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0190\n\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0198\n\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u01a1\n\37\3 \3 \3 \5 \u01a6\n \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01b4\n#\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\5$\u01bf\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u01ca\n%\3&\3&\3&\3&\3&\3&\5&\u01d2\n&\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u01d8\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\5)\u01ec\n)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\7\63\u0205\n\63\f\63\16\63\u0208\13\63\3\63")
        buf.write("\7\63\u020b\n\63\f\63\16\63\u020e\13\63\5\63\u0210\n\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\7\63\u0217\n\63\f\63\16\63\u021a")
        buf.write("\13\63\3\63\7\63\u021d\n\63\f\63\16\63\u0220\13\63\5\63")
        buf.write("\u0222\n\63\3\63\5\63\u0225\n\63\3\64\3\64\3\64\2\2\65")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\b\4\2\6\6\64\64\4\2")
        buf.write("//\64\64\5\2\30\30\33\33\36 \4\2\34\34!$\4\2\4\4%)\3\2")
        buf.write("*+\2\u023e\2h\3\2\2\2\4o\3\2\2\2\6q\3\2\2\2\bt\3\2\2\2")
        buf.write("\nx\3\2\2\2\f\u0088\3\2\2\2\16\u008a\3\2\2\2\20\u00a2")
        buf.write("\3\2\2\2\22\u00a4\3\2\2\2\24\u00ba\3\2\2\2\26\u00c0\3")
        buf.write("\2\2\2\30\u00cd\3\2\2\2\32\u00df\3\2\2\2\34\u00eb\3\2")
        buf.write("\2\2\36\u0103\3\2\2\2 \u0106\3\2\2\2\"\u0110\3\2\2\2$")
        buf.write("\u0123\3\2\2\2&\u012b\3\2\2\2(\u013b\3\2\2\2*\u013d\3")
        buf.write("\2\2\2,\u0155\3\2\2\2.\u0163\3\2\2\2\60\u0165\3\2\2\2")
        buf.write("\62\u016d\3\2\2\2\64\u0175\3\2\2\2\66\u017a\3\2\2\28\u0182")
        buf.write("\3\2\2\2:\u0197\3\2\2\2<\u01a0\3\2\2\2>\u01a5\3\2\2\2")
        buf.write("@\u01a7\3\2\2\2B\u01a9\3\2\2\2D\u01b3\3\2\2\2F\u01be\3")
        buf.write("\2\2\2H\u01c9\3\2\2\2J\u01d1\3\2\2\2L\u01d7\3\2\2\2N\u01d9")
        buf.write("\3\2\2\2P\u01eb\3\2\2\2R\u01ed\3\2\2\2T\u01ef\3\2\2\2")
        buf.write("V\u01f1\3\2\2\2X\u01f3\3\2\2\2Z\u01f5\3\2\2\2\\\u01f7")
        buf.write("\3\2\2\2^\u01f9\3\2\2\2`\u01fb\3\2\2\2b\u01fd\3\2\2\2")
        buf.write("d\u0224\3\2\2\2f\u0226\3\2\2\2hi\5\4\3\2ij\5\f\7\2j\3")
        buf.write("\3\2\2\2kl\5\6\4\2lm\5\4\3\2mp\3\2\2\2np\3\2\2\2ok\3\2")
        buf.write("\2\2on\3\2\2\2p\5\3\2\2\2qr\7\3\2\2rs\5\b\5\2s\7\3\2\2")
        buf.write("\2tu\7\4\2\2uv\5\n\6\2vw\7\5\2\2w\t\3\2\2\2xy\t\2\2\2")
        buf.write("y\13\3\2\2\2z{\5\22\n\2{|\5\f\7\2|\u0089\3\2\2\2}~\5\16")
        buf.write("\b\2~\177\5\f\7\2\177\u0089\3\2\2\2\u0080\u0081\5\"\22")
        buf.write("\2\u0081\u0082\5\f\7\2\u0082\u0089\3\2\2\2\u0083\u0084")
        buf.write("\5\36\20\2\u0084\u0085\5\f\7\2\u0085\u0089\3\2\2\2\u0086")
        buf.write("\u0089\5N(\2\u0087\u0089\3\2\2\2\u0088z\3\2\2\2\u0088")
        buf.write("}\3\2\2\2\u0088\u0080\3\2\2\2\u0088\u0083\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\r\3\2\2\2\u008a")
        buf.write("\u008b\5R*\2\u008b\u008c\5Z.\2\u008c\u008d\5f\64\2\u008d")
        buf.write("\u008e\7\7\2\2\u008e\u008f\5\20\t\2\u008f\u0090\7\b\2")
        buf.write("\2\u0090\u0091\5`\61\2\u0091\17\3\2\2\2\u0092\u0094\5")
        buf.write("R*\2\u0093\u0095\5f\64\2\u0094\u0093\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\7\t\2\2\u0097")
        buf.write("\u0099\3\2\2\2\u0098\u0092\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\5R*\2\u009e\u00a0")
        buf.write("\5f\64\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u009a\3\2\2\2")
        buf.write("\u00a2\u00a1\3\2\2\2\u00a3\21\3\2\2\2\u00a4\u00a5\5R*")
        buf.write("\2\u00a5\u00a6\5f\64\2\u00a6\u00a7\7\7\2\2\u00a7\u00a8")
        buf.write("\5\24\13\2\u00a8\u00a9\7\b\2\2\u00a9\u00aa\7\n\2\2\u00aa")
        buf.write("\u00ab\5\26\f\2\u00ab\u00ac\7\13\2\2\u00ac\23\3\2\2\2")
        buf.write("\u00ad\u00ae\5R*\2\u00ae\u00af\5f\64\2\u00af\u00b0\7\t")
        buf.write("\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b2\u00b5")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\5R*\2\u00b7")
        buf.write("\u00b8\5f\64\2\u00b8\u00bb\3\2\2\2\u00b9\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b3\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\25\3\2")
        buf.write("\2\2\u00bc\u00bd\5\30\r\2\u00bd\u00be\5\26\f\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00c1\5\30\r\2\u00c0\u00bc\3\2\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1\27\3\2\2\2\u00c2\u00ce\5\36\20\2")
        buf.write("\u00c3\u00ce\5\"\22\2\u00c4\u00ce\5$\23\2\u00c5\u00ce")
        buf.write("\5&\24\2\u00c6\u00ce\5.\30\2\u00c7\u00c8\5D#\2\u00c8\u00c9")
        buf.write("\5`\61\2\u00c9\u00ce\3\2\2\2\u00ca\u00ce\5\32\16\2\u00cb")
        buf.write("\u00ce\5J&\2\u00cc\u00ce\5L\'\2\u00cd\u00c2\3\2\2\2\u00cd")
        buf.write("\u00c3\3\2\2\2\u00cd\u00c4\3\2\2\2\u00cd\u00c5\3\2\2\2")
        buf.write("\u00cd\u00c6\3\2\2\2\u00cd\u00c7\3\2\2\2\u00cd\u00ca\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\31")
        buf.write("\3\2\2\2\u00cf\u00d0\7\f\2\2\u00d0\u00e0\5$\23\2\u00d1")
        buf.write("\u00d2\7\f\2\2\u00d2\u00d3\5d\63\2\u00d3\u00d4\5`\61\2")
        buf.write("\u00d4\u00e0\3\2\2\2\u00d5\u00d6\7\f\2\2\u00d6\u00d7\5")
        buf.write(":\36\2\u00d7\u00d8\5`\61\2\u00d8\u00e0\3\2\2\2\u00d9\u00da")
        buf.write("\7\f\2\2\u00da\u00db\5D#\2\u00db\u00dc\5`\61\2\u00dc\u00e0")
        buf.write("\3\2\2\2\u00dd\u00de\7\f\2\2\u00de\u00e0\5`\61\2\u00df")
        buf.write("\u00cf\3\2\2\2\u00df\u00d1\3\2\2\2\u00df\u00d5\3\2\2\2")
        buf.write("\u00df\u00d9\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\33\3\2")
        buf.write("\2\2\u00e1\u00e2\5d\63\2\u00e2\u00e3\7\t\2\2\u00e3\u00e5")
        buf.write("\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e9\u00ec\5d\63\2\u00ea\u00ec\3")
        buf.write("\2\2\2\u00eb\u00e6\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\35")
        buf.write("\3\2\2\2\u00ed\u00ef\5^\60\2\u00ee\u00ed\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00fd\5R*\2\u00f1")
        buf.write("\u00f3\5Z.\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00fe\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f7\u00f9\5\\/\2\u00f8\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd")
        buf.write("\u00f4\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0100\5f\64\2\u0100\u0101\5`\61\2\u0101\u0104\3")
        buf.write("\2\2\2\u0102\u0104\5 \21\2\u0103\u00ee\3\2\2\2\u0103\u0102")
        buf.write("\3\2\2\2\u0104\37\3\2\2\2\u0105\u0107\5^\60\2\u0106\u0105")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u0109\5R*\2\u0109\u010a\5f\64\2\u010a\u010b\7\r\2\2\u010b")
        buf.write("\u010c\t\3\2\2\u010c\u010d\7\16\2\2\u010d\u010e\5`\61")
        buf.write("\2\u010e!\3\2\2\2\u010f\u0111\5^\60\2\u0110\u010f\3\2")
        buf.write("\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u011f")
        buf.write("\5R*\2\u0113\u0115\5Z.\2\u0114\u0113\3\2\2\2\u0115\u0118")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0120\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\5\\/\2")
        buf.write("\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3")
        buf.write("\2\2\2\u011c\u011d\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0116\3\2\2\2\u011f\u011c\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0122\5&\24\2\u0122#\3\2\2\2\u0123")
        buf.write("\u0124\5f\64\2\u0124\u0125\7\7\2\2\u0125\u0126\5\34\17")
        buf.write("\2\u0126\u0127\7\b\2\2\u0127\u0128\5`\61\2\u0128%\3\2")
        buf.write("\2\2\u0129\u012c\5(\25\2\u012a\u012c\5*\26\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012a\3\2\2\2\u012c\'\3\2\2\2\u012d\u012e")
        buf.write("\5f\64\2\u012e\u012f\5b\62\2\u012f\u0130\5d\63\2\u0130")
        buf.write("\u0131\5`\61\2\u0131\u013c\3\2\2\2\u0132\u0133\5f\64\2")
        buf.write("\u0133\u0134\5b\62\2\u0134\u0135\5$\23\2\u0135\u013c\3")
        buf.write("\2\2\2\u0136\u0137\5f\64\2\u0137\u0138\5b\62\2\u0138\u0139")
        buf.write("\5D#\2\u0139\u013a\5`\61\2\u013a\u013c\3\2\2\2\u013b\u012d")
        buf.write("\3\2\2\2\u013b\u0132\3\2\2\2\u013b\u0136\3\2\2\2\u013c")
        buf.write(")\3\2\2\2\u013d\u013e\5f\64\2\u013e\u013f\7\r\2\2\u013f")
        buf.write("\u0140\t\3\2\2\u0140\u0141\7\16\2\2\u0141\u0142\5b\62")
        buf.write("\2\u0142\u0143\5,\27\2\u0143\u0144\5`\61\2\u0144+\3\2")
        buf.write("\2\2\u0145\u014b\7\n\2\2\u0146\u0147\5d\63\2\u0147\u0148")
        buf.write("\7\t\2\2\u0148\u014a\3\2\2\2\u0149\u0146\3\2\2\2\u014a")
        buf.write("\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u0150\5")
        buf.write("d\63\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u0156\7\13\2\2\u0152\u0153\7\n\2\2\u0153")
        buf.write("\u0156\7\13\2\2\u0154\u0156\5d\63\2\u0155\u0145\3\2\2")
        buf.write("\2\u0155\u0152\3\2\2\2\u0155\u0154\3\2\2\2\u0156-\3\2")
        buf.write("\2\2\u0157\u015b\5\60\31\2\u0158\u015a\5\62\32\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015e\u0160\5\64\33\2\u015f\u015e\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0164\3\2\2\2\u0161\u0164\5\66\34")
        buf.write("\2\u0162\u0164\58\35\2\u0163\u0157\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0163\u0162\3\2\2\2\u0164/\3\2\2\2\u0165\u0166")
        buf.write("\7\17\2\2\u0166\u0167\7\7\2\2\u0167\u0168\5:\36\2\u0168")
        buf.write("\u0169\7\b\2\2\u0169\u016a\7\n\2\2\u016a\u016b\5\26\f")
        buf.write("\2\u016b\u016c\7\13\2\2\u016c\61\3\2\2\2\u016d\u016e\7")
        buf.write("\20\2\2\u016e\u016f\7\7\2\2\u016f\u0170\5:\36\2\u0170")
        buf.write("\u0171\7\b\2\2\u0171\u0172\7\n\2\2\u0172\u0173\5\26\f")
        buf.write("\2\u0173\u0174\7\13\2\2\u0174\63\3\2\2\2\u0175\u0176\7")
        buf.write("\21\2\2\u0176\u0177\7\n\2\2\u0177\u0178\5\26\f\2\u0178")
        buf.write("\u0179\7\13\2\2\u0179\65\3\2\2\2\u017a\u017b\7\22\2\2")
        buf.write("\u017b\u017c\7\7\2\2\u017c\u017d\5:\36\2\u017d\u017e\7")
        buf.write("\b\2\2\u017e\u017f\7\n\2\2\u017f\u0180\5\26\f\2\u0180")
        buf.write("\u0181\7\13\2\2\u0181\67\3\2\2\2\u0182\u0183\7\23\2\2")
        buf.write("\u0183\u0184\7\7\2\2\u0184\u0185\5<\37\2\u0185\u0186\7")
        buf.write("\b\2\2\u0186\u0187\7\n\2\2\u0187\u0188\5\26\f\2\u0188")
        buf.write("\u0189\7\13\2\2\u01899\3\2\2\2\u018a\u018b\5d\63\2\u018b")
        buf.write("\u018c\5V,\2\u018c\u018d\5d\63\2\u018d\u0198\3\2\2\2\u018e")
        buf.write("\u0190\7\24\2\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2")
        buf.write("\2\u0190\u0191\3\2\2\2\u0191\u0198\5d\63\2\u0192\u0193")
        buf.write("\7\24\2\2\u0193\u0194\7\7\2\2\u0194\u0195\5:\36\2\u0195")
        buf.write("\u0196\7\b\2\2\u0196\u0198\3\2\2\2\u0197\u018a\3\2\2\2")
        buf.write("\u0197\u018f\3\2\2\2\u0197\u0192\3\2\2\2\u0198;\3\2\2")
        buf.write("\2\u0199\u019a\5> \2\u019a\u019b\5@!\2\u019b\u019c\7\25")
        buf.write("\2\2\u019c\u019d\5B\"\2\u019d\u01a1\3\2\2\2\u019e\u019f")
        buf.write("\7\25\2\2\u019f\u01a1\7\25\2\2\u01a0\u0199\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a1=\3\2\2\2\u01a2\u01a6\5\36\20\2\u01a3")
        buf.write("\u01a6\5\"\22\2\u01a4\u01a6\5&\24\2\u01a5\u01a2\3\2\2")
        buf.write("\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6?\3\2")
        buf.write("\2\2\u01a7\u01a8\5:\36\2\u01a8A\3\2\2\2\u01a9\u01aa\5")
        buf.write("D#\2\u01aaC\3\2\2\2\u01ab\u01ac\5F$\2\u01ac\u01ad\5T+")
        buf.write("\2\u01ad\u01ae\5F$\2\u01ae\u01b4\3\2\2\2\u01af\u01b0\7")
        buf.write("\7\2\2\u01b0\u01b1\5D#\2\u01b1\u01b2\7\b\2\2\u01b2\u01b4")
        buf.write("\3\2\2\2\u01b3\u01ab\3\2\2\2\u01b3\u01af\3\2\2\2\u01b4")
        buf.write("E\3\2\2\2\u01b5\u01bf\5H%\2\u01b6\u01b7\5H%\2\u01b7\u01b8")
        buf.write("\5T+\2\u01b8\u01b9\5F$\2\u01b9\u01bf\3\2\2\2\u01ba\u01bb")
        buf.write("\7\7\2\2\u01bb\u01bc\5F$\2\u01bc\u01bd\7\b\2\2\u01bd\u01bf")
        buf.write("\3\2\2\2\u01be\u01b5\3\2\2\2\u01be\u01b6\3\2\2\2\u01be")
        buf.write("\u01ba\3\2\2\2\u01bfG\3\2\2\2\u01c0\u01ca\5d\63\2\u01c1")
        buf.write("\u01c2\5d\63\2\u01c2\u01c3\5T+\2\u01c3\u01c4\5H%\2\u01c4")
        buf.write("\u01ca\3\2\2\2\u01c5\u01c6\7\7\2\2\u01c6\u01c7\5H%\2\u01c7")
        buf.write("\u01c8\7\b\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c0\3\2\2\2")
        buf.write("\u01c9\u01c1\3\2\2\2\u01c9\u01c5\3\2\2\2\u01caI\3\2\2")
        buf.write("\2\u01cb\u01cc\5d\63\2\u01cc\u01cd\5X-\2\u01cd\u01d2\3")
        buf.write("\2\2\2\u01ce\u01cf\5X-\2\u01cf\u01d0\5d\63\2\u01d0\u01d2")
        buf.write("\3\2\2\2\u01d1\u01cb\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d2")
        buf.write("K\3\2\2\2\u01d3\u01d4\7\26\2\2\u01d4\u01d8\5`\61\2\u01d5")
        buf.write("\u01d6\7\27\2\2\u01d6\u01d8\5`\61\2\u01d7\u01d3\3\2\2")
        buf.write("\2\u01d7\u01d5\3\2\2\2\u01d8M\3\2\2\2\u01d9\u01da\7\30")
        buf.write("\2\2\u01da\u01db\7\31\2\2\u01db\u01dc\7\7\2\2\u01dc\u01dd")
        buf.write("\5P)\2\u01dd\u01de\7\b\2\2\u01de\u01df\7\n\2\2\u01df\u01e0")
        buf.write("\5\26\f\2\u01e0\u01e1\7\13\2\2\u01e1O\3\2\2\2\u01e2\u01e3")
        buf.write("\7\30\2\2\u01e3\u01e4\7\32\2\2\u01e4\u01e5\7\t\2\2\u01e5")
        buf.write("\u01e6\7\33\2\2\u01e6\u01e7\7\34\2\2\u01e7\u01e8\7\35")
        buf.write("\2\2\u01e8\u01e9\7\r\2\2\u01e9\u01ec\7\16\2\2\u01ea\u01ec")
        buf.write("\3\2\2\2\u01eb\u01e2\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("Q\3\2\2\2\u01ed\u01ee\t\4\2\2\u01eeS\3\2\2\2\u01ef\u01f0")
        buf.write("\t\5\2\2\u01f0U\3\2\2\2\u01f1\u01f2\t\6\2\2\u01f2W\3\2")
        buf.write("\2\2\u01f3\u01f4\t\7\2\2\u01f4Y\3\2\2\2\u01f5\u01f6\7")
        buf.write("\34\2\2\u01f6[\3\2\2\2\u01f7\u01f8\7,\2\2\u01f8]\3\2\2")
        buf.write("\2\u01f9\u01fa\7-\2\2\u01fa_\3\2\2\2\u01fb\u01fc\7\25")
        buf.write("\2\2\u01fca\3\2\2\2\u01fd\u01fe\7.\2\2\u01fec\3\2\2\2")
        buf.write("\u01ff\u0225\7/\2\2\u0200\u0225\7\60\2\2\u0201\u0225\7")
        buf.write("\61\2\2\u0202\u0225\7\63\2\2\u0203\u0205\5Z.\2\u0204\u0203")
        buf.write("\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2\u0206")
        buf.write("\u0207\3\2\2\2\u0207\u0210\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0209\u020b\5\\/\2\u020a\u0209\3\2\2\2\u020b\u020e\3")
        buf.write("\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0210")
        buf.write("\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0206\3\2\2\2\u020f")
        buf.write("\u020c\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\7\64\2")
        buf.write("\2\u0212\u0213\7\r\2\2\u0213\u0214\t\3\2\2\u0214\u0225")
        buf.write("\7\16\2\2\u0215\u0217\5Z.\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u0222\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021d\5")
        buf.write("\\/\2\u021c\u021b\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0222\3\2\2\2\u0220")
        buf.write("\u021e\3\2\2\2\u0221\u0218\3\2\2\2\u0221\u021e\3\2\2\2")
        buf.write("\u0222\u0223\3\2\2\2\u0223\u0225\7\64\2\2\u0224\u01ff")
        buf.write("\3\2\2\2\u0224\u0200\3\2\2\2\u0224\u0201\3\2\2\2\u0224")
        buf.write("\u0202\3\2\2\2\u0224\u020f\3\2\2\2\u0224\u0221\3\2\2\2")
        buf.write("\u0225e\3\2\2\2\u0226\u0227\7\64\2\2\u0227g\3\2\2\2\62")
        buf.write("o\u0088\u0094\u009a\u009f\u00a2\u00b3\u00ba\u00c0\u00cd")
        buf.write("\u00df\u00e6\u00eb\u00ee\u00f4\u00fa\u00fd\u0103\u0106")
        buf.write("\u0110\u0116\u011c\u011f\u012b\u013b\u014b\u014f\u0155")
        buf.write("\u015b\u015f\u0163\u018f\u0197\u01a0\u01a5\u01b3\u01be")
        buf.write("\u01c9\u01d1\u01d7\u01eb\u0206\u020c\u020f\u0218\u021e")
        buf.write("\u0221\u0224")
        return buf.getvalue()


class grammarCParser ( Parser ):

    grammarFileName = "grammarC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'<'", "'.h>'", "'stdio'", 
                     "'('", "')'", "','", "'{'", "'}'", "'return'", "'['", 
                     "']'", "'if'", "'else if'", "'else'", "'while'", "'for'", 
                     "'!'", "';'", "'continue'", "'break'", "'int'", "'main'", 
                     "'argc'", "'char'", "'*'", "'argv'", "'float'", "'void'", 
                     "'bool'", "'+'", "'-'", "'%'", "'/'", "'>'", "'=='", 
                     "'<='", "'>='", "'!='", "'++'", "'--'", "'&'", "'const'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DIGIT", "FLT", "STR", "CHAR", "BOOL", 
                      "ID", "WS", "NL", "BC", "LC" ]

    RULE_program = 0
    RULE_libraryList = 1
    RULE_library = 2
    RULE_lib = 3
    RULE_libname = 4
    RULE_funcDefList = 5
    RULE_funcDecl = 6
    RULE_typeList = 7
    RULE_funcDef = 8
    RULE_argList = 9
    RULE_body = 10
    RULE_statement = 11
    RULE_returnStatement = 12
    RULE_parList = 13
    RULE_declaration = 14
    RULE_arrayDecl = 15
    RULE_definition = 16
    RULE_functionCall = 17
    RULE_assignment = 18
    RULE_normalAssignment = 19
    RULE_arrayAssignment = 20
    RULE_arrayOptions = 21
    RULE_conditional = 22
    RULE_ifStatement = 23
    RULE_elifStatement = 24
    RULE_elseStatement = 25
    RULE_whileStatement = 26
    RULE_loop = 27
    RULE_condition = 28
    RULE_forCondition = 29
    RULE_deel1 = 30
    RULE_deel2 = 31
    RULE_deel3 = 32
    RULE_operation = 33
    RULE_nextOperation = 34
    RULE_baseOperation = 35
    RULE_plusplus = 36
    RULE_kw = 37
    RULE_mainFunc = 38
    RULE_argListMain = 39
    RULE_types = 40
    RULE_operator = 41
    RULE_comparison = 42
    RULE_deincrement = 43
    RULE_pointer = 44
    RULE_reference = 45
    RULE_constant = 46
    RULE_endStatement = 47
    RULE_assign = 48
    RULE_rValue = 49
    RULE_lValue = 50

    ruleNames =  [ "program", "libraryList", "library", "lib", "libname", 
                   "funcDefList", "funcDecl", "typeList", "funcDef", "argList", 
                   "body", "statement", "returnStatement", "parList", "declaration", 
                   "arrayDecl", "definition", "functionCall", "assignment", 
                   "normalAssignment", "arrayAssignment", "arrayOptions", 
                   "conditional", "ifStatement", "elifStatement", "elseStatement", 
                   "whileStatement", "loop", "condition", "forCondition", 
                   "deel1", "deel2", "deel3", "operation", "nextOperation", 
                   "baseOperation", "plusplus", "kw", "mainFunc", "argListMain", 
                   "types", "operator", "comparison", "deincrement", "pointer", 
                   "reference", "constant", "endStatement", "assign", "rValue", 
                   "lValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    DIGIT=45
    FLT=46
    STR=47
    CHAR=48
    BOOL=49
    ID=50
    WS=51
    NL=52
    BC=53
    LC=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def libraryList(self):
            return self.getTypedRuleContext(grammarCParser.LibraryListContext,0)


        def funcDefList(self):
            return self.getTypedRuleContext(grammarCParser.FuncDefListContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grammarCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.libraryList()
            self.state = 103
            self.funcDefList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LibraryListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def library(self):
            return self.getTypedRuleContext(grammarCParser.LibraryContext,0)


        def libraryList(self):
            return self.getTypedRuleContext(grammarCParser.LibraryListContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_libraryList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibraryList" ):
                listener.enterLibraryList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibraryList" ):
                listener.exitLibraryList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibraryList" ):
                return visitor.visitLibraryList(self)
            else:
                return visitor.visitChildren(self)




    def libraryList(self):

        localctx = grammarCParser.LibraryListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_libraryList)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.library()
                self.state = 106
                self.libraryList()
                pass
            elif token in [grammarCParser.EOF, grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29, grammarCParser.T__42]:
                self.enterOuterAlt(localctx, 2)

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

    class LibraryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lib(self):
            return self.getTypedRuleContext(grammarCParser.LibContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_library

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibrary" ):
                listener.enterLibrary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibrary" ):
                listener.exitLibrary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibrary" ):
                return visitor.visitLibrary(self)
            else:
                return visitor.visitChildren(self)




    def library(self):

        localctx = grammarCParser.LibraryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_library)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(grammarCParser.T__0)
            self.state = 112
            self.lib()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LibContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def libname(self):
            return self.getTypedRuleContext(grammarCParser.LibnameContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_lib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLib" ):
                listener.enterLib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLib" ):
                listener.exitLib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLib" ):
                return visitor.visitLib(self)
            else:
                return visitor.visitChildren(self)




    def lib(self):

        localctx = grammarCParser.LibContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(grammarCParser.T__1)
            self.state = 115
            self.libname()
            self.state = 116
            self.match(grammarCParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LibnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarCParser.ID, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_libname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibname" ):
                listener.enterLibname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibname" ):
                listener.exitLibname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibname" ):
                return visitor.visitLibname(self)
            else:
                return visitor.visitChildren(self)




    def libname(self):

        localctx = grammarCParser.LibnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_libname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==grammarCParser.T__3 or _la==grammarCParser.ID):
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

    class FuncDefListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDef(self):
            return self.getTypedRuleContext(grammarCParser.FuncDefContext,0)


        def funcDefList(self):
            return self.getTypedRuleContext(grammarCParser.FuncDefListContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(grammarCParser.FuncDeclContext,0)


        def definition(self):
            return self.getTypedRuleContext(grammarCParser.DefinitionContext,0)


        def declaration(self):
            return self.getTypedRuleContext(grammarCParser.DeclarationContext,0)


        def mainFunc(self):
            return self.getTypedRuleContext(grammarCParser.MainFuncContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_funcDefList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDefList" ):
                listener.enterFuncDefList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDefList" ):
                listener.exitFuncDefList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDefList" ):
                return visitor.visitFuncDefList(self)
            else:
                return visitor.visitChildren(self)




    def funcDefList(self):

        localctx = grammarCParser.FuncDefListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDefList)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.funcDef()
                self.state = 121
                self.funcDefList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.funcDecl()
                self.state = 124
                self.funcDefList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.definition()
                self.state = 127
                self.funcDefList()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.declaration()
                self.state = 130
                self.funcDefList()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.mainFunc()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(grammarCParser.TypesContext,0)


        def pointer(self):
            return self.getTypedRuleContext(grammarCParser.PointerContext,0)


        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def typeList(self):
            return self.getTypedRuleContext(grammarCParser.TypeListContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = grammarCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.types()
            self.state = 137
            self.pointer()
            self.state = 138
            self.lValue()
            self.state = 139
            self.match(grammarCParser.T__4)
            self.state = 140
            self.typeList()
            self.state = 141
            self.match(grammarCParser.T__5)
            self.state = 142
            self.endStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.TypesContext)
            else:
                return self.getTypedRuleContext(grammarCParser.TypesContext,i)


        def lValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.LValueContext)
            else:
                return self.getTypedRuleContext(grammarCParser.LValueContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeList" ):
                return visitor.visitTypeList(self)
            else:
                return visitor.visitChildren(self)




    def typeList(self):

        localctx = grammarCParser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 144
                        self.types()
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==grammarCParser.ID:
                            self.state = 145
                            self.lValue()


                        self.state = 148
                        self.match(grammarCParser.T__6) 
                    self.state = 154
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 155
                self.types()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.ID:
                    self.state = 156
                    self.lValue()


                pass
            elif token in [grammarCParser.T__5]:
                self.enterOuterAlt(localctx, 2)

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

    class FuncDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(grammarCParser.TypesContext,0)


        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def argList(self):
            return self.getTypedRuleContext(grammarCParser.ArgListContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = grammarCParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.types()
            self.state = 163
            self.lValue()
            self.state = 164
            self.match(grammarCParser.T__4)
            self.state = 165
            self.argList()
            self.state = 166
            self.match(grammarCParser.T__5)
            self.state = 167
            self.match(grammarCParser.T__7)
            self.state = 168
            self.body()
            self.state = 169
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.TypesContext)
            else:
                return self.getTypedRuleContext(grammarCParser.TypesContext,i)


        def lValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.LValueContext)
            else:
                return self.getTypedRuleContext(grammarCParser.LValueContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = grammarCParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argList)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 171
                        self.types()
                        self.state = 172
                        self.lValue()
                        self.state = 173
                        self.match(grammarCParser.T__6) 
                    self.state = 179
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 180
                self.types()
                self.state = 181
                self.lValue()
                pass
            elif token in [grammarCParser.T__5]:
                self.enterOuterAlt(localctx, 2)

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

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(grammarCParser.StatementContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = grammarCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.statement()
                self.state = 187
                self.body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(grammarCParser.DeclarationContext,0)


        def definition(self):
            return self.getTypedRuleContext(grammarCParser.DefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(grammarCParser.FunctionCallContext,0)


        def assignment(self):
            return self.getTypedRuleContext(grammarCParser.AssignmentContext,0)


        def conditional(self):
            return self.getTypedRuleContext(grammarCParser.ConditionalContext,0)


        def operation(self):
            return self.getTypedRuleContext(grammarCParser.OperationContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(grammarCParser.ReturnStatementContext,0)


        def plusplus(self):
            return self.getTypedRuleContext(grammarCParser.PlusplusContext,0)


        def kw(self):
            return self.getTypedRuleContext(grammarCParser.KwContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = grammarCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.assignment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.operation()
                self.state = 198
                self.endStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 201
                self.plusplus()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 202
                self.kw()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(grammarCParser.FunctionCallContext,0)


        def rValue(self):
            return self.getTypedRuleContext(grammarCParser.RValueContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def condition(self):
            return self.getTypedRuleContext(grammarCParser.ConditionContext,0)


        def operation(self):
            return self.getTypedRuleContext(grammarCParser.OperationContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = grammarCParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnStatement)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(grammarCParser.T__9)
                self.state = 206
                self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(grammarCParser.T__9)
                self.state = 208
                self.rValue()
                self.state = 209
                self.endStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.match(grammarCParser.T__9)
                self.state = 212
                self.condition()
                self.state = 213
                self.endStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.match(grammarCParser.T__9)
                self.state = 216
                self.operation()
                self.state = 217
                self.endStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 219
                self.match(grammarCParser.T__9)
                self.state = 220
                self.endStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.RValueContext)
            else:
                return self.getTypedRuleContext(grammarCParser.RValueContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_parList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParList" ):
                listener.enterParList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParList" ):
                listener.exitParList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParList" ):
                return visitor.visitParList(self)
            else:
                return visitor.visitChildren(self)




    def parList(self):

        localctx = grammarCParser.ParListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parList)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__25, grammarCParser.T__41, grammarCParser.DIGIT, grammarCParser.FLT, grammarCParser.STR, grammarCParser.BOOL, grammarCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 223
                        self.rValue()
                        self.state = 224
                        self.match(grammarCParser.T__6) 
                    self.state = 230
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 231
                self.rValue()
                pass
            elif token in [grammarCParser.T__5]:
                self.enterOuterAlt(localctx, 2)

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

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(grammarCParser.TypesContext,0)


        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def constant(self):
            return self.getTypedRuleContext(grammarCParser.ConstantContext,0)


        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.PointerContext)
            else:
                return self.getTypedRuleContext(grammarCParser.PointerContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ReferenceContext,i)


        def arrayDecl(self):
            return self.getTypedRuleContext(grammarCParser.ArrayDeclContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = grammarCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__42:
                    self.state = 235
                    self.constant()


                self.state = 238
                self.types()
                self.state = 251
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__25:
                        self.state = 239
                        self.pointer()
                        self.state = 244
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 248
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__41:
                        self.state = 245
                        self.reference()
                        self.state = 250
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 253
                self.lValue()
                self.state = 254
                self.endStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.arrayDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(grammarCParser.TypesContext,0)


        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def DIGIT(self):
            return self.getToken(grammarCParser.DIGIT, 0)

        def ID(self):
            return self.getToken(grammarCParser.ID, 0)

        def constant(self):
            return self.getTypedRuleContext(grammarCParser.ConstantContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_arrayDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDecl" ):
                listener.enterArrayDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDecl" ):
                listener.exitArrayDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDecl" ):
                return visitor.visitArrayDecl(self)
            else:
                return visitor.visitChildren(self)




    def arrayDecl(self):

        localctx = grammarCParser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarCParser.T__42:
                self.state = 259
                self.constant()


            self.state = 262
            self.types()
            self.state = 263
            self.lValue()
            self.state = 264
            self.match(grammarCParser.T__10)
            self.state = 265
            _la = self._input.LA(1)
            if not(_la==grammarCParser.DIGIT or _la==grammarCParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 266
            self.match(grammarCParser.T__11)
            self.state = 267
            self.endStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(grammarCParser.TypesContext,0)


        def assignment(self):
            return self.getTypedRuleContext(grammarCParser.AssignmentContext,0)


        def constant(self):
            return self.getTypedRuleContext(grammarCParser.ConstantContext,0)


        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.PointerContext)
            else:
                return self.getTypedRuleContext(grammarCParser.PointerContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ReferenceContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = grammarCParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarCParser.T__42:
                self.state = 269
                self.constant()


            self.state = 272
            self.types()
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarCParser.T__25:
                    self.state = 273
                    self.pointer()
                    self.state = 278
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarCParser.T__41:
                    self.state = 279
                    self.reference()
                    self.state = 284
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 287
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def parList(self):
            return self.getTypedRuleContext(grammarCParser.ParListContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = grammarCParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.lValue()
            self.state = 290
            self.match(grammarCParser.T__4)
            self.state = 291
            self.parList()
            self.state = 292
            self.match(grammarCParser.T__5)
            self.state = 293
            self.endStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalAssignment(self):
            return self.getTypedRuleContext(grammarCParser.NormalAssignmentContext,0)


        def arrayAssignment(self):
            return self.getTypedRuleContext(grammarCParser.ArrayAssignmentContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = grammarCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignment)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.normalAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.arrayAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NormalAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def assign(self):
            return self.getTypedRuleContext(grammarCParser.AssignContext,0)


        def rValue(self):
            return self.getTypedRuleContext(grammarCParser.RValueContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(grammarCParser.FunctionCallContext,0)


        def operation(self):
            return self.getTypedRuleContext(grammarCParser.OperationContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_normalAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalAssignment" ):
                listener.enterNormalAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalAssignment" ):
                listener.exitNormalAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalAssignment" ):
                return visitor.visitNormalAssignment(self)
            else:
                return visitor.visitChildren(self)




    def normalAssignment(self):

        localctx = grammarCParser.NormalAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_normalAssignment)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.lValue()
                self.state = 300
                self.assign()
                self.state = 301
                self.rValue()
                self.state = 302
                self.endStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.lValue()
                self.state = 305
                self.assign()
                self.state = 306
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.lValue()
                self.state = 309
                self.assign()
                self.state = 310
                self.operation()
                self.state = 311
                self.endStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def assign(self):
            return self.getTypedRuleContext(grammarCParser.AssignContext,0)


        def arrayOptions(self):
            return self.getTypedRuleContext(grammarCParser.ArrayOptionsContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def DIGIT(self):
            return self.getToken(grammarCParser.DIGIT, 0)

        def ID(self):
            return self.getToken(grammarCParser.ID, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_arrayAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssignment" ):
                listener.enterArrayAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssignment" ):
                listener.exitArrayAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignment" ):
                return visitor.visitArrayAssignment(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssignment(self):

        localctx = grammarCParser.ArrayAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.lValue()
            self.state = 316
            self.match(grammarCParser.T__10)
            self.state = 317
            _la = self._input.LA(1)
            if not(_la==grammarCParser.DIGIT or _la==grammarCParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 318
            self.match(grammarCParser.T__11)
            self.state = 319
            self.assign()
            self.state = 320
            self.arrayOptions()
            self.state = 321
            self.endStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayOptionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.RValueContext)
            else:
                return self.getTypedRuleContext(grammarCParser.RValueContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_arrayOptions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOptions" ):
                listener.enterArrayOptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOptions" ):
                listener.exitArrayOptions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayOptions" ):
                return visitor.visitArrayOptions(self)
            else:
                return visitor.visitChildren(self)




    def arrayOptions(self):

        localctx = grammarCParser.ArrayOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayOptions)
        self._la = 0 # Token type
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(grammarCParser.T__7)
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 324
                        self.rValue()
                        self.state = 325
                        self.match(grammarCParser.T__6) 
                    self.state = 331
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarCParser.T__25) | (1 << grammarCParser.T__41) | (1 << grammarCParser.DIGIT) | (1 << grammarCParser.FLT) | (1 << grammarCParser.STR) | (1 << grammarCParser.BOOL) | (1 << grammarCParser.ID))) != 0):
                    self.state = 332
                    self.rValue()


                self.state = 335
                self.match(grammarCParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(grammarCParser.T__7)
                self.state = 337
                self.match(grammarCParser.T__8)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.rValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(grammarCParser.IfStatementContext,0)


        def elifStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ElifStatementContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ElifStatementContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(grammarCParser.ElseStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(grammarCParser.WhileStatementContext,0)


        def loop(self):
            return self.getTypedRuleContext(grammarCParser.LoopContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = grammarCParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.ifStatement()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarCParser.T__13:
                    self.state = 342
                    self.elifStatement()
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__14:
                    self.state = 348
                    self.elseStatement()


                pass
            elif token in [grammarCParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.whileStatement()
                pass
            elif token in [grammarCParser.T__16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.loop()
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

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(grammarCParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = grammarCParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(grammarCParser.T__12)
            self.state = 356
            self.match(grammarCParser.T__4)
            self.state = 357
            self.condition()
            self.state = 358
            self.match(grammarCParser.T__5)
            self.state = 359
            self.match(grammarCParser.T__7)
            self.state = 360
            self.body()
            self.state = 361
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElifStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(grammarCParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_elifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifStatement" ):
                listener.enterElifStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifStatement" ):
                listener.exitElifStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStatement" ):
                return visitor.visitElifStatement(self)
            else:
                return visitor.visitChildren(self)




    def elifStatement(self):

        localctx = grammarCParser.ElifStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(grammarCParser.T__13)
            self.state = 364
            self.match(grammarCParser.T__4)
            self.state = 365
            self.condition()
            self.state = 366
            self.match(grammarCParser.T__5)
            self.state = 367
            self.match(grammarCParser.T__7)
            self.state = 368
            self.body()
            self.state = 369
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElseStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = grammarCParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(grammarCParser.T__14)
            self.state = 372
            self.match(grammarCParser.T__7)
            self.state = 373
            self.body()
            self.state = 374
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(grammarCParser.ConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = grammarCParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(grammarCParser.T__15)
            self.state = 377
            self.match(grammarCParser.T__4)
            self.state = 378
            self.condition()
            self.state = 379
            self.match(grammarCParser.T__5)
            self.state = 380
            self.match(grammarCParser.T__7)
            self.state = 381
            self.body()
            self.state = 382
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forCondition(self):
            return self.getTypedRuleContext(grammarCParser.ForConditionContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = grammarCParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(grammarCParser.T__16)
            self.state = 385
            self.match(grammarCParser.T__4)
            self.state = 386
            self.forCondition()
            self.state = 387
            self.match(grammarCParser.T__5)
            self.state = 388
            self.match(grammarCParser.T__7)
            self.state = 389
            self.body()
            self.state = 390
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.RValueContext)
            else:
                return self.getTypedRuleContext(grammarCParser.RValueContext,i)


        def comparison(self):
            return self.getTypedRuleContext(grammarCParser.ComparisonContext,0)


        def condition(self):
            return self.getTypedRuleContext(grammarCParser.ConditionContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = grammarCParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.rValue()
                self.state = 393
                self.comparison()
                self.state = 394
                self.rValue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__17:
                    self.state = 396
                    self.match(grammarCParser.T__17)


                self.state = 399
                self.rValue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self.match(grammarCParser.T__17)
                self.state = 401
                self.match(grammarCParser.T__4)
                self.state = 402
                self.condition()
                self.state = 403
                self.match(grammarCParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deel1(self):
            return self.getTypedRuleContext(grammarCParser.Deel1Context,0)


        def deel2(self):
            return self.getTypedRuleContext(grammarCParser.Deel2Context,0)


        def deel3(self):
            return self.getTypedRuleContext(grammarCParser.Deel3Context,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = grammarCParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forCondition)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29, grammarCParser.T__42, grammarCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.deel1()
                self.state = 408
                self.deel2()
                self.state = 409
                self.match(grammarCParser.T__18)
                self.state = 410
                self.deel3()
                pass
            elif token in [grammarCParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(grammarCParser.T__18)
                self.state = 413
                self.match(grammarCParser.T__18)
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

    class Deel1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(grammarCParser.DeclarationContext,0)


        def definition(self):
            return self.getTypedRuleContext(grammarCParser.DefinitionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(grammarCParser.AssignmentContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_deel1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeel1" ):
                listener.enterDeel1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeel1" ):
                listener.exitDeel1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeel1" ):
                return visitor.visitDeel1(self)
            else:
                return visitor.visitChildren(self)




    def deel1(self):

        localctx = grammarCParser.Deel1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_deel1)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Deel2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(grammarCParser.ConditionContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_deel2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeel2" ):
                listener.enterDeel2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeel2" ):
                listener.exitDeel2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeel2" ):
                return visitor.visitDeel2(self)
            else:
                return visitor.visitChildren(self)




    def deel2(self):

        localctx = grammarCParser.Deel2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_deel2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Deel3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(grammarCParser.OperationContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_deel3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeel3" ):
                listener.enterDeel3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeel3" ):
                listener.exitDeel3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeel3" ):
                return visitor.visitDeel3(self)
            else:
                return visitor.visitChildren(self)




    def deel3(self):

        localctx = grammarCParser.Deel3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_deel3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.operation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nextOperation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.NextOperationContext)
            else:
                return self.getTypedRuleContext(grammarCParser.NextOperationContext,i)


        def operator(self):
            return self.getTypedRuleContext(grammarCParser.OperatorContext,0)


        def operation(self):
            return self.getTypedRuleContext(grammarCParser.OperationContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = grammarCParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_operation)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.nextOperation()
                self.state = 426
                self.operator()
                self.state = 427
                self.nextOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.match(grammarCParser.T__4)
                self.state = 430
                self.operation()
                self.state = 431
                self.match(grammarCParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NextOperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseOperation(self):
            return self.getTypedRuleContext(grammarCParser.BaseOperationContext,0)


        def operator(self):
            return self.getTypedRuleContext(grammarCParser.OperatorContext,0)


        def nextOperation(self):
            return self.getTypedRuleContext(grammarCParser.NextOperationContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_nextOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNextOperation" ):
                listener.enterNextOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNextOperation" ):
                listener.exitNextOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextOperation" ):
                return visitor.visitNextOperation(self)
            else:
                return visitor.visitChildren(self)




    def nextOperation(self):

        localctx = grammarCParser.NextOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_nextOperation)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.baseOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.baseOperation()
                self.state = 437
                self.operator()
                self.state = 438
                self.nextOperation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.match(grammarCParser.T__4)
                self.state = 441
                self.nextOperation()
                self.state = 442
                self.match(grammarCParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BaseOperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rValue(self):
            return self.getTypedRuleContext(grammarCParser.RValueContext,0)


        def operator(self):
            return self.getTypedRuleContext(grammarCParser.OperatorContext,0)


        def baseOperation(self):
            return self.getTypedRuleContext(grammarCParser.BaseOperationContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_baseOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseOperation" ):
                listener.enterBaseOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseOperation" ):
                listener.exitBaseOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseOperation" ):
                return visitor.visitBaseOperation(self)
            else:
                return visitor.visitChildren(self)




    def baseOperation(self):

        localctx = grammarCParser.BaseOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_baseOperation)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.rValue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.rValue()
                self.state = 448
                self.operator()
                self.state = 449
                self.baseOperation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.match(grammarCParser.T__4)
                self.state = 452
                self.baseOperation()
                self.state = 453
                self.match(grammarCParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlusplusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rValue(self):
            return self.getTypedRuleContext(grammarCParser.RValueContext,0)


        def deincrement(self):
            return self.getTypedRuleContext(grammarCParser.DeincrementContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_plusplus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusplus" ):
                listener.enterPlusplus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusplus" ):
                listener.exitPlusplus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusplus" ):
                return visitor.visitPlusplus(self)
            else:
                return visitor.visitChildren(self)




    def plusplus(self):

        localctx = grammarCParser.PlusplusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_plusplus)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__25, grammarCParser.T__41, grammarCParser.DIGIT, grammarCParser.FLT, grammarCParser.STR, grammarCParser.BOOL, grammarCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.rValue()
                self.state = 458
                self.deincrement()
                pass
            elif token in [grammarCParser.T__39, grammarCParser.T__40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.deincrement()
                self.state = 461
                self.rValue()
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

    class KwContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_kw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKw" ):
                listener.enterKw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKw" ):
                listener.exitKw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKw" ):
                return visitor.visitKw(self)
            else:
                return visitor.visitChildren(self)




    def kw(self):

        localctx = grammarCParser.KwContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_kw)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(grammarCParser.T__19)
                self.state = 466
                self.endStatement()
                pass
            elif token in [grammarCParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.match(grammarCParser.T__20)
                self.state = 468
                self.endStatement()
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

    class MainFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argListMain(self):
            return self.getTypedRuleContext(grammarCParser.ArgListMainContext,0)


        def body(self):
            return self.getTypedRuleContext(grammarCParser.BodyContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_mainFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainFunc" ):
                listener.enterMainFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainFunc" ):
                listener.exitMainFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainFunc" ):
                return visitor.visitMainFunc(self)
            else:
                return visitor.visitChildren(self)




    def mainFunc(self):

        localctx = grammarCParser.MainFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_mainFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(grammarCParser.T__21)
            self.state = 472
            self.match(grammarCParser.T__22)
            self.state = 473
            self.match(grammarCParser.T__4)
            self.state = 474
            self.argListMain()
            self.state = 475
            self.match(grammarCParser.T__5)
            self.state = 476
            self.match(grammarCParser.T__7)
            self.state = 477
            self.body()
            self.state = 478
            self.match(grammarCParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgListMainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_argListMain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgListMain" ):
                listener.enterArgListMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgListMain" ):
                listener.exitArgListMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgListMain" ):
                return visitor.visitArgListMain(self)
            else:
                return visitor.visitChildren(self)




    def argListMain(self):

        localctx = grammarCParser.ArgListMainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_argListMain)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(grammarCParser.T__21)
                self.state = 481
                self.match(grammarCParser.T__23)
                self.state = 482
                self.match(grammarCParser.T__6)
                self.state = 483
                self.match(grammarCParser.T__24)
                self.state = 484
                self.match(grammarCParser.T__25)
                self.state = 485
                self.match(grammarCParser.T__26)
                self.state = 486
                self.match(grammarCParser.T__10)
                self.state = 487
                self.match(grammarCParser.T__11)
                pass
            elif token in [grammarCParser.T__5]:
                self.enterOuterAlt(localctx, 2)

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

    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = grammarCParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarCParser.T__21) | (1 << grammarCParser.T__24) | (1 << grammarCParser.T__27) | (1 << grammarCParser.T__28) | (1 << grammarCParser.T__29))) != 0)):
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

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = grammarCParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarCParser.T__25) | (1 << grammarCParser.T__30) | (1 << grammarCParser.T__31) | (1 << grammarCParser.T__32) | (1 << grammarCParser.T__33))) != 0)):
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

    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = grammarCParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammarCParser.T__1) | (1 << grammarCParser.T__34) | (1 << grammarCParser.T__35) | (1 << grammarCParser.T__36) | (1 << grammarCParser.T__37) | (1 << grammarCParser.T__38))) != 0)):
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

    class DeincrementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_deincrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeincrement" ):
                listener.enterDeincrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeincrement" ):
                listener.exitDeincrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeincrement" ):
                return visitor.visitDeincrement(self)
            else:
                return visitor.visitChildren(self)




    def deincrement(self):

        localctx = grammarCParser.DeincrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_deincrement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            _la = self._input.LA(1)
            if not(_la==grammarCParser.T__39 or _la==grammarCParser.T__40):
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

    class PointerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = grammarCParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_pointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(grammarCParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = grammarCParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(grammarCParser.T__41)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = grammarCParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(grammarCParser.T__42)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EndStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_endStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndStatement" ):
                listener.enterEndStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndStatement" ):
                listener.exitEndStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndStatement" ):
                return visitor.visitEndStatement(self)
            else:
                return visitor.visitChildren(self)




    def endStatement(self):

        localctx = grammarCParser.EndStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_endStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(grammarCParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarCParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = grammarCParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(grammarCParser.T__43)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(grammarCParser.DIGIT, 0)

        def FLT(self):
            return self.getToken(grammarCParser.FLT, 0)

        def STR(self):
            return self.getToken(grammarCParser.STR, 0)

        def BOOL(self):
            return self.getToken(grammarCParser.BOOL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarCParser.ID)
            else:
                return self.getToken(grammarCParser.ID, i)

        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.PointerContext)
            else:
                return self.getTypedRuleContext(grammarCParser.PointerContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ReferenceContext,i)


        def getRuleIndex(self):
            return grammarCParser.RULE_rValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRValue" ):
                listener.enterRValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRValue" ):
                listener.exitRValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRValue" ):
                return visitor.visitRValue(self)
            else:
                return visitor.visitChildren(self)




    def rValue(self):

        localctx = grammarCParser.RValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_rValue)
        self._la = 0 # Token type
        try:
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(grammarCParser.DIGIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.match(grammarCParser.FLT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                self.match(grammarCParser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 512
                self.match(grammarCParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 516
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__25:
                        self.state = 513
                        self.pointer()
                        self.state = 518
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 522
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__41:
                        self.state = 519
                        self.reference()
                        self.state = 524
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 527
                self.match(grammarCParser.ID)
                self.state = 528
                self.match(grammarCParser.T__10)
                self.state = 529
                _la = self._input.LA(1)
                if not(_la==grammarCParser.DIGIT or _la==grammarCParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 530
                self.match(grammarCParser.T__11)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 543
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 534
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__25:
                        self.state = 531
                        self.pointer()
                        self.state = 536
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 540
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__41:
                        self.state = 537
                        self.reference()
                        self.state = 542
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 545
                self.match(grammarCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarCParser.ID, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_lValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLValue" ):
                listener.enterLValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLValue" ):
                listener.exitLValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLValue" ):
                return visitor.visitLValue(self)
            else:
                return visitor.visitChildren(self)




    def lValue(self):

        localctx = grammarCParser.LValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_lValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(grammarCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





