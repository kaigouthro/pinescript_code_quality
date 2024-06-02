# Pine Script - A Comprehensive Mini-Reference

This document provides a concise reference for Pine Script, a programming language specifically designed for trading strategies and indicators within TradingView.

## Operators

### Arithmetic Operators

#### Arithmetic Operators

| Operator | Description |
| --- | --- |
| + | Addition |
| \- | Subtraction |
| \* | Multiplication |
| / | Division |
| % | Modulus (Remainder of integer division) |

#### Comparison Operators

| Operator | Description |
| --- | --- |
| \== | Equal to |
| != | Not equal to |
| \> | Greater than |
| < | Less than |
| \>= | Greater than or equal to |
| <= | Less than or equal to |

#### Logical Operators

| Operator | Description |
| --- | --- |
| and | Logical AND |
| or | Logical OR |
| not | Logical NOT |
| ?: | Ternary operator (conditional expression) |

#### Assignment Operators

| Operator | Description |
| --- | --- |
| \= | Assignment |
| := | Re-assignment |
| += | Addition assignment |
| \-= | Subtraction assignment |
| \*= | Multiplication assignment |
| /= | Division assignment |
| %= | Modulus assignment |


## Keywords

These keywords are reserved in Pine Script and cannot be used as variable names.

Keyword | Description
------- | ---------------------------------------------------------------------------
import  | Imports a function from another script.
export  | Exports a function for use in other scripts.
method  | Defines a method within a user-defined type.
type    | Creates a user-defined type (similar to a class).
matrix  | Namespace for matrix-related functions.
var     | Declares a variable.
varip   | Declares a variable with intrabar persistence (value retained across bars).

> **Reserved Keywords:** `Catch`, `Class`, `Do`, `Ellipse`, `In`, `Is`, `Polygon`, `Range`, `Return`, `Struct`, `Text`, `Throw`, `Try`

---

## Storage Methods

These methods define the structure in which data is stored. `string` is used as an example type here.

Storage Method        | Description
--------------------- | ---------------------------------------------
`matrix<string>`      | Two-dimensional structure (rows and columns).
`array<string>`       | One-dimensional structure (ordered list).
`string[]`            | Shorthand notation for an array (legacy).
`string`              | Single data point.
`map<string, string>` | Key-value pair storage

## Built-in Types

Pine Script offers these fundamental data types.

Type       | Description
---------- | -------------------------------------------
`string`   | Textual data.
`int`      | Integer (whole number).
`float`    | Floating-point number (decimal).
`bool`     | Boolean (true/false).
`color`    | Represents a color using different formats.
`line`     | Line object.
`linefill` | Line fill object.
`box`      | Box object.
`label`    | Label object.
`table`    | Table object.

## User-Defined Types

These types, created with the `type` keyword, extend the language's capabilities by defining custom data structures. Methods can be defined externally.

Type             | Description
---------------- | ---------------------------------------------------------
`type <name>`    | Creates a user-defined type with a given name.
`<name>.new()`   | Creates a new instance (object) of the user-defined type.
`<name>.<field>` | Accesses a field (property) of the user-defined type.

```pinescript
type ExampleType
float fieldname1 = 0.0 // allowed default
string fieldname2 // allowed default but unused
array<int> fieldname3 // NOT allowed default
matrix<bool> fieldname4 // NOT allowed default
ExampleType field_udt // NOT allowed default
```

## Variables and Constants

Pine Script is loosely typed; you don't have to explicitly declare the type of a variable. The type is inferred during assignment. You cannot change the type of a variable after it has been assigned.

```pinescript
a = 1 // a is an integer
b = 1.2 // b is a float
c = "1.2" // c is a string
d = true // d is a boolean
e = color.new(color.red, 50) // e is a color
```

## Built-in Functions

### Technical Analysis Functions

The `ta` namespace provides a wide array of indicators. Here's a selection:

