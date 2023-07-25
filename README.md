# How to Solve Coding Problems


This repo has the solutions for two exercises that appear on a blog post I wrote [link to blog post].

In the post, I show you the steps you should follow when attempting to solve coding problems.

The solutions come in two forms:

1. Pseudocode for the algorithm that solves each problem
2. Python code for each solution

If you are learning how to code, and how to solve coding problems, please try them out on your own first before looking at my suggested solutions. That way you learn better as opposed to copying a solution.

**Caution**: The solutions suggested in this guide might not be the most optimal. Nor elegant. This guide just gives you a starting point to have a working piece of code. Then figure the rest on your own.

## Running the code

To run the python code locally in your machine, run each of the following commands in terminal:

1. Run the following command in terminal to clone the repo

    `git clone "https://github.com/JosephMainaDev/solving-coding-problems.git"`

1. Change to the directory

    `cd solving-coding-problems`

1. Run the Python files

    `python digit-sum.py`

1. Edit the files to include your own tests, and run them.

## Solution

### Exercise one

This is the first exercise on that post:

> Write a program that receives an alphanumeric string and prints the sum of the numeric digits in the string.

And this an example of the how the program you come up with is expected to do:

```bash
    >>> numericSum("h3l1o w07ld!")
    >>> 11
```

### Pseudocode for exercise one

The algorithm should follow these steps to solve the problem. Generally, there are no hard rules on how to write pseudocode. You can do it my way, or a different way. The idea is to be able to figure out the steps in your head so that you have a blueprint to follow when writing out the code. You may have to rewrite the pseudocode several times over. (I do this best with a pen and a piece of paper.)

```txt
Iterate through the string
For each character in the string
Check the type of the character
    If the character is a number
        Increment the total with the number
  
    Otherwise skip the character

Return the total
```

### Code for exercise one

The solution in Python code. You can rewrite the code in your favorite language.

```py
def numericSum(string):
    # Track the total
    total = 0
    for char in string:
        # The characters in the string are also of type string.
        # To tell whether a character is a number, try converting it to an integer.
        try:
            char = int(char)
        # If it cannot be converted to an integer, it is not a number.
        # Skip the character.
        except TypeError:
            pass
        # If the character was successfully converted to an integer, add it to the total.
        total += char
    
    return total
```

### Exercise two

Here is the second exercise:

> Given a list of a pair of points on a Cartesian plane, write a program that returns true if the points are on a straight line, and false otherwise.

```bash
    >>> straight([(1,2), (2,3), (3,4), (4,5)])
    >>> True

    >>> straight([(1,2), (2,3), (3,4), (4,8)])
    >>> False
```

### Pseudocode for exercise two

Before I give you the algorithm for solving this problem, let's first do a bit of math.

What do we know about points on a straight line? When I researched this problem, the most _interesting_ way I found to solve it is:

- You need at least three points on the line
- If the three points form a triangle, the points are not on a straight line.
- To check whether a triangle is formed compute the area.
  - A triangle has non-zero area
  - A line has area equal to zero

To compute the area of a triangle on a Cartesian plane, you can use the formula:

With that out of the way, my algorithm goes like this:

```txt
Iterate over the points on the line
Grab 3 points at a time
Compute area using the three points
    If the area is non-zero
        Return false, the three points formed a triangle

    Otherwise it is a straight line
        Return true

```

### Code for exercise two

