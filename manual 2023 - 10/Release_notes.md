This page contains release notes of notable changes in Pine Script®.

[2023](#id18)
---------------------------------------------------

### [September 2023](#id19)

New functions were added:

*   [chart.point.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_chart.point.new) - Creates a new [chart.point](https://www.tradingview.com/pine-script-reference/v5/#op_chart.point) object with the specified time, index, and price.
*   [request.seed](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}seed) - Requests data from a user-maintained GitHub repository and returns it as a series. An in-depth tutorial on how to add new data can be found [here](https://github.com/tradingview-pine-seeds/docs).

We’ve added the following functions for ticker ID construction and timeframe specification:

*   [ticker.inherit()](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker{dot}inherit) - Constructs a ticker ID for the specified `symbol` with additional parameters inherited from the ticker ID passed into the function call, allowing the script to request a symbol’s data using the same modifiers that the `from_tickerid` has, including extended session, dividend adjustment, currency conversion, non-standard chart types, back-adjustment, settlement-as-close, etc.
*   [timeframe.from\_seconds()](https://www.tradingview.com/pine-script-reference/v5/#fun_timeframe.from_seconds) - Converts a specified number of `seconds` into a valid timeframe string based on our [timeframe specification format](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Timeframes.html#timeframe-string-specifications).

The `dividends.*` namespace now includes variables for retrieving future dividend information:

*   [dividends.future\_amount](https://www.tradingview.com/pine-script-reference/v5/#var_dividends.future_amount) - Returns the payment amount of the upcoming dividend in the currency of the current instrument, or `na` if this data isn’t available.
*   [dividends.future\_ex\_date](https://www.tradingview.com/pine-script-reference/v5/#var_dividends.future_ex_date) - Returns the Ex-dividend date (Ex-date) of the current instrument’s next dividend payment, or `na` if this data isn’t available.
*   [dividends.future\_pay\_date](https://www.tradingview.com/pine-script-reference/v5/#var_dividends.future_pay_date) - Returns the Payment date (Pay date) of the current instrument’s next dividend payment, or `na` if this data isn’t available.

The [request.security\_lower\_tf()](https://www.tradingview.com/pine-script-reference/v5/#fun_request.security_lower_tf) function has a new parameter:

*   `ignore_invalid_timeframe` - Determines how the function behaves when the chart’s timeframe is smaller than the `timeframe` value in the function call. If `false`, the function will raise a runtime error and halt the script’s execution. If `true`, the function will return `na` without raising an error.

Users can now explicitly declare variables with the `const`, `simple`, and `series` type qualifiers, allowing more precise control over the types of variables in their scripts. For example:

```
//@version=5
indicator("My script")

//@variable A constant `string` used as the `title` in the `plot()` function.
const string plotTitle = "My plot"
//@variable An `int` variable whose value is consistent after the first chart bar.
simple int a = 10
//@variable An `int` variable whose value can change on every bar.
series int b = bar_index

plot(b % a, title = plotTitle)

```


### [August 2023](#id20)

Added the following alert [placeholders](https://www.tradingview.com/support/solutions/43000531021):

*   `{{syminfo.currency}}` - Returns the currency code of the current symbol (“EUR”, “USD”, etc.).
*   `{{syminfo.basecurrency}}` - Returns the base currency code of the current symbol if the symbol refers to a currency pair. Otherwise, it returns `na`. For example, it returns “EUR” when the symbol is “EURUSD”.

#### [Pine Script® Maps](#id21)

Maps are collections that hold elements in the form of _key-value pairs_. They associate unique keys of a _fundamental type_ with values of a _built-in_ or [user-defined](https://tradingview.com/pine-script-docs/en/v5/language/Type_system.html#pagetypesystem-userdefinedtypes) type. Unlike [arrays](https://tradingview.com/pine-script-docs/en/v5/language/Arrays.html#pagearrays) and [matrices](https://tradingview.com/pine-script-docs/en/v5/language/Matrices.html#pagematrices), these collections are _unordered_ and do not utilize an internal lookup index. Instead, scripts access the values of maps by referencing the _keys_ from the key-value pairs put into them. For more information on these new collections, see our [User Manual’s page on Maps](https://tradingview.com/pine-script-docs/en/v5/language/Maps.html#pagemaps).

### [July 2023](#id22)

Fixed an issue that caused strategies to occasionally calculate the sizes of limit orders incorrectly due to improper tick rounding of the `limit` price.

Added a new built-in variable to the `strategy.*` namespace:

*   [strategy.margin\_liquidation\_price](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}margin_liquidation_price) - When a strategy uses margin, returns the price value after which a margin call will occur.

### [May 2023](#id24)

New parameter added to the [strategy.entry()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry), [strategy.order()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}order), [strategy.close()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close), [strategy.close\_all()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close_all), and [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) functions:

*   `disable_alert` - Disables order fill alerts for any orders placed by the function.

Our “Indicator on indicator” feature, which allows a script to pass another indicator’s plot as a source value via the [input.source()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}source) function, now supports multiple external inputs. Scripts can use a multitude of external inputs originating from up to 10 different indicators.

We’ve added the following array functions:

*   [array.every()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}every) - Returns `true` if all elements of the `id` array are `true`, `false` otherwise.
*   [array.some()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}some) - Returns `true` if at least one element of the `id` array is `true`, `false` otherwise.

These functions also work with arrays of [int](https://www.tradingview.com/pine-script-reference/v5/#op_int) and [float](https://www.tradingview.com/pine-script-reference/v5/#op_float) types, in which case zero values are considered `false`, and all others `true`.

### [February 2023](#id27)

#### [Pine Script® Methods](#id28)

Pine Script® methods are specialized functions associated with specific instances of built-in or user-defined types. They offer a more convenient syntax than standard functions, as users can access methods in the same way as object fields using the handy dot notation syntax. Pine Script® includes built-in methods for [array](https://www.tradingview.com/pine-script-reference/v5/#op_array), [matrix](https://www.tradingview.com/pine-script-reference/v5/#op_matrix), [line](https://www.tradingview.com/pine-script-reference/v5/#op_line), [linefill](https://www.tradingview.com/pine-script-reference/v5/#op_linefill), [label](https://www.tradingview.com/pine-script-reference/v5/#op_label), [box](https://www.tradingview.com/pine-script-reference/v5/#op_box), and [table](https://www.tradingview.com/pine-script-reference/v5/#op_table) types and facilitates user-defined methods with the new [method](https://www.tradingview.com/pine-script-reference/v5/#op_method) keyword. For more details on this new feature, see our [User Manual’s page on methods](https://tradingview.com/pine-script-docs/en/v5/language/Methods.html#pagemethods).

[2022](#id30)
---------------------------------------------------

### [December 2022](#id31)

#### [Pine Objects](#id32)

Pine objects are instantiations of the new user-defined composite types (UDTs) declared using the [type](https://www.tradingview.com/pine-script-reference/v5/#op_type) keyword. Experienced programmers can think of UDTs as method-less classes. They allow users to create custom types that organize different values under one logical entity. A detailed rundown of the new functionality can be found in our [User Manual’s page on objects](https://www.tradingview.com/pine-script-docs/en/v5/language/Objects.html).

A new function was added:

*   [ticker.standard()](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker{dot}standard) - Creates a ticker to request data from a standard chart that is unaffected by modifiers like extended session, dividend adjustment, currency conversion, and the calculations of non-standard chart types: Heikin Ashi, Renko, etc.

New `strategy.*` functions were added:

*   [strategy.opentrades.entry\_comment()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}opentrades{dot}entry_comment) - The function returns the comment message of the open trade’s entry.
*   [strategy.closedtrades.entry\_comment()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}entry_comment) - The function returns the comment message of the closed trade’s entry.
*   [strategy.closedtrades.exit\_comment()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}exit_comment) - The function returns the comment message of the closed trade’s exit.

### [October 2022](#id34)

Pine Script® now has a new, more powerful and better-integrated editor. Read [our blog](https://www.tradingview.com/blog/en/new-vsc-style-pine-script-editor-34159/) to find out everything to know about all the new features and upgrades.

New overload for the [fill()](https://www.tradingview.com/pine-script-reference/v5/#fun_fill) function was added. Now it can create vertical gradients. More info about it in the [blog post](https://www.tradingview.com/blog/en/pine-script-vertical-gradients-33586/).

A new function was added:

*   [str.format\_time()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}format_time) - Converts a timestamp to a formatted string using the specified format and time zone.

### [August 2022](#id36)

A new label style [label.style\_text\_outline](https://www.tradingview.com/pine-script-reference/v5/#var_label{dot}style_text_outline) was added.

A new parameter for the [ta.pivot\_point\_levels()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}pivot_point_levels) function was added:

*   `developing` - If `false`, the values are those calculated the last time the anchor condition was true. They remain constant until the anchor condition becomes true again. If `true`, the pivots are developing, i.e., they constantly recalculate on the data developing between the point of the last anchor (or bar zero if the anchor condition was never true) and the current bar. Cannot be `true` when `type` is set to `"Woodie"`.

A new parameter for the [box.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}new) function was added:

*   `text_wrap` - It defines whether the text is presented in a single line, extending past the width of the box if necessary, or wrapped so every line is no wider than the box itself.

This parameter supports two arguments:

*   [text.wrap\_none](https://www.tradingview.com/pine-script-reference/v5/#var_text{dot}wrap_none) - Disabled wrapping mode for [box.new](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}new) and [box.set\_text\_wrap](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text_wrap) functions.
*   [text.wrap\_auto](https://www.tradingview.com/pine-script-reference/v5/#var_text{dot}wrap_auto) - Automatic wrapping mode for [box.new](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}new) and [box.set\_text\_wrap](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text_wrap) functions.

New built-in functions were added:

*   [ta.min()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}min) - Returns the all-time low value of `source` from the beginning of the chart up to the current bar.
*   [ta.max()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}max) - Returns the all-time high value of `source` from the beginning of the chart up to the current bar.

A new annotation `//@strategy_alert_message` was added. If the annotation is added to the strategy, the text written after it will be automatically set as the default alert message in the Create Alert window.

```
//@version=5
// @strategy_alert_message My Default Alert Message
strategy("My Strategy")
plot(close)

```


### [July 2022](#id37)

It is now possible to fine-tune where a script’s plot values are displayed through the introduction of new arguments for the `display` parameter of the [plot()](https://www.tradingview.com/pine-script-reference/v5/#fun_plot), [plotchar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotchar), [plotshape()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotshape), [plotarrow()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotarrow), [plotcandle()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotcandle), and [plotbar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotbar) functions.

Four new arguments were added, complementing the previously available [display.all](https://www.tradingview.com/pine-script-reference/v5/#var_display{dot}all) and [display.none](https://www.tradingview.com/pine-script-reference/v5/#var_display{dot}none):

*   [display.data\_window](https://www.tradingview.com/pine-script-reference/v5/#var_display{dot}data_window) displays the plot values in the Data Window, one of the items available from the chart’s right sidebar.
*   [display.pane](https://www.tradingview.com/pine-script-reference/v5/#var_display{dot}pane) displays the plot in the pane where the script resides, as defined in with the `overlay` parameter of the script’s [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator), [strategy()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy), or [library()](https://www.tradingview.com/pine-script-reference/v5/#fun_library) declaration statement.
*   [display.price\_scale](https://www.tradingview.com/pine-script-reference/v5/#var_display{dot}price_scale) controls the display of the plot’s label and price in the price scale, if the chart’s settings allow them.
*   [display.status\_line](https://www.tradingview.com/pine-script-reference/v5/#var_display{dot}status_line) displays the plot values in the script’s status line, next to the script’s name on the chart, if the chart’s settings allow them.

The `display` parameter supports the addition and subtraction of its arguments:

*   `display.all - display.status_line` will display the plot’s information everywhere except in the script’s status line.
*   `display.price_scale + display.status_line` will display the plot in the price scale and status line only.

### [June 2022](#id38)

The behavior of the argument used with the `qty_percent` parameter of [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) has changed. Previously, the percentages used on successive exit orders of the same position were calculated from the remaining position at any given time. Instead, the percentages now always apply to the initial position size. When executing the following strategy, for example:

```
//@version=5
strategy("strategy.exit() example", overlay = true)
strategy.entry("Long", strategy.long, qty = 100)
strategy.exit("Exit Long1", "Long", trail_points = 50, trail_offset = 0, qty_percent = 20)
strategy.exit("Exit Long2", "Long", trail_points = 100, trail_offset = 0, qty_percent = 20)

```


20% of the initial position will be closed on each [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) call. Before, the first call would exit 20% of the initial position, and the second would exit 20% of the remaining 80% of the position, so only 16% of the initial position.

Two new parameters for the built-in [ta.vwap()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}vwap) function were added:

*   `anchor` - Specifies the condition that triggers the reset of VWAP calculations. When `true`, calculations reset; when `false`, calculations proceed using the values accumulated since the previous reset.
*   `stdev_mult` - If specified, the [ta.vwap()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}vwap) calculates the standard deviation bands based on the main VWAP series and returns a `[vwap, upper_band, lower_band]` tuple.

New overloaded versions of the [strategy.close()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close) and [strategy.close\_all()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close_all) functions with the `immediately` parameter. When `immediately` is set to `true`, the closing order will be executed on the tick where it has been placed, ignoring the strategy parameters that restrict the order execution to the open of the next bar.

New built-in functions were added:

*   [timeframe.change()](https://www.tradingview.com/pine-script-reference/v5/#fun_timeframe{dot}change) - Returns `true` on the first bar of a new `timeframe`, `false` otherwise.
*   [ta.pivot\_point\_levels()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}pivot_point_levels) - Returns a float array with numerical values representing 11 pivot point levels: `[P, R1, S1, R2, S2, R3, S3, R4, S4, R5, S5]`. Levels absent from the specified `type` return na values.

New built-in variables were added:

*   [session.isfirstbar](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}isfirstbar) - returns `true` if the current bar is the first bar of the day’s session, `false` otherwise.
*   [session.islastbar](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}islastbar) - returns `true` if the current bar is the last bar of the day’s session, `false` otherwise.
*   [session.isfirstbar\_regular](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}isfirstbar_regular) - returns `true` on the first regular session bar of the day, `false` otherwise.
*   [session.islastbar\_regular](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}islastbar_regular) - returns `true` on the last regular session bar of the day, `false` otherwise.
*   [chart.left\_visible\_bar\_time](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}left_visible_bar_time) - returns the `time` of the leftmost bar currently visible on the chart.
*   [chart.right\_visible\_bar\_time](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}right_visible_bar_time) - returns the `time` of the rightmost bar currently visible on the chart.

### [May 2022](#id39)

[Matrix](https://www.tradingview.com/pine-script-reference/v5/#op_matrix) support has been added to the [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security) function.

The historical states of [arrays](https://www.tradingview.com/pine-script-reference/v5/#op_array) and [matrices](https://www.tradingview.com/pine-script-reference/v5/#op_matrix) can now be referenced with the [\[\]](https://www.tradingview.com/pine-script-reference/v5/#op_[]) operator. In the example below, we reference the historic state of a matrix 10 bars ago:

```
//@version=5
indicator("matrix.new<float> example")
m = matrix.new<float>(1, 1, close)
float x = na
if bar_index > 10
    x := matrix.get(m[10], 0, 0)
plot(x)
plot(close)

```


The [ta.change()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}change) function now can take values of [int](https://www.tradingview.com/pine-script-reference/v5/#op_int) and [bool](https://www.tradingview.com/pine-script-reference/v5/#op_bool) types as its `source` parameter and return the difference in the respective type.

New built-in variables were added:

*   [chart.bg\_color](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}bg_color) - Returns the color of the chart’s background from the `"Chart settings/Appearance/Background"` field.
*   [chart.fg\_color](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}fg_color) - Returns a color providing optimal contrast with [chart.bg\_color](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}bg_color).
*   [chart.is\_standard](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_standard) - Returns true if the chart type is bars, candles, hollow candles, line, area or baseline, false otherwise.
*   [currency.USDT](https://www.tradingview.com/pine-script-reference/v5/#var_currency{dot}USDT) - A constant for the Tether currency code.

New functions were added:

*   [syminfo.prefix()](https://www.tradingview.com/pine-script-reference/v5/#fun_syminfo{dot}prefix) - returns the exchange prefix of the `symbol` passed to it, e.g. “NASDAQ” for “NASDAQ:AAPL”.
*   [syminfo.ticker()](https://www.tradingview.com/pine-script-reference/v5/#fun_syminfo{dot}ticker) - returns the ticker of the `symbol` passed to it without the exchange prefix, e.g. “AAPL” for “NASDAQ:AAPL”.
*   [request.security\_lower\_tf()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security_lower_tf) - requests data from a lower timeframe than the chart’s.

Added `use_bar_magnifier` parameter for the [strategy()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy) function. When `true`, the [Broker Emulator](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Strategies.html#broker-emulator) uses lower timeframe data during history backtesting to achieve more realistic results.

Fixed behaviour of [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) function when stop loss triggered at prices outside the bars price range.

Added new `comment` and `alert` message parameters for the [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) function:

*   `comment_profit` - additional notes on the order if the exit was triggered by crossing `profit` or `limit` specifically.
*   `comment_loss` - additional notes on the order if the exit was triggered by crossing `stop` or `loss` specifically.
*   `comment_trailing` - additional notes on the order if the exit was triggered by crossing `trail_offset` specifically.
*   `alert_profit` - text that will replace the `'{{strategy.order.alert_message}}'` placeholder if the exit was triggered by crossing `profit` or `limit` specifically.
*   `alert_loss` - text that will replace the `'{{strategy.order.alert_message}}'` placeholder if the exit was triggered by crossing `stop` or `loss` specifically.
*   `alert_trailing` - text that will replace the `'{{strategy.order.alert_message}}'` placeholder if the exit was triggered by crossing `trail_offset` specifically.

### [April 2022](#id40)

Added the `display` parameter to the following functions: [barcolor](https://www.tradingview.com/pine-script-reference/v5/#fun_barcolor), [bgcolor](https://www.tradingview.com/pine-script-reference/v5/#fun_bgcolor), [fill](https://www.tradingview.com/pine-script-reference/v5/#fun_fill), [hline](https://www.tradingview.com/pine-script-reference/v5/#fun_hline).

A new function was added:

*   [request.economic()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}economic) - Economic data includes information such as the state of a country’s economy or of a particular industry.

New built-in variables were added:

*   [strategy.max\_runup](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}max_runup) - Returns the maximum equity run-up value for the whole trading interval.
*   [syminfo.volumetype](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}volumetype) - Returns the volume type of the current symbol.
*   [chart.is\_heikinashi](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_heikinashi) - Returns true if the chart type is Heikin Ashi, false otherwise.
*   [chart.is\_kagi](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_kagi) - Returns true if the chart type is Kagi, false otherwise.
*   [chart.is\_linebreak](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_linebreak) - Returns true if the chart type is Line break, false otherwise.
*   [chart.is\_pnf](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_pnf) - Returns true if the chart type is Point & figure, false otherwise.
*   [chart.is\_range](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_range) - Returns true if the chart type is Range, false otherwise.
*   [chart.is\_renko](https://www.tradingview.com/pine-script-reference/v5/#var_chart{dot}is_renko) - Returns true if the chart type is Renko, false otherwise.

New matrix functions were added:

*   [matrix.new<type>](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix%7Bdot%7Dnew%3Ctype%3E) - Creates a new matrix object. A matrix is a two-dimensional data structure containing rows and columns. All elements in the matrix must be of the type specified in the type template (“<type>”).
*   [matrix.row()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}row) - Creates a one-dimensional array from the elements of a matrix row.
*   [matrix.col()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}col) - Creates a one-dimensional array from the elements of a matrix column.
*   [matrix.get()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}get) - Returns the element with the specified index of the matrix.
*   [matrix.set()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}set) - Assigns `value` to the element at the `column` and `row` index of the matrix.
*   [matrix.rows()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}rows) - Returns the number of rows in the matrix.
*   [matrix.columns()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}columns) - Returns the number of columns in the matrix.
*   [matrix.elements\_count()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}elements_count) - Returns the total number of matrix elements.
*   [matrix.add\_row()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}add_row) - Adds a row to the matrix. The row can consist of `na` values, or an array can be used to provide values.
*   [matrix.add\_col()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}add_col) - Adds a column to the matrix. The column can consist of `na` values, or an array can be used to provide values.
*   [matrix.remove\_row()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}remove_row) - Removes the row of the matrix and returns an array containing the removed row’s values.
*   [matrix.remove\_col()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}remove_col) - Removes the column of the matrix and returns an array containing the removed column’s values.
*   [matrix.swap\_rows()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}swap_rows) - Swaps the rows in the matrix.
*   [matrix.swap\_columns()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}swap_columns) - Swaps the columns in the matrix.
*   [matrix.fill()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}fill) - Fills a rectangular area of the matrix defined by the indices `from_column` to `to_column`.
*   [matrix.copy()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}copy) - Creates a new matrix which is a copy of the original.
*   [matrix.submatrix()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}submatrix) - Extracts a submatrix within the specified indices.
*   [matrix.reverse()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}reverse) - Reverses the order of rows and columns in the matrix. The first row and first column become the last, and the last become the first.
*   [matrix.reshape()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}reshape) - Rebuilds the matrix to `rows` x `cols` dimensions.
*   [matrix.concat()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}concat) - Append one matrix to another.
*   [matrix.sum()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}sum) - Returns a new matrix resulting from the sum of two matrices, or of a matrix and a scalar (a numerical value).
*   [matrix.diff()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}diff) - Returns a new matrix resulting from the subtraction between matrices, or of matrix and a scalar (a numerical value).
*   [matrix.mult()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}mult) - Returns a new matrix resulting from the product between the matrices, or between a matrix and a scalar (a numerical value), or between a matrix and a vector (an array of values).
*   [matrix.sort()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}sort) - Rearranges the rows in the `id` matrix following the sorted order of the values in the `column`.
*   [matrix.avg()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}avg) - Calculates the average of all elements in the matrix.
*   [matrix.max()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}max) - Returns the largest value from the matrix elements.
*   [matrix.min()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}min) - Returns the smallest value from the matrix elements.
*   [matrix.median()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}median) - Calculates the median (“the middle” value) of matrix elements.
*   [matrix.mode()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}mode) - Calculates the mode of the matrix, which is the most frequently occurring value from the matrix elements. When there are multiple values occurring equally frequently, the function returns the smallest of those values.
*   [matrix.pow()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}pow) - Calculates the product of the matrix by itself `power` times.
*   [matrix.det()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}det) - Returns the determinant of a square matrix.
*   [matrix.transpose()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}transpose) - Creates a new, transposed version of the matrix by interchanging the row and column index of each element.
*   [matrix.pinv()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}pinv) - Returns the pseudoinverse of a matrix.
*   [matrix.inv()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}inv) - Returns the inverse of a square matrix.
*   [matrix.rank()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}rank) - Calculates the rank of the matrix.
*   [matrix.trace()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}eigenvalues) - Calculates the trace of a matrix (the sum of the main diagonal’s elements).
*   [matrix.eigenvalues()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}eigenvectors) - Returns an array containing the eigenvalues of a square matrix.
*   [matrix.eigenvectors()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}) - Returns a matrix of eigenvectors, in which each column is an eigenvector of the matrix.
*   [matrix.kron()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}kronis_zero) - Returns the Kronecker product for the two matrices.
*   [matrix.is\_zero()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_zero) - Determines if all elements of the matrix are zero.
*   [matrix.is\_identity()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_identity) - Determines if a matrix is an identity matrix (elements with ones on the main diagonal and zeros elsewhere).
*   [matrix.is\_binary()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_binary) - Determines if the matrix is binary (when all elements of the matrix are 0 or 1).
*   [matrix.is\_symmetric()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_symmetric) - Determines if a square matrix is symmetric (elements are symmetric with respect to the main diagonal).
*   [matrix.is\_antisymmetric()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_antisymmetric) - Determines if a matrix is antisymmetric (its transpose equals its negative).
*   [matrix.is\_diagonal()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_diagonal) - Determines if the matrix is diagonal (all elements outside the main diagonal are zero).
*   [matrix.is\_antidiagonal()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_antidiagonal) - Determines if the matrix is anti-diagonal (all elements outside the secondary diagonal are zero).
*   [matrix.is\_triangular()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_triangular) - Determines if the matrix is triangular (if all elements above or below the main diagonal are zero).
*   [matrix.is\_stochastic()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_stochastic) - Determines if the matrix is stochastic.
*   [matrix.is\_square()](https://www.tradingview.com/pine-script-reference/v5/#fun_matrix{dot}is_square) - Determines if the matrix is square (it has the same number of rows and columns).

Added a new parameter for the [strategy()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy) function:

*   `risk_free_rate` - The risk-free rate of return is the annual percentage change in the value of an investment with minimal or zero risk, used to calculate the Sharpe and Sortino ratios.

### [March 2022](#id41)

New array functions were added:

*   [array.sort\_indices()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}sort_indices) - returns an array of indices which, when used to index the original array, will access its elements in their sorted order.
*   [array.percentrank()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}percentrank) - returns the percentile rank of a value in the array.
*   [array.percentile\_nearest\_rank()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}percentile_nearest_rank) - returns the value for which the specified percentage of array values (percentile) are less than or equal to it, using the nearest-rank method.
*   [array.percentile\_linear\_interpolation()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}percentile_linear_interpolation) - returns the value for which the specified percentage of array values (percentile) are less than or equal to it, using linear interpolation.
*   [array.abs()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}abs) - returns an array containing the absolute value of each element in the original array.
*   [array.binary\_search()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}binary_search) - returns the index of the value, or -1 if the value is not found.
*   [array.binary\_search\_leftmost()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}binary_search_leftmost) - returns the index of the value if it is found or the index of the next smallest element to the left of where the value would lie if it was in the array.
*   [array.binary\_search\_rightmost()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}binary_search_rightmost) - returns the index of the value if it is found or the index of the element to the right of where the value would lie if it was in the array.

