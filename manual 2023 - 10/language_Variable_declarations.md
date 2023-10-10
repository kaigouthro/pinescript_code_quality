Understanding the impact that declaration modes have on the behavior of variables requires prior knowledge of Pine Script®’s [execution model](https://tradingview.com/pine-script-docs/en/v5/language/Execution_model.html#pageexecutionmodel).

When you declare a variable, if a declaration mode is specified, it must come first. Three modes can be used:

### [On each bar](#id6)

When no explicit declaration mode is specified, i.e. no [var](https://www.tradingview.com/pine-script-reference/v5/#op_var) or [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) keyword is used, the variable is declared and initialized on each bar, e.g., the following declarations from our first set of examples in this page’s introduction:

```
BULL_COLOR = color.lime
i = 1
len = input(20, "Length")
float f = 10.5
closeRoundedToTick = math.round_to_mintick(close)
st = ta.supertrend(4, 14)
[macdLine, signalLine, histLine] = ta.macd(close, 12, 26, 9)
plotColor = if close > open
    color.green
else
    color.red

```


### [\`var\`](#id7)

When the [var](https://www.tradingview.com/pine-script-reference/v5/#op_var) keyword is used, the variable is only initialized once, on the first bar if the declaration is in the global scope, or the first time the local block is executed if the declaration is inside a local block. After that, it will preserve its last value on successive bars, until we reassign a new value to it. This behavior is very useful in many cases where a variable’s value must persist through the iterations of a script across successive bars. For example, suppose we’d like to count the number of green bars on the chart:

```
//@version=5
indicator("Green Bars Count")
var count = 0
isGreen = close >= open
if isGreen
    count := count + 1
plot(count)

```


![../_images/VariableDeclarations-GreenBarsCount.png](https://tradingview.com/pine-script-docs/en/v5/_images/VariableDeclarations-GreenBarsCount.png)

Without the `var` modifier, variable `count` would be reset to zero (thus losing its value) every time a new bar update triggered a script recalculation.

Declaring variables on the first bar only is often useful to manage drawings more efficiently. Suppoose we want to extend the last bar’s [close](https://www.tradingview.com/pine-script-reference/v5/#var_close) line to the right of the right chart. We could write:

```
//@version=5
indicator("Inefficient version", "", true)
closeLine = line.new(bar_index - 1, close, bar_index, close, extend = extend.right, width = 3)
line.delete(closeLine[1])

```


but this is inefficient because we are creating and deleting the line on each historical bar and on each update in the realtime bar. It is more efficient to use:

```
//@version=5
indicator("Efficient version", "", true)
var closeLine = line.new(bar_index - 1, close, bar_index, close, extend = extend.right, width = 3)
if barstate.islast
    line.set_xy1(closeLine, bar_index - 1, close)
    line.set_xy2(closeLine, bar_index, close)

```


Note that:

*   We initialize `closeLine` on the first bar only, using the [var](https://www.tradingview.com/pine-script-reference/v5/#op_var) declaration mode
*   We restrict the execution of the rest of our code to the chart’s last bar by enclosing our code that updates the line in an [if](https://www.tradingview.com/pine-script-reference/v5/#op_if) [barstate.islast](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}islast) structure.

There is a very slight penalty performance for using the [var](https://www.tradingview.com/pine-script-reference/v5/#op_var) declaration mode. For that reason, when declaring constants, it is preferable not to use [var](https://www.tradingview.com/pine-script-reference/v5/#op_var) if performance is a concern, unless the initialization involves calculations that take longer than the maintenance penalty, e.g., functions with complex code or string manipulations.

### [\`varip\`](#id8)

Understanding the behavior of variables using the [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) declaration mode requires prior knowledge of Pine Script®’s [execution model](https://tradingview.com/pine-script-docs/en/v5/language/Execution_model.html#pageexecutionmodel) and [bar states](https://tradingview.com/pine-script-docs/en/v5/concepts/Bar_states.html#pagebarstates).

The [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) keyword can be used to declare variables that escape the _rollback process_, which is explained in the page on Pine Script®’s [execution model](https://tradingview.com/pine-script-docs/en/v5/language/Execution_model.html#pageexecutionmodel).

Whereas scripts only execute once at the close of historical bars, when a script is running in realtime, it executes every time the chart’s feed detects a price or volume update. At every realtime update, Pine Script®’s runtime normally resets the values of a script’s variables to their last committed value, i.e., the value they held when the previous bar closed. This is generally handy, as each realtime script execution starts from a known state, which simplifies script logic.

Sometimes, however, script logic requires code to be able to save variable values **between different executions** in the realtime bar. Declaring variables with [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) makes that possible. The “ip” in [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) stands for _intrabar persist_.

Let’s look at the following code, which does not use [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip):

```
//@version=5
indicator("")
int updateNo = na
if barstate.isnew
    updateNo := 1
else
    updateNo := updateNo + 1

plot(updateNo, style = plot.style_circles)

```


On historical bars, [barstate.isnew](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isnew) is always true, so the plot shows a value of “1” because the `else` part of the [if](https://www.tradingview.com/pine-script-reference/v5/#op_if) structure is never executed. On realtime bars, [barstate.isnew](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isnew) is only [true](https://www.tradingview.com/pine-script-reference/v5/#op_true) when the script first executes on the bar’s “open”. The plot will then briefly display “1” until subsequent executions occur. On the next executions during the realtime bar, the second branch of the [if](https://www.tradingview.com/pine-script-reference/v5/#op_if) statement is executed because [barstate.isnew](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isnew) is no longer true. Since `updateNo` is initialized to [na](https://www.tradingview.com/pine-script-reference/v5/#var_na) at each execution, the `updateNo + 1` expression yields [na](https://www.tradingview.com/pine-script-reference/v5/#var_na), so nothing is plotted on further realtime executions of the script.

If we now use [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) to declare the `updateNo` variable, the script behaves very differently:

```
//@version=5
indicator("")
varip int updateNo = na
if barstate.isnew
    updateNo := 1
else
    updateNo := updateNo + 1

plot(updateNo, style = plot.style_circles)

```


The difference now is that `updateNo` tracks the number of realtime updates that occur on each realtime bar. This can happen because the [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) declaration allows the value of `updateNo` to be preserved between realtime updates; it is no longer rolled back at each realtime execution of the script. The test on [barstate.isnew](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isnew) allows us to reset the update count when a new realtime bar comes in.

Because [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) only affects the behavior of your code in the realtime bar, it follows that backtest results on strategies designed using logic based on [varip](https://www.tradingview.com/pine-script-reference/v5/#op_varip) variables will not be able to reproduce that behavior on historical bars, which will invalidate test results on them. This also entails that plots on historical bars will not be able to reproduce the script’s behavior in realtime.

[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)