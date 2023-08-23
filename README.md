# Stack Implementation in Python

This repository contains a Python implementation of a stack data structure.

## Description

The code in this repository demonstrates a simple stack implementation using Python classes. The stack supports push and pop operations, and you can visualize the current state of the stack.


### Usage

You can use the provided classes to create and manipulate a stack. Here's an example of how to use the stack:

```python

# Import the Stacks class
from stack import Stacks

# Create a stack instance
stacked_data = Stacks()

# Push elements onto the stack
stacked_data.push('first')
stacked_data.push('second')
stacked_data.push('latest')

# Print the current state of the stack
stacked_data.print_nodes()

# Pop an element from the beginning of the stack
popped_element = stacked_data.pop_from_beginning()
print("Popped Element:", popped_element.value)

# Print the updated stack
stacked_data.print_nodes()