Added a new optional `nth` parameter for the [array.min()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}min) and [array.max()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}max) functions.

Added `index` in [for..in](https://www.tradingview.com/pine-script-reference/v5/#op_for{dot}{dot}{dot}in) operator. It tracks the current iteration’s index.

### [February 2022](#id43)

Added templates and the ability to create arrays via templates. Instead of using one of the `array.new_*()` functions, a template function [array.new<type>](https://www.tradingview.com/pine-script-reference/v5/#fun_array%7Bdot%7Dnew%3Ctype%3E) can be used. In the example below, we use this functionality to create an array filled with `float` values:

```
//@version=5
indicator("array.new<float> example")
length = 5
var a = array.new<float>(length, close)
if array.size(a) == length
        array.remove(a, 0)
        array.push(a, close)
plot(array.sum(a) / length, "SMA")

```


New functions were added:

*   [timeframe.in\_seconds(timeframe)](https://www.tradingview.com/pine-script-reference/v5/#fun_timeframe{dot}in_seconds) - converts the timeframe passed to the `timeframe` argument into seconds.
*   [input.text\_area()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}text_area) - adds multiline text input area to the Script settings.
*   [strategy.closedtrades.entry\_id()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}entry_id) - returns the id of the closed trade’s entry.
*   [strategy.closedtrades.exit\_id()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}exit_id) - returns the id of the closed trade’s exit.
*   [strategy.opentrades.entry\_id()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}opentrades{dot}entry_id) - returns the id of the open trade’s entry.

