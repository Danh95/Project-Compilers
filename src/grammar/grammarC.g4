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

ID
	:	[a-zA-Z]([0-9]|[a-zA-Z])*
	;

funcDef
	:	types ID '(' argList ')' '{' body '}' endStatement
	;

argList
	:	(types ID ',')*(types ID)
	|
	;

body
	:	statement* 'return' types ? ID
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
	:	ID '(' parList ')' endStatement
	;

parList
	:	(ID ',')*(ID)
	|
	;

assignment
	:	ID '=' operation endStatement
	|	ID '=' functionCall endStatement
	|	ID '=' LIT endStatement
	|	ID '=' ID endStatement
	|	ID deincrement endStatement
	|	deincrement ID endStatement
	;

deincrement
	:	'++'
	|	'--'
	;

LIT		//literal
	:	[0-9][0-9]*
	;

declaration
	:	constant? types pointer* ID endStatement	
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
	:	'int main(' argListMain ')' '{' body '}' endStatement
	;

argListMain
	: 'int argc, char *argv[]'
	|
	;

KW
	:	'continue;' 
	|	'break;' 
	|	'return;'
	;

WS		//whiteSpace
    :   [ \t]+
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

