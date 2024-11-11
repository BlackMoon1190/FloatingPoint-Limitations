
# Floating-Point Arithmetic Examples in Python

This repository provides examples of common floating-point arithmetic behaviors and issues. These Python examples illustrate how the limitations of floating-point representation can impact accuracy and cause unexpected results in computations.

## Overview

Floating-point arithmetic is widely used in programming but comes with inherent limitations due to how computers represent decimal numbers in binary. This repository contains very simple Python functions demonstrating:

- Rounding errors caused by binary representation limitations
- Loss of precision when adding numbers of significantly different magnitudes
- Infinite loops due to floating-point inaccuracy and solutions to avoid them
- Fixed-point arithmetic as an alternative to floating-point for consistent precision

## Function Descriptions

### `rounding_error()`
Illustrates a common rounding error. In this example, adding `0.1` and `0.2` does not yield `0.3` due to the binary representation of these decimal numbers, which cannot be represented exactly. This causes a small rounding error, resulting in an unexpected output.

### `addition_of_large_and_small_numbers()`
Shows how adding a very large number (`1e10`) and a very small number (`1e-10`) can result in the small number being ignored. The limited precision of floating-point arithmetic causes the smaller number to have no effect on the outcome.

### `infinite_loop_example()`
Demonstrates an infinite loop caused by floating-point inaccuracy. Here, `b` is incremented by `0.1` in each iteration but never exactly equals `a` (1.0) due to the inaccuracy in representing `0.1` in binary. This causes the loop to continue indefinitely.

### `infinite_loop_solution()`
Provides a solution to the infinite loop issue by using an `epsilon` value - small tolerance. Instead of checking for exact equality, this function checks if `b` is within a very small range of `a`, preventing an infinite loop.

### `fixed_point_operations()`
Demonstrates fixed-point arithmetic, an alternative to floating-point arithmetic. Fixed-point arithmetic allows for consistent precision without rounding errors by using integer operations to represent decimal values. This approach is particularly useful in applications that require exact precision, such as financial calculations.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

This repository is for educational purposes and highlights the importance of understanding the limitations and behavior of floating-point arithmetic in programming.