[2021](#id45)
---------------------------------------------------

### [December 2021](#id46)

#### [New functions for string manipulation](#id48)

Added a number of new functions that provide more ways to process strings, and introduce regular expressions to Pine Script®:

*   [str.contains(source, str)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}contains) - Determines if the `source` string contains the `str` substring.
*   [str.pos(source, str)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}pos) - Returns the position of the `str` string in the `source` string.
*   [str.substring(source, begin\_pos, end\_pos)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}substring) - Extracts a substring from the `source` string.
*   [str.replace(source, target, replacement, occurrence)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}replace) - Contrary to the existing [str.replace\_all()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}replace_all) function, `str.replace()` allows the selective replacement of a matched substring with a replacement string.
*   [str.lower(source)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}lower) and [str.upper(source)](https://www.tradingview.com/pine-script-reference/v5/#fun_str%7Bdot%7Dupper) - Convert all letters of the `source` string to lower or upper case:
*   [str.startswith(source, str)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}startswith) and [str.endswith(source, str)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}endswith) - Determine if the `source` string starts or ends with the `str` substring.
*   [str.match(source, regex)](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}match) - Extracts the substring matching the specified [regular expression](https://en.wikipedia.org/wiki/Regular_expression#Perl_and_PCRE).

#### [Textboxes](#id49)

Box drawings now supports text. The [box.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}new) function has five new parameters for text manipulation: `text`, `text_size`, `text_color`, `text_valign`, and `text_halign`. Additionally, five new functions to set the text properties of existing boxes were added:

