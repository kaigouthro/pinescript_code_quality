[Introduction](#id1)
-------------------------------------------------------------------

Pine Script® has hundreds of _built-in_ variables and functions. They provide your scripts with valuable information and make calculations for you, dispensing you from coding them. The better you know the built-ins, the more you will be able to do with your Pine scripts.

In this page we present an overview of some of Pine Script®’s built-in variables and functions. They will be covered in more detail in the pages of this manual covering specific themes.

All built-in variables and functions are defined in the Pine Script® [v5 Reference Manual](https://www.tradingview.com/pine-script-reference/v5/). It is called a “Reference Manual” because it is the definitive reference on the Pine Script® language. It is an essential tool that will accompany you anytime you code in Pine, whether you are a beginner or an expert. If you are learning your first programming language, make the [Reference Manual](https://www.tradingview.com/pine-script-reference/v5/) your friend. Ignoring it will make your programming experience with Pine Script® difficult and frustrating — as it would with any other programming language.

Variables and functions in the same family share the same _namespace_, which is a prefix to the function’s name. The [ta.sma()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}sma) function, for example, is in the `ta` namespace, which stands for “technical analysis”. A namespace can contain both variables and functions.

Some variables have function versions as well, e.g.:

*   The [ta.tr](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}tr) variable returns the “True Range” of the current bar. The [ta.tr(true)](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}tr) function call also returns the “True Range”, but when the previous [close](https://www.tradingview.com/pine-script-reference/v5/#var_close) value which is normally needed to calculate it is [na](https://www.tradingview.com/pine-script-reference/v5/#var_na), it calculates using `high - low` instead.
*   The [time](https://www.tradingview.com/pine-script-reference/v5/#var_time) variable gives the time at the [open](https://www.tradingview.com/pine-script-reference/v5/#var_open) of the current bar. The [time(timeframe)](https://www.tradingview.com/pine-script-reference/v5/#fun_time) function returns the time of the bar’s [open](https://www.tradingview.com/pine-script-reference/v5/#var_open) from the `timeframe` specified, even if the chart’s timeframe is different. The [time(timeframe, session)](https://www.tradingview.com/pine-script-reference/v5/#fun_time) function returns the time of the bar’s [open](https://www.tradingview.com/pine-script-reference/v5/#var_open) from the `timeframe` specified, but only if it is within the `session` time. The [time(timeframe, session, timezone)](https://www.tradingview.com/pine-script-reference/v5/#fun_time) function returns the time of the bar’s [open](https://www.tradingview.com/pine-script-reference/v5/#var_open) from the `timeframe` specified, but only if it is within the `session` time in the specified `timezone`.

[Built-in variables](#id2)
-------------------------------------------------------------------------------

Built-in variables exist for different purposes. These are a few examples:

*   Price- and volume-related variables: [open](https://www.tradingview.com/pine-script-reference/v5/#var_open), [high](https://www.tradingview.com/pine-script-reference/v5/#var_high), [low](https://www.tradingview.com/pine-script-reference/v5/#var_low), [close](https://www.tradingview.com/pine-script-reference/v5/#var_close), [hl2](https://www.tradingview.com/pine-script-reference/v5/#var_hl2), [hlc3](https://www.tradingview.com/pine-script-reference/v5/#var_hlc3), [ohlc4](https://www.tradingview.com/pine-script-reference/v5/#var_ohlc4), and [volume](https://www.tradingview.com/pine-script-reference/v5/#var_volume).
*   Symbol-related information in the `syminfo` namespace: [syminfo.basecurrency](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}basecurrency), [syminfo.currency](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}currency), [syminfo.description](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}description), [syminfo.mintick](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}mintick), [syminfo.pointvalue](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}pointvalue), [syminfo.prefix](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}prefix), [syminfo.root](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}root), [syminfo.session](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}session), [syminfo.ticker](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}ticker), [syminfo.tickerid](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}tickerid), [syminfo.timezone](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}timezone), and [syminfo.type](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}type).
*   Timeframe (a.k.a. “interval” or “resolution”, e.g., 15sec, 30min, 60min, 1D, 3M) variables in the `timeframe` namespace: [timeframe.isseconds](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}isseconds), [timeframe.isminutes](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}isminutes), [timeframe.isintraday](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}isintraday), [timeframe.isdaily](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}isdaily), [timeframe.isweekly](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}isweekly), [timeframe.ismonthly](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}ismonthly), [timeframe.isdwm](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}isdwm), [timeframe.multiplier](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}multiplier), and [timeframe.period](https://www.tradingview.com/pine-script-reference/v5/#var_timeframe{dot}period).
*   Bar states in the `barstate` namespace (see the [Bar states](https://tradingview.com/pine-script-docs/en/v5/concepts/Bar_states.html#pagebarstates) page): [barstate.isconfirmed](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isconfirmed), [barstate.isfirst](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isfirst), [barstate.ishistory](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}ishistory), [barstate.islast](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}islast), [barstate.islastconfirmedhistory](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}islastconfirmedhistory), [barstate.isnew](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isnew), and [barstate.isrealtime](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isrealtime).
*   Strategy-related information in the `strategy` namespace: [strategy.equity](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}equity), [strategy.initial\_capital](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}initial_capital), [strategy.grossloss](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}grossloss), [strategy.grossprofit](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}grossprofit), [strategy.wintrades](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}wintrades), [strategy.losstrades](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}losstrades), [strategy.position\_size](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}position_size), [strategy.position\_avg\_price](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}position_avg_price), [strategy.wintrades](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}wintrades), etc.

