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
	|   funcDecl funcDefList
	|	mainFunc
	|
	;

funcDecl
    :   types pointer lValue '(' typeList ')' endStatement
    ;

typeList
    :   (types (lValue)? ',')*(types (lValue)?)
    |
    ;

funcDef
	:	types lValue '(' argList ')' '{' body '}'
	;

argList
	:	(types lValue ',')*(types lValue)
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
	|   plusplus
	|	kw
	;

returnStatement
	:	'return' functionCall
	|	'return' rValue endStatement
	|	'return' condition endStatement
	|	'return' operation endStatement
	|	'return' endStatement
	;

parList
	:	(rValue ',')*(rValue)
	|
	;

declaration
	:	constant? types (pointer* | reference*) lValue endStatement
	|	constant? types pointer* lValue '[' (DIGIT | ID) ']' endStatement	
	|	constant? types '(' pointer+ lValue ')' '[' (DIGIT | ID) ']' endStatement
	;


definition
	:	constant? types (pointer* | reference*) assignment
	;

functionCall
	:	lValue '(' parList ')' endStatement
	;

assignment
	: normalAssignment
	| arrayAssignment
	;

normalAssignment
	:	lValue assign rValue endStatement
	|	lValue assign functionCall
	|	lValue assign operation endStatement
	;

arrayAssignment
	:	lValue '[' (DIGIT | ID) ']' assign arrayOptions endStatement
	|	lValue '[' (DIGIT | ID) ']' assign arrayOptions endStatement
	|	lValue '[' (DIGIT | ID) ']' assign arrayOptions endStatement
	;

arrayOptions
    :   '{' (rValue ',')* (rValue)? '}'
    |   '{' '}'
    |   rValue
    ;

conditional
	:	ifStatement (elifStatement)* (elseStatement)?
    |   whileStatement
    |	loop
	;

ifStatement
    :   'if' '(' condition ')' '{' body '}'
    ;

elifStatement
    :   'else if' '(' condition ')' '{' body '}'
    ;

elseStatement
    :   'else' '{' body '}'
    ;

whileStatement
    :   'while' '(' condition ')' '{' body '}'
    ;

loop
    :   'for' '(' forCondition ')' '{' body '}'
    ;

condition
	:	rValue comparison rValue
	|	'!'? rValue
	|	condition ('&&' | '||') condition
	| 	'!' '(' condition ')'
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
	:	rValue operator rValue
	|	rValue operator operation
	|   '(' operation ')'
    |   '(' operation ')' operator operation
    |   '(' operation ')' operator rValue
	;

plusplus
    :   rValue deincrement
	|	deincrement rValue
	;

kw
	:	'continue' endStatement	
	|	'break' endStatement
	;

mainFunc
	:	'int' 'main' '(' argListMain ')' '{' body '}'
	;

argListMain
	:	'int' 'argc' ',' 'char' '*' 'argv' '[' ']'
	|
	;

types
	:	'int'
	|	'float'
	|	'char'
	|	'void'
	|   'bool'
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
	|   '!='
	;

deincrement
	:	'++'
	|	'--'
	;

pointer
	:	'*'
	;

reference
	: '&'
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

rValue		//literal
	:	DIGIT
	|	FLT 
	|	STR
	|	BOOL
	|	ID
	;

lValue
	:	ID
	;

DIGIT
	:	'-'?[0-9]+
	;

FLT
	:	'-'?[0-9]*'.'[0-9]+
	|	'-'?[0-9]+'.'[0-9]*
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

