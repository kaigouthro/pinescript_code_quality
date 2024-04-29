# Maps

- Introduction
- Declaring a map

  - Using `var` and `varip` keywords

- Reading and writing

  - Putting and getting key-value pairs
  - Inspecting keys and values

    - `map.keys()` and `map.values()`
    - `map.contains()`

  - Removing key-value pairs
  - Combining maps

- Looping through a map
- Copying a map

  - Shallow copies
  - Deep copies

- Scope and history
- Maps of other collections

Note This page has advanced material. If you are a beginner in Pine Script™ programming, we recommend becoming familiar with other more accessible features before venturing here.

## Introduction

Pine Script™ Maps store elements in key-value pairs. They allow scripts to collect multiple value references associated with unique identifiers (keys).

Unlike arrays and matrices, maps are considered unordered collections. Scripts can access a map's values quickly by referencing the keys from the key-value pairs rather than traversing an internal index.

A map's keys can be of any fundamental type, and its values can be of any built-in or user-defined type. Maps cannot directly use other collections (maps, arrays, or matrices) as values, but they can hold UDT instances containing these data structures within their fields. See this section for more information.

As with other collections, maps can contain up to 100,000 elements in total. Since each key-value pair in a map consists of two elements (a unique key and its associated value), the maximum number of key-value pairs a map can hold is 50,000.

## Declaring a map

Pine Script™ uses the following syntax to declare maps:

```
[var/varip ][map<keyType, valueType> ]<identifier> = <expression>
```

Where `<keyType, valueType>` is the map's type template that declares the types of keys and values it will contain, and the `<expression>` returns either a map instance or `na`.

When declaring a map variable assigned to `na`, users must include the map keyword followed by a type template to tell the compiler that the variable can accept maps with `keyType` keys and `valueType` values.

For example, this line of code declares a new `myMap` variable that can accept map instances holding pairs of string keys and float values:

```lua
map<string, float> myMap = na
```

When the `<expression>` is not `na`, the compiler does not require explicit type declaration, as it will infer the type information from the assigned map object.

This line declares a `myMap` variable assigned to an empty map with string keys and float values. Any maps assigned to this variable later must have the same key and value types:

```lua
myMap = map.new<string, float>()
```

### Using `var` and `varip` keywords

Users can include the var or varip keywords to instruct their scripts to declare map variables only on the first chart bar. Variables that use these keywords point to the same map instances on each script iteration until explicitly reassigned.

For example, this script declares a `colorMap` variable assigned to a map that holds pairs of string keys and color values on the first chart bar. The script displays an `oscillator` on the chart and uses the values it put into the `colorMap` on the first bar to color the plots on all bars:

```lua
//@version=5
indicator("var map demo")

//@variable A map associating color values with string keys.
var colorMap = map.new<string, color>()

// Put `<string, color>` pairs into `colorMap` on the first bar.
if bar_index == 0
    colorMap.put("Bull", color.green)
    colorMap.put("Bear", color.red)
    colorMap.put("Neutral", color.gray)

//@variable The 14-bar RSI of `close`.
float oscillator = ta.rsi(close, 14)

//@variable The color of the `oscillator`.
color oscColor = switch oscillator > 50 => colorMap.get("Bull") oscillator < 50 => colorMap.get("Bear") => colorMap.get("Neutral")

// Plot the `oscillator` using the `oscColor` from our `colorMap`.
plot(oscillator, "Histogram", oscColor, 2, plot.style_histogram, histbase = 50)
plot(oscillator, "Line", oscColor, 3)
```

Map variables declared using varip behave as ones using var on historical data but update their key-value pairs for real-time bars on each new price tick. Maps assigned to varip variables can only hold values of int, float, bool, color, or string types or user-defined types that exclusively contain these types or collections (arrays, matrices, or maps) of these types.

## Reading and writing

### Putting and getting key-value pairs

The map.put() function is the primary method to put a new key-value pair into a map. It associates the key argument with the value argument and adds the pair to the specified map. If the key argument in the map.put() call already exists in the map's keys, the new pair passed into the function will replace the existing one. To retrieve the value from a map associated with a given key, use map.get(). This function returns the value if the map contains the key; otherwise, it returns na.