Function/Var             | Description
------------------------ | --------------------------------------
`ta.accdist`             | Accumulation/Distribution line.
`ta.alma()`              | Arnaud Legoux Moving Average.
`ta.atr()`               | Average True Range.
`ta.bb()`                | Bollinger Bands.
`ta.bbw()`               | Bollinger Width.
`ta.cci()`               | Commodity Channel Index.
`ta.cmo()`               | Chande Momentum Oscillator.
`ta.cog()`               | Center of Gravity.
`ta.dmi()`               | Directional Movement Index.
`ta.ema()`               | Exponential Moving Average.
`ta.hma()`               | Hull Moving Average.
`ta.iii`                 | Intraday Intensity Index.
`ta.kc()`                | Keltner Channels.
`ta.kcw()`               | Keltner Channels Width.
`ta.linreg()`            | Linear Regression Overlay.
`ta.macd()`              | Moving Average Convergence/Divergence.
`ta.mfi()`               | Money Flow Index.
`ta.mom()`               | Momentum.
`ta.nvi`                 | Negative Volume Index.
`ta.obv`                 | On-Balance Volume.
`ta.pvi`                 | Positive Volume Index.
`ta.pvt`                 | Price Volume Trend.
`ta.rma()`               | Roughness Moving Average.
`ta.roc()`               | Rate of Change.
`ta.rsi(source, length)` | Relative Strength Index.
`ta.sar()`               | Parabolic Stop and Reverse.
`ta.sma()`               | Simple Moving Average.
`ta.stoch()`             | Stochastic Oscillator.
`ta.supertrend()`        | Supertrend.
`ta.swma(source)`        | Smoothed Weighted Moving Average.
`ta.tr`                  | True Range.
`ta.tsi()`               | True Strength Index.
`ta.vwap`                | Volume Weighted Average Price.
`ta.vwma()`              | Volume Weighted Moving Average.
`ta.wad`                 | Williams Accumulation/Distribution.
`ta.wma()`               | Weighted Moving Average.
`ta.wpr()`               | Williams %R.
`ta.wvad`                | Volume Accumulation/Distribution.

### Supporting Functions

These functions provide various utilities for Pine Script development.

Function                                   | Description
------------------------------------------ | ------------------------------------------------------------------------
`ta.barsince()`                            | Number of bars since a condition was true.
`ta.change()`                              | Percent change from the previous bar's close.
`ta.correlation(source1, source2, length)` | Pearson's correlation coefficient between two prices.
`ta.cross(source1, source2)`               | Checks for a crossover (source1 crosses source2 upwards).
`ta.crossover(source1, source2)`           | Same as `ta.cross`.
`ta.crossunder(source1, source2)`          | Checks for a crossunder (source1 crosses source2 downwards).
`ta.cum(source)`                           | Cumulative sum of a source.
`ta.dev()`                                 | Standard deviation.
`ta.falling()`                             | True if the current bar's close is lower than the previous bar's close.
`ta.highest()`                             | Highest value from a source.
`ta.highestbars()`                         | Highest value within a specified number of bars.
`ta.lowest()`                              | Lowest value from a source.
`ta.lowestbars()`                          | Lowest value within a specified number of bars.
`ta.median()`                              | Median value of a source.
`ta.mode()`                                | Mode value of a source.
`ta.percentile_linear_interpolation()`     | Percentile of data using linear interpolation.
`ta.percentile_nearest_rank()`             | Percentile of data using nearest rank.
`ta.percentrank(n)`                        | Percentile rank within a specified number of bars.
`ta.pivothigh()`                           | Highest high/low preceding the current bar.
`ta.pivotlow()`                            | Lowest high/low preceding the current bar.
`ta.range()`                               | High to low range of a source.
`ta.rising()`                              | True if the current bar's close is higher than the previous bar's close.
`ta.stdev()`                               | Standard deviation of a source.
`ta.valuewhen()`                           | Last value of a source when a condition was true.
`ta.variance()`                            | Variance of a source.

### Math Functions

The `math` namespace offers common mathematical operations.

