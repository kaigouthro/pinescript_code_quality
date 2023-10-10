Identifiers are names used for user-defined variables and functions:

*   They must begin with an uppercase (`A-Z`) or lowercase (`a-z`) letter, or an underscore (`_`).
*   The next characters can be letters, underscores or digits (`0-9`).
*   They are case-sensitive.

Here are some examples:

```swift
myVar
_myVar
my123Var
functionName
MAX_LEN
max_len
maxLen
3barsDown  // NOT VALID!

```


The Pine Script® [Style Guide](writing/Style_guide.html#pagestyleguide) recommends using uppercase SNAKE\_CASE for constants, and camelCase for other identifiers:

```swift
GREEN_COLOR = #4CAF50
MAX_LOOKBACK = 100
int fastLength = 7
// Returns 1 if the argument is `true`, 0 if it is `false` or `na`.
zeroOne(boolValue) => boolValue ? 1 : 0

```


[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)
