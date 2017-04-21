grammar grammarC;


program
	:	libraryList funcDefList
	;

libraryList
	:	library libraryList
	|
	;

library
	:	'#include' lib
	;

lib
	:	'<' libname '.h>'
	;

libname
	:	'stdio'
	|	ID
	;

funcDefList
	:	funcDef funcDefList
	|
	;

funcDef
	:	types ID '(' argList ')' '{' body '}' endStatement
	;

argList
	:	(types ID ',')*(types ID)
	|
	;

body
	:	statements
	;

statements
	:	statement statements
	|
	;
	
statement
	:	declaration
	|	definition
	|	functionCall
	|	assignment	
	|	conditional
	|	operation endStatement
	|	returnStatement
	|	kw
	;

returnStatement
	:	'return' functionCall
	|	'return' condition endStatement
	|	'return' lit endStatement
	|	'return' ID endStatement
	|	'return' operation endStatement
	|	'return' endStatement
	;

parList
	:	((lit|ID) ',')*(lit|ID)
	|
	;

declaration
	:	constant? types pointer* ID endStatement
	|	constant? types pointer* ID '[' (DIGIT | ID) ']' endStatement	
	|	constant? types '(' pointer+ ID ')' '[' (DIGIT | ID) ']' endStatement
	;


definition
	:	constant? types pointer* assignment
	;

functionCall
	:	ID '(' parList ')' endStatement
	;

assignment
	: normalAssignment
	| arrayAssignment
	;

normalAssignment
	:	ID assign lit endStatement
	|	ID assign ID endStatement
	|	ID assign functionCall
	|	ID assign operation endStatement
	;

arrayAssignment
	:	ID '[' (DIGIT | ID) ']' assign '{' ((lit | ID) ',')* (lit | ID)? '}' endStatement 
	|	ID '[' (DIGIT | ID) ']' assign '{' '}' endStatement
	|	ID '[' (DIGIT | ID) ']' assign (lit | ID) endStatement
	;

conditional
	:	'if' '(' condition ')' '{' body '}'  ('else' '{' body '}')?
	|	'while' '(' condition ')' '{' body '}'
	|	'for' '(' forCondition ')' '{' body '}'
	;

condition
	:	ID comparison ID
	|	ID comparison lit
	|	BOOL
	;

forCondition
	:	deel1 deel2 ';' deel3
	|	';' ';' 
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
	:	ID operator ID
	|	ID operator lit
	|	lit operator lit
	|	operation operator ID
	|	operation operator lit
	|	ID deincrement
	|	deincrement ID
	;

kw
	:	'continue' endStatement	
	|	'break' endStatement
	;

//mainFunc
	//:	'int' 'main' '(' argListMain ')' '{' body '}'
	//;

//argListMain
	//:	'int' 'argc' ',' 'char' '*' 'argv' '[' ']'
	//|
	//;

types
	:	'int'
	|	'float'
	|	'char'
	|	'void'
	;

operator
	:	'+'
	|	'-'
	|	'%'
	|	'*'
	|	'/'
	;

comparison
	:	'<'
	|	'>'
	|	'=='
	|	'<='
	|	'>='
	;

deincrement
	:	'++'
	|	'--'
	;

pointer
	:	'*'
	;

constant
	:	'const'
	;

endStatement
	:	';'
	;

assign
	:	'='
	;

lit		//literal
	:	DIGIT
	|	FLT 
	|	STR
	|	BOOL
	;


DIGIT
	:	[0-9]+
	;

FLT
	:	[0-9]*'.'[0-9]+
	|	[0-9]+'.'[0-9]*
	;

STR
	:	'\'' [a-zA-Z][a-zA-Z]+ '\''
	|	CHAR	
	;

CHAR
	:	'\'' [a-zA-Z] '\''
	;

BOOL
	:	'true'
	|	'false'
	;

ID
	:	[a-zA-Z]([a-zA-Z0-9_])*
	;

WS		//whiteSpace
    :   [ \t\r\n]+
        -> skip
    ;

NL		//newLine
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

BC		//blockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LC		//lineComment
    :   '//' ~[\r\n]*
        -> skip
	;

