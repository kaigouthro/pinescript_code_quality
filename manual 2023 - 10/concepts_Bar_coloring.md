[

![Pine Script® logo](https://tradingview.com/pine-script-docs/en/v5/_images/Pine-script-logo.svg)

](https://www.tradingview.com/pine-script-docs/en/v5/Introduction.md)

The [barcolor()](https://www.tradingview.com/pine-script-reference/v5/#fun_barcolor) function lets you color chart bars. It is the only Pine Script® function that allows a script running in a pane to affect the chart.

The function’s signature is:

```swift
barcolor(color, offset, editable, show_last, title) → void

```


The coloring can be conditional because the `color` parameter accepts “series color” arguments.

The following script renders _inside_ and _outside_ bars in different colors:

![../_images/BarColoring-1.png](https://tradingview.com/pine-script-docs/en/v5/_images/BarColoring-1.png)

```swift
//@version=5
indicator("barcolor example", overlay = true)
isUp = close > open
isDown = close <= open
isOutsideUp = high > high[1] and low < low[1] and isUp
isOutsideDown = high > high[1] and low < low[1] and isDown
isInside = high < high[1] and low > low[1]
barcolor(isInside ? color.yellow : isOutsideUp ? color.aqua : isOutsideDown ? color.purple : na)

```


Note that:

*   The [na](https://www.tradingview.com/pine-script-reference/v5/#var_na) value leaves bars as is.
*   In the [barcolor()](https://www.tradingview.com/pine-script-reference/v5/#fun_barcolor) call, we use embedded [?:](https://www.tradingview.com/pine-script-reference/v5/#op_{question}{colon}) ternary operator expressions to select the color.

[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)
