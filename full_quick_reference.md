Here's the reformatted version of the provided Markdown document with a unified and consistent style:

Pine Script - A Comprehensive Documentation
=============================================

Pine Script Operators
---------------------

| Operator | Description    |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| \*       | Multiplication |
| /        | Division       |
| %        | Modulus        |

Pine Script Comparison Operators
-------------------------------

| Operator | Description              |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |

Pine Script Logical Operators
----------------------------

| Operator | Description      |
| -------- | ---------------- |
| and      | Logical and      |
| or       | Logical or       |
| not      | Logical not      |
| ?:       | Ternary operator |

Pine Script Assignment Operators
------------------------------

| Operator | Description               |
| -------- | ------------------------- |
| =        | Assignment                |
| :=       | Re-assignment             |
| +=       | Addition assignment       |
| -=       | Subtraction assignment    |
| \*=      | Multiplication assignment |
| /=       | Division assignment       |
| %=       | Modulo assignment         |

Pine Script Keywords
-------------------

| Keyword | Description                                  |
| ------- | -------------------------------------------- |
| import  | Imports a function                           |
| export  | Exports a function                           |
| method  | Creates a method                             |
| type    | Creates a user defined type statement        |
| matrix  | Namespace, see matrix                        |
| var     | Creates a variable                           |
| varip   | Creates a variable with intrabar persistence |

Pine Script Reserved Keywords
-----------------------------

* Catch, Class, Do, Ellipse, In, Is, Polygon, Range, Return, Struct, Text, Throw, Try

Storage Methods
---------------

Storage methods are methods that are used in type declarations.

**TYPE** is a built-in type, or a user defined type,
identifier format is a letter or underscore followed by any number of letters, numbers, and underscores.
the type might have a class name prefix, which is a letter or underscore followed by any number of letters, numbers, and underscores, followed by a '.'

storage methods can be:

* TYPE
* TYPE []
* matrix<TYPE>
* array<TYPE>

Pine Script Built-in Types
-------------------------

The following types are built-in for variables, and can appear in storage types

