To translate the concept of a Python class to a Pine Script User-Defined Type (UDT) and demonstrate how it can be initialized with Pine Script functions, let's consider an example. 

### Python Class Example

In Python, a class with an initializer (`__init__`) might look like this:

```python
class Pivot:
    def __init__(self, x, y, xloc='bar_time'):
        self.x = x
        self.y = y
        self.xloc = xloc
```

This class defines a `PivotPoint` with `x`, `y`, and `xloc` attributes, where `xloc` has a default value of `'bar_time'`.

### Pine Script UDT Equivalent

In Pine Script, as described in the `objects.md` file, you would first define a UDT and then use a constructor function to initialize it. Pine Script does not have a direct equivalent of Python's `__init__` method; instead, you create objects using the UDT's `new()` method.

Here's how you could define a similar structure in Pine Script:

```pinescript
//@version=5
indicator("Pivot Point Example", overlay = true)

// Define the `pivotPoint` UDT.
type Pivot
    int x
    float y
    string xloc = xloc.bar_time

// Example function to create and return a new pivotPoint object
method init_pivot(int x, float y) =>
    Pivot.new(x, y)

// Example usage
var Pivot myPivot = na
if (bar_index == 10)
    myPivot := init_pivot(bar_index, high)

```

### Explanation

1. **UDT Definition**: The `pivotPoint` UDT is defined with fields `x`, `y`, and `xloc`, similar to the Python class's attributes. The `xloc` field has a default value of `xloc.bar_time`, mirroring the default parameter value in the Python class.

2. **Object Creation**: In Pine Script, objects of a UDT are created using the `new()` method. This example includes a custom function `createPivotPoint` that wraps the creation of a `pivotPoint` object, demonstrating how you might encapsulate object creation logic in a function, akin to using an `__init__` method in Python.

3. **Usage Example**: The script demonstrates how to conditionally create a `pivotPoint` object at a specific bar index. This is a simplified example to show object creation and usage within Pine Script.

This example illustrates how to translate the concept of a Python class and its initialization to Pine Script's UDTs and functions. Pine Script's approach to object-oriented programming is more limited compared to Python, focusing on structuring data rather than behavior.
