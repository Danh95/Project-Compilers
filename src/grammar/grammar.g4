Grammar C;

startExpression 
	:	Identifier
	|	Constant
	|	'('expression')'
	;

statement
	: 	
	;

types
	:	'int'
	|	'float'
	|	'char'
	|	'void'
	;

pointer
	:	types '*'
	;

keywords
	:	'continue'
	|	'break'
	|	'return'
	;

conditionals
	:	'if'
	|	'else'
	|	'while'
	|	'for'
	;

constant
	:	'const' types
	;

import
	:	'#include' library
	;

library
	: '<stdio.h>'
	;

functionDef
	:	types name '(' argumentlist ')'
	;

endStatement
	: ';'
	;

whitespace
    :   [ \t]+
        -> skip
    ;

newLine
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

blockComment
    :   '/*' .*? '*/'
        -> skip
    ;

lineComment
    :   '//' ~[\r\n]*
        -> skip
	;
