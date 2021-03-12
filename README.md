# The Swas programming language
This is a language that was made for fun.

# Installation
Step 1. Clone this repo or download it as a zip <br>
Step 2. Run `pip install -r requirements.txt`

This is all that you need to do to start writing in swas lang.

# Running 
```bash
python swas.py [filename]
```
The filename is optional, if no filename is provided it will run the shell.

# Getting Started

## Hello World
```
upload "Hello, World!"
```

## Variables
Variables are containers for storing data.

### Creating Variables
Swas has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

```
x => 5
y => "Mark"
```

### Using Variables
To use the variables, simply reference them

```
upload x
upload y
```

### Case Sensitive 
Note: Variables names are case sensitive i.e. `a => 5` is not the same as `A => 5`

## Operators
Operators are used to perform operations on variables and values.

| Operator | Name           | Example |
|----------|----------------|---------|
| +        | Addition       | x + y   |
| -        | Subtraction    | x - y   |
| *        | Multiplication | x * y   |
| /        | Division       | x / y   |
| %        | Modulus        | x % y   |
| ==       | Equality       | x == y  |
| inc      | Increment      | inc x   |
| dec      | Decrement      | dec x   |

### Join Operator ( &&& )
The Join Operator ( &&& ) lets you join 2 statements into 1. 

Example
```
upload "Hi" &&& upload "Bye"
```

### If Else
An "if else statement" is written by using the if and else keywords.

Syntax
```
if condition => 
  statement
else =>
  statement
```
Note: The indentation isn't needed, it has been used here for readability

Example
```
name => "John" &&&
if name == "John" =>
  upload "hi " + name
else =>
  upload "bye " + name
```
