# Generated from ./src/grammar/grammarC.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u024d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3u\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7\u0087\n\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0091\n\b\3\t\3\t\7\t\u0095\n\t\f\t\16")
        buf.write("\t\u0098\13\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00a2")
        buf.write("\n\n\3\n\3\n\7\n\u00a6\n\n\f\n\16\n\u00a9\13\n\3\n\3\n")
        buf.write("\5\n\u00ad\n\n\3\n\5\n\u00b0\n\n\3\13\3\13\7\13\u00b4")
        buf.write("\n\13\f\13\16\13\u00b7\13\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\5\f\u00c3\n\f\3\f\3\f\3\f\7\f")
        buf.write("\u00c8\n\f\f\f\16\f\u00cb\13\f\3\f\3\f\5\f\u00cf\n\f\3")
        buf.write("\f\3\f\3\f\5\f\u00d4\n\f\3\r\3\r\5\r\u00d8\n\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00e0\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ed\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u00ff\n\20\3\21\3\21\3")
        buf.write("\21\7\21\u0104\n\21\f\21\16\21\u0107\13\21\3\21\3\21\5")
        buf.write("\21\u010b\n\21\3\22\5\22\u010e\n\22\3\22\3\22\7\22\u0112")
        buf.write("\n\22\f\22\16\22\u0115\13\22\3\22\7\22\u0118\n\22\f\22")
        buf.write("\16\22\u011b\13\22\5\22\u011d\n\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u0123\n\22\3\23\5\23\u0126\n\23\3\23\3\23\7\23\u012a")
        buf.write("\n\23\f\23\16\23\u012d\13\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\5\24\u0136\n\24\3\24\3\24\7\24\u013a\n\24\f")
        buf.write("\24\16\24\u013d\13\24\3\24\7\24\u0140\n\24\f\24\16\24")
        buf.write("\u0143\13\24\5\24\u0145\n\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\5\26\u0151\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0161\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\7\31\u016f\n\31\f\31\16\31")
        buf.write("\u0172\13\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u017a")
        buf.write("\n\31\3\32\3\32\7\32\u017e\n\32\f\32\16\32\u0181\13\32")
        buf.write("\3\32\5\32\u0184\n\32\3\32\3\32\5\32\u0188\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \5 \u01b4\n \3 \3 \3 \3")
        buf.write(" \3 \3 \5 \u01bc\n \3!\3!\3!\3!\3!\3!\3!\5!\u01c5\n!\3")
        buf.write("\"\3\"\3\"\5\"\u01ca\n\"\3#\3#\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u01d8\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01e3")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01ee\n\'")
        buf.write("\3(\3(\3(\3(\3(\3(\5(\u01f6\n(\3)\3)\3)\3)\5)\u01fc\n")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\5+\u0210\n+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\7\65\u0229\n\65\f\65\16\65\u022c\13\65\3\65\7\65")
        buf.write("\u022f\n\65\f\65\16\65\u0232\13\65\5\65\u0234\n\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\7\65\u023b\n\65\f\65\16\65\u023e")
        buf.write("\13\65\3\65\7\65\u0241\n\65\f\65\16\65\u0244\13\65\5\65")
        buf.write("\u0246\n\65\3\65\5\65\u0249\n\65\3\66\3\66\3\66\2\2\67")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\b\4\2\6\6\64\64\4")
        buf.write("\2//\64\64\5\2\30\30\33\33\36 \4\2\34\34!$\4\2\4\4%)\3")
        buf.write("\2*+\2\u0265\2l\3\2\2\2\4t\3\2\2\2\6v\3\2\2\2\by\3\2\2")
        buf.write("\2\n}\3\2\2\2\f\u0086\3\2\2\2\16\u0090\3\2\2\2\20\u0092")
        buf.write("\3\2\2\2\22\u00af\3\2\2\2\24\u00b1\3\2\2\2\26\u00d3\3")
        buf.write("\2\2\2\30\u00d5\3\2\2\2\32\u00df\3\2\2\2\34\u00ec\3\2")
        buf.write("\2\2\36\u00fe\3\2\2\2 \u010a\3\2\2\2\"\u0122\3\2\2\2$")
        buf.write("\u0125\3\2\2\2&\u0135\3\2\2\2(\u0148\3\2\2\2*\u0150\3")
        buf.write("\2\2\2,\u0160\3\2\2\2.\u0162\3\2\2\2\60\u0179\3\2\2\2")
        buf.write("\62\u0187\3\2\2\2\64\u0189\3\2\2\2\66\u0191\3\2\2\28\u0199")
        buf.write("\3\2\2\2:\u019e\3\2\2\2<\u01a6\3\2\2\2>\u01bb\3\2\2\2")
        buf.write("@\u01c4\3\2\2\2B\u01c9\3\2\2\2D\u01cb\3\2\2\2F\u01cd\3")
        buf.write("\2\2\2H\u01d7\3\2\2\2J\u01e2\3\2\2\2L\u01ed\3\2\2\2N\u01f5")
        buf.write("\3\2\2\2P\u01fb\3\2\2\2R\u01fd\3\2\2\2T\u020f\3\2\2\2")
        buf.write("V\u0211\3\2\2\2X\u0213\3\2\2\2Z\u0215\3\2\2\2\\\u0217")
        buf.write("\3\2\2\2^\u0219\3\2\2\2`\u021b\3\2\2\2b\u021d\3\2\2\2")
        buf.write("d\u021f\3\2\2\2f\u0221\3\2\2\2h\u0248\3\2\2\2j\u024a\3")
        buf.write("\2\2\2lm\5\4\3\2mn\5\f\7\2no\5\16\b\2o\3\3\2\2\2pq\5\6")
        buf.write("\4\2qr\5\4\3\2ru\3\2\2\2su\3\2\2\2tp\3\2\2\2ts\3\2\2\2")
        buf.write("u\5\3\2\2\2vw\7\3\2\2wx\5\b\5\2x\7\3\2\2\2yz\7\4\2\2z")
        buf.write("{\5\n\6\2{|\7\5\2\2|\t\3\2\2\2}~\t\2\2\2~\13\3\2\2\2\177")
        buf.write("\u0080\5\"\22\2\u0080\u0081\5\f\7\2\u0081\u0087\3\2\2")
        buf.write("\2\u0082\u0083\5&\24\2\u0083\u0084\5\f\7\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0087\3\2\2\2\u0086\177\3\2\2\2\u0086\u0082")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\r\3\2\2\2\u0088\u0089")
        buf.write("\5\24\13\2\u0089\u008a\5\16\b\2\u008a\u0091\3\2\2\2\u008b")
        buf.write("\u008c\5\20\t\2\u008c\u008d\5\16\b\2\u008d\u0091\3\2\2")
        buf.write("\2\u008e\u0091\5R*\2\u008f\u0091\3\2\2\2\u0090\u0088\3")
        buf.write("\2\2\2\u0090\u008b\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\17\3\2\2\2\u0092\u0096\5V,\2\u0093\u0095")
        buf.write("\5^\60\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0099\u009a\5j\66\2\u009a\u009b\7")
        buf.write("\7\2\2\u009b\u009c\5\22\n\2\u009c\u009d\7\b\2\2\u009d")
        buf.write("\u009e\5d\63\2\u009e\21\3\2\2\2\u009f\u00a1\5V,\2\u00a0")
        buf.write("\u00a2\5j\66\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7\t\2\2\u00a4\u00a6\3")
        buf.write("\2\2\2\u00a5\u009f\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\u00ac\5V,\2\u00ab\u00ad\5j\66\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b0\3\2\2\2")
        buf.write("\u00ae\u00b0\3\2\2\2\u00af\u00a7\3\2\2\2\u00af\u00ae\3")
        buf.write("\2\2\2\u00b0\23\3\2\2\2\u00b1\u00b5\5V,\2\u00b2\u00b4")
        buf.write("\5^\60\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00b9\5j\66\2\u00b9\u00ba\7")
        buf.write("\7\2\2\u00ba\u00bb\5\26\f\2\u00bb\u00bc\7\b\2\2\u00bc")
        buf.write("\u00bd\7\n\2\2\u00bd\u00be\5\32\16\2\u00be\u00bf\7\13")
        buf.write("\2\2\u00bf\25\3\2\2\2\u00c0\u00c2\5V,\2\u00c1\u00c3\5")
        buf.write("\30\r\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00c5\5j\66\2\u00c5\u00c6\7\t\2\2")
        buf.write("\u00c6\u00c8\3\2\2\2\u00c7\u00c0\3\2\2\2\u00c8\u00cb\3")
        buf.write("\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc")
        buf.write("\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00ce\5V,\2\u00cd\u00cf")
        buf.write("\5\30\r\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d1\5j\66\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d4\3\2\2\2\u00d3\u00c9\3\2\2\2\u00d3\u00d2\3")
        buf.write("\2\2\2\u00d4\27\3\2\2\2\u00d5\u00d7\7\f\2\2\u00d6\u00d8")
        buf.write("\7/\2\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00da\7\r\2\2\u00da\31\3\2\2\2\u00db")
        buf.write("\u00dc\5\34\17\2\u00dc\u00dd\5\32\16\2\u00dd\u00e0\3\2")
        buf.write("\2\2\u00de\u00e0\5\34\17\2\u00df\u00db\3\2\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0\33\3\2\2\2\u00e1\u00ed\5\"\22\2\u00e2\u00ed")
        buf.write("\5&\24\2\u00e3\u00ed\5(\25\2\u00e4\u00ed\5*\26\2\u00e5")
        buf.write("\u00ed\5\62\32\2\u00e6\u00e7\5H%\2\u00e7\u00e8\5d\63\2")
        buf.write("\u00e8\u00ed\3\2\2\2\u00e9\u00ed\5\36\20\2\u00ea\u00ed")
        buf.write("\5N(\2\u00eb\u00ed\5P)\2\u00ec\u00e1\3\2\2\2\u00ec\u00e2")
        buf.write("\3\2\2\2\u00ec\u00e3\3\2\2\2\u00ec\u00e4\3\2\2\2\u00ec")
        buf.write("\u00e5\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ec\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\35\3\2")
        buf.write("\2\2\u00ee\u00ef\7\16\2\2\u00ef\u00ff\5(\25\2\u00f0\u00f1")
        buf.write("\7\16\2\2\u00f1\u00f2\5h\65\2\u00f2\u00f3\5d\63\2\u00f3")
        buf.write("\u00ff\3\2\2\2\u00f4\u00f5\7\16\2\2\u00f5\u00f6\5> \2")
        buf.write("\u00f6\u00f7\5d\63\2\u00f7\u00ff\3\2\2\2\u00f8\u00f9\7")
        buf.write("\16\2\2\u00f9\u00fa\5H%\2\u00fa\u00fb\5d\63\2\u00fb\u00ff")
        buf.write("\3\2\2\2\u00fc\u00fd\7\16\2\2\u00fd\u00ff\5d\63\2\u00fe")
        buf.write("\u00ee\3\2\2\2\u00fe\u00f0\3\2\2\2\u00fe\u00f4\3\2\2\2")
        buf.write("\u00fe\u00f8\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\37\3\2")
        buf.write("\2\2\u0100\u0101\5h\65\2\u0101\u0102\7\t\2\2\u0102\u0104")
        buf.write("\3\2\2\2\u0103\u0100\3\2\2\2\u0104\u0107\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0108\u010b\5h\65\2\u0109\u010b\3")
        buf.write("\2\2\2\u010a\u0105\3\2\2\2\u010a\u0109\3\2\2\2\u010b!")
        buf.write("\3\2\2\2\u010c\u010e\5b\62\2\u010d\u010c\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u011c\5V,\2\u0110")
        buf.write("\u0112\5^\60\2\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u011d\3")
        buf.write("\2\2\2\u0115\u0113\3\2\2\2\u0116\u0118\5`\61\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2")
        buf.write("\u011c\u0113\3\2\2\2\u011c\u0119\3\2\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u011f\5j\66\2\u011f\u0120\5d\63\2\u0120\u0123")
        buf.write("\3\2\2\2\u0121\u0123\5$\23\2\u0122\u010d\3\2\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123#\3\2\2\2\u0124\u0126\5b\62\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u012b\5V,\2\u0128\u012a\5^\60\2\u0129\u0128\3\2")
        buf.write("\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012b\3\2\2\2\u012e")
        buf.write("\u012f\5j\66\2\u012f\u0130\7\f\2\2\u0130\u0131\7/\2\2")
        buf.write("\u0131\u0132\7\r\2\2\u0132\u0133\5d\63\2\u0133%\3\2\2")
        buf.write("\2\u0134\u0136\5b\62\2\u0135\u0134\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0144\5V,\2\u0138\u013a")
        buf.write("\5^\60\2\u0139\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u0145\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013e\u0140\5`\61\2\u013f\u013e\3")
        buf.write("\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0144")
        buf.write("\u013b\3\2\2\2\u0144\u0141\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0147\5*\26\2\u0147\'\3\2\2\2\u0148\u0149\5j\66")
        buf.write("\2\u0149\u014a\7\7\2\2\u014a\u014b\5 \21\2\u014b\u014c")
        buf.write("\7\b\2\2\u014c\u014d\5d\63\2\u014d)\3\2\2\2\u014e\u0151")
        buf.write("\5,\27\2\u014f\u0151\5.\30\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151+\3\2\2\2\u0152\u0153\5j\66\2\u0153")
        buf.write("\u0154\5f\64\2\u0154\u0155\5h\65\2\u0155\u0156\5d\63\2")
        buf.write("\u0156\u0161\3\2\2\2\u0157\u0158\5j\66\2\u0158\u0159\5")
        buf.write("f\64\2\u0159\u015a\5(\25\2\u015a\u0161\3\2\2\2\u015b\u015c")
        buf.write("\5j\66\2\u015c\u015d\5f\64\2\u015d\u015e\5H%\2\u015e\u015f")
        buf.write("\5d\63\2\u015f\u0161\3\2\2\2\u0160\u0152\3\2\2\2\u0160")
        buf.write("\u0157\3\2\2\2\u0160\u015b\3\2\2\2\u0161-\3\2\2\2\u0162")
        buf.write("\u0163\5j\66\2\u0163\u0164\7\f\2\2\u0164\u0165\t\3\2\2")
        buf.write("\u0165\u0166\7\r\2\2\u0166\u0167\5f\64\2\u0167\u0168\5")
        buf.write("\60\31\2\u0168\u0169\5d\63\2\u0169/\3\2\2\2\u016a\u0170")
        buf.write("\7\n\2\2\u016b\u016c\5h\65\2\u016c\u016d\7\t\2\2\u016d")
        buf.write("\u016f\3\2\2\2\u016e\u016b\3\2\2\2\u016f\u0172\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3")
        buf.write("\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\5h\65\2\u0174\u0175")
        buf.write("\7\13\2\2\u0175\u017a\3\2\2\2\u0176\u0177\7\n\2\2\u0177")
        buf.write("\u017a\7\13\2\2\u0178\u017a\5h\65\2\u0179\u016a\3\2\2")
        buf.write("\2\u0179\u0176\3\2\2\2\u0179\u0178\3\2\2\2\u017a\61\3")
        buf.write("\2\2\2\u017b\u017f\5\64\33\2\u017c\u017e\5\66\34\2\u017d")
        buf.write("\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3")
        buf.write("\2\2\2\u0182\u0184\58\35\2\u0183\u0182\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0188\3\2\2\2\u0185\u0188\5:\36\2\u0186")
        buf.write("\u0188\5<\37\2\u0187\u017b\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188\63\3\2\2\2\u0189\u018a\7\17")
        buf.write("\2\2\u018a\u018b\7\7\2\2\u018b\u018c\5> \2\u018c\u018d")
        buf.write("\7\b\2\2\u018d\u018e\7\n\2\2\u018e\u018f\5\32\16\2\u018f")
        buf.write("\u0190\7\13\2\2\u0190\65\3\2\2\2\u0191\u0192\7\20\2\2")
        buf.write("\u0192\u0193\7\7\2\2\u0193\u0194\5> \2\u0194\u0195\7\b")
        buf.write("\2\2\u0195\u0196\7\n\2\2\u0196\u0197\5\32\16\2\u0197\u0198")
        buf.write("\7\13\2\2\u0198\67\3\2\2\2\u0199\u019a\7\21\2\2\u019a")
        buf.write("\u019b\7\n\2\2\u019b\u019c\5\32\16\2\u019c\u019d\7\13")
        buf.write("\2\2\u019d9\3\2\2\2\u019e\u019f\7\22\2\2\u019f\u01a0\7")
        buf.write("\7\2\2\u01a0\u01a1\5> \2\u01a1\u01a2\7\b\2\2\u01a2\u01a3")
        buf.write("\7\n\2\2\u01a3\u01a4\5\32\16\2\u01a4\u01a5\7\13\2\2\u01a5")
        buf.write(";\3\2\2\2\u01a6\u01a7\7\23\2\2\u01a7\u01a8\7\7\2\2\u01a8")
        buf.write("\u01a9\5@!\2\u01a9\u01aa\7\b\2\2\u01aa\u01ab\7\n\2\2\u01ab")
        buf.write("\u01ac\5\32\16\2\u01ac\u01ad\7\13\2\2\u01ad=\3\2\2\2\u01ae")
        buf.write("\u01af\5h\65\2\u01af\u01b0\5Z.\2\u01b0\u01b1\5h\65\2\u01b1")
        buf.write("\u01bc\3\2\2\2\u01b2\u01b4\7\24\2\2\u01b3\u01b2\3\2\2")
        buf.write("\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01bc")
        buf.write("\5h\65\2\u01b6\u01b7\7\24\2\2\u01b7\u01b8\7\7\2\2\u01b8")
        buf.write("\u01b9\5> \2\u01b9\u01ba\7\b\2\2\u01ba\u01bc\3\2\2\2\u01bb")
        buf.write("\u01ae\3\2\2\2\u01bb\u01b3\3\2\2\2\u01bb\u01b6\3\2\2\2")
        buf.write("\u01bc?\3\2\2\2\u01bd\u01be\5B\"\2\u01be\u01bf\5D#\2\u01bf")
        buf.write("\u01c0\7\25\2\2\u01c0\u01c1\5F$\2\u01c1\u01c5\3\2\2\2")
        buf.write("\u01c2\u01c3\7\25\2\2\u01c3\u01c5\7\25\2\2\u01c4\u01bd")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5A\3\2\2\2\u01c6\u01ca")
        buf.write("\5\"\22\2\u01c7\u01ca\5&\24\2\u01c8\u01ca\5*\26\2\u01c9")
        buf.write("\u01c6\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2")
        buf.write("\u01caC\3\2\2\2\u01cb\u01cc\5> \2\u01ccE\3\2\2\2\u01cd")
        buf.write("\u01ce\5H%\2\u01ceG\3\2\2\2\u01cf\u01d0\5J&\2\u01d0\u01d1")
        buf.write("\5X-\2\u01d1\u01d2\5J&\2\u01d2\u01d8\3\2\2\2\u01d3\u01d4")
        buf.write("\7\7\2\2\u01d4\u01d5\5H%\2\u01d5\u01d6\7\b\2\2\u01d6\u01d8")
        buf.write("\3\2\2\2\u01d7\u01cf\3\2\2\2\u01d7\u01d3\3\2\2\2\u01d8")
        buf.write("I\3\2\2\2\u01d9\u01e3\5L\'\2\u01da\u01db\5L\'\2\u01db")
        buf.write("\u01dc\5X-\2\u01dc\u01dd\5J&\2\u01dd\u01e3\3\2\2\2\u01de")
        buf.write("\u01df\7\7\2\2\u01df\u01e0\5J&\2\u01e0\u01e1\7\b\2\2\u01e1")
        buf.write("\u01e3\3\2\2\2\u01e2\u01d9\3\2\2\2\u01e2\u01da\3\2\2\2")
        buf.write("\u01e2\u01de\3\2\2\2\u01e3K\3\2\2\2\u01e4\u01ee\5h\65")
        buf.write("\2\u01e5\u01e6\5h\65\2\u01e6\u01e7\5X-\2\u01e7\u01e8\5")
        buf.write("L\'\2\u01e8\u01ee\3\2\2\2\u01e9\u01ea\7\7\2\2\u01ea\u01eb")
        buf.write("\5L\'\2\u01eb\u01ec\7\b\2\2\u01ec\u01ee\3\2\2\2\u01ed")
        buf.write("\u01e4\3\2\2\2\u01ed\u01e5\3\2\2\2\u01ed\u01e9\3\2\2\2")
        buf.write("\u01eeM\3\2\2\2\u01ef\u01f0\5h\65\2\u01f0\u01f1\5\\/\2")
        buf.write("\u01f1\u01f6\3\2\2\2\u01f2\u01f3\5\\/\2\u01f3\u01f4\5")
        buf.write("h\65\2\u01f4\u01f6\3\2\2\2\u01f5\u01ef\3\2\2\2\u01f5\u01f2")
        buf.write("\3\2\2\2\u01f6O\3\2\2\2\u01f7\u01f8\7\26\2\2\u01f8\u01fc")
        buf.write("\5d\63\2\u01f9\u01fa\7\27\2\2\u01fa\u01fc\5d\63\2\u01fb")
        buf.write("\u01f7\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fcQ\3\2\2\2\u01fd")
        buf.write("\u01fe\7\30\2\2\u01fe\u01ff\7\31\2\2\u01ff\u0200\7\7\2")
        buf.write("\2\u0200\u0201\5T+\2\u0201\u0202\7\b\2\2\u0202\u0203\7")
        buf.write("\n\2\2\u0203\u0204\5\32\16\2\u0204\u0205\7\13\2\2\u0205")
        buf.write("S\3\2\2\2\u0206\u0207\7\30\2\2\u0207\u0208\7\32\2\2\u0208")
        buf.write("\u0209\7\t\2\2\u0209\u020a\7\33\2\2\u020a\u020b\7\34\2")
        buf.write("\2\u020b\u020c\7\35\2\2\u020c\u020d\7\f\2\2\u020d\u0210")
        buf.write("\7\r\2\2\u020e\u0210\3\2\2\2\u020f\u0206\3\2\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210U\3\2\2\2\u0211\u0212\t\4\2\2\u0212")
        buf.write("W\3\2\2\2\u0213\u0214\t\5\2\2\u0214Y\3\2\2\2\u0215\u0216")
        buf.write("\t\6\2\2\u0216[\3\2\2\2\u0217\u0218\t\7\2\2\u0218]\3\2")
        buf.write("\2\2\u0219\u021a\7\34\2\2\u021a_\3\2\2\2\u021b\u021c\7")
        buf.write(",\2\2\u021ca\3\2\2\2\u021d\u021e\7-\2\2\u021ec\3\2\2\2")
        buf.write("\u021f\u0220\7\25\2\2\u0220e\3\2\2\2\u0221\u0222\7.\2")
        buf.write("\2\u0222g\3\2\2\2\u0223\u0249\7/\2\2\u0224\u0249\7\60")
        buf.write("\2\2\u0225\u0249\7\61\2\2\u0226\u0249\7\63\2\2\u0227\u0229")
        buf.write("\5^\60\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u0234\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u022f\5`\61\2\u022e\u022d\3")
        buf.write("\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0233")
        buf.write("\u022a\3\2\2\2\u0233\u0230\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235\u0236\7\64\2\2\u0236\u0237\7\f\2\2\u0237\u0238")
        buf.write("\t\3\2\2\u0238\u0249\7\r\2\2\u0239\u023b\5^\60\2\u023a")
        buf.write("\u0239\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u0246\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023f\u0241\5`\61\2\u0240\u023f\3\2\2\2\u0241\u0244")
        buf.write("\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write("\u0246\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u023c\3\2\2\2")
        buf.write("\u0245\u0242\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0249\7")
        buf.write("\64\2\2\u0248\u0223\3\2\2\2\u0248\u0224\3\2\2\2\u0248")
        buf.write("\u0225\3\2\2\2\u0248\u0226\3\2\2\2\u0248\u0233\3\2\2\2")
        buf.write("\u0248\u0245\3\2\2\2\u0249i\3\2\2\2\u024a\u024b\7\64\2")
        buf.write("\2\u024bk\3\2\2\28t\u0086\u0090\u0096\u00a1\u00a7\u00ac")
        buf.write("\u00af\u00b5\u00c2\u00c9\u00ce\u00d3\u00d7\u00df\u00ec")
        buf.write("\u00fe\u0105\u010a\u010d\u0113\u0119\u011c\u0122\u0125")
        buf.write("\u012b\u0135\u013b\u0141\u0144\u0150\u0160\u0170\u0179")
        buf.write("\u017f\u0183\u0187\u01b3\u01bb\u01c4\u01c9\u01d7\u01e2")
        buf.write("\u01ed\u01f5\u01fb\u020f\u022a\u0230\u0233\u023c\u0242")
        buf.write("\u0245\u0248")
        return buf.getvalue()


class grammarCParser ( Parser ):

    grammarFileName = "grammarC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'<'", "'.h>'", "'stdio'", 
                     "'('", "')'", "','", "'{'", "'}'", "'['", "']'", "'return'", 
                     "'if'", "'else if'", "'else'", "'while'", "'for'", 
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
    RULE_globalList = 5
    RULE_funcDefList = 6
    RULE_funcDecl = 7
    RULE_typeList = 8
    RULE_funcDef = 9
    RULE_argList = 10
    RULE_arraySign = 11
    RULE_body = 12
    RULE_statement = 13
    RULE_returnStatement = 14
    RULE_parList = 15
    RULE_declaration = 16
    RULE_arrayDecl = 17
    RULE_definition = 18
    RULE_functionCall = 19
    RULE_assignment = 20
    RULE_normalAssignment = 21
    RULE_arrayAssignment = 22
    RULE_arrayOptions = 23
    RULE_conditional = 24
    RULE_ifStatement = 25
    RULE_elifStatement = 26
    RULE_elseStatement = 27
    RULE_whileStatement = 28
    RULE_loop = 29
    RULE_condition = 30
    RULE_forCondition = 31
    RULE_deel1 = 32
    RULE_deel2 = 33
    RULE_deel3 = 34
    RULE_operation = 35
    RULE_nextOperation = 36
    RULE_baseOperation = 37
    RULE_plusplus = 38
    RULE_kw = 39
    RULE_mainFunc = 40
    RULE_argListMain = 41
    RULE_types = 42
    RULE_operator = 43
    RULE_comparison = 44
    RULE_deincrement = 45
    RULE_pointer = 46
    RULE_reference = 47
    RULE_constant = 48
    RULE_endStatement = 49
    RULE_assign = 50
    RULE_rValue = 51
    RULE_lValue = 52

    ruleNames =  [ "program", "libraryList", "library", "lib", "libname", 
                   "globalList", "funcDefList", "funcDecl", "typeList", 
                   "funcDef", "argList", "arraySign", "body", "statement", 
                   "returnStatement", "parList", "declaration", "arrayDecl", 
                   "definition", "functionCall", "assignment", "normalAssignment", 
                   "arrayAssignment", "arrayOptions", "conditional", "ifStatement", 
                   "elifStatement", "elseStatement", "whileStatement", "loop", 
                   "condition", "forCondition", "deel1", "deel2", "deel3", 
                   "operation", "nextOperation", "baseOperation", "plusplus", 
                   "kw", "mainFunc", "argListMain", "types", "operator", 
                   "comparison", "deincrement", "pointer", "reference", 
                   "constant", "endStatement", "assign", "rValue", "lValue" ]

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


        def globalList(self):
            return self.getTypedRuleContext(grammarCParser.GlobalListContext,0)


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
            self.state = 106
            self.libraryList()
            self.state = 107
            self.globalList()
            self.state = 108
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
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.library()
                self.state = 111
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
            self.state = 116
            self.match(grammarCParser.T__0)
            self.state = 117
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
            self.state = 119
            self.match(grammarCParser.T__1)
            self.state = 120
            self.libname()
            self.state = 121
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
            self.state = 123
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

    class GlobalListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(grammarCParser.DeclarationContext,0)


        def globalList(self):
            return self.getTypedRuleContext(grammarCParser.GlobalListContext,0)


        def definition(self):
            return self.getTypedRuleContext(grammarCParser.DefinitionContext,0)


        def getRuleIndex(self):
            return grammarCParser.RULE_globalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalList" ):
                listener.enterGlobalList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalList" ):
                listener.exitGlobalList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalList" ):
                return visitor.visitGlobalList(self)
            else:
                return visitor.visitChildren(self)




    def globalList(self):

        localctx = grammarCParser.GlobalListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_globalList)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.declaration()
                self.state = 126
                self.globalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.definition()
                self.state = 129
                self.globalList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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
        self.enterRule(localctx, 12, self.RULE_funcDefList)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.funcDef()
                self.state = 135
                self.funcDefList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.funcDecl()
                self.state = 138
                self.funcDefList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.mainFunc()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

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


        def lValue(self):
            return self.getTypedRuleContext(grammarCParser.LValueContext,0)


        def typeList(self):
            return self.getTypedRuleContext(grammarCParser.TypeListContext,0)


        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.PointerContext)
            else:
                return self.getTypedRuleContext(grammarCParser.PointerContext,i)


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
        self.enterRule(localctx, 14, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.types()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammarCParser.T__25:
                self.state = 145
                self.pointer()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.lValue()
            self.state = 152
            self.match(grammarCParser.T__4)
            self.state = 153
            self.typeList()
            self.state = 154
            self.match(grammarCParser.T__5)
            self.state = 155
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
        self.enterRule(localctx, 16, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 157
                        self.types()
                        self.state = 159
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==grammarCParser.ID:
                            self.state = 158
                            self.lValue()


                        self.state = 161
                        self.match(grammarCParser.T__6) 
                    self.state = 167
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 168
                self.types()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.ID:
                    self.state = 169
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


        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.PointerContext)
            else:
                return self.getTypedRuleContext(grammarCParser.PointerContext,i)


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
        self.enterRule(localctx, 18, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.types()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammarCParser.T__25:
                self.state = 176
                self.pointer()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.lValue()
            self.state = 183
            self.match(grammarCParser.T__4)
            self.state = 184
            self.argList()
            self.state = 185
            self.match(grammarCParser.T__5)
            self.state = 186
            self.match(grammarCParser.T__7)
            self.state = 187
            self.body()
            self.state = 188
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


        def arraySign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.ArraySignContext)
            else:
                return self.getTypedRuleContext(grammarCParser.ArraySignContext,i)


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
        self.enterRule(localctx, 20, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 190
                        self.types()
                        self.state = 192
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==grammarCParser.T__9:
                            self.state = 191
                            self.arraySign()


                        self.state = 194
                        self.lValue()
                        self.state = 195
                        self.match(grammarCParser.T__6) 
                    self.state = 201
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 202
                self.types()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__9:
                    self.state = 203
                    self.arraySign()


                self.state = 206
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

    class ArraySignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(grammarCParser.DIGIT, 0)

        def getRuleIndex(self):
            return grammarCParser.RULE_arraySign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraySign" ):
                listener.enterArraySign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraySign" ):
                listener.exitArraySign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraySign" ):
                return visitor.visitArraySign(self)
            else:
                return visitor.visitChildren(self)




    def arraySign(self):

        localctx = grammarCParser.ArraySignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arraySign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(grammarCParser.T__9)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarCParser.DIGIT:
                self.state = 212
                self.match(grammarCParser.DIGIT)


            self.state = 215
            self.match(grammarCParser.T__10)
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
        self.enterRule(localctx, 24, self.RULE_body)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.statement()
                self.state = 218
                self.body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.assignment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.operation()
                self.state = 229
                self.endStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 232
                self.plusplus()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 233
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
        self.enterRule(localctx, 28, self.RULE_returnStatement)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(grammarCParser.T__11)
                self.state = 237
                self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(grammarCParser.T__11)
                self.state = 239
                self.rValue()
                self.state = 240
                self.endStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(grammarCParser.T__11)
                self.state = 243
                self.condition()
                self.state = 244
                self.endStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(grammarCParser.T__11)
                self.state = 247
                self.operation()
                self.state = 248
                self.endStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.match(grammarCParser.T__11)
                self.state = 251
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
        self.enterRule(localctx, 30, self.RULE_parList)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__25, grammarCParser.T__41, grammarCParser.DIGIT, grammarCParser.FLT, grammarCParser.STR, grammarCParser.BOOL, grammarCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 254
                        self.rValue()
                        self.state = 255
                        self.match(grammarCParser.T__6) 
                    self.state = 261
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 262
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
        self.enterRule(localctx, 32, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__42:
                    self.state = 266
                    self.constant()


                self.state = 269
                self.types()
                self.state = 282
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__25:
                        self.state = 270
                        self.pointer()
                        self.state = 275
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__41:
                        self.state = 276
                        self.reference()
                        self.state = 281
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 284
                self.lValue()
                self.state = 285
                self.endStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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


        def DIGIT(self):
            return self.getToken(grammarCParser.DIGIT, 0)

        def endStatement(self):
            return self.getTypedRuleContext(grammarCParser.EndStatementContext,0)


        def constant(self):
            return self.getTypedRuleContext(grammarCParser.ConstantContext,0)


        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarCParser.PointerContext)
            else:
                return self.getTypedRuleContext(grammarCParser.PointerContext,i)


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
        self.enterRule(localctx, 34, self.RULE_arrayDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarCParser.T__42:
                self.state = 290
                self.constant()


            self.state = 293
            self.types()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammarCParser.T__25:
                self.state = 294
                self.pointer()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 300
            self.lValue()
            self.state = 301
            self.match(grammarCParser.T__9)
            self.state = 302
            self.match(grammarCParser.DIGIT)
            self.state = 303
            self.match(grammarCParser.T__10)
            self.state = 304
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
        self.enterRule(localctx, 36, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammarCParser.T__42:
                self.state = 306
                self.constant()


            self.state = 309
            self.types()
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarCParser.T__25:
                    self.state = 310
                    self.pointer()
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarCParser.T__41:
                    self.state = 316
                    self.reference()
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 324
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
        self.enterRule(localctx, 38, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.lValue()
            self.state = 327
            self.match(grammarCParser.T__4)
            self.state = 328
            self.parList()
            self.state = 329
            self.match(grammarCParser.T__5)
            self.state = 330
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
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.normalAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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
        self.enterRule(localctx, 42, self.RULE_normalAssignment)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.lValue()
                self.state = 337
                self.assign()
                self.state = 338
                self.rValue()
                self.state = 339
                self.endStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.lValue()
                self.state = 342
                self.assign()
                self.state = 343
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.lValue()
                self.state = 346
                self.assign()
                self.state = 347
                self.operation()
                self.state = 348
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
        self.enterRule(localctx, 44, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.lValue()
            self.state = 353
            self.match(grammarCParser.T__9)
            self.state = 354
            _la = self._input.LA(1)
            if not(_la==grammarCParser.DIGIT or _la==grammarCParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 355
            self.match(grammarCParser.T__10)
            self.state = 356
            self.assign()
            self.state = 357
            self.arrayOptions()
            self.state = 358
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
        self.enterRule(localctx, 46, self.RULE_arrayOptions)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(grammarCParser.T__7)
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 361
                        self.rValue()
                        self.state = 362
                        self.match(grammarCParser.T__6) 
                    self.state = 368
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 369
                self.rValue()
                self.state = 370
                self.match(grammarCParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(grammarCParser.T__7)
                self.state = 373
                self.match(grammarCParser.T__8)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
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
        self.enterRule(localctx, 48, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.ifStatement()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==grammarCParser.T__13:
                    self.state = 378
                    self.elifStatement()
                    self.state = 383
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__14:
                    self.state = 384
                    self.elseStatement()


                pass
            elif token in [grammarCParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.whileStatement()
                pass
            elif token in [grammarCParser.T__16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
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
        self.enterRule(localctx, 50, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(grammarCParser.T__12)
            self.state = 392
            self.match(grammarCParser.T__4)
            self.state = 393
            self.condition()
            self.state = 394
            self.match(grammarCParser.T__5)
            self.state = 395
            self.match(grammarCParser.T__7)
            self.state = 396
            self.body()
            self.state = 397
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
        self.enterRule(localctx, 52, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(grammarCParser.T__13)
            self.state = 400
            self.match(grammarCParser.T__4)
            self.state = 401
            self.condition()
            self.state = 402
            self.match(grammarCParser.T__5)
            self.state = 403
            self.match(grammarCParser.T__7)
            self.state = 404
            self.body()
            self.state = 405
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
        self.enterRule(localctx, 54, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(grammarCParser.T__14)
            self.state = 408
            self.match(grammarCParser.T__7)
            self.state = 409
            self.body()
            self.state = 410
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
        self.enterRule(localctx, 56, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(grammarCParser.T__15)
            self.state = 413
            self.match(grammarCParser.T__4)
            self.state = 414
            self.condition()
            self.state = 415
            self.match(grammarCParser.T__5)
            self.state = 416
            self.match(grammarCParser.T__7)
            self.state = 417
            self.body()
            self.state = 418
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
        self.enterRule(localctx, 58, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(grammarCParser.T__16)
            self.state = 421
            self.match(grammarCParser.T__4)
            self.state = 422
            self.forCondition()
            self.state = 423
            self.match(grammarCParser.T__5)
            self.state = 424
            self.match(grammarCParser.T__7)
            self.state = 425
            self.body()
            self.state = 426
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
        self.enterRule(localctx, 60, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.rValue()
                self.state = 429
                self.comparison()
                self.state = 430
                self.rValue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammarCParser.T__17:
                    self.state = 432
                    self.match(grammarCParser.T__17)


                self.state = 435
                self.rValue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.match(grammarCParser.T__17)
                self.state = 437
                self.match(grammarCParser.T__4)
                self.state = 438
                self.condition()
                self.state = 439
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
        self.enterRule(localctx, 62, self.RULE_forCondition)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21, grammarCParser.T__24, grammarCParser.T__27, grammarCParser.T__28, grammarCParser.T__29, grammarCParser.T__42, grammarCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.deel1()
                self.state = 444
                self.deel2()
                self.state = 445
                self.match(grammarCParser.T__18)
                self.state = 446
                self.deel3()
                pass
            elif token in [grammarCParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(grammarCParser.T__18)
                self.state = 449
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
        self.enterRule(localctx, 64, self.RULE_deel1)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
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
        self.enterRule(localctx, 66, self.RULE_deel2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
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
        self.enterRule(localctx, 68, self.RULE_deel3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
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
        self.enterRule(localctx, 70, self.RULE_operation)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.nextOperation()
                self.state = 462
                self.operator()
                self.state = 463
                self.nextOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.match(grammarCParser.T__4)
                self.state = 466
                self.operation()
                self.state = 467
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
        self.enterRule(localctx, 72, self.RULE_nextOperation)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.baseOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.baseOperation()
                self.state = 473
                self.operator()
                self.state = 474
                self.nextOperation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.match(grammarCParser.T__4)
                self.state = 477
                self.nextOperation()
                self.state = 478
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
        self.enterRule(localctx, 74, self.RULE_baseOperation)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.rValue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.rValue()
                self.state = 484
                self.operator()
                self.state = 485
                self.baseOperation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 487
                self.match(grammarCParser.T__4)
                self.state = 488
                self.baseOperation()
                self.state = 489
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
        self.enterRule(localctx, 76, self.RULE_plusplus)
        try:
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__25, grammarCParser.T__41, grammarCParser.DIGIT, grammarCParser.FLT, grammarCParser.STR, grammarCParser.BOOL, grammarCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.rValue()
                self.state = 494
                self.deincrement()
                pass
            elif token in [grammarCParser.T__39, grammarCParser.T__40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.deincrement()
                self.state = 497
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
        self.enterRule(localctx, 78, self.RULE_kw)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(grammarCParser.T__19)
                self.state = 502
                self.endStatement()
                pass
            elif token in [grammarCParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(grammarCParser.T__20)
                self.state = 504
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
        self.enterRule(localctx, 80, self.RULE_mainFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(grammarCParser.T__21)
            self.state = 508
            self.match(grammarCParser.T__22)
            self.state = 509
            self.match(grammarCParser.T__4)
            self.state = 510
            self.argListMain()
            self.state = 511
            self.match(grammarCParser.T__5)
            self.state = 512
            self.match(grammarCParser.T__7)
            self.state = 513
            self.body()
            self.state = 514
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
        self.enterRule(localctx, 82, self.RULE_argListMain)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammarCParser.T__21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(grammarCParser.T__21)
                self.state = 517
                self.match(grammarCParser.T__23)
                self.state = 518
                self.match(grammarCParser.T__6)
                self.state = 519
                self.match(grammarCParser.T__24)
                self.state = 520
                self.match(grammarCParser.T__25)
                self.state = 521
                self.match(grammarCParser.T__26)
                self.state = 522
                self.match(grammarCParser.T__9)
                self.state = 523
                self.match(grammarCParser.T__10)
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
        self.enterRule(localctx, 84, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
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
        self.enterRule(localctx, 86, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
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
        self.enterRule(localctx, 88, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
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
        self.enterRule(localctx, 90, self.RULE_deincrement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
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
        self.enterRule(localctx, 92, self.RULE_pointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
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
        self.enterRule(localctx, 94, self.RULE_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
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
        self.enterRule(localctx, 96, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
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
        self.enterRule(localctx, 98, self.RULE_endStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
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
        self.enterRule(localctx, 100, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
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
        self.enterRule(localctx, 102, self.RULE_rValue)
        self._la = 0 # Token type
        try:
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.match(grammarCParser.DIGIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.match(grammarCParser.FLT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 547
                self.match(grammarCParser.STR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 548
                self.match(grammarCParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 561
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 552
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__25:
                        self.state = 549
                        self.pointer()
                        self.state = 554
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 558
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__41:
                        self.state = 555
                        self.reference()
                        self.state = 560
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 563
                self.match(grammarCParser.ID)
                self.state = 564
                self.match(grammarCParser.T__9)
                self.state = 565
                _la = self._input.LA(1)
                if not(_la==grammarCParser.DIGIT or _la==grammarCParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 566
                self.match(grammarCParser.T__10)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 579
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 570
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__25:
                        self.state = 567
                        self.pointer()
                        self.state = 572
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass

                elif la_ == 2:
                    self.state = 576
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==grammarCParser.T__41:
                        self.state = 573
                        self.reference()
                        self.state = 578
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass


                self.state = 581
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
        self.enterRule(localctx, 104, self.RULE_lValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(grammarCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





