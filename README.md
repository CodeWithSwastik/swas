# The Swas programming language
This is a language that was made for fun. It is completely written in python. <br>

`Latest Version: 1.8.3`

# Installation

Stable Release: `pip install swas` <br>
Working Version: `pip install git+https://github.com/CodeWithSwastik/swas.git`

This is all that you need to do to start writing in swas lang.

# Running 
```
python -m swas [filename]
```
The filename is optional, if no filename is provided it will run the shell.

# Online IDE 
If you don't want to use swas on your local machine you can try it out on the Online IDE: https://codewithswastik.github.io/swas/

# Getting Started

## Hello World
```js
output "Hello, World!"
```

## Variables
Variables are containers for storing data.

### Creating Variables
Swas has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

```js
x = 5
y = "Mark"
```

### Using Variables
To use the variables, simply reference them

```js
output x
output y
```

### Case Sensitive 
Note: Variables names are case sensitive i.e. `a = 5` is not the same as `A = 5`

## Comments
A Comment starts with a //, and anything after them will be ignored:
```js
//This is a comment
output "Hello, World!"
```


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
| ^        | Exponent       | x ^ y   |

### Logical Operators
| Operator | Name                     | Example |
|----------|--------------------------|---------|
| ==       | Equals                   | x == y  |
| !=       | Not Equals               | x != y  |
| >        | Greater than             | x > y   |
| >=       | Greater than or equal to | x >= y  |
| <        | Lesser than              | x < y   |
| <=       | Lesser than or equal to  | x <= y  |



### The Assignment Operator ( = )
The Assignment Operator ( = ) is used to assign a variable to a value.


### If Else 
An "if else statement" is written by using the if and else keywords.

Syntax
```cpp
if condition {
  statement 
}
else {
  statement 
}
```
Note: The indentation isn't needed, it has been used here for readability

Example
```cpp
name = input "Enter your name: "
if name == "John" {
  output "hi," + name 
}
else {
  output "bye," + name 
}
```

### While Do
With the while loop you can execute a set of statements as long as a condition is true.

Syntax
```cpp
while condition 
do {
  statement
}
```

Note: The indentation isn't needed, it has been used here for readability

Example
```cpp
start = 1 
end = 10 

while start != end
do {
  output start
  inc start 
}
```

## Data Types

### Lists/Arrays
List/Array is a data structure consisting of a collection of values or variables. A list can be created using square brackets ([])

Example
```cpp
list = [1,2,3,4,5]
```