Function                        | Description
------------------------------- | ---------------------------------------------------------------
`math.abs(number)`              | Absolute value.
`math.acos(number)`             | Arc cosine.
`math.asin(number)`             | Arc sine.
`math.atan(number)`             | Arc tangent.
`math.avg()`                    | Average of a list of numbers.
`math.ceil(number)`             | Ceiling (round up to the nearest integer).
`math.cos(angle)`               | Cosine of an angle.
`math.exp(number)`              | Exponential.
`math.floor(number)`            | Floor (round down to the nearest integer).
`math.log(number)`              | Natural logarithm.
`math.log10(number)`            | Base-10 logarithm.
`math.max()`                    | Maximum value.
`math.min()`                    | Minimum value.
`math.pow()`                    | Exponentiation (raise to a power).
`math.random()`                 | Random number between 0 and 1.
`math.round(number, precision)` | Round to a specified number of decimal places.
`math.round_to_mintick(number)` | Round to the smallest increment allowed by the broker.
`math.sign(number)`             | Sign of a number (1 for positive, -1 for negative, 0 for zero).
`math.sin(angle)`               | Sine of an angle.
`math.sqrt(number)`             | Square root.
`math.sum()`                    | Sum of a list of numbers.
`math.tan(angle)`               | Tangent of an angle.
`math.todegrees()`              | Convert radians to degrees.
`math.toradians()`              | Convert degrees to radians.

### Requesting External Data

The `request` namespace enables you to fetch data from external sources.

Function                                    | Description
------------------------------------------- | ---------------------------------------------
`request.financial()`                       | Financial data like P/E ratio and market cap.
`request.quandl()`                          | Quandl datasets.
`request.security(<...>, timeframe, <...>)` | Data for a different security.
`request.splits()`                          | Stock splits data.
`request.dividends()`                       | Dividend information.
`request.earnings()`                        | Earnings data.

### Ticker Functions

The `ticker` namespace is used to create and work with different chart types.

Function               | Description
---------------------- | ------------------------------
`ticker.heikinashi()`  | Create a Heikin-Ashi chart.
`ticker.kagi()`        | Create a Kagi chart.
`ticker.linebreak()`   | Create a Line Break chart.
`ticker.pointfigure()` | Create a Point & Figure chart.
`ticker.renko()`       | Create a Renko chart.
`ticker.new()`         | Create a new ticker object.

### Array Functions

The `array` namespace provides functions for manipulating arrays.

Function                                  | Description
----------------------------------------- | ---------------------------------------------
`array.abs()`                             | Absolute value of each element.
`array.avg()`                             | Average of array elements.
`array.binary_search()`                   | Search for a value in a sorted array.
`array.binary_search_leftmost()`          | Index of the leftmost matching element.
`array.binary_search_rightmost()`         | Index of the rightmost matching element.
`array.clear()`                           | Remove all elements.
`array.concat()`                          | Concatenate two arrays.
`array.copy()`                            | Create a copy of an array.
`array.covariance()`                      | Covariance of array elements.
`array.every()`                           | Check if all elements pass a test.
`array.fill()`                            | Fill the array with a value.
`array.first()`                           | First element.
`array.from()`                            | Create an array from a list of values.
`array.get()`                             | Get element at a specified index.
`array.includes()`                        | Check if an array contains a value.
`array.indexof()`                         | Index of the first occurrence of a value.
`array.insert()`                          | Insert a new element at a given index.
`array.join()`                            | Concatenate array elements into a string.
`array.last()`                            | Last element.
`array.lastindexof()`                     | Index of the last occurrence of a value.
`array.max()`                             | Maximum value in the array.
`array.median()`                          | Median value of array elements.
`array.min()`                             | Minimum value in the array.
`array.mode()`                            | Mode value of array elements.
`array.new<bool>()`                       | Create a new array of booleans.
`array.new<box>()`                        | Create a new array of boxes.
`array.new<color>()`                      | Create a new array of colors.
`array.new<float>()`                      | Create a new array of floats.
`array.new<int>()`                        | Create a new array of integers.
`array.new<label>()`                      | Create a new array of labels.
`array.new<line>()`                       | Create a new array of lines.
`array.new<linefill>()`                   | Create a new array of linefills.
`array.new<string>()`                     | Create a new array of strings.
`array.new<table>()`                      | Create a new array of tables.
`array.new()`                             | Create a new array of a specified type.
`array.percentile_linear_interpolation()` | Percentile using linear interpolation.
`array.percentile_nearest_rank()`         | Percentile using nearest rank.
`array.percentrank()`                     | Percentile rank of a value.
`array.pop()`                             | Remove and return the last element.
`array.push()`                            | Add elements to the end.
`array.range()`                           | Create an array with a range of numbers.
`array.remove()`                          | Remove an element at a specified index.
`array.reverse()`                         | Reverse the order of elements.
`array.set()`                             | Set the value of an element at a given index.
`array.shift()`                           | Remove and return the first element.
`array.size()`                            | Number of elements in the array.
`array.slice()`                           | Extract a section of the array.
`array.some()`                            | Check if at least one element passes a test.
`array.sort()`                            | Sort array elements in place.
`array.sort_indices()`                    | Indices of sorted elements.
`array.splice()`                          | Add or remove elements.
`array.standardize()`                     | Standardize array elements.
`array.stdev()`                           | Standard deviation of array elements.
`array.sum()`                             | Sum of array elements.
`array.unshift()`                         | Add elements to the beginning.
`array.variance()`                        | Variance of array elements.