For example, this script calculates the difference between the bar_index values from when close was last rising and falling over a given length with the help of map.put() and map.get() methods. The script puts a ("Rising", bar_index) pair into the data map when the price is rising and puts a ("Falling", bar_index) pair into the map when the price is falling. It then puts a pair containing the "Difference" between the "Rising" and "Falling" values into the map and plots its value on the chart:

```lua
//@version=5
indicator("Putting and getting demo")

//@variable The length of the ta.rising() and ta.falling() calculation.
int length = input.int(2, "Length")

//@variable A map associating string keys with int values.
var data = map.new<string, int>()

// Put a new ("Rising", bar_index) pair into the data map when close is rising.
if ta.rising(close, length)
    data.put("Rising", bar_index)
// Put a new ("Falling", bar_index) pair into the data map when close is falling.
if ta.falling(close, length)
    data.put("Falling", bar_index)

// Put the "Difference" between current "Rising" and "Falling" values into the data map.
data.put("Difference", data.get("Rising") - data.get("Falling"))

//@variable The difference between the last "Rising" and "Falling" bar_index.
int index = data.get("Difference")

//@variable Returns color.green when index is positive, color.red when negative, and color.gray otherwise.
color indexColor = index > 0 ? color.green : index < 0 ? color.red : color.gray

plot(index, color = indexColor, style = plot.style_columns)
```

Note that this script replaces the values associated with the "Rising", "Falling", and "Difference" keys on successive data.put() calls, as each of these keys is unique and can only appear once in the data map. Replacing the pairs in a map does not change the internal insertion order of its keys.

### Inspecting keys and values

#### map.keys() and map.values()

To retrieve all keys and values put into a map, use map.keys() and map.values(). These functions return arrays containing all key and value references within a map, respectively. Modifying the arrays returned from either of these functions does not affect the original map. Although maps are unordered collections, Pine Script™ internally maintains the insertion order of a map's key-value pairs. Therefore, the map.keys() and map.values() functions always return arrays with their elements ordered based on the map's insertion order.

The script below demonstrates this by displaying the key and value arrays from an m map in a label once every 50 bars:

```lua
//@version=5
indicator("Keys and values demo")

if bar_index % 50 == 0
    //@variable A map containing pairs of string keys and float values.
    m = map.new<string, float>()

    // Put pairs into m. The map will maintain this insertion order.
    m.put("First", math.round(math.random(0, 100)))
    m.put("Second", m.get("First") + 1)
    m.put("Third", m.get("Second") + 1)

    //@variable An array containing the keys of m in their insertion order.
    array<string> keys = m.keys()
    //@variable An array containing the values of m in their insertion order.
    array<float> values = m.values()

    //@variable A label displaying the size of m and the keys and values arrays.
    label debugLabel = label.new(
         bar_index, 0,
         str.format("Pairs: {0}\nKeys: {1}\nValues: {2}", m.size(), keys, values),
         color = color.navy, style = label.style_label_center,
         textcolor = color.white, size = size.huge
     )
```

Note that the elements in m.keys() and m.values() arrays point to the same keys and values in the m map. Consequently, when modifying an element in one of these arrays, the change also affects the corresponding key or value in the map.

#### map.contains()

To check if a specific key exists within a map, use map.contains(). This function is a convenient alternative to calling array.includes() on the array returned from map.keys().

For example, this script checks if various keys exist within an m map and displays the results in a label:

```lua
//@version=5
indicator("Inspecting keys demo")

//@variable A map containing string keys and string values.
m = map.new<string, string>()

// Put key-value pairs into the map.
m.put("A", "B")
m.put("C", "D")
m.put("E", "F")

//@variable An array of keys to check for in m.
array<string> testKeys = array.from("A", "B", "C", "D", "E", "F")

//@variable An array containing all valid elements from testKeys found in the keys of m.
array<string> mappedKeys = array.new<string>()

for key in testKeys
    // Add the key to mappedKeys if m contains it.
    if m.contains(key)
        mappedKeys.push(key)

//@variable A string representing the testKeys array and the elements found within the keys of m.
string testText = str.format("Tested keys: {0}\nKeys found: {1}", testKeys, mappedKeys)

if bar_index == last_bar_index - 1
    //@variable Displays the testText in a label at the bar_index before the last.
    label debugLabel = label.new(
         bar_index, 0, testText, style = label.style_label_center,
         textcolor = color.white, size = size.huge
     )
```

