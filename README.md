# What is this repo

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
`git clone "https:github.com/josephmainadev/solving-coding-problems/"`
2. Change to the directory
`cd solving-coding-problems`
3. Run the Python files
`python -m digit-sum.py`
4. Edit the files to include your own tests, then run the files again.

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

```py
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