### Color Functions

Function    | Description
----------- | --------------------------------------------------------------
`color.a`   | Alpha component (transparency).
`color.b`   | Blue component.
`color.g`   | Green component.
`color.r`   | Red component.
`color.rgb` | Create a color from red, green, blue, and transparency values.

### Matrix Functions

The `matrix` namespace provides functions and methods for matrix operations.

Function/Method           | Description
------------------------- | -----------------------------------------
`matrix.add_col`          | Add a column.
`matrix.add_row`          | Add a row.
`matrix.avg`              | Average of matrix elements.
`matrix.col`              | Get a column from a matrix.
`matrix.columns`          | Number of columns.
`matrix.concat`           | Concatenate two matrices.
`matrix.copy`             | Copy a matrix.
`matrix.det`              | Determinant of a matrix.
`matrix.diff`             | Difference of a matrix.
`matrix.eigenvalues`      | Eigenvalues of a matrix.
`matrix.eigenvectors`     | Eigenvectors of a matrix.
`matrix.elements_count`   | Number of elements.
`matrix.fill`             | Fill a matrix with a value.
`matrix.get`              | Get the value of a matrix element.
`matrix.inv`              | Inverse of a matrix.
`matrix.is_antidiagonal`  | Check if a matrix is antidiagonal.
`matrix.is_antisymmetric` | Check if a matrix is antisymmetric.
`matrix.is_binary`        | Check if a matrix is binary.
`matrix.is_diagonal`      | Check if a matrix is diagonal.
`matrix.is_identity`      | Check if a matrix is the identity matrix.
`matrix.is_square`        | Check if a matrix is square.
`matrix.is_stochastic`    | Check if a matrix is stochastic.
`matrix.is_symmetric`     | Check if a matrix is symmetric.
`matrix.is_triangular`    | Check if a matrix is triangular.
`matrix.is_zero`          | Check if a matrix is the zero matrix.
`matrix.kron`             | Kronecker product of two matrices.
`matrix.max`              | Maximum value in a matrix.
`matrix.median`           | Median value of matrix elements.
`matrix.min`              | Minimum value in a matrix.
`matrix.mode`             | Mode value of matrix elements.
`matrix.mult`             | Product of two matrices.
`matrix.new`              | Create a new matrix of a specific type.
`matrix.pinv`             | Pseudoinverse of a matrix.
`matrix.pow`              | Power of a matrix.
`matrix.rank`             | Rank of a matrix.
`matrix.remove_col`       | Remove a column.
`matrix.remove_row`       | Remove a row.
`matrix.reshape`          | Reshape a matrix.
`matrix.reverse`          | Reverse the order of elements.
`matrix.row`              | Get a row from a matrix.
`matrix.rows`             | Number of rows.
`matrix.set`              | Set the value of a matrix element.
`matrix.sort`             | Sort matrix elements.
`matrix.submatrix`        | Get a submatrix.
`matrix.sum`              | Sum of matrix elements.
`matrix.swap_columns`     | Swap two columns.
`matrix.swap_rows`        | Swap two rows.
`matrix.trace`            | Trace of a matrix.
`matrix.transpose`        | Transpose of a matrix.

