
# Floating-Point Arithmetic Examples in Python

This repository provides examples of common floating-point arithmetic behaviors and issues. These Python examples illustrate how the limitations of floating-point representation can impact accuracy and cause unexpected results in computations.

## Overview

Floating-point arithmetic is widely used in programming but comes with inherent limitations due to how computers represent decimal numbers in binary. This repository contains very simple Python functions demonstrating:

- **Rounding errors** due to binary representation limitations
- **Precision loss** when combining numbers of vastly different magnitudes
- **Floating-point inaccuracies leading to unintended code behavior** and solutions to address them
- **Fixed-point arithmetic example** as an alternative to floating-point for consistent precision

## Function Descriptions

### `rounding_error()`
This function illustrates rounding errors that occur when decimal numbers like `0.1` and `0.2` are represented in binary. Numbers like these cannot be precisely represented in binary floating-point form due to the limited bits available for the mantissa. As a result, adding `0.1` and `0.2` may yield a result slightly different from `0.3`, causing unexpected behavior in programs that rely on exact comparisons.

### `addition_of_large_and_small_numbers()`
Shows how adding a very large number (e.g., `1e10`) to a very small one (e.g., `1e-10`) can effectively ignore the smaller number due to limited precision in the mantissa. This behavior, known as "catastrophic cancellation," results from the mantissa’s inability to retain enough detail to differentiate the smaller number when combined with a much larger one.

### `infinite_loop_example()`
Demonstrates how floating-point inaccuracy can lead to an infinite loop. Here, a variable `b` is incremented by `0.1` in each iteration but never exactly reaches `a` (1.0). This is due to the fact that `0.1` cannot be represented exactly in binary form, causing cumulative rounding errors. Consequently, the loop never terminates.

### `infinite_loop_solution()`
Offers a solution to the above infinite loop using an `epsilon` value, or tolerance. Rather than checking for exact equality (which is unreliable with floating-point numbers), the function checks if `b` is within a very small range of `a`. This approach avoids the infinite loop by allowing approximate comparison within an acceptable margin of error.

### `fixed_point_operations()`
Explains fixed-point arithmetic as an alternative to floating-point. Fixed-point arithmetic avoids rounding issues by using integer math to represent decimal values, maintaining precise control over the decimal place. This is particularly useful in financial and scientific applications where exact precision is crucial. Unlike floating-point, fixed-point values have a set number of decimal places, allowing for consistent precision at the cost of a fixed range.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This repository is designed for educational purposes to underscore the importance of understanding floating-point arithmetic limitations and behaviors in programming. By gaining insights into the IEEE 754 standard and potential pitfalls, beginner developers can make more informed choices about numeric representation in their applications.
