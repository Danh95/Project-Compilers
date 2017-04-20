grammar grammarC;


program
	:	library* funcDef* mainFunc
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

funcDef
	:	types ID '(' argList ')' '{' body '}' endStatement
	;

argList
	:	(types ID ',')*(types ID)
	|
	;

body
	:	statement*
	;

statement
	:	functionCall
	|	declaration
	//|	definition
	//|	assignment	
	//|	conditional
	//|	operation
	//|	returnStatement
	//|	KW endStatement
	;

returnStatement
	:	'return' functionCall
	|	'return' condition	endStatement
	|	'return' LIT endStatement
	|	'return' ID endStatement
	|	'return' endStatement
	;

functionCall
	:	ID '(' parList ')' endStatement
	;

parList
	:	(ID ',')*(ID)
	|
	;

EQ
	: '='
	;

deincrement
	:	'++'
	|	'--'
	;

LIT		//literal
	:	INT
	|	FLOAT
	|	STR
	;

declaration
	:	constant? types pointer* ID endStatement
	|	constant? types pointer* ID '[' (INT | ID) ']' endStatement	
	//|	constant? types '(' pointer+ ID ')' '[' (INT | ID) ']' endStatement
	;

definition
	:	constant? types pointer* assignment
	;

assignment
	: normalAssignment
	| arrayAssignment
	;

normalAssignment
	:	ID EQ LIT endStatement
	|	ID EQ ID endStatement
	|	ID EQ functionCall
	|	ID EQ operation endStatement
	;

arrayAssignment
	:	ID '[' LIT ']' EQ '{' ((LIT | ID) ',')* (LIT | ID)? '}' endStatement 
	|	ID '[' LIT ']' EQ '{' '}' endStatement
	|	ID '[' LIT ']' EQ (LIT | ID) endStatement
	;

conditional
	:	'if' '(' condition ')' '{' body '}'  ('else' '{' body '}')?
	|	'while' '(' condition ')' '{' body '}'
	|	'for' '(' forCondition ')' '{' body '}'
	;

condition
	:	ID comparison ID
	|	ID comparison LIT
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
	:	ID operator ID
	|	ID operator LIT
	|	LIT operator LIT
	|	operation operator ID
	|	operation operator LIT
	|	ID deincrement endStatement
	|	deincrement ID endStatement
	;

operator
	:	'+'
	|	'-'
	|	'%'
	|	'*'
	|	'/'
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

constant
	:	'const'
	;

endStatement
	:	';'
	;

mainFunc
	:	'int' 'main' '(' argListMain ')' '{' body '}'
	;

argListMain
	:	'int' 'argc' ',' 'char' '*' 'argv' '[' ']'
	|
	;

INT
	:	[0-9]+
	;

FLOAT
	:	[0-9]*.[0-9]+
	|	[0-9]+.[0-9]*
	;

STR
	:	'\'' [a-zA-Z][a-zA-Z]+ '\''
	|	CHAR	
	;

CHAR
	: '\'' [a-zA-Z] '\''
	;

VALUE
	:	LIT
	|	STR
	;
KW
	:	'continue'			
	|	'break'
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