[Built-in functions](#id3)
-------------------------------------------------------------------------------

Many functions are used for the result(s) they return. These are a few examples:

*   Math-related functions in the `math` namespace: [math.abs()](https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}abs), [math.log()](https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}log), [math.max()](https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}max), [math.random()](https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}random), [math.round\_to\_mintick()](https://www.tradingview.com/pine-script-reference/v5/#fun_math{dot}round_to_mintick), etc.
*   Technical indicators in the `ta` namespace: [ta.sma()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}sma), [ta.ema()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}ema), [ta.macd()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}macd), [ta.rsi()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}rsi), [ta.supertrend()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}supertrend), etc.
*   Support functions often used to calculate technical indicators in the `ta` namespace: [ta.barssince()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}barssince), [ta.crossover()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}crossover), [ta.highest()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}highest), etc.
*   Functions to request data from other symbols or timeframes in the `request` namespace: [request.dividends()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}dividends), [request.earnings()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}earnings), [request.financial()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}financial), [request.quandl()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}quandl), [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security), [request.splits()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}splits).
*   Functions to manipulate strings in the `str` namespace: [str.format()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}format), [str.length()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}length), [str.tonumber()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}tonumber), [str.tostring()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}tostring), etc.
*   Functions used to define the input values that script users can modify in the script’s “Settings/Inputs” tab, in the `input` namespace: [input()](https://www.tradingview.com/pine-script-reference/v5/#fun_input), [input.color()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}color), [input.int()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}int), [input.session()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}session), [input.symbol()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}symbol), etc.
*   Functions used to manipulate colors in the `color` namespace: [color.from\_gradient()](https://www.tradingview.com/pine-script-reference/v5/#fun_color{dot}from_gradient), [color.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_color{dot}rgb), [color.rgb()](https://www.tradingview.com/pine-script-reference/v5/#fun_color{dot}new), etc.

Some functions do not return a result but are used for their side effects, which means they do something, even if they don’t return a result:

*   Functions used as a declaration statement defining one of three types of Pine scripts, and its properties. Each script must begin with a call to one of these functions: [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator), [strategy()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy) or [library()](https://www.tradingview.com/pine-script-reference/v5/#fun_library).
*   Plotting or coloring functions: [bgcolor()](https://www.tradingview.com/pine-script-reference/v5/#fun_bgcolor), [plotbar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotbar), [plotcandle()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotcandle), [plotchar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotchar), [plotshape()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotshape), [fill()](https://www.tradingview.com/pine-script-reference/v5/#fun_fill).
*   Strategy functions placing orders, in the `strategy` namespace: [strategy.cancel()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}cancel), [strategy.close()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close), [strategy.entry()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry), [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit), [strategy.order()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}order), etc.
*   Strategy functions returning information on indivdual past trades, in the `strategy` namespace: [strategy.closedtrades.entry\_bar\_index()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}entry_bar_index), [strategy.closedtrades.entry\_price()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}entry_price), [strategy.closedtrades.entry\_time()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}entry_time), [strategy.closedtrades.exit\_bar\_index()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}exit_bar_index), [strategy.closedtrades.max\_drawdown()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}max_drawdown), [strategy.closedtrades.max\_runup()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}max_runup), [strategy.closedtrades.profit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}closedtrades{dot}profit), etc.
*   Functions to generate alert events: [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) and [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition).

