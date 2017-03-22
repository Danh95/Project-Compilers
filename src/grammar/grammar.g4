Grammar C;

Program
	:	import* function* main

import
	:	'#include' library
	;

library
	: 	'<' filename '.h>'
	;

filename
	:	'stdio'
	|	Identifier
	;

identifier
	:	[a-zA-Z]([0-9] | [a-zA-Z])*
	;

function	//function definition
	:	types identifier '(' argList ')' '{' body '}' endStatement
	;

argList
	:	(types identifier ',')*(types identifier)
	|	
	;

endStatement
	:	';'
	;


statement
	:	functionCall
	|	assignment
	|	declaration
	|	definition	
	|	conditional
	|	operation
	;

functionCall
	:	identifier '(' parList ')' endStatement
	;

parList
	:	(identifier ',')*(identifier)
	|
	;

assignment
	:	identifier '=' operation endStatement
	|	identifier '=' functionCall endStatement
	|	identifier '=' literal endStatement
	|	identifier '=' identifier endStatement
	|	identifier deincrement endStatement
	|	deincrement identifier endStatement
	;

deincrement
	:	'++'
	|	'--'
	;

literal
	:	[0-9]*
	;

declaration
	:	constant? types pointer* identifier endStatement	
	;

definition
	:	constant? types pointer* assignment  
	;

conditional
	:	'if' '(' condition ')' '{' body '}'  ('else' '{' body '}')?
	|	'while' '(' condition ')' '{' body '}'
	|	'for' '(' forCondition ')' '{' body '}'
	;

condition
	:	Identifier comparison Identifier
	|	Identifier comparison literal
	;

comparison
	:	'<'
	|	'>'
	|	'=='
	|	'<='
	|	'>='
	;

forCondition
	:	deel1 ';' deel2 ';' deel3
	|	' ; ; ' 
	;

deel1
	: 	declaration
	|	definition
	|	assignment
	;

deel2
	:	condition
	;

deel3
	:	operation
	;

operation
	:	identifier operator identifier
	|	identifier operator literal
	|	literal operator literal
	|	operation operator identifier
	|	operation operator literal	
	;

operator
	:	'+'
	|	'-'
	|	'%'
	|	'*'
	|	'/'
	;
	
body
	:	statement* 'return' types ? Identifier	
	;

types
	:	'int'
	|	'float'
	|	'char'
	|	'void'
	;

pointer
	:	'*'
	;

keywords
	:	'continue' endStatement
	|	'break' endStatement
	|	'return' endStatement
	;

constant
	:	'const'
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
