[Introduction](#id1)
-------------------------------------------------------------------

This guide documents the **changes** made to Pine Script® from v4 to v5. It will guide you in the adaptation of existing Pine scripts to Pine Script® v5. See our [Release notes](Release_notes.html#pagereleasenotes-october2021) for a list of the **new** features in Pine Script® v5.

The most frequent adaptations required to convert older scripts to v5 are:

*   Changing [study()](https://www.tradingview.com/pine-script-reference/v4/#fun_study) for [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator) (the function’s signature has not changed).
*   Renaming built-in function calls to include their new namespace (e.g., [highest()](https://www.tradingview.com/pine-script-reference/v4/#fun_highest) in v4 becomes [ta.highest()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}highest) in v5).
*   Restructuring inputs to use the more specialized `input.*()` functions.
*   Eliminating uses of the deprecated `transp` parameter by using [color.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_color{dot}new) to simultaneously define color and transparency for use with the `color` parameter.
*   If you used the `resolution` and `resolution_gaps` parameters in v4’s [study()](https://www.tradingview.com/pine-script-reference/v4/#fun_study), they will require changing to `timeframe` and `timeframe_gaps` in v5’s [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator).

[v4 to v5 converter](#id2)
-------------------------------------------------------------------------------

The Pine Script® Editor includes a utility to automatically convert v4 scripts to v5. To access it, open a script with `//@version=4` in it and select the “Convert to v5” option in the “More” menu identified by three dots at the top-right of the Editor’s pane:

![../_images/v4_to_v5_convert_button.png](https://tradingview.com/pine-script-docs/en/v5/_images/v4_to_v5_convert_button.png)

Not all scripts can be automatically converted from v4 to v5. If you want to convert the script manually or if your indicator returns a compilation error after conversion, use the following sections to determine how to complete the conversion. A list of some errors you can encounter during the automatic conversion and how to fix them can be found in the [Common script conversion errors](migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-commonconversionerrors) section of this guide.

[Renamed functions and variables](#id3)
---------------------------------------------------------------------------------------------------------

For clarity and consistency, many built-in functions and variables were renamed in v5. The inclusion of v4 function names in a new namespace is the cause of most changes. For example, the [sma()](https://www.tradingview.com/pine-script-reference/v4/#fun_sma) function in v4 is moved to the `ta.` namespace in v5: [ta.sma()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}sma). Remembering the new namespaces is not necessary; if you type the older name of a function without its namespace in the Editor and press the ‘Auto-complete’ hotkey (Ctrl + Space, or Cmd + Space on MacOS), a popup showing matching suggestions appears:

![../_images/v5_autocomplete.png](https://tradingview.com/pine-script-docs/en/v5/_images/v5_autocomplete.png)

Not counting functions moved to new namespaces, only two functions have been renamed:

*   `study()` is now [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator).
*   `tickerid()` is now [ticker.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker{dot}new).

The full list of renamed functions and variables can be found in the [All variable, function, and parameter name changes](migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-allvariables) section of this guide.

[Renamed function parameters](#id4)
-------------------------------------------------------------------------------------------------

The parameter names of some built-in functions were changed to improve the nomenclature. This has no bearing on most scripts, but if you used these parameter names when calling functions, they will require adaptation. For example, we have standardized all mentions:

```swift
// Valid in v4. Not valid in v5.
timev4 = time(resolution = "1D")
// Valid in v5.
timev5 = time(timeframe = "1D")
// Valid in v4 and v5.
timeBoth = time("1D")

```


The full list of renamed function parameters can be found in the [All variable, function, and parameter name changes](migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-allvariables) section of this guide.

[Removed an \`rsi()\` overload](#id5)
-----------------------------------------------------------------------------------------------

In v4, the [rsi()](https://www.tradingview.com/pine-script-reference/v4/#fun_rsi) function had two different overloads:

*   `rsi(series float, simple int)` for the normal RSI calculation, and
*   `rsi(series float, series float)` for an overload used in the MFI indicator, which did a calculation equivalent to `100.0 - (100.0 / (1.0 + arg1 / arg2))`.

This caused a single built-in function to behave in two very different ways, and it was difficult to distinguish which one applied because it depended on the type of the second argument. As a result, a number of indicators misused the function and were displaying incorrect results. To avoid this, the second overload was removed in v5.

The [ta.rsi()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rsi) function in v5 only accepts a “simple int” argument for its `length` parameter. If your v4 code used the now deprecated overload of the function with a `float` second argument, you can replace the whole `rsi()` call with the following formula, which is equivalent:

```swift
100.0 - (100.0 / (1.0 + arg1 / arg2))

```


Note that when your v4 code used a “series int” value as the second argument to [rsi()](https://www.tradingview.com/pine-script-reference/v4/#fun_rsi), it was automatically cast to “series float” and the second overload of the function was used. While this was syntactically correct, it most probably did **not** yield the result you expected. In v5, [ta.rsi()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rsi) requires a “simple int” for the argument to `length`, which precludes dynamic (or “series”) lengths. The reason for this is that RSI calculations use the [ta.rma()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rma) moving average, which is similar to [ta.ema()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}ema) in that it relies on a length-dependent recursive process using the values of previous bars. This makes it impossible to achieve correct results with a “series” length that could vary bar to bar.

If your v4 code used a length that was “const int”, “input int” or “simple int”, no changes are required.

[Reserved keywords](#id6)
-----------------------------------------------------------------------------

A number of words are reserved and cannot be used for variable or function names. They are: `catch`, `class`, `do`, `ellipse`, `in`, `is`, `polygon`, `range`, `return`, `struct`, `text`, `throw`, `try`. If your v4 indicator uses any of these, rename your variable or function for the script to work in v5.

[Removed \`iff()\` and \`offset()\`](#id7)
---------------------------------------------------------------------------------------------------

The [iff()](https://www.tradingview.com/pine-script-reference/v4/#fun_iff) and [offset()](https://www.tradingview.com/pine-script-reference/v4/#fun_offset) functions have been removed. Code using the [iff()](https://www.tradingview.com/pine-script-reference/v4/#fun_iff) function can be rewritten using the ternary operator:

```swift
// iff(<condition>, <return_when_true>, <return_when_false>)
// Valid in v4, not valid in v5
barColorIff = iff(close >= open, color.green, color.red)
// <condition> ? <return_when_true> : <return_when_false>
// Valid in v4 and v5
barColorTernary = close >= open ? color.green : color.red

```


Note that the ternary operator is evaluated “lazily”; only the required value is calculated (depending on the condition’s evaluation to `true` or `false`). This is different from [iff()](https://www.tradingview.com/pine-script-reference/v4/#fun_iff), which always evaluated both values but returned only the relevant one.

Some functions require evaluation on every bar to correctly calculate, so you will need to make special provisions for these by pre-evaluating them before the ternary:

```swift
// `iff()` in v4: `highest()` and `lowest()` are calculated on every bar
v1 = iff(close > open, highest(10), lowest(10))
plot(v1)
// In v5: forced evaluation on every bar prior to the ternary statement.
h1 = ta.highest(10)
l1 = ta.lowest(10)
v1 = close > open ? h1 : l1
plot(v1)

```


The [offset()](https://www.tradingview.com/pine-script-reference/v4/#fun_offset) function was deprecated because the more readable [\[\]](https://www.tradingview.com/pine-script-reference/v5/#op_[]) operator is equivalent:

```swift
// Valid in v4. Not valid in v5.
prevClosev4 = offset(close, 1)
// Valid in v4 and v5.
prevClosev5 = close[1]

```


[Split of \`input()\` into several functions](#id8)
---------------------------------------------------------------------------------------------------------------------------

The v4 [input()](https://www.tradingview.com/pine-script-reference/v4/#fun_input) function was becoming crowded with a plethora of overloads and parameters. We split its functionality into different functions to clear that space and provide a more robust structure to accommodate the additions planned for inputs. Each new function uses the name of the `input.*` type of the v4 `input()` call it replaces. E.g., there is now a specialized [input.float()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}float) function replacing the v4 `input(1.0, type = input.float)` call. Note that you can still use `input(1.0)` in v5, but because only [input.float()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}float) allows for parameters such as `minval`, `maxval`, etc., it is more powerful. Also note that [input.int()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}int) is the only specialized input function that does not use its equivalent v4 `input.integer` name. The `input.*` constants have been removed because they were used as arguments for the `type` parameter, which was deprecated.

To convert, for example, a v4 script using an input of type `input.symbol`, the [input.symbol()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}symbol) function must be used in v5:

```swift
// Valid in v4. Not valid in v5.
aaplTicker = input("AAPL", type = input.symbol)
// Valid in v5
aaplTicker = input.symbol("AAPL")

```


The [input()](https://www.tradingview.com/pine-script-reference/v5/#fun_input) function persists in v5, but in a simpler form, with less parameters. It has the advantage of automatically detecting input types “bool/color/int/float/string/source” from the argument used for `defval`:

```swift
// Valid in v4 and v5.
// While "AAPL" is a valid symbol, it is only a string here because `input.symbol()` is not used.
tickerString = input("AAPL", title = "Ticker string")

```


[Some function parameters now require built-in arguments](#id9)
---------------------------------------------------------------------------------------------------------------------------------------------------------

In v4, built-in constants such as `plot.style_area` used as arguments when calling Pine Script® functions corresponded to pre-defined values of a specific type. For example, the value of `barmerge.lookahead_on` was `true`, so you could use `true` instead of the named constant when supplying an argument to the `lookahead` parameter in a [security()](https://www.tradingview.com/pine-script-reference/v4/#fun_security) function call. We found this to be a common source of confusion, which caused unsuspecting programmers to produce code yielding unintended results.

In v5, the use of correct built-in named constants as arguments to function parameters requiring them is mandatory:

```swift
// Not valid in v5: `true` is used as an argument for `lookahead`.
request.security(syminfo.tickerid, "1D", close, lookahead = true)
// Valid in v5: uses a named constant instead of `true`.
request.security(syminfo.tickerid, "1D", close, lookahead = barmerge.lookahead_on)

// Would compile in v4 because `plot.style_columns` was equal to 5.
// Won’t compile in v5.
a = 2 * plot.style_columns
plot(a)

```


To convert your script from v4 to v5, make sure you use the correct named built-in constants as function arguments.

[Deprecated the \`transp\` parameter](#id10)
--------------------------------------------------------------------------------------------------------------

The `transp=` parameter used in the signature of many v4 plotting functions was deprecated because it interfered with RGB functionality. Transparency must now be specified along with the color as an argument to parameters such as `color`, `textcolor`, etc. The [color.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_color{dot}new) or [color.rgb()](https://www.tradingview.com/pine-script-reference/v5/#fun_color{dot}rgb) functions will be needed in those cases to join a color and its transparency.

Note that in v4, the [bgcolor()](https://www.tradingview.com/pine-script-reference/v5/#fun_bgcolor) and [fill()](https://www.tradingview.com/pine-script-reference/v5/#fun_fill) functions had an optional `transp` parameter that used a default value of 90. This meant that the code below could display Bollinger Bands with a semi-transparent fill between two bands and a semi-transparent backround color where bands cross price, even though no argument is used for the `transp` parameter in its [bgcolor()](https://www.tradingview.com/pine-script-reference/v5/#fun_bgcolor) and [fill()](https://www.tradingview.com/pine-script-reference/v5/#fun_fill) calls:

```swift
//@version=4
study("Bollinger Bands", overlay = true)
[middle, upper, lower] = bb(close, 5, 4)
plot(middle, color=color.blue)
p1PlotID = plot(upper, color=color.green)
p2PlotID = plot(lower, color=color.green)
crossUp = crossover(high, upper)
crossDn = crossunder(low, lower)
// Both `fill()` and `bgcolor()` have a default `transp` of 90
fill(p1PlotID, p2PlotID, color = color.green)
bgcolor(crossUp ? color.green : crossDn ? color.red : na)

```


In v5 we need to explictly mention the 90 transparency with the color, yielding:

```swift
//@version=5
indicator("Bollinger Bands", overlay = true)
[middle, upper, lower] = ta.bb(close, 5, 4)
plot(middle, color=color.blue)
p1PlotID = plot(upper, color=color.green)
p2PlotID = plot(lower, color=color.green)
crossUp = ta.crossover(high, upper)
crossDn = ta.crossunder(low, lower)
var TRANSP = 90
// We use `color.new()` to explicitly pass transparency to both functions
fill(p1PlotID, p2PlotID, color = color.new(color.green, TRANSP))
bgcolor(crossUp ? color.new(color.green, TRANSP) : crossDn ? color.new(color.red, TRANSP) : na)

```


[Changed the default session days for \`time()\` and \`time\_close()\`](#id11)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default set of days for `session` strings used in the [time()](https://www.tradingview.com/pine-script-reference/v5/#fun_time) and [time\_close()](https://www.tradingview.com/pine-script-reference/v5/#fun_time_close) functions, and returned by [input.session()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}session), has changed from `"23456"` (Monday to Friday) to `"1234567"` (Sunday to Saturday):

```swift
// On symbols that are traded during weekends, this will behave differently in v4 and v5.
t0 = time("1D", "1000-1200")
// v5 equivalent of the behavior of `t0` in v4.
t1 = time("1D", "1000-1200:23456")
// v5 equivalent of the behavior of `t0` in v5.
t2 = time("1D", "1000-1200:1234567")

```


This change in behavior should not have much impact on scripts running on conventional markets that are closed during weekends. If it is important for you to ensure your session definitions preserve their v4 behavior in v5 code, add `":23456"` to your session strings. See this manual’s page on [Sessions](concepts_Sessions.html#pagesessions) for more information.

[\`strategy.exit()\` now must do something](#id12)
------------------------------------------------------------------------------------------------------------------------

Gone are the days when the [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) function was allowed to loiter. Now it must actually have an effect on the strategy by using at least one of the following parameters: `profit`, `limit`, `loss`, `stop`, or one of the following pairs: `trail_offset` combined with either `trail_price` or `trail_points`. When uses of [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) not meeting these criteria trigger an error while converting a strategy to v5, you can safely eliminate these lines, as they didn’t do anything in your code anyway.

[Common script conversion errors](#id13)
----------------------------------------------------------------------------------------------------------

### Invalid argument ‘style’/’linestyle’ in ‘plot’/’hline’ call

To make this work, you need to change the “int” arguments used for the `style` and `linestyle` arguments in [plot()](https://www.tradingview.com/pine-script-reference/v5/#fun_plot) and [hline()](https://www.tradingview.com/pine-script-reference/v5/#fun_hline) for built-in constants:

```swift
// Will cause an error during conversion
plotStyle = input(1)
hlineStyle = input(1)
plot(close, style = plotStyle)
hline(100, linestyle = hlineStyle)

// Will work in v5
//@version=5
indicator("")
plotStyleInput = input.string("Line", options = ["Line", "Stepline", "Histogram", "Cross", "Area", "Columns", "Circles"])
hlineStyleInput = input.string("Solid", options = ["Solid", "Dashed", "Dotted"])

plotStyle = plotStyleInput == "Line" ? plot.style_line :
             plotStyleInput == "Stepline" ? plot.style_stepline :
             plotStyleInput == "Histogram" ? plot.style_histogram :
             plotStyleInput == "Cross" ? plot.style_cross :
             plotStyleInput == "Area" ? plot.style_area :
             plotStyleInput == "Columns" ? plot.style_columns :
             plot.style_circles

hlineStyle = hlineStyleInput == "Solid" ? hline.style_solid :
             hlineStyleInput == "Dashed" ? hline.style_dashed :
             hline.style_dotted

plot(close, style = plotStyle)
hline(100, linestyle = hlineStyle)

```


See the [Some function parameters now require built-in arguments](migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-somefunctionparametersnowrequirebuiltinarguments) section of this guide for more information.

### Undeclared identifier ‘input.%input\_name%’

To fix this issue, remove the `input.*` constants from your code:

```swift
// Will cause an error during conversion
_integer = input.integer
_bool = input.bool
i1 = input(1, "Integer", _integer)
i2 = input(true, "Boolean", _bool)

// Will work in v5
i1 = input.int(1, "Integer")
i2 = input.bool(true, "Boolean")

```


See the User Manual’s page on [Inputs](concepts_Inputs.html#pageinputs), and the [Some function parameters now require built-in arguments](https://tradingview.com/pine-script-docs/en/v5/migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-somefunctionparametersnowrequirebuiltinarguments) section of this guide for more information.

### Invalid argument ‘when’ in ‘strategy.close’ call

This is caused by a confusion between [strategy.entry()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry) and [strategy.close()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close).

The second parameter of [strategy.close()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close) is `when`, which expects a “bool” argument. In v4, it was allowed to use `strategy.long` an argument because it was a “bool”. With v5, however, named built-in constants must be used as arguments, so `strategy.long` is no longer allowed as an argument to the `when` parameter.

The `strategy.close("Short", strategy.long)` call in this code is equivalent to `strategy.close("Short")`, which is what must be used in v5:

```swift
// Will cause an error during conversion
if (longCondition)
    strategy.close("Short", strategy.long)
    strategy.entry("Long", strategy.long)

// Will work in v5:
if (longCondition)
    strategy.close("Short")
    strategy.entry("Long", strategy.long)

```


See the [Some function parameters now require built-in arguments](migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-somefunctionparametersnowrequirebuiltinarguments) section of this guide for more information.

### Cannot call ‘input.int’ with argument ‘minval’=’%value%’. An argument of ‘literal float’ type was used but a ‘const int’ is expected

In v4, it was possible to pass a “float” argument to `minval` when an “int” value was being input. This is no longer possible in v5; “int” values are required for “int” inputs:

```swift
// Works in v4, will break on conversion because minval is a 'float' value
int_input = input(1, "Integer", input.integer, minval = 1.0)

// Works in v5
int_input = input.int(1, "Integer", minval = 1)

```


See the User Manual’s page on [Inputs](concepts_Inputs.html#pageinputs), and the [Some function parameters now require built-in arguments](https://tradingview.com/pine-script-docs/en/v5/migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5-somefunctionparametersnowrequirebuiltinarguments) section of this guide for more information.

[All variable, function, and parameter name changes](#id14)
----------------------------------------------------------------------------------------------------------------------------------------------

### Removed functions and variables


|v4                    |v5                           |
|----------------------|-----------------------------|
|input.bool input      |Replaced by input.bool()     |
|input.color input     |Replaced by input.color()    |
|input.float input     |Replaced by input.float()    |
|input.integer input   |Replaced by input.int()      |
|input.resolution input|Replaced by input.timeframe()|
|input.session input   |Replaced by input.session()  |
|input.source input    |Replaced by input.source()   |
|input.string input    |Replaced by input.string()   |
|input.symbol input    |Replaced by input.symbol()   |
|input.time input      |Replaced by input.time()     |
|iff()                 |Use the ?: operator instead  |
|offset()              |Use the [] operator instead  |


### Renamed functions and parameters

#### No namespace change



* v4: study(<...>, resolution, resolution_gaps, <...>)
  * v5: indicator(<...>, timeframe, timeframe_gaps, <...>)
* v4: strategy.entry(long)
  * v5: strategy.entry(direction)
* v4: strategy.order(long)
  * v5: strategy.order(direction)
* v4: time(resolution)
  * v5: time(timeframe)
* v4: time_close(resolution)
  * v5: time_close(timeframe)
* v4: nz(x, y)
  * v5: nz(source, replacement)


#### “ta” namespace for technical analysis functions and variables


|v4                                     |v5                                      |
|---------------------------------------|----------------------------------------|
|Indicator functions and variables      |                                        |
|accdist                                |ta.accdist                              |
|alma()                                 |ta.alma()                               |
|atr()                                  |ta.atr()                                |
|bb()                                   |ta.bb()                                 |
|bbw()                                  |ta.bbw()                                |
|cci()                                  |ta.cci()                                |
|cmo()                                  |ta.cmo()                                |
|cog()                                  |ta.cog()                                |
|dmi()                                  |ta.dmi()                                |
|ema()                                  |ta.ema()                                |
|hma()                                  |ta.hma()                                |
|iii                                    |ta.iii                                  |
|kc()                                   |ta.kc()                                 |
|kcw()                                  |ta.kcw()                                |
|linreg()                               |ta.linreg()                             |
|macd()                                 |ta.macd()                               |
|mfi()                                  |ta.mfi()                                |
|mom()                                  |ta.mom()                                |
|nvi                                    |ta.nvi                                  |
|obv                                    |ta.obv                                  |
|pvi                                    |ta.pvi                                  |
|pvt                                    |ta.pvt                                  |
|rma()                                  |ta.rma()                                |
|roc()                                  |ta.roc()                                |
|rsi(x, y)                              |ta.rsi(source, length)                  |
|sar()                                  |ta.sar()                                |
|sma()                                  |ta.sma()                                |
|stoch()                                |ta.stoch()                              |
|supertrend()                           |ta.supertrend()                         |
|swma(x)                                |ta.swma(source)                         |
|tr                                     |ta.tr                                   |
|tr()                                   |ta.tr()                                 |
|tsi()                                  |ta.tsi()                                |
|vwap                                   |ta.vwap                                 |
|vwap(x)                                |ta.vwap(source)                         |
|vwma()                                 |ta.vwma()                               |
|wad                                    |ta.wad                                  |
|wma()                                  |ta.wma()                                |
|wpr()                                  |ta.wpr()                                |
|wvad                                   |ta.wvad                                 |
|Supporting functions                   |                                        |
|barsince()                             |ta.barsince()                           |
|change()                               |ta.change()                             |
|correlation(source_a, source_b, length)|ta.correlation(source1, source2, length)|
|cross(x, y)                            |ta.cross(source1, source2)              |
|crossover(x, y)                        |ta.crossover(source1, source2)          |
|crossunder(x, y)                       |ta.crossunder(source1, source2)         |
|cum(x)                                 |ta.cum(source)                          |
|dev()                                  |ta.dev()                                |
|falling()                              |ta.falling()                            |
|highest()                              |ta.highest()                            |
|highestbars()                          |ta.highestbars()                        |
|lowest()                               |ta.lowest()                             |
|lowestbars()                           |ta.lowestbars()                         |
|median()                               |ta.median()                             |
|mode()                                 |ta.mode()                               |
|percentile_linear_interpolation()      |ta.percentile_linear_interpolation()    |
|percentile_nearest_rank()              |ta.percentile_nearest_rank()            |
|percentrank()                          |ta.percentrank()                        |
|pivothigh()                            |ta.pivothigh()                          |
|pivotlow()                             |ta.pivotlow()                           |
|range()                                |ta.range()                              |
|rising()                               |ta.rising()                             |
|stdev()                                |ta.stdev()                              |
|valuewhen()                            |ta.valuewhen()                          |
|variance()                             |ta.variance()                           |


#### “request” namespace for functions that request external data


|v4                                |v5                                       |
|----------------------------------|-----------------------------------------|
|financial()                       |request.financial()                      |
|quandl()                          |request.quandl()                         |
|security(<...>, resolution, <...>)|request.security(<...>, timeframe, <...>)|
|splits()                          |request.splits()                         |
|dividends()                       |request.dividends()                      |
|earnings()                        |request.earnings()                       |


#### “ticker” namespace for functions that help create tickers


|v4           |v5                  |
|-------------|--------------------|
|heikinashi() |ticker.heikinashi() |
|kagi()       |ticker.kagi()       |
|linebreak()  |ticker.linebreak()  |
|pointfigure()|ticker.pointfigure()|
|renko()      |ticker.renko()      |
|tickerid()   |ticker.new()        |


#### “str” namespace for functions that manipulate strings


|v4            |v5                         |
|--------------|---------------------------|
|tostring(x, y)|str.tostring(value, format)|
|tonumber(x)   |str.tonumber(string)       |


[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)
