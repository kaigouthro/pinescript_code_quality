# Language¶

- Execution model

  - Calculation based on historical bars
  - Calculation based on realtime bars
  - Events triggering the execution of a script
  - More information
  - Historical values of functions

    - Why this behavior?
    - Exceptions

- Time series
- Script structure

  - Version
  - Declaration statement
  - Code
  - Comments
  - Line wrapping
  - Compiler annotations

- Identifiers
- Operators

  - Introduction
  - Arithmetic operators
  - Comparison operators
  - Logical operators
  - `?:` ternary operator
  - `[ ]` history-referencing operator
  - Operator precedence
  - `=` assignement operator
  - `:=` reassignement operator

- Variable declarations

  - Introduction

    - Initialization with `na`
    - Tuple declarations

  - Variable reassignment
  - Declaration modes

    - On each bar
    - `var`
    - `varip`

- Conditional structures

  - Introduction
  - `if` structure

    - `if` used for its side effects
    - `if` used to return a value

  - `switch` structure

    - `switch` with an expression
    - `switch` without an expression

  - Matching local block type requirement

- Loops

  - Introduction

    - When loops are not needed
    - When loops are necessary

  - `for`
  - `while`

- Type system

  - Introduction
  - Qualifiers

    - const
    - input
    - simple
    - series

  - Types

    - int
    - float
    - bool
    - color
    - string
    - plot and hline
    - Drawing types
    - Chart points
    - Collections
    - User-defined types
    - void

  - `na` value
  - Type templates
  - Type casting
  - Tuples

- Built-ins

  - Introduction
  - Built-in variables
  - Built-in functions

- User-defined functions

  - Introduction
  - Single-line functions
  - Multi-line functions
  - Scopes in the script
  - Functions that return multiple results
  - Limitations

- Objects

  - Introduction
  - Creating objects
  - Changing field values
  - Collecting objects
  - Copying objects
  - Shadowing

- Methods

  - Introduction
  - Built-in methods
  - User-defined methods
  - Method overloading
  - Advanced example

- Arrays

  - Introduction
  - Declaring arrays

    - Using `var` and `varip` keywords

  - Reading and writing array elements
  - Looping through array elements
  - Scope
  - History referencing
  - Inserting and removing array elements

    - Inserting
    - Removing
    - Using an array as a stack
    - Using an array as a queue

  - Calculations on arrays
  - Manipulating arrays

    - Concatenation
    - Copying
    - Joining
    - Sorting
    - Reversing
    - Slicing

  - Searching arrays
  - Error handling

    - Index xx is out of bounds. Array size is yy
    - Cannot call array methods when ID of array is 'na'
    - Array is too large. Maximum size is 100000
    - Cannot create an array with a negative size
    - Cannot use shift() if array is empty.
    - Cannot use pop() if array is empty.
    - Index 'from' should be less than index 'to'
    - Slice is out of bounds of the parent array

- Matrices

  - Introduction
  - Declaring a matrix

    - Using `var` and `varip` keywords

  - Reading and writing matrix elements

    - `matrix.get()` and `matrix.set()`
    - `matrix.fill()`

  - Rows and columns

    - Retrieving
    - Inserting
    - Removing
    - Swapping
    - Replacing

  - Looping through a matrix

    - `for`
    - `for…in`

  - Copying a matrix

    - Shallow copies
    - Deep copies
    - Submatrices

  - Scope and history
  - Inspecting a matrix
  - Manipulating a matrix

    - Reshaping
    - Reversing
    - Transposing
    - Sorting
    - Concatenating

  - Matrix calculations

    - Element-wise calculations
    - Special calculations

  - Error handling

    - The row/column index (xx) is out of bounds, row/column size is (yy).
    - The array size does not match the number of rows/columns in the matrix.
    - Cannot call matrix methods when the ID of matrix is 'na'.
    - Matrix is too large. Maximum size of the matrix is 100,000 elements.
    - The row/column index must be 0 <= from_row/column < to_row/column.
    - Matrices 'id1' and 'id2' must have an equal number of rows and columns to be added.
    - The number of columns in the 'id1' matrix must equal the number of rows in the matrix (or the number of elements in the array) 'id2'.
    - Operation not available for non-square matrices.

- Maps

  - Introduction
  - Declaring a map

    - Using `var` and `varip` keywords

  - Reading and writing

    - Putting and getting key-value pairs
    - Inspecting keys and values
    - Removing key-value pairs
    - Combining maps

  - Looping through a map
  - Copying a map

    - Shallow copies
    - Deep copies

  - Scope and history
  - Maps of other collections

© Copyright 2024, TradingView.
