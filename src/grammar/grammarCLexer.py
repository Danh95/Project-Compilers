# Generated from ./src/grammar/grammarC.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u0194\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write(".\6.\u0118\n.\r.\16.\u0119\3/\7/\u011d\n/\f/\16/\u0120")
        buf.write("\13/\3/\3/\6/\u0124\n/\r/\16/\u0125\3/\6/\u0129\n/\r/")
        buf.write("\16/\u012a\3/\3/\7/\u012f\n/\f/\16/\u0132\13/\3/\6/\u0135")
        buf.write("\n/\r/\16/\u0136\5/\u0139\n/\3\60\3\60\3\60\3\60\7\60")
        buf.write("\u013f\n\60\f\60\16\60\u0142\13\60\3\60\3\60\3\60\3\60")
        buf.write("\7\60\u0148\n\60\f\60\16\60\u014b\13\60\3\60\5\60\u014e")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0156\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u0163\n\62\3\63\3\63\7\63\u0167\n\63\f\63\16\63")
        buf.write("\u016a\13\63\3\64\6\64\u016d\n\64\r\64\16\64\u016e\3\64")
        buf.write("\3\64\3\65\3\65\5\65\u0175\n\65\3\65\5\65\u0178\n\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\7\66\u0180\n\66\f\66\16\66")
        buf.write("\u0183\13\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u018e\n\67\f\67\16\67\u0191\13\67\3\67\3\67\3")
        buf.write("\u0181\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8\3\2\t\3\2\62;\3\2))\3\2$$\4\2C\\c|\6\2\62;C\\aa")
        buf.write("c|\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2\u01ab\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5x\3\2\2\2\7")
        buf.write("z\3\2\2\2\t~\3\2\2\2\13\u0084\3\2\2\2\r\u0086\3\2\2\2")
        buf.write("\17\u0088\3\2\2\2\21\u008a\3\2\2\2\23\u008c\3\2\2\2\25")
        buf.write("\u008e\3\2\2\2\27\u0090\3\2\2\2\31\u0092\3\2\2\2\33\u0099")
        buf.write("\3\2\2\2\35\u009c\3\2\2\2\37\u00a4\3\2\2\2!\u00a9\3\2")
        buf.write("\2\2#\u00af\3\2\2\2%\u00b3\3\2\2\2\'\u00b5\3\2\2\2)\u00b7")
        buf.write("\3\2\2\2+\u00c0\3\2\2\2-\u00c6\3\2\2\2/\u00ca\3\2\2\2")
        buf.write("\61\u00cf\3\2\2\2\63\u00d4\3\2\2\2\65\u00d9\3\2\2\2\67")
        buf.write("\u00db\3\2\2\29\u00e0\3\2\2\2;\u00e6\3\2\2\2=\u00eb\3")
        buf.write("\2\2\2?\u00f0\3\2\2\2A\u00f2\3\2\2\2C\u00f4\3\2\2\2E\u00f6")
        buf.write("\3\2\2\2G\u00f8\3\2\2\2I\u00fa\3\2\2\2K\u00fd\3\2\2\2")
        buf.write("M\u0100\3\2\2\2O\u0103\3\2\2\2Q\u0106\3\2\2\2S\u0109\3")
        buf.write("\2\2\2U\u010c\3\2\2\2W\u010e\3\2\2\2Y\u0114\3\2\2\2[\u0117")
        buf.write("\3\2\2\2]\u0138\3\2\2\2_\u014d\3\2\2\2a\u0155\3\2\2\2")
        buf.write("c\u0162\3\2\2\2e\u0164\3\2\2\2g\u016c\3\2\2\2i\u0177\3")
        buf.write("\2\2\2k\u017b\3\2\2\2m\u0189\3\2\2\2op\7%\2\2pq\7k\2\2")
        buf.write("qr\7p\2\2rs\7e\2\2st\7n\2\2tu\7w\2\2uv\7f\2\2vw\7g\2\2")
        buf.write("w\4\3\2\2\2xy\7>\2\2y\6\3\2\2\2z{\7\60\2\2{|\7j\2\2|}")
        buf.write("\7@\2\2}\b\3\2\2\2~\177\7u\2\2\177\u0080\7v\2\2\u0080")
        buf.write("\u0081\7f\2\2\u0081\u0082\7k\2\2\u0082\u0083\7q\2\2\u0083")
        buf.write("\n\3\2\2\2\u0084\u0085\7*\2\2\u0085\f\3\2\2\2\u0086\u0087")
        buf.write("\7+\2\2\u0087\16\3\2\2\2\u0088\u0089\7.\2\2\u0089\20\3")
        buf.write("\2\2\2\u008a\u008b\7}\2\2\u008b\22\3\2\2\2\u008c\u008d")
        buf.write("\7\177\2\2\u008d\24\3\2\2\2\u008e\u008f\7]\2\2\u008f\26")
        buf.write("\3\2\2\2\u0090\u0091\7_\2\2\u0091\30\3\2\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095\7v\2\2\u0095\u0096")
        buf.write("\7w\2\2\u0096\u0097\7t\2\2\u0097\u0098\7p\2\2\u0098\32")
        buf.write("\3\2\2\2\u0099\u009a\7k\2\2\u009a\u009b\7h\2\2\u009b\34")
        buf.write("\3\2\2\2\u009c\u009d\7g\2\2\u009d\u009e\7n\2\2\u009e\u009f")
        buf.write("\7u\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7\"\2\2\u00a1\u00a2")
        buf.write("\7k\2\2\u00a2\u00a3\7h\2\2\u00a3\36\3\2\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8 \3\2\2\2\u00a9\u00aa\7y\2\2\u00aa\u00ab")
        buf.write("\7j\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\"\3\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7t\2\2\u00b2$\3\2\2\2\u00b3\u00b4")
        buf.write("\7#\2\2\u00b4&\3\2\2\2\u00b5\u00b6\7=\2\2\u00b6(\3\2\2")
        buf.write("\2\u00b7\u00b8\7e\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7")
        buf.write("p\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7g\2\2\u00bf*\3")
        buf.write("\2\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7m\2\2\u00c5,\3")
        buf.write("\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9.\3\2\2\2\u00ca\u00cb\7o\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\60")
        buf.write("\3\2\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7i\2\2\u00d2\u00d3\7e\2\2\u00d3\62\3\2\2\2\u00d4\u00d5")
        buf.write("\7e\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\64\3\2\2\2\u00d9\u00da\7,\2\2\u00da\66\3")
        buf.write("\2\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7i\2\2\u00de\u00df\7x\2\2\u00df8\3\2\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7v\2\2\u00e5:\3\2\2\2\u00e6\u00e7")
        buf.write("\7x\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7f\2\2\u00ea<\3\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7n\2\2\u00ef>\3")
        buf.write("\2\2\2\u00f0\u00f1\7-\2\2\u00f1@\3\2\2\2\u00f2\u00f3\7")
        buf.write("/\2\2\u00f3B\3\2\2\2\u00f4\u00f5\7\'\2\2\u00f5D\3\2\2")
        buf.write("\2\u00f6\u00f7\7\61\2\2\u00f7F\3\2\2\2\u00f8\u00f9\7@")
        buf.write("\2\2\u00f9H\3\2\2\2\u00fa\u00fb\7?\2\2\u00fb\u00fc\7?")
        buf.write("\2\2\u00fcJ\3\2\2\2\u00fd\u00fe\7>\2\2\u00fe\u00ff\7?")
        buf.write("\2\2\u00ffL\3\2\2\2\u0100\u0101\7@\2\2\u0101\u0102\7?")
        buf.write("\2\2\u0102N\3\2\2\2\u0103\u0104\7#\2\2\u0104\u0105\7?")
        buf.write("\2\2\u0105P\3\2\2\2\u0106\u0107\7-\2\2\u0107\u0108\7-")
        buf.write("\2\2\u0108R\3\2\2\2\u0109\u010a\7/\2\2\u010a\u010b\7/")
        buf.write("\2\2\u010bT\3\2\2\2\u010c\u010d\7(\2\2\u010dV\3\2\2\2")
        buf.write("\u010e\u010f\7e\2\2\u010f\u0110\7q\2\2\u0110\u0111\7p")
        buf.write("\2\2\u0111\u0112\7u\2\2\u0112\u0113\7v\2\2\u0113X\3\2")
        buf.write("\2\2\u0114\u0115\7?\2\2\u0115Z\3\2\2\2\u0116\u0118\t\2")
        buf.write("\2\2\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\\\3\2\2\2\u011b\u011d")
        buf.write("\t\2\2\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0121\u0123\7\60\2\2\u0122\u0124")
        buf.write("\t\2\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0139\3\2\2\2")
        buf.write("\u0127\u0129\t\2\2\2\u0128\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\u0130\7\60\2\2\u012d\u012f\t\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0139\3\2\2\2\u0132\u0130\3")
        buf.write("\2\2\2\u0133\u0135\t\2\2\2\u0134\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0139\3\2\2\2\u0138\u011e\3\2\2\2\u0138\u0128\3\2\2\2")
        buf.write("\u0138\u0134\3\2\2\2\u0139^\3\2\2\2\u013a\u014e\5a\61")
        buf.write("\2\u013b\u0140\7)\2\2\u013c\u013f\n\3\2\2\u013d\u013f")
        buf.write("\7$\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u014e\7")
        buf.write(")\2\2\u0144\u0149\7$\2\2\u0145\u0148\n\4\2\2\u0146\u0148")
        buf.write("\7)\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014c\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014e\7")
        buf.write("$\2\2\u014d\u013a\3\2\2\2\u014d\u013b\3\2\2\2\u014d\u0144")
        buf.write("\3\2\2\2\u014e`\3\2\2\2\u014f\u0150\7)\2\2\u0150\u0151")
        buf.write("\t\5\2\2\u0151\u0156\7)\2\2\u0152\u0153\7$\2\2\u0153\u0154")
        buf.write("\t\5\2\2\u0154\u0156\7$\2\2\u0155\u014f\3\2\2\2\u0155")
        buf.write("\u0152\3\2\2\2\u0156b\3\2\2\2\u0157\u0158\7v\2\2\u0158")
        buf.write("\u0159\7t\2\2\u0159\u015a\7w\2\2\u015a\u0163\7g\2\2\u015b")
        buf.write("\u0163\7\63\2\2\u015c\u015d\7h\2\2\u015d\u015e\7c\2\2")
        buf.write("\u015e\u015f\7n\2\2\u015f\u0160\7u\2\2\u0160\u0163\7g")
        buf.write("\2\2\u0161\u0163\7\62\2\2\u0162\u0157\3\2\2\2\u0162\u015b")
        buf.write("\3\2\2\2\u0162\u015c\3\2\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("d\3\2\2\2\u0164\u0168\t\5\2\2\u0165\u0167\t\6\2\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169f\3\2\2\2\u016a\u0168\3\2\2")
        buf.write("\2\u016b\u016d\t\7\2\2\u016c\u016b\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0171\b\64\2\2\u0171h\3\2\2\2\u0172")
        buf.write("\u0174\7\17\2\2\u0173\u0175\7\f\2\2\u0174\u0173\3\2\2")
        buf.write("\2\u0174\u0175\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0178")
        buf.write("\7\f\2\2\u0177\u0172\3\2\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("\u0179\3\2\2\2\u0179\u017a\b\65\2\2\u017aj\3\2\2\2\u017b")
        buf.write("\u017c\7\61\2\2\u017c\u017d\7,\2\2\u017d\u0181\3\2\2\2")
        buf.write("\u017e\u0180\13\2\2\2\u017f\u017e\3\2\2\2\u0180\u0183")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7,\2\2")
        buf.write("\u0185\u0186\7\61\2\2\u0186\u0187\3\2\2\2\u0187\u0188")
        buf.write("\b\66\2\2\u0188l\3\2\2\2\u0189\u018a\7\61\2\2\u018a\u018b")
        buf.write("\7\61\2\2\u018b\u018f\3\2\2\2\u018c\u018e\n\b\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0192\u0193\b\67\2\2\u0193n\3\2\2\2\27\2\u0119")
        buf.write("\u011e\u0125\u012a\u0130\u0136\u0138\u013e\u0140\u0147")
        buf.write("\u0149\u014d\u0155\u0162\u0168\u016e\u0174\u0177\u0181")
        buf.write("\u018f\3\b\2\2")
        return buf.getvalue()


class grammarCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    DIGIT = 45
    FLT = 46
    STR = 47
    CHAR = 48
    BOOL = 49
    ID = 50
    WS = 51
    NL = 52
    BC = 53
    LC = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#include'", "'<'", "'.h>'", "'stdio'", "'('", "')'", "','", 
            "'{'", "'}'", "'['", "']'", "'return'", "'if'", "'else if'", 
            "'else'", "'while'", "'for'", "'!'", "';'", "'continue'", "'break'", 
            "'int'", "'main'", "'argc'", "'char'", "'*'", "'argv'", "'float'", 
            "'void'", "'bool'", "'+'", "'-'", "'%'", "'/'", "'>'", "'=='", 
            "'<='", "'>='", "'!='", "'++'", "'--'", "'&'", "'const'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "DIGIT", "FLT", "STR", "CHAR", "BOOL", "ID", "WS", "NL", "BC", 
            "LC" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "DIGIT", "FLT", "STR", "CHAR", "BOOL", "ID", "WS", "NL", 
                  "BC", "LC" ]

    grammarFileName = "grammarC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


