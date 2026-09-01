# ==============================================================================
# Python Decorators
# A decorator is a function that takes another function as an argument,
# extends its behavior without modifying it, and returns the modified function.
# ==============================================================================

# 1. Outer function: Receives the target function 'func' to be decorated
def decorator(func):
    # 2. Inner function (Wrapper): Wraps around the original function
    #    *args    -> Accepts any number of positional arguments (e.g., "Alice", 3, 5)
    #    **kwargs -> Accepts any number of keyword arguments (e.g., name="Alice", age=25)
    def wrapper(*args, **kwargs):
        # Code executed BEFORE the original function runs
        print("Before the function call")

        # Execute the original function with forwarded arguments and capture its return value
        result = func(*args, **kwargs)

        # Code executed AFTER the original function runs
        print("After the function call")

        # Return the original function's result back to the caller
        return result

    # Return the wrapper function reference (without calling it yet)
    return wrapper


# ------------------------------------------------------------------------------
# Example 1: Decorating a function with 1 argument
# @decorator is equivalent to: say_hello = decorator(say_hello)
# ------------------------------------------------------------------------------
@decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Calling the decorated function:
say_hello("Alice")


# ------------------------------------------------------------------------------
# Example 2: Decorating a function with multiple arguments and return value
# @decorator is equivalent to: add = decorator(add)
# ------------------------------------------------------------------------------
@decorator
def add(a, b):
    c = a + b
    # If we use 'return c' instead of 'print':
    # 1. 'func(*args, **kwargs)' inside the wrapper evaluates to 'c' (8).
    # 2. 'result = func(...)' captures that value (8).
    # 3. 'return result' at line 20 passes the value back to the caller.
    # Without 'return result' in the wrapper, the caller would receive None.
    return c

# Calling the decorated function and capturing the returned value:
total = add(3, 5)
print(f"Returned value received by caller: {total}")