### Removing key-value pairs

To remove a specific key-value pair from a map, use map.remove(). This function removes the key and its associated value from the map while preserving the insertion order of other key-value pairs. It returns the removed value if the map contained the key; otherwise, it returns na.

To remove all key-value pairs from a map at once, use map.clear().

The script below creates a new m map, puts key-value pairs into the map, uses m.remove() within a loop to remove each valid key listed in the removeKeys array, then calls m.clear() to remove all remaining key-value pairs. It uses a custom debugLabel() method to display the size, keys, and values of m after each change:

```lua
//@version=5
indicator("Removing key-value pairs demo")

//@function Returns a label to display the keys and values from a map.
method debugLabel(
     map<string, int> this, int barIndex = bar_index,
     color bgColor = color.blue, string note = ""
 ) =>
    //@variable A string representing the size, keys, and values in this map.
    string repr = str.format(
         "{0}\nSize: {1}\nKeys: {2}\nValues: {3}",
         note, this.size(), str.tostring(this.keys()), str.tostring(this.values())
     )
    label.new(
         barIndex, 0, repr, color = bgColor, style = label.style_label_center,
         textcolor = color.white, size = size.huge
     )

if bar_index == last_bar_index - 1
    //@variable A map containing string keys and int values.
    m = map.new<string, int>()

    // Put key-value pairs into m.
    for [i, key] in array.from("A", "B", "C", "D", "E")
        m.put(key, i)
    m.debugLabel(bar_index, color.green, "Added pairs")

    //@variable An array of keys to remove from m.
    array<string> removeKeys = array.from("B", "B", "D", "F", "a")

    // Remove each key in removeKeys from m.
    for key in removeKeys
        m.remove(key)
    m.debugLabel(bar_index + 10, color.red, "Removed pairs")

    // Remove all remaining keys from m.
    m.clear()
    m.debugLabel(bar_index + 20, color.purple, "Cleared the map")
```

### Combining maps

Scripts can combine two maps using map.put_all(). This function puts all key-value pairs from the second map into the first map, in their insertion order. If any keys in the second map are also present in the first map, this function replaces the existing key-value pairs without affecting their initial insertion order.

This example shows a user-defined hexMap() function that maps decimal int keys to string representations of their hexadecimal forms. The script uses this function to create two maps, mapA and mapB, then uses mapA.put_all(mapB) to put all key-value pairs from mapB into mapA.

The script uses a custom debugLabel() function to display labels showing the keys and values of mapA and mapB, then another label displaying the contents of mapA after putting all key-value pairs from mapB into it:

```lua
//@version=5
indicator("Combining maps demo", "Hex map")

//@variable An array of string hex digits.
var array<string> hexDigits = str.split("0123456789ABCDEF", "")

//@function Returns a hexadecimal string for the specified value.
hex(int value) =>
    //@variable A string representing the hex form of the value.
    string result = ""
    //@variable A temporary value for digit calculation.
    int tempValue = value
    while tempValue > 0
        //@variable The next integer digit.
        int digit = tempValue % 16
        // Add the hex form of the digit to the result.
        result := hexDigits.get(digit) + result
        // Divide the tempValue by the base.
        tempValue := int(tempValue / 16)
    result

//@function Returns a map holding the numbers as keys and their hex strings as values.
hexMap(array<int> numbers) =>
    //@variable A map associating int keys with string values.
    result = map.new<int, string>()
    for number in numbers
        // Put a pair containing the number and its hex() representation into the result.
        result.put(number, hex(number))
    result

//@variable A map with int keys and hexadecimal string values.
map<int, string> mapA = hexMap(array.from(101, 202, 303, 404))
//@variable A map containing key-value pairs to add to mapA.
map<int, string> mapB = hexMap(array.from(303, 404, 505, 606, 707, 808))

// Put all pairs from mapB into mapA.
mapA.put_all(mapB)

//@variable A label showing the contents of mapA.
label debugLabel = label.new(
     bar_index, 0, color = color.navy, textcolor = color.white, size = size.huge
 )
debugLabel.set_text("mapA: " + str.tostring(mapA))
```

## Looping through a map

Pine Script allows scripts to iteratively access the keys and values in a map using a for...in loop. The loop iterates over the key-value pairs of a map, returning the key and value on each iteration. This loop is designed specifically for maps and ensures that the key-value pairs are accessed in their insertion order.

