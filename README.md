# The Swas programming language
This is a language that was made for fun.

# Installation
Step 0: Make sure you have python installed <br>
Step 1. Clone this repo or download it as a zip <br>
Step 2. Run `pip install -r requirements.txt`

This is all that you need to do to start writing in swas lang.

# Running 
```bash
python -m swas [filename]
```
The filename is optional, if no filename is provided it will run the shell.

# Getting Started

## Hello World
```
output "Hello, World!"
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
output x
output y
```

### Case Sensitive 
Note: Variables names are case sensitive i.e. `a => 5` is not the same as `A => 5`

## Operators
Operators are used to perform operations on variables and values.

### Arithmetic Operators

| Operator | Name           | Example |
|----------|----------------|---------|
| +        | Addition       | x + y   |
| -        | Subtraction    | x - y   |
| *        | Multiplication | x * y   |
| /        | Division       | x / y   |
| %        | Modulus        | x % y   |
| inc      | Increment      | inc x   |
| dec      | Decrement      | dec x   |

### Logical Operators
| Operator | Name                     | Example |
|----------|--------------------------|---------|
| ==       | Equals                   | x == y  |
| !=       | Not Equals               | x != y  |
| >        | Greater than             | x > y   |
| >=       | Greater than or equal to | x >= y  |
| <        | Lesser than              | x < y   |
| <=       | Lesser than or equal to  | x <= y  |


### Join Operator ( & )
The Join Operator ( & ) lets you join 2 statements into 1. 

Example
```
output "Hi" & output "Bye"
```

### The Assignment Operator ( => )
The Assignment Operator ( => ) is used to assign a variable to a value.


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
name => "John" &
if name == "John" =>
  output "hi " + name
else =>
  output "bye " + name
```

### While Do
With the while loop you can execute a set of statements as long as a condition is true.

Syntax
```
while condition 
do
  statement
```

Note: The indentation isn't needed, it has been used here for readability

Example 
```
ignore This Program outputs numbers from 1 to 10
start => 1 &
end => 10 &
while start != end
do 
  output start & inc start 
```
