# Author: Your Name / your_email Evans Bishop Leb0134@auburn.edu
# Date: 2024-09-01
# Assignment Name: hw02

import sys
import numpy as np

def p1(f, a, b, epsilon, name, f_prime=None):
    """
    @param f: a function name
    @param a: real number, the left end of the interval
    @param b: real number, the right end of the interval
    @param epsilon: function tolerance
    @param name: the name of the method to use
    @param f_prime: the derivative of the function f (only needed for Newton's method)

    @return: tuple (c, n), 
             c is the root of the function f in the interval [a, b]
             n is the number of iterations
    """
    # Write your code here (bisection code is provided) 
    if name=="bisection":
        # bisection method
        n = 0
        c = (a+b)/2
        while abs(f(c))>epsilon:
            n += 1
            if f(a)*f(c)<0:
                b = c
            else:
                a = c
            c = (a+b)/2
        return c,n
    elif name=="newton":
        # Newton's method 
def newton(f, df, x0, tol=1e-9):
    iterations = 0
    while abs(f(x0)) > tol:
        x0 = x0 - f(x0) / df(x0)
        iterations += 1
    return x0, iterations
        pass
    elif name=="secant":
        # Secant method
def secant(f, x0, x1, tol=1e-9):
    iterations = 0
    while abs(x1 - x0) > tol:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
        iterations += 1
    return x1, iterations
        pass
    elif name=="regula_falsi":
        # False position method
def false_position(f, a, b, tol=1e-9):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    iterations = 0
    while abs(b - a) > tol:
        c = a - f(a) * (b - a) / (f(b) - f(a))
        if f(c) == 0:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return c, iterations
        pass
    elif name=="steffensen":
        # Steffensen's method
def steffensen(f, x0, tol=1e-9):
    iterations = 0
    while abs(f(x0)) > tol:
        g = (f(x0 + f(x0)) - f(x0)) / f(x0)
        x1 = x0 - f(x0) / g
        x0 = x1
        iterations += 1
    return x0, iterations
        pass
    else:
        print("Invalid name")
        
def p2():
    """
    summarize the iteration number for each method name in the table

    |name          | iter | 
    |--------------|------|
    |bisection     |  30    |
    |secant        |   6   |
    |newton        |  5    |
    |regula_falsi  |   12   |
    |steffensen    |   4   |
    """


def p3(f, a, b , epsilon):
    """
    For 6630 students only.

    Implement the Illinois algorithm to find the root of the function f in the interval [a, b]

    @param f: a function name
    @param a: real number, the left end of the interval
    @param b: real number, the right end of the interval
    @param epsilon: function tolerance

    @return: tuple (c, n), 
             c is the root of the function f in the interval [a, b]
             n is the number of iterations
    """
    # Write your code here
    pass

def p4(f, a, b , epsilon):
    """
    For 6630 students only.

    Implement the Pegasus algorithm to find the root of the function f in the interval [a, b]

    @param f: a function name
    @param a: real number, the left end of the interval
    @param b: real number, the right end of the interval
    @param epsilon: function tolerance
    
    @return: tuple (c, n), 
             c is the root of the function f in the interval [a, b]
             n is the number of iterations
    """
    # Write your code here
    pass