| Types    | Description                                                                       |
| -------- | --------------------------------------------------------------------------------- |
| string   | String of characters                                                              |
| int      | Integer (whole number)                                                            |
| float    | Float (number with decimal and optional _[Ee]_)                                   |
| bool     | Boolean (true/false)                                                              |
| color    | 3 options (color.name, #RRGGBBTT, rgba(r, g, b, a))                               |
| line     | line object (line.new(x1, y1, x2, y2, xloc, extend, style, width, color))         |
| linefill | line fill object (linefill.new(l1, l1, coor))                                     |
| box      | box object (box.new(left, top, right, bottom, .. etc.. )                          |
| label    | label object (label.new(x, y, string, xloc, yloc, style, color, .. etc.. )        |
| table    | table object (table.new(position, columns, rows, bgcolor, bordercolor, .. etc.. ) |

Pine Script User-defined Types
------------------------------

The following types are available for user-defined types.
A type can be defined with the type keyword.
A type is similar to a class in object-oriented languages,
but methods are declared afterwards and externally

| Type              | Description                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| type UdtName      | Create a user-defined type with name                                                           |
| UdtName.new()     | Create a new user-defined type object                                                          |
| UdtName.fieldname | calls the stored field item of the type either to reassign, or as an expression's return value |

Example
--------

```
//@type A Demo of a UDT / USer Defined Type
//@param myfield (string) a string field
//@param myfield (bool) a string field
//@param myfield (float) a string field
//@param myfield (int) a string field
//@param myfield (color) a string field
//@param myfield (map) a string field

//@version=5
indicator("UDT - Pivot Point Example", overlay = true)

// Define the `pivotPoint` UDT.
type PivotPoint
    int    x    = bar_index
    float  y    = close
    string xloc = xloc.bar_time

// Example function to create and return a new PivotPoint object
PivotPoint createPivotPoint(int x, float y) =>
    PivotPoint.new(x, y)

// Example usage
var PivotPoint myPivot = na
if (high < ta.lowest(high,3))
    myPivot := createPivotPoint(bar_index[3], high)
```

Pine Script Variables and Constants
----------------------------------

Pine Script is a loosely typed language. This means that
you do not need to specify the type of data a variable
refers to on asignment unless it is 'na'.
The data type is automatically assigned when
the variable is assigned a value.
It is NOT possible to change the data type after.

Example

```pinescript
a = 1                         // a is  a int
b = 1.2                       // b is  a float
c = "1.2"                     // c is  a string
d = true                      // d is  a bool
e = color.new(color.red, 50)  // e is  a color
```

Example

```pinescript
// type inference
// declare a variable without an initial value
// the variable type will be 'na' until it is assigned a value
var int a = na
// assign a value to the na int
a := 1
// variable type is now a value
```

Pine Script Maps
---------------

Maps are collections that store elements in key-value pairs.
They allow scripts to collect multiple value references associated with unique identifiers (keys).
Unlike arrays and matrices, maps are considered _unordered_ collections.
Scripts quickly access a map’s values by referencing the keys from the key-value pairs put into them rather than traversing an internal index.
A map’s keys can be of any _fundamental type_, and its values can be of any built-in or user-defined type.
Maps cannot directly use other _collections_ (maps, arrays, or matrices) as values, but they can hold UDT instances containing these data structures within their fields.
Maps can contain up to 100,000 elements in total.
The maximum number of key-value pairs a map can hold is 50,000.

### Syntax


```
[var/varip][map<keyType,  valueType>]  <identifier>  =  <expression>
```

* `<keyType, valueType>` is the map’s type template that declares the types of keys and values it will contain, and the `<expression>` returns either a map instance or `na`.
* When declaring a map variable assigned to `na`, users must include the map keyword followed by a type template to tell the compiler that the variable can accept maps with `keyType` keys and `valueType` values.
* Using `var` and `varip` keywords instructs scripts to declare map variables only on the first chart bar. Variables that use these keywords point to the same map instances on each script iteration until explicitly reassigned.

### Reading and writing


The `map.put()` function adds a new key-value pair to a map `id`. The `key` argument is associated with the `value` argument in the call and adds the pair to the map `id`. If the `key` argument in the `map.put()` call already exists in the map’s keys, the new pair passed into the function will **replace** the existing one.

To retrieve the value from a map `id` associated with a given `key`, use `map.get()`. This function returns the value if the `id` map contains the `key`. Otherwise, it returns `na`.

### Inspecting keys and values


* `map.keys()` and `map.values()` copy all key/value references within a map `id` to a new array object. Modifying the array returned from either of these functions does not affect the `id` map.
* Although maps are _unordered_ collections, Pine Script® internally maintains the _insertion order_ of a map’s key-value pairs. As a result, the `map.keys()` and `map.values()` functions always return arrays with their elements ordered based on the `id` map’s insertion order.
* `map.contains()` checks if a specific `key` exists within a map `id`. This function is a convenient alternative to calling `array.includes()` on the array returned from `map.keys()`.

### Removing key-value pairs


* `map.remove()` removes the `key` and its associated value from the map while preserving the insertion order of other key-value pairs. It returns the removed value if the map contained the `key`. Otherwise, it returns `na`.
* `map.clear()` removes all key-value pairs from a map `id` at once.

### Combining maps


The `map.put_all()` function combines two maps. It puts _all_ key-value pairs from the `id2` map, in their insertion order, into the `id1` map. As with `map.put()`, if any keys in `id2` are also present in `id1`, this function **replaces** the key-value pairs that contain those keys without affecting their initial insertion order.

### Looping through a map


There are several ways scripts can iteratively access the keys and values in a map.
One can loop through a map’s keys() array and get() the value for each `key`.
However, Pine recommends using a `for...in` loop directly on a map, as it iterates over the map’s key-value pairs in their insertion order, returning a tuple containing the next pair’s key and value on each iteration.

### Copying a map


* Shallow copies, made using the `map.copy()` function, do not affect the original map or its internal insertion order.
* Deep copies create a new map with key-value pairs containing copies of each value in the original map.

### Scope and history


* As with other collections in Pine, map variables leave historical trails on each bar, allowing a script to access past map instances assigned to a variable using the history-referencing operator `[]`.
* Scripts can also assign maps to global variables and interact with them from the scopes of functions, methods, and conditional structures.

### Maps of other collections


Maps cannot directly use other maps, arrays, or matrices as values, but they can hold values of a user-defined type that contains collections within its fields.

### Putting and getting key-value pairs


* **Put**: To put a new key-value pair into a map, use `map.put(key, val)`
* **Get**: To retrieve a specific value within an already existing key-value pair, use `map.get(key)`.

Example of using a map to collect market summaries:

```
//@version=5
indicator("My Script")

// Create a map to store daily market summaries.
var market_summaries = map.new(string, float)

// Update the map with daily market data.
market_summaries.put("Close", close)
market_summaries.put("Volume", volume)

// Iterate through the key-value pairs in the map.
for [key, value] in market_summaries
    print(key + ": " + value)
```

Pine Script Functions and Variables
----------------------------------

### Function Declaration

A function declaration consists of:

* **Annotations (optional):**
	+ `@function` tag = description of the function
	+ `@param` tag = name of parameter, optional storage method, description of a parameter
	+ `@return` tag = description of a return value
* **Function declaration:**
	+ "export" keyword is optional on Library scripts, not Indicator or strategy.
	+ "method" keyword is optional second keyword
	+ NAME is a letter or underscore followed by any number of letters, numbers, and underscores
	+ '(' PARAMS ')'
		- PARAMS is a comma separated list of PARAMS, and may be multiline where lines have an offset of 2 spaces
			- optional "series" or "simple"
			- optional storage method
			- NAME of parameter
			- optional default value, which is "=" followed by a value of the type of the field
				- DEFAULT only allowed if TYPE is specified
				- DEFAULT not permitted for array, matrix, or UDT type
				- PARAMS with default values must be at the end of the list
	+ '=>'
		- denotes start of code
	+ SINGLE\_LINE\_RETURN or NEW\_LINE + INDENTED\_BLOCK
		- SINGLE\_LINE\_RETURN is a single line of code
		- NEW\_LINE + INDENTED\_BLOCK is a block of code statements

### Function Statements

* **Assignment statement:**
	+ assigns a value to a variable
	+ consists of a variable name, an assignment operator, and a value
	+ the value can be a literal, a variable, or an expression
* **Control statement:**
	+ used to control the flow of the program
	+ consists of a keyword, followed by a condition, and a block of code
* **Function call statement:**
	+ calls a function
	+ consists of a function name, followed by a list of arguments

* **The regex Pattern to capture a statement:**

Syntax Summary
-------------

User Defined Types:
------------------

* A UDT must have a name
* A UDT must have at least one field
* A UDT field must have a name
* A UDT field must have a type
* A UDT field name cannot start with a number
* A UDT field name can only contain letters, numbers, and underscores
* A UDT field type can only be a TYPE or a TYPE[] or matrix<TYPE> or array<TYPE>
* A UDT field name cannot be a storage type
* A UDT field type can be the UDT itself in any of the above forms
* A UDT field doed not require a default value
* A UDT field with a UDT type cannot have a default value
* A UDT definition ends after the fields when a newline begins with a character hat is no a commentt or whitespac

User Defined Functions:
-----------------------

* A FUNCTION must have a name
* A FUNCTION may be a method
* A FUNCTION wiht method must have the TYPE specified for fisrt parameter
* A FUNCTION wiht method must have the TYPE specified for fisrt parameter
* A FUNCTION must have at least one parameter
* A FUNCTION parameter must have a name
* A FUNCTION parameter must have a type
* A FUNCTION parameter name cannot start with a number
* A FUNCTION parameter name can only contain letters, numbers, and underscores
* A FUNCTION parameter type can only be a TYPE or a TYPE[] or matrix<TYPE> or array<TYPE>
* A FUNCTION parameter name cannot be a storage type
* A FUNCTION parameter type can be the UDT itself in any of the above forms
* A FUNCTION parameter doed not require a default value
* A FUNCTION parameter with a UDT type can not have a default value
* A FUNCTION definition ends after the return value when a newline begins with a character hat is no a commentt or whitespac

Annotations:
-----------

* Annotations must start a line by themselves
* Annotations must start with '//' and a '@' character
* Annotations must be followed by a tag, which is a specified comment from the list here:
	+ `@description` - script description before the "library" or "indicator" or "strategy" script declaration witth a '(' and string title first arg
	+ `@type` - description a UDT definition
	+ `@field` - description of a field in a UDT definition
	+ `@function` - description of a function
	+ `@param` - description of a parameter
	+ `@return` - description of a return value
* Annotations description is any text following until code on a new line or the next annotation.
* Annotations may include markdown formatting on several lines, each starting with '//' after the @tag line

Comments:
---------

* Comments start with twwo slashes : '//'
* Comments may start a line or follow anything else
* Comments run from slash to line end, and end a line

Storage Types:
-------------

* Storage types can be:
	+ TYPE
	+ TYPE[]
	+ matrix<TYPE>
	+ array<TYPE>
* Storage types can not be:
	+ TYPE[] []
	+ matrix<TYPE> []
	+ array<TYPE> []
	+ matrix<TYPE> matrix<TYPE>
	+ array<TYPE> matrix<TYPE>
	+ matrix<TYPE> array<TYPE>
	+ array<TYPE> array<TYPE>

Default Values:
----------------

* Values can be:
	+ A number
	+ A string
	+ A boolean
	+ Na
	+ A system variable
* Values cannot be:
	+ A list of values
	+ A function
	+ A UDT


# BUILT INS

## Pine Script Indicator functions and variables

| Function/Var           | Description                                        |
| ---------------------- | -------------------------------------------------- |
| `ta.accdist`            | Returns the accumulation/distribution line.        |
| `ta.alma()`             | Returns the Arnaud Legoux Moving Average.          |
| `ta.atr()`              | ATR Returns the Average True Range indicator.      |
| `ta.bb()`               | Returns the Bollinger Bands.                       |
| `ta.bbw()`              | Returns the Bollinger Width indicator.             |
| `ta.cci()`              | Returns the Commodity Channel index.               |
| `ta.cmo()`              | Returns the Chande Momentum Oscillator.            |
| `ta.cog()`              | Returns the Center of Gravity indicator.           |
| `ta.dmi()`              | Returns the Directional Movement indicator.        |
| `ta.ema()`              | Returns the Exponential Moving Average.            |
| `ta.hma()`              | Returns the Hull Moving Average.                   |
| `ta.iii`               | Returns the Intraday Intensity Index indicator.    |
| `ta.kc()`               | Returns the Keltner Channels.                      |
| `ta.kcw()`              | Returns the Keltner Channels width.                |
| `ta.linreg()`           | Returns the Linear Regression Overlay.             |
| `ta.macd()`              | Returns the Moving Average Convergence/Divergence. |
| `ta.mfi()`              | Returns the Money Flow Index.                      |
| `ta.mom()`              | Returns the Momentum indicator.                    |
| `ta.nvi`                | Returns the Negative Volume Index.                 |
| `ta.obv`                | Returns the On-Balance Volume indicator.           |
| `ta.pvi`                | Returns the Positive Volume Index.                 |
| `ta.pvt`                | Returns the Price Volume Trend indicator.          |
| `ta.rma()`              | Returns the Roughness Moving Average.              |
| `ta.roc()`              | Returns the Rate of Change indicator.              |
| `ta.rsi(source, length)` | Returns the Relative Strength Index.               |
| `ta.sar()`              | Returns the Parabolic Stop and Reverse.            |
| `ta.sma()`              | Returns the Simple Moving Average.                 |
| `ta.stoch()`            | Returns the Stochastic oscillator.                 |
| `ta.supertrend()`       | Returns the Supertrend indicator.                  |
| `ta.swma(source)`       | Returns the Smoothed Weighted Moving Average.      |
| `ta.tr`                 | Returns the True Range.                            |
| `ta.tsi()`              | Returns the True Strength Index.                   |
| `ta.vwap`               | Returns the Volume Weighted Average Price.         |
| `ta.vwma()`              | Returns the Volume Weighted Moving Average.        |
| `ta.wad`                | Returns the Williams Accumulation/Distribution.    |
| `ta.wma()`              | Returns the Weighted Moving Average.               |
| `ta.wpr()`              | Returns the Williams %R indicator.                 |
| `ta.wvad`               | Returns the Volume Accumulation/Distribution.      |


## Pine Script Supporting functions

| Function                                 | Description                                                                                  |
| ---------------------------------------- | -------------------------------------------------------------------------------------------- |
| `ta.barsince()`                            | Returns the number of bars since a condition has been true.                                  |
| `ta.change()`                              | Returns the percent change of a bar compared to the previous bar.                            |
| `ta.correlation(source1, source2, length)` | Returns the Pearson’s correlation coefficient between two prices.                            |
| `ta.cross(source1, source2)`               | Returns true if source1 crossed source2 from downward to upward.                             |
| `ta.crossover(source1, source2)`           | Returns true if source1 crossed source2 from downward to upward.                             |
| `ta.crossunder(source1, source2)`          | Returns true if source1 crossed source2 from upward to downward.                             |
| `ta.cum(source)`                           | Returns the cumulative sum of a source.                                                      |
| `ta.dev()`                                 | Returns the standard deviation of a source.                                                  |
| `ta.falling()`                             | Returns true if the current bar’s close price is lower than the previous bar’s close price.  |
| `ta.highest()`                             | Returns the highest value from the source.                                                   |
| `ta.highestbars()`                         | Returns the highest value from the source within n bars.                                     |
| `ta.lowest()`                              | Returns the lowest value from the source.                                                    |
| `ta.lowestbars()`                          | Returns the lowest value from the source within n bars.                                      |
| `ta.median()`                              | Returns the median given the source.                                                           |
| `ta.mode()`                                | Returns the mode given the source.                                                             |
| `ta.percentile_linear_interpolation()`     | Returns the percentile of the data using linear interpolation.                               |
| `ta.percentile_nearest_rank()`             | Returns the percentile of the data using the nearest rank.                                    |
| `ta.percentrank(n)`                        | Returns the percentile rank based on the source within n bars.                               |
| `ta.pivothigh()`                           | Returns the highest high/low that preceded the current bar.                                  |
| `ta.pivotlow()`                            | Returns the lowest high/low that preceded the current bar.                                   |
| `ta.range()`                               | Returns the high to low range of the source.                                                 |
| `ta.rising()`                              | Returns true if the current bar’s close price is higher than the previous bar’s close price. |
| `ta.stdev()`                               | Returns the standard deviation of the source.                                                |
| `ta.valuewhen()`                           | Returns the source’s last value when a condition of a given length was true.                 |
| `ta.variance()`                            | Returns the variance for a given source                                                      |

## Pine Script “math” namespace for math-related functions and variables

| Function                      | Description                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| `math.abs(number)`            | Returns the absolute value of the number.                                               |
| `math.acos(number)`           | Returns the arc cosine of the number.                                                 |
| `math.asin(number)`           | Returns the arc sine of the number.                                                   |
| `math.atan(number)`           | Returns the arc tangent of the number.                                                  |
| `math.avg()`                  | Returns the average of the numbers.                                                     |
| `math.ceil(number)`           | Returns the ceiling of the number.                                                      |
| `math.cos(angle)`             | Returns the cosine of an angle.                                                         |
| `math.exp(number)`            | Returns the exponential of the number.                                              |
| `math.floor(number)`          | Returns the floor of the number.                                                        |
| `math.log(number)`            | Returns the natural logarithm of a number.                                            |
| `math.log10(number)`          | Returns the base-10 logarithm of a number.                                              |
| `math.max()`                  | Returns the maximum of the numbers.                                                     |
| `math.min()`                  | Returns the minimum of the numbers.                                                     |
| `math.pow()`                  | Returns the value of the first number raised to the power of the second number.         |
| `math.random()`               | Returns a random number between 0 and 1.                                              |
| `math.round(number, precision)` | Rounds the number to a given number of decimal places.                                  |
| `math.round_to_mintick(number)` | Rounds the number to the smallest increment allowed by the broker                       |
| `math.sign(number)`           | Returns a 1 for a postive number and a -1 for a negative number, or 0 for a zero number |
| `math.sin(angle)`             | Returns the sine of an angle.                                                           |
| `math.sqrt(number)`           | Returns the square root of a number.                                                      |
| `math.sum()`                  | Returns the sum of the numbers.                                                         |
| `math.tan(angle)`             | Returns the tangent of an angle.                                                        |
| `math.todegrees()`            | Converts an angle from radians to degrees.                                              |
| `math.toradians()`            | Converts an angle from degrees to radians.                                              |

## Pine Script “request” namespace for functions that request external data

| Function                                  | Description                                                                                |
| ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| `request.financial()`                       | Requests financial data such as P/E ratio and market capitalization from an online source. |
| `request.quandl()`                          | Requests a dataset stored online using Quandl.                                             |
| `request.security(<...>, timeframe, <...>)` | Requests a certain security to be plotted on the chart.                                    |
| `request.splits()`                          | Requests stock splits data from an online source.                                          |
| `request.dividends()`                       | Requests dividend information from an online source.                                       |
| `request.earnings()`                        | Requests earnings data from an online source.                                              |

## Pine Script “ticker” namespace for functions that help create tickers

| Function             | Description                     |
| -------------------- | ------------------------------- |
| `ticker.heikinashi()`  | Creates a Heikin-Ashi ticker.   |
| `ticker.kagi()`        | Creates a Kagi chart.           |
| `ticker.linebreak()`   | Creates a Line Break chart.     |
| `ticker.pointfigure()` | Creates a Point & Figure chart. |
| `ticker.renko()`       | Creates a Renko chart.          |
| `ticker.new()`         | Creates a new ticker.           |


## Pine Script™ Colors

The following functions are available for colors.

| Function  | Description                                    |
| --------- | ---------------------------------------------- |
| `color.a`   | Returns the alpha component of the color.      |
| `color.b`   | Returns the blue component of the color.       |
| `color.g`   | Returns the green component of the color.      |
| `color.r`   | Returns the red component of the color.        |
| `color.rgb` | Returns a color from red, green, blue , transp |

## Pine Script™ Time

The following functions are available for time.

| Function         | Description                                        |
| ---------------- | -------------------------------------------------- |
| `time.dayofmonth`  | Returns the day of the month.                      |
| `time.dayofweek`   | Returns the day of the week.                       |
| `time.dayofyear`   | Returns the day of the year.                       |
| `time.hour`        | Returns the hour.                                  |
| `time.isdst`       | Returns whether daylight saving time is in effect. |
| `time.millisecond` | Returns the millisecond.                           |
| `time.minute`      | Returns the minute.                                |
| `time.month`       | Returns the month.                                 |
| `time.second`      | Returns the second.                                |
| `time.timezone`    | Returns the time zone.                             |
| `time.tzoffset`    | Returns the time zone offset.                      |
| `time.year`        | Returns the year.                                  |


## Python String Functions

| Function                                                | Description                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `str.length(string) -> int`                             | Returns the length of the string.                                                                       |
| `str.tonumber(string) -> float`                         | Converts the string to a number.                                                                        |
| `str.tostring(x) -> string`                             | Converts the input to a string.                                                                         |
| `str.format(string, ...) -> string`                     | Formats the string, replacing placeholders with provided values.                                        |
| `str.replace(string, substring, replacement) -> string` | Replaces occurrences of substring with replacement.                                                     |
| `str.contains(string, substring) -> bool`               | Checks if the string contains the substring.                                                            |
| `str.slice(string, start, end) -> string`               | Extracts a section of the string.                                                                       |
| `str.split(string, separator) -> array[string]`         | Splits the string into an array of strings based on the separator.                                      |
| `str.toupper(string) -> string`                         | Converts the string to uppercase.                                                                       |
| `str.tolower(string) -> string`                         | Converts the string to lowercase.                                                                       |
| `str.trim(string) -> string`                            | Removes whitespace from both ends of the string.                                                        |
| `str.indexof(string, substring, fromIndex) -> int`      | Returns the index of the first occurrence of substring in the string, starting the search at fromIndex. |
| `str.lastindexof(string, substring, fromIndex) -> int`  | Returns the index of the last occurrence of substring in the string, starting the search at fromIndex.  |
| `str.startswith(string, substring) -> bool`             | Checks if the string starts with the substring.                                                         |
| `str.endswith(string, substring) -> bool`               | Checks if the string ends with the substring.                                                           |
| `str.repeat(string, count) -> string`                   | Returns a new string consisting of count copies of the string.                                          |
| `str.insert(string, index, substring) -> string`        | Inserts substring into the string at the specified index.                                               |
| `str.remove(string, index, count) -> string`            | Removes count characters from the string starting at index.                                             |


## Pine Script™ Arrays

Arrays allow you to store multiple values in a single variable. Each value in the array is identified by a unique index number. The first element in an array is always 0, the second element is 1, and so on.

| Function                                 | Description                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| array.abs ()                             | Returns the absolute value of each element in the array.                                                      |
| array.avg ()                             | Returns the average of the array elements.                                                                    |
| array.binary_search ()                   | Searches for a value in a sorted array and returns the index of the element that matches the value.           |
| array.binary_search_leftmost ()          | Searches for a value in a sorted array and returns the index of the leftmost element that matches the value.  |
| array.binary_search_rightmost ()         | Searches for a value in a sorted array and returns the index of the rightmost element that matches the value. |
| array.clear ()                           | Removes all elements from the array.                                                                          |
| array.concat ()                          | Concatenates two arrays.                                                                                      |
| array.copy ()                            | Copies the array.                                                                                             |
| array.covariance ()                      | Returns the covariance of the array elements.                                                                 |
| array.every ()                           | Tests whether all elements in the array pass the provided test function.                                      |
| array.fill ()                            | Fills the array with a value.                                                                                 |
| array.first ()                           | Returns the first element in the array.                                                                       |
| array.from ()                            | Creates an array from a list of values.                                                                       |
| array.get ()                             | Returns the element at the specified index.                                                                   |
| array.includes ()                        | Returns true if the array contains the specified value.                                                       |
| array.indexof ()                         | Returns the index of the first occurrence of a value in the array.                                            |
| array.insert ()                          | Inserts a new element at the specified index.                                                                 |
| array.join ()                            | Joins all elements of an array into a string.                                                                 |
| array.last ()                            | Returns the last element in the array.                                                                        |
| array.lastindexof ()                     | Returns the index of the last occurrence of a value in the array.                                             |
| array.max ()                             | Returns the maximum value in the array.                                                                       |
| array.median ()                          | Returns the median of the array elements.                                                                     |
| array.min ()                             | Returns the minimum value in the array.                                                                       |
| array.mode ()                            | Returns the mode of the array elements.                                                                       |
| array.new\<bool\>()                      | Creates a new array of booleans.                                                                              |
| array.new\<box\>()                       | Creates a new array of boxes.                                                                                 |
| array.new\<color\>()                     | Creates a new array of colors.                                                                                |
| array.new\<float\>()                     | Creates a new array of floats.                                                                                |
| array.new\<int\>()                       | Creates a new array of integers.                                                                              |
| array.new\<label\>()                     | Creates a new array of labels.                                                                                |
| array.new\<line\>()                      | Creates a new array of lines.                                                                                 |
| array.new\<linefill\>()                  | Creates a new array of linefills.                                                                             |
| array.new\<string\>()                    | Creates a new array of strings.                                                                               |
| array.new\<table\>()                     | Creates a new array of tables.                                                                                |
| array.new\<type\>()                      | Creates a new array of the specified type.                                                                    |
| array.percentile_linear_interpolation () | Returns the value at the given percentile using linear interpolation.                                         |
| array.percentile_nearest_rank ()         | Returns the value at the given percentile using the nearest rank method.                                      |
| array.percentrank ()                     | Returns the percentile rank of a value in the array.                                                          |
| array.pop ()                             | Removes the last element from the array and returns it.                                                       |
| array.push ()                            | Adds one or more elements to the end of the array and returns the new length of the array.                    |
| array.range ()                           | Creates a new array with a range of numbers.                                                                  |
| array.remove ()                          | Removes the element at the specified index from the array.                                                    |
| array.reverse ()                         | Reverses the order of the elements in the array.                                                              |
| array.set ()                             | Sets the element at the specified index.                                                                      |
| array.shift ()                           | Removes the first element from the array and returns it.                                                      |
| array.size ()                            | Returns the number of elements in the array.                                                                  |
| array.slice ()                           | Returns a section of the array.                                                                               |
| array.some ()                            | Tests whether at least one element in the array is true if bool, or if any value exists otherwise             |
| array.sort ()                            | Sorts the elements of an array in place.                                                                      |
| array.sort ()                            | Sorts the elements of the array.                                                                              |
| array.sort_indices ()                    | Returns a new array containing the indices of the original array's elements in sorted order.                  |
| array.splice ()                          | Adds and/or removes elements from the array.                                                                  |
| array.standardize ()                     | Standardizes the array elements by subtracting the mean and dividing by the standard deviation.               |
| array.stdev ()                           | Returns the standard deviation of the array elements.                                                         |
| array.sum ()                             | Returns the sum of the array elements.                                                                        |
| array.unshift ()                         | Adds one or more elements to the beginning of the array and returns the new length of the array.              |
| array.variance ()                        | Returns the variance of the array elements.                                                                   |

## Pine Script™ Matrices

The following functions are available for matrices as functions and methods

| Function                                                                     | Description                                                                                 |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| ---                                                                          | ---                                                                                         |
| matrix.add\_col(matrix\_id, column, array\_id)                               | Inserts a new column into the matrix at the specified index.                                |
| matrix.add\_row(matrix\_id, row, array\_id)                                  | Inserts a new row into the matrix at the specified index.                                   |
| matrix.avg                                                                   | Returns the average of a matrix                                                             |
| matrix.col(matrix\_id, column)                                               | Retrieves all values from a specified column as an array.                                   |
| matrix.columns                                                               | Returns the number of columns in a matrix                                                   |
| matrix.concat(matrix\_id1, matrix\_id2, dimension)                           | Concatenates two matrices along the specified dimension.                                    |
| matrix.copy(matrix\_id)                                                      | Creates a shallow copy of the matrix.                                                       |
| matrix.det(matrix\_id)                                                       | Calculates the determinant of the matrix.                                                   |
| matrix.diff(matrix\_id, dimension)                                           | Calculates the difference between adjacent elements along the specified dimension.          |
| matrix.eigenvalues                                                           | Returns the eigenvalues of a matrix                                                         |
| matrix.eigenvectors                                                          | Returns the eigenvectors of a matrix                                                        |
| matrix.elements_count                                                        | Returns the number of elements in a matrix                                                  |
| matrix.fill(matrix\_id, value, from\_row, to\_row, from\_column, to\_column) | Fills the matrix or a specified range within the matrix with a given value.                 |
| matrix.get(matrix\_id, row, column)                                          | Retrieves the value from a specified row and column in the matrix.                          |
| matrix.inv(matrix\_id)                                                       | Calculates the inverse of the matrix.                                                       |
| matrix.is_antidiagonal                                                       | Returns true if a matrix is antidiagonal                                                    |
| matrix.is_antisymmetric                                                      | Returns true if a matrix is antisymmetric                                                   |
| matrix.is_binary                                                             | Returns true if a matrix is binary                                                          |
| matrix.is_diagonal                                                           | Returns true if a matrix is diagonal                                                        |
| matrix.is_identity                                                           | Returns true if a matrix is identity                                                        |
| matrix.is_square                                                             | Returns true if a matrix is square                                                          |
| matrix.is_stochastic                                                         | Returns true if a matrix is stochastic                                                      |
| matrix.is_symmetric                                                          | Returns true if a matrix is symmetric                                                       |
| matrix.is_triangular                                                         | Returns true if a matrix is triangular                                                      |
| matrix.is_zero                                                               | Returns true if a matrix is zero                                                            |
| matrix.kron                                                                  | Returns the Kronecker product of two matrices                                               |
| matrix.max                                                                   | Returns the maximum value of a matrix                                                       |
| matrix.median                                                                | Returns the median of a matrix                                                              |
| matrix.min                                                                   | Returns the minimum value of a matrix                                                       |
| matrix.mode                                                                  | Returns the mode of a matrix                                                                |
| matrix.mult(matrix\_id1, matrix\_id2)                                        | Performs matrix multiplication.                                                             |
| matrix.new\<type\>(rows, columns, initial\_value)                            | Creates a new matrix instance with specified dimensions and initial value for all elements. |
| matrix.pinv(matrix\_id)                                                      | Calculates the pseudo-inverse of the matrix.                                                |
| matrix.pow                                                                   | Returns the power of a matrix                                                               |
| matrix.rank(matrix\_id)                                                      | Calculates the rank of the matrix.                                                          |
| matrix.remove\_col(matrix\_id, column)                                       | Removes a column from the matrix.                                                           |
| matrix.remove\_row(matrix\_id, row)                                          | Removes a row from the matrix.                                                              |
| matrix.reshape(matrix\_id, rows, columns)                                    | Changes the shape of the matrix to the specified dimensions.                                |
| matrix.reverse(matrix\_id, dimension)                                        | Reverses the elements in the matrix along the specified dimension (rows or columns).        |
| matrix.row(matrix\_id, row)                                                  | Retrieves all values from a specified row as an array.                                      |
| matrix.rows                                                                  | Returns the number of rows in a matrix                                                      |
| matrix.set(matrix\_id, row, column, value)                                   | Sets the value at a specified row and column in the matrix.                                 |
| matrix.sort(matrix\_id, dimension, comparator)                               | Sorts the elements in the matrix along the specified dimension using a comparator function. |
| matrix.submatrix                                                             | Returns a submatrix from a matrix                                                           |
| matrix.sum(matrix\_id, dimension)                                            | Calculates the sum of elements along the specified dimension.                               |
| matrix.swap\_columns(matrix\_id, column1, column2)                           | Swaps two columns in the matrix.                                                            |
| matrix.swap\_rows(matrix\_id, row1, row2)                                    | Swaps two rows in the matrix.                                                               |
| matrix.trace                                                                 | Returns the trace of a matrix                                                               |
| matrix.transpose(matrix\_id)                                                 | Transposes the matrix (swaps rows and columns).                                             |