Other functions return a result, but we don’t always use it, e.g.: [hline()](https://www.tradingview.com/pine-script-reference/v5/#fun_hline), [plot()](https://www.tradingview.com/pine-script-reference/v5/#fun_plot), [array.pop()](https://www.tradingview.com/pine-script-reference/v5/#fun_array{dot}pop), [label.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_label{dot}new), etc.

All built-in functions are defined in the Pine Script® [v5 Reference Manual](https://www.tradingview.com/pine-script-reference/v5/). You can click on any of the function names listed here to go to its entry in the Reference Manual, which documents the function’s signature, i.e., the list of _parameters_ it accepts and the form-type of the value(s) it returns (a function can return more than one result). The Reference Manual entry will also list, for each parameter:

*   Its name.
*   The form-type of the value it requires (we use _argument_ to name the values passed to a function when calling it).
*   If the parameter is required or not.

All built-in functions have one or more parameters defined in their signature. Not all parameters are required for every function.

Let’s look at the [ta.vwma()](https://www.tradingview.com/pine-script-reference/v5/#fun_ta{dot}vwma) function, which returns the volume-weighted moving average of a source value. This is its entry in the Reference Manual:

![../_images/BuiltIns-BuiltInFunctions.png](https://tradingview.com/pine-script-docs/en/v5/_images/BuiltIns-BuiltInFunctions.png)

The entry gives us the information we need to use it:

*   What the function does.
    
*   Its signature (or definition):
    
    ```
ta.vwma(source, length) → series float

```

    
*   The parameters it includes: `source` and `length`
    
*   The form and type of the result it returns: “series float”.
    
*   An example showing it in use: `plot(ta.vwma(close, 15))`.
    
*   An example showing what it does, but in long form, so you can better understand its calculations. Note that this is meant to explain — not as usable code, because it is more complicated and takes longer to execute. There are only disadvantages to using the long form.
    
*   The “RETURNS” section explains exacty what value the function returns.
    
*   The “ARGUMENTS” section lists each parameter and gives the critical information concerning what form-type is required for arguments used when calling the function.
    
*   The “SEE ALSO” section refers you to related Reference Manual entries.
    

This is a call to the function in a line of code that declares a `myVwma` variable and assigns the result of `ta.vwma(close, 20)` to it:

```
myVwma = ta.vwma(close, 20)

```


Note that:

*   We use the built-in variable [close](https://www.tradingview.com/pine-script-reference/v5/#var_close) as the argument for the `source` parameter.
*   We use `20` as the argument for the `length` parameter.
*   If placed in the global scope (i.e., starting in a line’s first position), it will be executed by the Pine Script® runtime on each bar of the chart.

We can also use the parameter names when calling the function. Parameter names are called _keyword arguments_ when used in a function call:

```
myVwma = ta.vwma(source = close, length = 20)

```


You can change the position of arguments when using keyword arguments, but only if you use them for all your arguments. When calling functions with many parameters such as [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator), you can also forego keyword arguments for the first arguments, as long as you don’t skip any. If you skip some, you must then use keyword arguments so the Pine Script® compiler can figure out which parameter they correspond to, e.g.:

```
indicator("Example", "Ex", true, max_bars_back = 100)

```


Mixing things up this way is not allowed:

```
indicator(precision = 3, "Example") // Compilation error!

```


**When calling built-ins, it is critical to ensure that the arguments you use are of the form and type required, which will vary for each parameter.**

To learn how to do this, one needs to understand Pine Script®’s [type system](https://tradingview.com/pine-script-docs/en/v5/language/Type_system.html#pagetypesystem). The Reference Manual entry for each built-in function includes an “ARGUMENTS” section which lists the form-type required for the argument supplied to each of the function’s parameters.

[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)