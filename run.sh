#!/bin/sh
java -jar ./src/grammar/antlr-4.7-complete.jar -Dlanguage=Python3 ./src/grammar/grammarC.g4 -visitor
python3 ./src/parser.py ./src/test/test1.c
python3 ./src/parser.py ./src/test/test2.c
python3 ./src/parser.py ./src/test/test3.c
python3 ./src/parser.py ./src/test/test4.c
python3 ./src/parser.py ./src/test/test5.c
python3 ./src/parser.py ./src/test/test6.c