For example, the following line of code loops through each key-value pair in the thisMap map, starting from the first pair put into it:

```lua
for [key, value] in thisMap
```

Let's use this structure to write a script that displays a map's key-value pairs in a table. In the example below, we've defined a custom toTable() method that creates a table and uses a for...in loop to iterate over the map's key-value pairs and populate the table cells. The script uses this method to visualize a map containing length-bar averages of price and volume data:

```lua
//@version=5
indicator("Looping through a map demo", "Table of averages")

//@variable The length of the moving average.
int length = input.int(20, "Length")

//@variable Displays the pairs of thisMap within a table.
//@param    this A map with string keys and float values.
//@param    position The position of the table on the chart.
//@param    header The string to display on the top row of the table.
//@returns  A new table object with cells displaying each pair in this.
method toTable(map<string, float> this, string position = position.middle_center, string header = na) =>
    tablename = table.new(position)
    table.column(tablename, "Key", string, color="white", bgcolor="black")
    table.column(tablename, "Value", bgcolor="white")
    table.header(tablename, header)
    keylist = this.keys()
    length = array.size(keylist)
    for i = 0 to length - 1
        table.cell(tablename, i, 0, keylist[i])
        table.cell(tablename, i, 1, str.tostring(this.get(keylist[i])))
    tablename

//@variable A map with string keys and float values.
var thisMap = map.new<string, float>()
thisMap.put("Key 1", 100)
thisMap.put("Key 2", 200)
thisMap.put("Key 3", 300)
thisMap.put("Key 4", 400)

//@variable Displays the thisMap in a table.
toTable(thisMap)
```

# Maps

**Introduction**

- Dec

## Copying a map

### Shallow copies

Scripts can make a shallow copy of a map `id` using the map.copy() function. Modifying a shallow copy does not affect the original `id` map or its insertion order.

Example script:

```lua
//@version=5
indicator("Shallow copy demo")

method debugLabel(map<string, float> this, int barIndex = bar_index, color bgColor = color.blue, color textColor = color.white, string note = "") =>
    labelText = note + "\n{" for [key, value] in this labelText += str.format("{0}: {1}, ", key, value)labelText := str.replace(labelText, ", ", "}", this.size() - 1) if barstate.ishistorylabel result = label.new(barIndex, 0, labelText, color = bgColor, style = label.style_label_center, textcolor = textColor, size = size.huge)

if bar_index == last_bar_index - 1
    m = map.new<string, float>()
    for key in array.from("A", "B", "C", "D")
        m.put(key, math.random(0, 10))
    mCopy = m.copy()
    for [i, key] in mCopy.keys()
        mCopy.put(key, i)
    m.debugLabel(bar_index, note = "Original")
    mCopy.debugLabel(bar_index + 10, color.purple, note = "Copied and changed")
```

### Deep copies

While a shallow copy is suitable for copying maps with values of a fundamental type, shallow copies of a map holding values of a reference type can lead to unintended side effects. To make changes to copied maps independent of the original, a deep copy is needed. This creates a new map with copies of each value from the original map.

Example script:

```lua
//@version=5
indicator("Deep copy demo")

method deepCopy(map<string, label> this) =>
    result = map.new<string, label>()
    for [key, value] in this
        result.put(key, value.copy())
    result

var original = map.new<string, label>()

if bar_index == last_bar_index - 1
    map.put(
         original, "Test",
         label.new(bar_index, 0, "Original", textcolor = color.white, size = size.huge)
     )

    map<string, label> shallow = original.copy()
    map<string, label> deep = original.deepCopy()

    label shallowLabel = shallow.get("Test")
    label deepLabel = deep.get("Test")

    original.get("Test").set_y(label.all.size())

    shallowLabel.set_text("Shallow copy")
    shallowLabel.set_color(color.red)
    shallowLabel.set_style(label.style_label_up)

    deepLabel.set_text("Deep copy")
    deepLabel.set_color(color.navy)
    deepLabel.set_style(label.style_label_left)
    deepLabel.set_x(bar_index + 5)
```

Note: The `deepCopy()` method creates a new map `result` and copies each value from `this` map into it.

## Scope and history

Like other collections in Pine, maps leave historical trails, allowing scripts to access past map instances using the history-referencing operator []. Maps can be assigned to global variables and interacted with from the scopes of functions, methods, and conditional structures.