### Time Functions

Function           | Description
------------------ | --------------------------
`time.dayofmonth`  | Day of the month.
`time.dayofweek`   | Day of the week.
`time.dayofyear`   | Day of the year.
`time.hour`        | Hour.
`time.isdst`       | Daylight saving time flag.
`time.millisecond` | Millisecond.
`time.minute`      | Minute.
`time.month`       | Month.
`time.second`      | Second.
`time.timezone`    | Time zone.
`time.tzoffset`    | Time zone offset.
`time.year`        | Year.

### Map Functions

The `map` namespace provides functions and methods for manipulating maps.

Function/Method                 | Description
------------------------------- | -----------------------------------------------------------------------------
`map.contains(key)`             | Checks if a key exists in the map.
`map.copy()`                    | Creates a shallow copy of the map.
`map.get(key)`                  | Returns the value associated with a given key, or na if the key is not found.
`map.keys()`                    | Returns an array of all the keys in the map.
`map.new<keyType, valueType>()` | Creates a new map with specified key and value types.
`map.put(key, value)`           | Adds or updates a key-value pair in the map.
`map.put_all(otherMap)`         | Adds all key-value pairs from another map into the current map.
`map.remove(key)`               | Removes the key-value pair associated with the specified key.
`map.size()`                    | Returns the number of key-value pairs in the map.
`map.values()`                  | Returns an array of all the values in the map.

## Basic vital Notes on Pine Script

- **Storage Methods:** Storage methods like `TYPE`, `TYPE[]`, `matrix<TYPE>`, `array<TYPE>`, and `map<TYPE, TYPE>` define how data is structured in variables and function parameters.
- **User Defined Types (UDTs):** UDTs allow you to define custom data structures by combining fields (variables) of various types. They enhance code organization and reusability.
- **Function Declaration:** Functions are defined with a name, parameters (with types and optional default values), and a return type. They can be exported for use in other scripts.
- **Annotations:** Annotations (comments starting with `//@`) provide documentation and metadata for scripts, UDTs, functions, parameters, and variables.
- **Comments:** Comments in Pine Script start with `//` and continue to the end of the line.
- **Default Values:** Default values can be used for function parameters, allowing flexibility in how functions are called. Default values are only allowed for simple types (like `int`, `float`, `string`, `bool`) and not for complex structures (arrays, matrices, or UDTs).

---

# Extended Notes about Pine Script:

## Storage methods:

> Storage methods are methods that are used in type declarations.

> TYPE is a built-in type, or a user-defined type, identifier format is a letter or underscore followed by any number of letters, numbers, and underscores.

> the type might have a class name prefix, which is a letter or underscore followed by any number of letters, numbers, and underscores, followed by a '.'

### Storage methods can be:

- `TYPE`
- `TYPE []`
- `matrix`
- `array`
- `map<key_type, value_type>`

## UDT - User defined types:

> The User Defined Types (UDTs) are the types that are defined in the source code, and are used in the function declarations.

a UDT FIELD is a name, which is a letter or underscore followed by any number of letters, numbers, and underscores,

### A UDT is a User Defined Type that consists of:

- **OPTIONAL annotations:**

  - `@type tag = description of the UDT`
  - `@field tag = name of field, description of a contained field`

- **Type declaration:**

  - "export" keyword is optional (only for Library Scripts, not in strategy or indicator scripts)
  - "type" keyword is required
  - name of the UDT being created

