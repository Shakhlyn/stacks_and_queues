# Queue and Stack Implementations in Python

This repository contains Python implementations of a **Queue** and a **Stack** data structure.

## Queue

The `Queues` class provides a simple implementation of a queue data structure using a linked list. It supports the following methods:

- `enqueue(value)`: Add an element to the end of the queue.
- `dequeue()`: Remove and return the element from the front of the queue.
- `print_nodes()`: Print the elements of the queue.

### Usage

```python
new_queue = Queues()

new_queue.enqueue('first')
new_queue.enqueue('second')
new_queue.enqueue('third')
new_queue.enqueue('fourth')

new_queue.print_nodes()

new_queue.dequeue()
new_queue.dequeue()
new_queue.print_nodes()
```

## Stack

The `Stacks` class provides a basic implementation of a stack data structure using a linked list. It supports the following methods:

- `push(value)`: Add an element to the top of the stack.
- `pop_from_beginning()`: Remove and return the element from the top of the stack.
- `print_nodes()`: Print the elements of the stack.

### Usage

```python
stacked_data = Stacks()

stacked_data.push('first')
stacked_data.push('second')
stacked_data.push('latest')

stacked_data.print_nodes()

stacked_data.pop_from_beginning()
stacked_data.pop_from_beginning()
stacked_data.print_nodes()
```