Example script:

```lua
//@version=5
indicator("Scope and history demo", overlay = true)

float source = input.source(close, "Source")

globalData = map.new<int, float>()

update() =>
    map<int, float> previous = globalData[1]

    if na(previous)
        for i = 10 to 200
            globalData.put(i, source)
    else
        for [key, value] in previous
            float alpha = 2.0 / (key + 1.0)
            float ema = (1.0 - alpha) * value + alpha * source
            globalData.put(key, ema)

update()

array<float> values = globalData.values()

plot(values.max(), "Max EMA", color.green, 2)
plot(values.min(), "Min EMA", color.red, 2)
plot(globalData.get(50), "50-bar EMA", color.orange, 3)
```

## Maps of other collections

Maps cannot directly use other maps, arrays, or matrices as values, but they can hold values of a user-defined type that contains collections within its fields.

Example script:

```lua
//@version=5
indicator("Nested map demo")

string tf = input.timeframe("D", "Timeframe")
string symbol1 = input.symbol("EURUSD", "Symbol 1")
string symbol2 = input.symbol("GBPUSD", "Symbol 2")
string symbol3 = input.symbol("EURGBP", "Symbol 3")

type Wrapper
    map<string, float> data

requestData(string tickerID, string timeframe) =>
    [o, h, l, c, v] = request.security(
         tickerID, timeframe,
         [open, high, low, close, volume]
     )
    result = map.new<string, float>()
    result.put("Open", o)
    result.put("High", h)
    result.put("Low", l)
    result.put("Close", c)
    result.put("Volume", v)
    Wrapper.new(result)

method toString(map<string, Wrapper> this) =>
    string result = "{"
    for [key1, wrapper] in this
        result += key1
        string innerStr = ": {"
        for [key2, value] in wrapper.data
            innerStr += str.format("{0}: {1}, ", key2, str.tostring(value))
        result += str.replace(innerStr, ", ", "},\n", wrapper.data.size() - 1)
    result := str.replace(result, ",\n", "}", this.size() - 1)
    result

var mapOfMaps = map.new<string, Wrapper>()
var debugLabel = label.new(
     bar_index, 0, color = color.navy, textcolor = color.white, size = size.huge,
     style = label.style_label_center, text_font_family = font.family_monospace
 )

mapOfMaps.put(symbol1, requestData(symbol1, tf))
mapOfMaps.put(symbol2, requestData(symbol2, tf))
mapOfMaps.put(symbol3, requestData(symbol3, tf))

debugLabel.set_text(mapOfMaps.toString())
debugLabel.set_x(bar_index)
```

Note: The `toString()` method creates a string representation of the nested maps using a custom format.






# Full example syntax:

```lua
//@version=5
indicator("Combined Example")

//@function Returns a label to display the keys and values from a map.
method debugLabel(map<string, float> this, int barIndex = bar_index, color bgColor = color.blue, color textColor = color.white, string note = "") =>
    labelText = note + "\n{" 
    for [key, value] in this
        if barstate.ishistory
            labelresult = label.new(barIndex, 0, labelText, color = bgColor, style = label.style_label_center, textcolor = textColor, size = size.huge)
        labelText := str.replace(labelText, ", ", "}", this.size() - 1) 
        labelText += str.format("{0}: {1}, ", key, value)

//@variable A map containing pairs of string keys and float values.
var data = map.new<string, float>()

// Put a new ("Rising", bar_index) pair into the data map when close is rising.
if ta.rising(close, 2)
    data.put("Rising", bar_index)
// Put a new ("Falling", bar_index) pair into the data map when close is falling.
if ta.falling(close, 2)
    data.put("Falling", bar_index)

// Put the "Difference" between current "Rising" and "Falling" values into the data map.
data.put("Difference", data.get("Rising") - data.get("Falling"))

//@variable The difference between the last "Rising" and "Falling" bar_index.
int index = int(data.get("Difference"))

//@variable Returns color.green when index is positive, color.red when negative, and color.gray otherwise.
color indexColor = index > 0 ? color.green : index < 0 ? color.red : color.gray

plot(index, color = indexColor, style = plot.style_columns)

//@variable A map with int keys and hexadecimal string values.
var thisMap = map.new<int, string>()

import kaigouthro/Hex/1 as hex

for number in array.from(101, 202, 303, 404)
    thisMap.put(number, hex.fromDigits(number))

if bar_index == last_bar_index - 1
    m = map.new<string, float>()
    for key in array.from("A", "B", "C", "D")
        m.put(key, math.random(0, 10))
    mCopy = m.copy()
    for [i, key] in mCopy.keys()
        mCopy.put(key, i)
    m.debugLabel(bar_index, note = "Original")
    m.copy().debugLabel(bar_index + 10, color.purple, note = "Copied and changed")
    
float source = input.source(close, "Source")

globalData = map.new<int, float>()

update() =>
    map<int, float> previous = globalData[1]

    if na(previous)
        for i = 10 to 200
            globalData.put(i, source)
    else
        for [key, value] in previous
            float alpha = 2.0 / (key + 1.0)
            float ema = (1.0 - alpha) * value + alpha * source
            globalData.put(key, ema)

update()

array<float> values = globalData.values()

plot(values.max(), "Max EMA", color.green, 2)
plot(values.min(), "Min EMA", color.red, 2)
plot(globalData.get(50), "50-bar EMA", color.orange, 3)

//@variable The length of the moving average.
int length = input.int(20, "Length")

//@variable An array of string hex digits.
var array<string> hexDigits = str.split("0123456789ABCDEF", "")

//@function Returns a hexadecimal string for the specified value.
hex(int value) =>
    //@variable A string representing the hex form of the value.
    string result = ""
    //@variable A temporary value for digit calculation.
    int tempValue = value
    while tempValue > 0
        //@variable The next integer digit.
        int digit = tempValue % 16
        // Add the hex form of the digit to the result.
        result := hexDigits.get(digit) + result
        // Divide the tempValue by the base.
        tempValue := int(tempValue / 16)
    result

//@function Returns a map holding the numbers as keys and their hex strings as values.
hexMap(array<int> numbers) =>
    //@variable A map associating int keys with string values.
    result = map.new<int, string>()
    for number in numbers
        // Put a pair containing the number and its hex() representation into the result.
        result.put(number, hex(number))
    result

//@variable A map with int keys and hexadecimal string values.
map<int, string> mapA = hexMap(array.from(101, 202, 303, 404))
//@variable A map containing key-value pairs to add to mapA.
map<int, string> mapB = hexMap(array.from(303, 404, 505, 606, 707, 808))

// Put all pairs from mapB into mapA.
mapA.put_all(mapB)

//@variable A label showing the contents of mapA.
label debugLabel = label.new(
       bar_index, 0, str.tostring(mapA.values()),
       textcolor = color.white, size = size.huge
   )

string tf = input.timeframe("D", "Timeframe")
string symbol1 = input.symbol("EURUSD", "Symbol 1")
string symbol2 = input.symbol("GBPUSD", "Symbol 2")
string symbol3 = input.symbol("EURGBP", "Symbol 3")

type Wrapper
    map<string, float> data

requestData(string tickerID, string timeframe) =>
    [o, h, l, c, v] = request.security(
         tickerID, timeframe,
         [open, high, low, close, volume]
     )
    result = map.new<string, float>()
    result.put("Open", o)
    result.put("High", h)
    result.put("Low", l)
    result.put("Close", c)
    result.put("Volume", v)
    Wrapper.new(result)

method toString(map<string, Wrapper> this) =>
    string result = "{"
    for [key1, wrapper] in this
        result += key1
        string innerStr = ": {"
        for [key2, value] in wrapper.data
            innerStr += str.format("{0}: {1}, ", key2, str.tostring(value))
        result += str.replace(innerStr, ", ", "},\n", wrapper.data.size() - 1)
    result := str.replace(result, ",\n", "}", this.size() - 1)
    result

var mapOfMaps = map.new<string, Wrapper>()
debugLabel := label.new(
      bar_index, 0, color = color.navy, textcolor = color.white, size = size.huge,
     style = label.style_label_center, text_font_family = font.family_monospace
  )

mapOfMaps.put(symbol1, requestData(symbol1, tf))
mapOfMaps.put(symbol2, requestData(symbol2, tf))
mapOfMaps.put(symbol3, requestData(symbol3, tf))

debugLabel.set_text(mapOfMaps.toString())
debugLabel.set_x(bar_index)
```
