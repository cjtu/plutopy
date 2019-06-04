# Using docstrings to document functions in Python

In this tutorial, you will learn:
- Why using functions is good practice
- How define a simple function in python
- How to get help when using python functions
- What docstrings are
- How to document your functions using docstrings
- How to write an informative docstring

___

## Functions

If you are already familiar with functions in python, you can skip this section and go straight to the docstrings! If you are not familiar with functions,
[this website offers additional examples and explanations](https://www.w3schools.com/python/python_functions.asp "Python Function Examples") of functions in Python.


### What is a Function?

Simply put, functions are sections of code that are run when they are called. This means that you can write the code for a function in one place and actually run it in another. Another advantage of functions is that you can run them multiple times in different places and with different inputs, thus saving many lines of code. Functions are an effective practice for making your code shorter, simpler, and easier to understand when implemented properly. 

Some real examples of functions I have written for my own scientific work are:
- A function that takes a temperature and a wavelength and returns the spectral density at that wavelenght according to Planck's formula for blackbody radiation
- A function that takes a spectrum and a wavelength and normalizes the spectrum to 1 at that wavelength
- A function that takes in a list of data and a sigma value and returns that data with outliers rejected according to the sigma level given
- A function that queries the Vizier catalog and returns the data in a format I want

### How do I define a Function?

Here is a simple example: 

```python
def square(x):
    return x**2

print(square(2))
print(square(3))
```

If you run this example in python, it should print the number 4, then the number 9. Here is how it works, line by line:
1. I define the function with `def` and name the function `square`. Inside the parentheses, I give the function one input, `x`. Then, I put the colon `:` to tell python to expect an indented block with the function definition inside. 
2. I use `return` to specify what the function should output when it is called, in this case, it returns `x**2`, the square of the input `x`
3. I left this line blank for style reasons--to separate my function from the rest of the code
4. I call the function `square` using the input `2`, using `square(2)` and wrap this in a `print()` call so I can see the output
5. Similarly, I call the function `square` using the input `3`, using `square(3)` and wrap this in a `print()` call so I can see the output

In general, a function is defined like this:

```python
def function_name(inputs, separated, by, commas):
    # code that turns your inputs 
    # into something you want to output
    return output
```

### Understanding unfamiliar functions

Often in scientific work, there are functions that other people have written and are available to us to use in our own code, but we don't know how to implement them (for instance,  mathematical functions in `numpy` and `scipy` modules or plotting functions in the `matplotlib` module). Fortunately, python has a built in way to get help on unfamiliar functions: the `help()` function!

For instance, take the built in function `len`. If we don't know what this function does, we can simply put the name of the function into the `help()` function and get some useful information about it. Running

```python
help(len)
```

returns

```
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

This tells us that `len` is a built in function that comes with python, and that it takes one input (an object) and returns the number of items in that container object. 

`help()` also works on other objects, such as variables, which can be useful if you aren't sure what a particular variable is. For instance:

```python
x = [1, 2]
help(x)
```

tells us that `x` is a list, and gives us all sorts of information about the sorts of methods and functions that can be used with lists (since the output for this example is long, I've truncated it): 

```
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 
...

 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

```

___

## Docstrings

What happens if you write a function for your own code and then make it publicly available for other people to use? How will users know what your function does if they need to understand it or adapt it? Well, you could comment your code (always good practice), but for functions (and classes) in particular, you can use the magic of **_docstrings_**. 

### How do I write a docstring?

It's easy to write a docstring. Just under your function definition, add triple quotes ` """ `, write your docstring, and then end the docstring with another set of triple quotes ` """ `. For example: 

```python
def square(x):
    """This is my docstring"""
    return x**2
```

Now that we have our docstring, it will show up when we run `help()` on our function! This is a major advantage of using docstrings instead of comments when documenting functions. For instance: 

```python
def square(x):
    """This is my docstring"""
    return x**2

help(square)
```

returns

```
Help on function square in module __main__:

square(x)
    This is my docstring

```

which tells us that the function `square` is defined in the main code, it takes one input `x`, and that... it has a docstring that says `this is my docstring`. That's a docstring alright, but it isn't a very helpful one...

### How do I write a _good_ docstring?

It is only slightly harder to write a good docstring than it is to write a docstring. Best practices for writing a docstrings are: 
- Describe what the function _returns_ (this is usually the first line)
- Describe what the function takes as an input, including data types, formats, variable names, and units if applicable
- Describe what the function gives as an output, including data types, formats, and units if applicable
- Note any domains over which the function will/will not work (for instance: does this work for integers only? Positive numbers?) and any exceptions the function might raise
- Note any dependencies the function has on other packages, functions, object types, etc. and related functions with similar usages
- Provide examples of the use of your function

Note that with the triple quotes, you can write a docstring that spans multiple lines, so if this seems like a lot to include, you have as much room as you need. 

In addition to these general guidelines, there are also specific styles guides for formatting your docstrings for consistency. The major advantages of using style guides are that they provide user with a consistent format and are easier for automatic documentation softwares to parse. You can [learn about different documentation styles at this site](http://queirozf.com/entries/docstrings-by-example-documenting-python-code-the-right-way "Different Documentation Styles"). In this example, I will use the numpy style, which is used by many common scientific Python packages and is well worth learning. 

Here is how I would document the `square` function in the numpy style:

```python
def square(x):
    """
    Returns the square of the input x.
    
    Parameters
    ----------
    x : int or float
        input number that will be squared
    
    Returns
    ----------
    int or float
        the square of the input number x
        
    Examples
    ----------
    >>> square(2)
    4
    """
    return x**2
```

Now when we run `help(square)` we get: 

```
Help on function square in module __main__:

square(x)
    Returns the square of the input x.
    
    Parameters
    ----------
    x : int or float
        input number that will be squared
    
    Returns
    ----------
    int or float
        the square of the input number x
        
    Examples
    ----------
    >>> square(2)
    4

```

Much better! Of course, this is a simple example that you could probably figure out just from the function definition, but docstrings are very useful when writing more complicated functions with multiple inputs, complicated outputs, or functions that require input of a certain format, unit, or data type. They help future readers (including yourself!) understand the code you've written. 

Docstrings should also be used when defining python classes--recall how we can also use `help()` on objects like lists. For classes, the docstring goes in the same place as for functions: in triple quotes, beneath the class definition and above the class methods. This site gives [an example of using docstrings for classes](https://www.geeksforgeeks.org/python-docstrings/ 'Docstrings for Classes').

It is best practice to __always include a docstring when defining functions and classes__. Now that you know how to write a good docstring, include docstrings in your own programs!

## Exercise

Practice writing docstrings by finishing the docstring of the following function according to the numpy style (note: this function's usage depends on the `square` function defined above). 

```python
def sum_of_squares(x, y):
    """
    Returns the sum of the squares of the inputs x and y. 
    
    Parameters
    ----------
    
    Returns
    ----------
    
    See Also
    ----------
    
    Examples
    ----------
    >>> sum_of_squares(3, 4)
    25
    """
    return square(x) + square(y)
```