- **Fields**

  - fields of the UDT, each field is a storage method followed by a field name, and optional default value on [ string, boolean, int, float, color ] types.

  - each field consists of:

    - an indent exactly 1 level deep.
    - a storage declaration (see above, "Storage methods")
    - a field name, which cannot start with a number and can only contain letters, numbers, and underscores
    - `OPTIONAL` :

      - default value, which is "=" followed by a value of the type of the field

## FUNCTION declaration consists of:

- **OPTIONAL annotations:**

  - `@function tag = description of the function`
  - `@param tag = name of parameter, optional storage method, description of a parameter`
  - `@return tag = description of the return value`

- **function declaration:**

  - "export" keyword is optional on Library scripts, not Indicator or strategy.

  - "method" keyword is optional second keyword

  - NAME is a letter or underscore followed by any number of letters, numbers, and underscores

  - '(' PARAMS ')'

  - PARAMS is a comma separated list of PARAMS, and may be multiline where lines have an offset of 2 spaces

  - optional "series" or "simple"

  - optional storage method

  - NAME of parameter

  - optional default value, which is "=" followed by a value of the type of the field

  - DEFAULT only allowed if TYPE is specified

  - DEFAULT not permitted for array, matrix, or UDT type

  - PARAMS with default values must be at the end of the list

  - '=>'

  - denotes start of code

  - SINGLE_LINE_RETURN or NEW_LINE + INDENTED_BLOCK

  - SINGLE_LINE_RETURN is a single line of code

  - NEW_LINE + INDENTED_BLOCK is a block of code statements

## Annotations:

- **Script:**

  - for the script "library" declaration, the annotation is linked to the script itself.
  - it is also useful on "indicator" and "strategy" declarations, but not required.
  - the tag is `@description` for the script description
  - the tag is `@version=` for the pinescript version and mandatory

Example:

```pinescript
@description this is a script
```

- **UDT (user defined type):** for a udt (user defined type) declaration, the tag is `@type` and conttent is a description of the type. for udt fields, the tag is `@field` and the content is:

  - (req) name of the field
  - (opt) storage type of the field
  - (opt) a description of the field.

Exaample:

```pinescript
@field myfield int this is my field
```

- **Function:**

  - for function declaration, the tag is `@function` and the content is a description of the function. for any other function annotators, it is required

Exaample:

```pinescript
@function this is my function
```

- for function parameters, the tag is `@param` and the content is a description of the parameter.

- (req) name of the parameter

- (opt) storage type of the parameter

- (opt) a default value for the parameter.

- (opt) a description of the parameter.

Example:

```pinescript
@param myparam string this is my parameter
@param myparam matrix<lib.type> this is my parameter
```

- for function return values, the tag is `@returns` and the content is a description of the return value. - (opt) storage type of the return value - (opt) a description of the return value.

Example:

```pinescript
@returns int this is my return value
```

- **variable declarations (optional)**

  - for variable declarations, the tag is `@variable` and the content is a description of the variable.

  - (req) name of the variable

  - (opt) storage type of the variable

  - (opt) a description of the variable.

Example:

```pinescript
@variable myvar int this is my variable
@variable myvar matrix<implib.udtimp> this is my variable
@variable myvar array<int> this is my variable
```

# Statements:

Statements are commands that are used to execute actions or to assign values to variables.

- **Assignment statement:**

  - assigns a value to a variable
  - consists of a variable name, an assignment operator, and a value
  - the value can be a literal, a variable, or an expression

- **Control statement:**

  - used to control the flow of the program
  - consists of a keyword, followed by a condition, and a block of code

- **Function call statement:**

  - calls a function
  - consists of a function name, followed by a list of arguments

- the regex Pattern to capture a statement:

# summary of the declaration rules:

User defined types:

- a UDT must have a name
- a UDT must have at least one field
- a UDT field must have a name
- a UDT field must have a type
- a UDT field name cannot start with a number
- a UDT field name can only contain letters, numbers, and underscores
- a UDT field type can only be a `TYPE` or a `TYPE[]` or `matrix<TYPE>` or array or `map<key_type, value_type>`