*   [box.set\_text()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text)
*   [box.set\_text\_color()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text_color)
*   [box.set\_text\_size()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text_size)
*   [box.set\_text\_valign()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text_valign)
*   [box.set\_text\_halign()](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}set_text_halign)

#### [New built-in variables](#id50)

Added new built-in variables that return the `bar_index` and `time` values of the last bar in the dataset. Their values are known at the beginning of the script’s calculation:

*   [last\_bar\_index](https://www.tradingview.com/pine-script-reference/v5/#var_last_bar_index) - Bar index of the last chart bar.
*   [last\_bar\_time](https://www.tradingview.com/pine-script-reference/v5/#var_last_bar_time) - UNIX time of the last chart bar.

New built-in `source` variable:

*   [hlcc4](https://www.tradingview.com/pine-script-reference/v5/#var_hlcc4) - A shortcut for `(high + low + close + close)/4`. It averages the high and low values with the double-weighted close.

### [November 2021](#id51)

#### [for…in](#id52)

Added a new [for…in](https://www.tradingview.com/pine-script-reference/v5/#op_for{dot}{dot}{dot}in) operator to iterate over all elements of an array:

```
//@version=5
indicator("My Script")
int[] a1 = array.from(1, 3, 6, 3, 8, 0, -9, 5)

highest(array) =>
    var int highestNum = na
    for item in array
        if na(highestNum) or item > highestNum
            highestNum := item
    highestNum

plot(highest(a1))

```


#### [Function overloads](#id53)

Added function overloads. Several functions in a script can now share the same name, as long one of the following conditions is true:

*   Each overload has a different number of parameters:
    
    ```
//@version=5
indicator("Function overload")

// Two parameters
mult(x1, x2) =>
    x1 * x2

// Three parameters
mult(x1, x2, x3) =>
    x1 * x2 * x3

plot(mult(7, 4))
plot(mult(7, 4, 2))

```

    
*   When overloads have the same number of parameters, all parameters in each overload must be explicitly typified, and their type combinations must be unique:
    
    ```
//@version=5
indicator("Function overload")

// Accepts both 'int' and 'float' values - any 'int' can be automatically cast to 'float'
mult(float x1, float x2) =>
    x1 * x2

// Returns a 'bool' value instead of a number
mult(bool x1, bool x2) =>
    x1 and x2 ? true : false

mult(string x1, string x2) =>
    str.tonumber(x1) * str.tonumber(x2)

// Has three parameters, so explicit types are not required
mult(x1, x2, x3) =>
    x1 * x2 * x3

plot(mult(7, 4))
plot(mult(7.5, 4.2))
plot(mult(true, false) ? 1 : 0)
plot(mult("5", "6"))
plot(mult(7, 4, 2))

```

    

### [October 2021](#id55)

Pine Script® v5 is here! This is a list of the **new** features added to the language, and a few of the **changes** made. See the Pine Script® v5 [Migration guide](https://tradingview.com/pine-script-docs/en/v5/migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5) for a complete list of the **changes** in v5.

#### [Changes](#id57)

Many built-in variables, functions and function arguments were renamed or moved to new namespaces in v5. The venerable `study()`, for example, is now [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator), and `security()` is now [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security). New namespaces now group related functions and variables together. This consolidation implements a more rational nomenclature and provides an orderly space to accommodate the many additions planned for Pine Script®.

See the Pine Script® v5 [Migration guide](https://tradingview.com/pine-script-docs/en/v5/migration_guides/v4_to_v5_migration_guide.html#pagetopineversion5) for a complete list of the **changes** made in v5.

### [September 2021](#id58)

New parameter has been added for the `dividends()`, `earnings()`, `financial()`, `quandl()`, `security()`, and `splits()` functions:

*   `ignore_invalid_symbol` - determines the behavior of the function if the specified symbol is not found: if `false`, the script will halt and return a runtime error; if `true`, the function will return `na` and execution will continue.

### [July 2021](#id59)

`tostring` now accepts “bool” and “string” types.

New argument for `time` and `time_close` functions was added:

*   `timezone` - timezone of the `session` argument, can only be used when a session is specified. Can be written out in GMT notation (e.g. “GMT-5”) or as an [IANA time zone database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g. “America/New\_York”).

It is now possible to place a drawing object in the future with `xloc = xloc.bar_index`.

New argument for `study` and `strategy` functions was added:

*   `explicit_plot_zorder` - specifies the order in which the indicator’s plots, fills, and hlines are rendered. If true, the plots will be drawn based on the order in which they appear in the indicator’s code, each newer plot being drawn above the previous ones.

### [June 2021](#id60)

New variable was added:

*   `barstate.islastconfirmedhistory` - returns `true` if script is executing on the dataset’s last bar when market is closed, or script is executing on the bar immediately preceding the real-time bar, if market is open. Returns `false` otherwise.

New function was added:

*   `round_to_mintick(x)` - returns the value rounded to the symbol’s mintick, i.e. the nearest value that can be divided by `syminfo.mintick`, without the remainder, with ties rounding up.

Expanded `tostring()` functionality. The function now accepts three new formatting arguments:

*   `format.mintick` to format to tick precision.
*   `format.volume` to abbreviate large values.
*   `format.percent` to format percentages.

### [May 2021](#id61)

Improved backtesting functionality by adding the Leverage mechanism.

Added support for table drawings and functions for working with them. Tables are unique objects that are not anchored to specific bars; they float in a script’s space, independently of the chart bars being viewed or the zoom factor used. For more information, see the [Tables](https://tradingview.com/pine-script-docs/en/v5/concepts/Tables.html#pagetables) User Manual page.

New functions were added:

*   `color.rgb(red, green, blue, transp)` - creates a new color with transparency using the RGB color model.
*   `color.from_gradient(value, bottom_value, top_value, bottom_color, top_color)` - returns color calculated from the linear gradient between bottom\_color to top\_color.
*   `color.r(color)`, `color.g(color)`, `color.b(color)`, `color.t(color)` - retrieves the value of one of the color components.
*   `array.from()` - takes a variable number of arguments with one of the types: `int`, `float`, `bool`, `string`, `label`, `line`, `color`, `box`, `table` and returns an array of the corresponding type.

A new `box` drawing has been added to Pine Script®, making it possible to draw rectangles on charts using the Pine Script® syntax. For more details see the Pine Script® [reference](https://www.tradingview.com/pine-script-reference/v5/#fun_box{dot}new) and the [Lines and boxes](https://tradingview.com/pine-script-docs/en/v5/concepts/Lines_and_boxes.html#pagelinesandboxes) User Manual page.

The `color.new` function can now accept series and input arguments, in which case, the colors will be calculated at runtime. For more information about this, see our [Colors](https://tradingview.com/pine-script-docs/en/v5/concepts/Colors.html#pagecolors) User Manual page.

### [April 2021](#id62)

New math constants were added:

*   `math.pi` - is a named constant for Archimedes’ constant. It is equal to 3.1415926535897932.
*   `math.phi` - is a named constant for the golden ratio. It is equal to 1.6180339887498948.
*   `math.rphi` - is a named constant for the golden ratio conjugate. It is equal to 0.6180339887498948.
*   `math.e` - is a named constant for Euler’s number. It is equal to 2.7182818284590452.

New math functions were added:

*   `round(x, precision)` - returns the value of `x` rounded to the nearest integer, with ties rounding up. If the precision parameter is used, returns a float value rounded to that number of decimal places.
*   `median(source, length)` - returns the median of the series.
*   `mode(source, length)` - returns the mode of the series. If there are several values with the same frequency, it returns the smallest value.
*   `range(source, length)` - returns the difference between the `min` and `max` values in a series.
*   `todegrees(radians)` - returns an approximately equivalent angle in degrees from an angle measured in radians.
*   `toradians(degrees)` - returns an approximately equivalent angle in radians from an angle measured in degrees.
*   `random(min, max, seed)` - returns a pseudo-random value. The function will generate a different sequence of values for each script execution. Using the same value for the optional seed argument will produce a repeatable sequence.

New functions were added:

*   `session.ismarket` - returns `true` if the current bar is a part of the regular trading hours (i.e. market hours), `false` otherwise.
*   `session.ispremarket` - returns `true` if the current bar is a part of the pre-market, `false` otherwise.
*   `session.ispostmarket` - returns `true` if the current bar is a part of the post-market, `false` otherwise.
*   `str.format` - converts the values to strings based on the specified formats. Accepts certain `number` modifiers: `integer`, `currency`, `percent`.

### [March 2021](#id63)

New assignment operators were added:

*   `+=` - addition assignment
*   `-=` - subtraction assignment
*   `*=` - multiplication assignment
*   `/=` - division assignment
*   `%=` - modulus assignment

New parameters for inputs customization were added:

*   `inline` - combines all the input calls with the same inline value in one line.
*   `group` - creates a header above all inputs that use the same group string value. The string is also used as the header text.
*   `tooltip` - adds a tooltip icon to the `Inputs` menu. The tooltip string is shown when hovering over the tooltip icon.

New argument for `fill` function was added:

*   `fillgaps` - controls whether fills continue on gaps when one of the `plot` calls returns an `na` value.

A new keyword was added:

*   `varip` - is similar to the `var` keyword, but variables declared with `varip` retain their values between the updates of a real-time bar.

New functions were added:

*   `tonumber()` - converts a string value into a float.
*   `time_close()` - returns the UNIX timestamp of the close of the current bar, based on the resolution and session that is passed to the function.
*   `dividends()` - requests dividends data for the specified symbol.
*   `earnings()` - requests earnings data for the specified symbol.
*   `splits()` - requests splits data for the specified symbol.

New arguments for the study() function were added:

*   `resolution_gaps` - fills the gaps between values fetched from higher timeframes when using `resolution`.
*   `format.percent` - formats the script output values as a percentage.

### [February 2021](#id64)

New variable was added:

*   `time_tradingday` - the beginning time of the trading day the current bar belongs to.

[2020](#id66)
----------------------------------------------------

### [December 2020](#id67)

New array types were added:

*   `array.new_line()`
*   `array.new_label()`
*   `array.new_string()`

New functions were added:

*   `str.length()` - returns number of chars in source string.
*   `array.join()` - concatenates all of the elements in the array into a string and separates these elements with the specified separator.
*   `str.split()` - splits a string at a given substring separator.

### [November 2020](#id68)

*   New `max_labels_count` and `max_lines_count` parameters were added to the study and strategy functions. Now you can manage the number of lines and labels by setting values for these parameters from 1 to 500.

New function was added:

*   `array.range()` - return the difference between the min and max values in the array.

### [October 2020](#id69)

The behavior of `rising()` and `falling()` functions have changed. For example, `rising(close,3)` is now calculated as following:

```
close[0] > close[1] and close[1] > close[2] and close[2] > close[3]

```


### [September 2020](#id70)

Added support for `input.color` to the `input()` function. Now you can provide script users with color selection through the script’s “Settings/Inputs” tab with the same color widget used throughout the TradingView user interface. Learn more about this feature in our [blog](https://www.tradingview.com/blog/en/create-color-inputs-in-pine-20751/):

```
//@version=4
study("My Script", overlay = true)
color c_labelColor = input(color.green, "Main Color", input.color)
var l = label.new(bar_index, close, yloc = yloc.abovebar, text = "Colored label")
label.set_x(l, bar_index)
label.set_color(l, c_labelColor)

```


![_images/ReleaseNotes-input_color.png](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-input_color.png)

Added support for arrays and functions for working with them. You can now use the powerful new array feature to build custom datasets. See our [User Manual page on arrays](https://www.tradingview.com/pine-script-docs/en/v4/essential/Arrays.html) and our [blog](https://www.tradingview.com/blog/en/arrays-are-now-available-in-pine-script-20052/):

```
//@version=4
study("My Script")
a = array.new_float(0)
for i = 0 to 5
    array.push(a, close[i] - open[i])
plot(array.get(a, 4))

```


The following functions now accept a series length parameter. Learn more about this feature in our [blog](https://www.tradingview.com/blog/en/pine-functions-support-dynamic-length-arguments-20554/):

*   [alma()](https://www.tradingview.com/pine-script-reference/v4/#fun_alma)
*   [change()](https://www.tradingview.com/pine-script-reference/v4/#fun_change)
*   [highest()](https://www.tradingview.com/pine-script-reference/v4/#fun_highest)
*   [highestbars()](https://www.tradingview.com/pine-script-reference/v4/#fun_highestbars)
*   [linreg()](https://www.tradingview.com/pine-script-reference/v4/#fun_linreg)
*   [lowest()](https://www.tradingview.com/pine-script-reference/v4/#fun_lowest)
*   [lowestbars()](https://www.tradingview.com/pine-script-reference/v4/#fun_lowestbars)
*   [mom()](https://www.tradingview.com/pine-script-reference/v4/#fun_mom)
*   [sma()](https://www.tradingview.com/pine-script-reference/v4/#fun_sma)
*   [sum()](https://www.tradingview.com/pine-script-reference/v4/#fun_sum)
*   [vwma()](https://www.tradingview.com/pine-script-reference/v4/#fun_vwma)
*   [wma()](https://www.tradingview.com/pine-script-reference/v4/#fun_wma)

```
//@version=4
study("My Script", overlay = true)
length = input(10, "Length", input.integer, minval = 1, maxval = 100)
avgBar = avg(highestbars(length), lowestbars(length))
float dynLen = nz(abs(avgBar) + 1, length)
dynSma = sma(close, int(dynLen))
plot(dynSma)

```


### [August 2020](#id71)

*   Optimized script compilation time. Scripts now compile 1.5 to 2 times faster.

### [June 2020](#id73)

*   New `resolution` parameter was added to the `study` function. Now you can add MTF functionality to scripts and decide the timeframe you want the indicator to run on.

![_images/ReleaseNotes-Mtf.png](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-Mtf.png)

Please note that you need to reapply the indicator in order for the resolution parameter to appear.

*   The `tooltip` argument was added to the `label.new` function along with the `label.set_tooltip` function:
    
    ```
//@version=4
study("My Script", overlay=true)
var l=label.new(bar_index, close, yloc=yloc.abovebar, text="Label")
label.set_x(l,bar_index)
label.set_tooltip(l, "Label Tooltip")

```

    

![_images/ReleaseNotes-Tooltip.png](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-Tooltip.png)

*   Added an ability to create [alerts on strategies](https://www.tradingview.com/support/solutions/43000481368).
*   A new function [line.get\_price()](https://www.tradingview.com/pine-script-reference/v4/#fun_line{dot}get_price) can be used to determine the price level at which the line is located on a certain bar.
*   New [label styles](https://www.tradingview.com/pine-script-reference/v4/#fun_label{dot}new) allow you to position the label pointer in any direction.

![_images/ReleaseNotes-new_label_styles.png](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-new_label_styles.png)

*   Find and Replace was added to Pine Script® Editor. To use this, press CTRL+F (find) or CTRL+H (find and replace).

![_images/ReleaseNotes-FindReplace.jpg](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-FindReplace.jpg)

*   `timezone` argument was added for time functions. Now you can specify timezone for `second`, `minute`, `hour`, `year`, `month`, `dayofmonth`, `dayofweek` functions:
    
    ```
//@version=4
study("My Script")
plot(hour(1591012800000, "GMT+1"))

```

    
*   `syminfo.basecurrency` variable was added. Returns the base currency code of the current symbol. For EURUSD symbol returns EUR.
    

### [May 2020](#id74)

*   `else if` statement was added
*   The behavior of `security()` function has changed: the `expression` parameter can be series or tuple.

### [April 2020](#id75)

New function was added:

*   `quandl()` - request quandl data for a symbol

### [March 2020](#id76)

New function was added:

*   `financial()` - request financial data for a symbol

New functions for common indicators were added:

*   `cmo()` - Chande Momentum Oscillator
*   `mfi()` - Money Flow Index
*   `bb()` - Bollinger Bands
*   `bbw()` - Bollinger Bands Width
*   `kc()` - Keltner Channels
*   `kcw()` - Keltner Channels Width
*   `dmi()` - DMI/ADX
*   `wpr()` - Williams % R
*   `hma()` - Hull Moving Average
*   `supertrend()` - SuperTrend

Added a detailed description of all the fields in the [Strategy Tester Report](https://www.tradingview.com/support/solutions/43000561856/)

### [February 2020](#id77)

*   New Pine Script® indicator VWAP Anchored was added. Now you can specify the time period: Session, Month, Week, Year.
    
*   Fixed a problem with calculating `percentrank` function. Now it can return a zero value, which did not happen before due to an incorrect calculation.
    
*   The default `transparency` parameter for the `plot()`, `plotshape()`, and `plotchar()` functions is now 0%.
    
*   For the functions `plot()`, `plotshape()`, `plotchar()`, `plotbar()`, `plotcandle()`, `plotarrow()`, you can set the `display` parameter, which controls the display of the plot. The following values can be assigned to it:
    
    *   `display.none` - the plot is not displayed
    *   `display.all` - the plot is displayed (Default)
*   The `textalign` argument was added to the `label.new` function along with the `label.set_textalign` function. Using those, you can control the alignment of the label’s text:
    
    ```
//@version=4
study("My Script", overlay = true)
var l = label.new(bar_index, high, text="Right\n aligned\n text", textalign=text.align_right)
label.set_xy(l, bar_index, high)

```

    
    ![_images/ReleaseNotes-Label_text_align.png](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-Label_text_align.png)

### [January 2020](#id78)

New built-in variables were added:

*   `iii` - Intraday Intensity Index
*   `wvad` - Williams Variable Accumulation/Distribution
*   `wad` - Williams Accumulation/Distribution
*   `obv` - On Balance Volume
*   `pvt` - Price-Volume Trend
*   `nvi` - Negative Volume Index
*   `pvi` - Positive Volume Index

New parameters were added for `strategy.close()`:

*   `qty` - the number of contracts/shares/lots/units to exit a trade with
*   `qty_percent` - defines the percentage of entered contracts/shares/lots/units to exit a trade with
*   `comment` - addtional notes on the order

New parameter was added for `strategy.close_all`:

*   `comment` - additional notes on the order

[2019](#id79)
----------------------------------------------------

### [December 2019](#id80)

*   Warning messages were added.
    
    For example, if you don’t specify exit parameters for `strategy.exit` - `profit`, `limit`, `loss`, `stop` or one of the following pairs: `trail_offset` and `trail_price` / `trail_points` - you will see a warning message in the console in the Pine Script® editor.
    
*   Increased the maximum number of arguments in `max`, `min`, `avg` functions. Now you can use up to ten arguments in these functions.
    

### [October 2019](#id81)

*   `plotchar()` function now supports most of the Unicode symbols:
    
    ```
//@version=4
study("My Script", overlay=true)
plotchar(open > close, char="🐻")

```

    
    ![_images/ReleaseNotes-Bears_in_plotchar.png](https://tradingview.com/pine-script-docs/en/v5/_images/ReleaseNotes-Bears_in_plotchar.png)
*   New `bordercolor` argument of the `plotcandle()` function allows you to change the color of candles’ borders:
    
    ```
//@version=4
study("My Script")
plotcandle(open, high, low, close, title='Title', color = open < close ? color.green : color.red, wickcolor=color.black, bordercolor=color.orange)

```

    
*   New variables added:
    
    *   `syminfo.description` - returns a description of the current symbol
    *   `syminfo.currency` - returns the currency code of the current symbol (EUR, USD, etc.)
    *   `syminfo.type` - returns the type of the current symbol (stock, futures, index, etc.)

### [September 2019](#id82)

New parameters to the `strategy` function were added:

*   `process_orders_on_close` allows the broker emulator to try to execute orders after calculating the strategy at the bar’s close
*   `close_entries_rule` allows to define the sequence used for closing positions

Some fixes were made:

*   `fill()` function now works correctly with `na` as the `color` parameter value
*   `sign()` function now calculates correctly for literals and constants

`str.replace_all(source, target, replacement)` function was added. It replaces each occurrence of a `target` string in the `source` string with a `replacement` string

### [July-August 2019](#id83)

New variables added:

*   `timeframe.isseconds` returns true when current resolution is in seconds
*   `timeframe.isminutes` returns true when current resolution is in minutes
*   `time_close` returns the current bar’s close time

The behavior of some functions, variables and operators has changed:

*   The `time` variable returns the correct open time of the bar for more special cases than before
    
*   An optional _seconds_ parameter of the `timestamp()` function allows you to set the time to within seconds
    
*   `security()` function:
    
    *   Added the possibility of requesting resolutions in seconds:
        
        1, 5, 15, 30 seconds (chart resolution should be less than or equal to the requested resolution)
        
    *   Reduced the maximum value that can be requested in some of the other resolutions:
        
        from 1 to 1440 minutes
        
        from 1 to 365 days
        
        from 1 to 52 weeks
        
        from 1 to 12 months
        
*   Changes to the evaluation of ternary operator branches:
    
    In Pine Script® v3, during the execution of a ternary operator, both its branches are calculated, so when this script is added to the chart, a long position is opened, even if the long() function is not called:
    
    ```
//@version=3
strategy(title = "My Strategy")
long() =>
    strategy.entry("long", true, 1, when = open > high[1])
    1
c = 0
c := true ? 1 : long()
plot(c)

```

    
    Pine Script® v4 contains built-in functions with side effects ( `line.new` and `label.new` ). If calls to these functions are present in both branches of a ternary operator, both function calls would be executed following v3 conventions. Thus, in Pine Script® v4, only the branch corresponding to the evaluated condition is calculated. While this provides a viable solution in some cases, it will modify the behavior of scripts which depended on the fact that both branches of a ternary were evaluated. The solution is to pre-evaluate expressions prior to the ternary operator. The conversion utility takes this requirement into account when converting scripts from v3 to v4, so that script behavior will be identical in v3 and v4.
    

### [June 2019](#id84)

*   Support for drawing objects. Added _label_ and _line_ drawings
*   `var` keyword for one time variable initialization
*   Type system improvements:
    *   _series string_ data type
    *   functions for explicit type casting
    *   syntax for explicit variable type declaration
    *   new _input_ type forms
*   Renaming of built-ins and a version 3 to 4 converter utility
*   `max_bars_back` function to control series variables internal history buffer sizes
*   Pine Script® documentation versioning