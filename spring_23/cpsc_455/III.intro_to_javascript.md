# History of JS
Created by Brendan Eich as a built in scripting language in the Netscape bowser. IE shipped a nearly identical version JScript. ECMA international accepted JavaScript as the ECMASript standard. Initially JS was more like Lisp, however early users complained that it was not like Java so changes were made. 

Frontend Javacript only executes inside of the browser, however backend Javascript rund in a runtime like Node.js which can access filesystems, hardware, and other low level resources.
Node.js has a REPL, or read-evaluate-print-loop, which accepts and executes javascript statements, executes them, and outputs the results.

Two types of variables in primitives and objects. functions are first class values in javascript and internally are treated as callable objects. parseInt will parse until it encounters the first invalid character, given the base. The second, optional argument to parseInt specifies the base. 
Any number that begins with 0 padding will be interpreted as octal.

The result of an operation in which NaN is an operand, or a part of an operand, will always be NaN. Bad apples. The most reliable way to check for NaN is to use the built-in isNaN function. Division by 0 will result in the builtIn Infinty value( - Infinty if the numerand was negative, or we divided by -0). parseFloat is similar to parseInt, but for floats.

Javascript strings are encoded using UTF-16. UTF-16 charachters are 2 bytes long. All strings are null-terminated, and the null-terminator is also 2 bytes long. Javascript strings are immutable. Therefore if we want to modify them, internally javascript creates a new instance of the string, modify it, and assign it to the reference for the original string. Prevents race conditions. In fact all javascript primitives are immutable. Values can be truthy or falsy, and are evaluated according to their value of that property when passed to conditional statements.

Variables can be devlared with let, const, or var keywords to denote their scope and mutability. let is used to declare blockscoped variables, while const is used to declare block-scoped immutable values. Var variables are hoisted to the topof the scope and so can potentially be read before they are initialized. This can create a myriad of issues, which makes var a bad practice. var variables are only not hoisted when declared iniside of functions, within each function it is hoisted to the top of the function scope.
The plus operator applied to strings results in string concatenation, wehn you add a string to an integer, everything is implicitly cast as a string: `'3' + 4 + 5 = '345'`.  There are two types of comparison operators: `==` and `===`. == first performs a type conversion then compares, while === just performs a strict comparison. For comparison operators > and < there is always type conversion. There are also bitwise operators, however there is no shift operators.
Short circuiting logic refers to how compilers and interpreters parse compound statements, specifically in which they decide to evaulate only as many of the statements until the statement is either false or completes.
Javascript objects are collections of name-value pairs. They resemble dictionaries in Python, Hashes in Perl and Ruby, Has tables in C/c++, hashmaps in java, and associative arrays in php. You can access values in an object using either dot notation or bracket notation. Bracket notation allows us to access vlaues using string key values.
You can create an instance of an object from prototype using a function constructor:
```javascript
fucntion Person(name, age) {
	this.name = name;
	this.age = age;
}

let you = new Person('you', 24);
```

A javacript fucntion is an object with an execuable part. During its execution this references the newly created object inside the Person function. this.name and this.age set the new objects keys of that name to the values passed to the function. Whenever you set a variable equal to an object you are setting it to the reference to that object so any changes to the original object will propagate to the assigned reference so long as they are coupled. The only way to make a deep copy is to create a new instance of the object.

Every function has a property called arguments that stores all the params passed to the function. Functions in js are objects so they can be passed as args to other functions. Functions can be anonymous as long as there is a refernce to them. 

Every object has a prototype which specifies what properties are defined on instances of that object. By adding methods to the prototype instead of the constructor we make our memory use more efficient because the fucntion code is not duplicated with every instance of the class.