- a UDT field name cannot be a storage type

- a UDT field type can be the UDT itself in any of the above forms

- a UDT field does not require a default value
- a UDT field with a UDT type cannot have a default value
- a UDT definition ends after the fields when a newline begins with a character that is not a comment or whitespace

user defined functions

- a FUNCTION must have a name
- a FUNCTION may be a method
- a FUNCTION with method must have the `TYPE` specified for the first parameter
- a FUNCTION must have at least one parameter
- a FUNCTION parameter must have a name
- a FUNCTION parameter must have a type
- a FUNCTION parameter name cannot start with a number
- a FUNCTION parameter name can only contain letters, numbers, and underscores
- a FUNCTION parameter type can only be a be a `TYPE` or a `TYPE[]` or `matrix<TYPE>` or array or `map<key_type, value_type>`

- a FUNCTION parameter name cannot be a storage type

- a FUNCTION parameter type can be the UDT itself in any of the above forms

- a FUNCTION parameter does not require a default value
- a FUNCTION parameter with a UDT type cannot have a default value
- a FUNCTION definition ends after the return value when a newline begins with a character that is not a comment or whitespace

annotations

- annotations must start a line by themselves
- annotations must start with '//' and a '@' character
- annotations must be followed by a tag, which is a specified comment from the list here:
- `@description` - script description before the "library" or "indicator" or "strategy" script declaration with a '(' and string title first arg
- `@type` - description of a UDT definition
- `@field` - description of a field in a UDT definition
- `@function` - description of a function
- `@param` - description of a parameter
- `@returns` - description of a return value
- annotations of fields and parameters must be followed by the name, then description
- annotations description is any text following until code on a new line or the next annotation.
- annotations may include markdown formatting on several lines, each starting with '//' after the @tag line

comments

- comments start with two slashes : '//'
- comments may start a line or follow anything else
- comments run from slash to line end, and end a line

storage types

- storage types can be:

  - `TYPE`
  - `TYPE[]`
  - `matrix<TYPE>`
  - `array<TYPE>`
  - `map<BUILTIN_TYPE, TYPE>`
  - Any UDT in place of TYPE above

- storage types can not be:

  - TYPE[] []
  - matrix[]
  - array[]
  - matrix

    <matrix>
    </matrix>

  - array

    <matrix>
    </matrix>

default values

- values can be:

  - a number
  - a string
  - a boolean
  - na
  - a system variable

- default values cannot be:

  - a matrix
  - an array
  - a function
  - a UDT
  - a map

# Maps:

Maps are key-value pair structures in Pine Script.

- They are **unordered** collections: The order you add elements doesn't impact how you access them later.
- Keys can be any fundamental type (string, int, float, bool, color).
- Values can be any built-in type or User Defined Type (UDT).

## Declaring a map:

```pine
// declare a map named "myMap"
var myMap = map.new<string, float>()
```

- `map.new<keyType, valueType>()`: Creates an empty map with specified types for the keys and values.
- **Example**: `map.new<string, float>()` creates a map where keys are strings and values are floating point numbers.

## Common Map Operations

### Adding elements:

```pine
// adds a pair where "FirstValue" is the key and 1.5 is the value
myMap.put("FirstValue", 1.5) 
```

### Retrieving values:

```pine
myMap.get("FirstValue") // Returns 1.5 (the value associated with the key "FirstValue")
```

### Checking for a key's presence:

```pine
if myMap.contains("FirstValue") // true if the key exists
```

### Removing elements:

```pine
myMap.remove("FirstValue") // Removes the pair associated with the "FirstValue" key
```

## Additional Map Features

- **Copying maps**: `map.copy()`, `deepCopy()`: Create shallow or deep copies to prevent unintended modifications to the original map.
- **Iteration**: Loop through key-value pairs using the for-in structure:

```pine
for [key, value] in myMap
// access the 'key' and 'value' on each iteration
```
