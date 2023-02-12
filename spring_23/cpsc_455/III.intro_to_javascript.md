# History of JS
Created by Brendan Eich as a built in scripting language in the Netscape bowser. IE shipped a nearly identical version JScript. ECMA international accepted JavaScript as the ECMASript standard. Initially JS was more like Lisp, however early users complained that it was not like Java so changes were made. 

Frontend Javacript only executes inside of the browser, however backend Javascript rund in a runtime like Node.js which can access filesystems, hardware, and other low level resources.
Node.js has a REPL, or read-evaluate-print-loop, which accepts and executes javascript statements, executes them, and outputs the results.

Two types of variables in primitives and objects. functions are first class values in javascript and internally are treated as callable objects. parseInt will parse until it encounters the first invalid character, given the base. The second, optional argument to parseInt specifies the base. 
Any number that begins with 0 padding will be interpreted as octal.

The result of an operation in which NaN is an operand, or a part of an operand, will always be NaN. Bad apples. The most reliable way to check for NaN is to use the built-in isNaN function. Division by 0 will result in the builtIn Infinty value( - Infinty if the numerand was negative, or we divided by -0). parseFloat is similar to parseInt, but for floats.

Javascript strings are encoded using UTF-16. UTF-16 charachters are 2 bytes long. All strings are null-terminated, and the null-terminator is also 2 bytes long. Javascript strings are immutable. Therefore if we want to modify them, internally javascript creates a new instance of the string, modify it, and assign it to the reference for the original string. Prevents race conditions. In fact all javascript primitives are immutable. Values can be truthy or falsy, and are evaluated according to their value of that property when passed to conditional statements.

Variables can be devlared with let, const, or var keywords to denote their scope and mutability. let is used to declare blockscoped variables, while const is used to declare block-scoped immutable values. 
