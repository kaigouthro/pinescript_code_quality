[

![Pine Script® logo](https://tradingview.com/pine-script-docs/en/v5/_images/Pine-script-logo.svg)

](https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html)

[Introduction](#id5)
-------------------------------------------------------------------

TradingView alerts run 24x7 on our servers and do not require users to be logged in to execute. Alerts are created from the charts user interface (_UI_). You will find all the information necessary to understand how alerts work and how to create them from the charts UI in the Help Center’s [About TradingView alerts](https://www.tradingview.com/support/solutions/43000520149) page.

Some of the alert types available on TradingView (_generic alerts_, _drawing alerts_ and _script alerts_ on order fill events) are created from symbols or scripts loaded on the chart and do not require specific coding. Any user can create these types of alerts from the charts UI.

Other types of alerts (_script alerts_ triggering on _alert() function calls_, and _alertcondition() alerts_) require specific Pine Script® code to be present in a script to create an _alert event_ before script users can create alerts from them using the charts UI. Additionally, while script users can create _script alerts_ triggering on _order fill events_ from the charts UI on any strategy loaded on their chart, Programmers can specify explicit order fill alert messages in their script for each type of order filled by the broker emulator.

This page covers the different ways Pine Script® programmers can code their scripts to create alert events from which script users will in turn be able to create alerts from the charts UI. We will cover:

*   How to use the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function to _alert() function calls_ in indicators or strategies, which can then be included in _script alerts_ created from the charts UI.
*   How to add custom alert messages to be included in _script alerts_ triggering on the _order fill events_ of strategies.
*   How to use the [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) function to generate, in indicators only, _alertcondition() events_ which can then be used to create _alertcondition() alerts_ from the charts UI.

Keep in mind that:

*   No alert-related Pine Script® code can create a running alert in the charts UI; it merely creates alert events which can then be used by script users to create running alerts from the charts UI.
*   Alerts only trigger in the realtime bar. The operational scope of Pine Script® code dealing with any type of alert is therefore restricted to realtime bars only.
*   When an alert is created in the charts UI, TradingView saves a mirror image of the script and its inputs, along with the chart’s main symbol and timeframe to run the alert on its servers. Subsequent changes to your script’s inputs or the chart will thus not affect running alerts previously created from them. If you want any changes to your context to be reflected in a running alert’s behavior, you will need to delete the alert and create a new one in the new context.

### [Background](#id6)

The different methods Pine programmers can use today to create alert events in their script are the result of successive enhancements deployed throughout Pine Script®’s evolution. The [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) function, which works in indicators only, was the first feature allowing Pine Script® programmers to create alert events. Then came order fill alerts for strategies, which trigger when the broker emulator creates _order fill events_. _Order fill events_ require no special code for script users to create alerts on them, but by way of the `alert_message` parameter for order-generating `strategy.*()` functions, programmers can customize the message of alerts triggering on _order fill events_ by defining a distinct alert message for any number of order fulfillment events.

The [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function is the most recent addition to Pine Script®. It more or less supersedes [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition), and when used in strategies, provides a useful complement to alerts on _order fill events_.

### [Which type of alert is best?](#id7)

For Pine Script® programmers, the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function will generally be easier and more flexible to work with. Contrary to [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition), it allows for dynamic alert messages, works in both indicators and strategies and the programmer decides on the frequency of [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) events.

While [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls can be generated on any logic programmable in Pine, including when orders are **sent** to the broker emulator in strategies, they cannot be coded to trigger when orders are **executed** (or _filled_) because after orders are sent to the broker emulator, the emulator controls their execution and does not report fill events back to the script directly.

When a script user wants to generate an alert on a strategy’s order fill events, he must include those events when creating a _script alert_ on the strategy in the “Create Alert” dialog box. No special code is required in scripts for users to be able to do this. The message sent with order fill events can, however, be customized by programmers through use of the `alert_message` parameter in order-generating `strategy.*()` function calls. A combination of [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls and the use of custom `alert_message` arguments in order-generating `strategy.*()` calls should allow programmers to generate alert events on most conditions occurring in their script’s execution.

The [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) function remains in Pine Script® for backward compatibility, but it can also be used advantageously to generate distinct alerts available for selection as individual items in the “Create Alert” dialog box’s “Condition” field.

[Script alerts](#id8)
---------------------------------------------------------------------

When a script user creates a _script alert_ using the “Create Alert” dialog box, the events able to trigger the alert will vary depending on whether the alert is created from an indicator or a strategy.

A _script alert_ created from an **indicator** will trigger when:

*   The indicator contains [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls.
*   The code’s logic allows a specific [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call to execute.
*   The frequency specified in the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call allows the alert to trigger.

A _script alert_ created from a **strategy** can trigger on _alert() function calls_, on _order fill events_, or both. The script user creating an alert on a strategy decides which type of events he wishes to include in his _script alert_. While users can create a _script alert_ on _order fill events_ without the need for a strategy to include special code, it must contain [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls for users to include _alert() function calls_ in their _script alert_.

### [\`alert()\` function events](#id9)

The [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function has the following signature:

`message`

A “series string” representing the message text sent when the alert triggers. Because this argument allows the “series” form, it can be generated at runtime and differ bar to bar, making it dynamic.

`freq`

An “input string” specifying the triggering frequency of the alert. Valid arguments are:

*   `alert.freq_once_per_bar`: Only the first call per realtime bar triggers the alert (default value).
*   `alert.freq_once_per_bar_close`: An alert is only triggered when the realtime bar closes and an [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call is executed during that script iteration.
*   `alert.freq_all`: All calls during the realtime bar trigger the alert.

The [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function can be used in both indicators and strategies. For an [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call to trigger a _script alert_ configured on _alert() function calls_, the script’s logic must allow the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call to execute, **and** the frequency determined by the `freq` parameter must allow the alert to trigger.

Note that by default, strategies are recalculated at the bar’s close, so if the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function with the frequency `alert.freq_all` or `alert.freq_once_per_bar` is used in a strategy, then it will be called no more often than once at the bar’s close. In order to enable the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function to be called during the bar construction process, you need to enable the `calc_on_every_tick` option.

#### [Using all \`alert()\` calls](#id10)

Let’s look at an example where we detect crosses of the RSI centerline:

```
//@version=5
indicator("All `alert()` calls")
r = ta.rsi(close, 20)

// Detect crosses.
xUp = ta.crossover( r, 50)
xDn = ta.crossunder(r, 50)
// Trigger an alert on crosses.
if xUp
    alert("Go long (RSI is " + str.tostring(r, "#.00)"))
else if xDn
    alert("Go short (RSI is " + str.tostring(r, "#.00)"))

plotchar(xUp, "Go Long",  "▲", location.bottom, color.lime, size = size.tiny)
plotchar(xDn, "Go Short", "▼", location.top,    color.red,  size = size.tiny)
hline(50)
plot(r)

```


If a _script alert_ is created from this script:

*   When RSI crosses the centerline up, the _script alert_ will trigger with the “Go long…” message. When RSI crosses the centerline down, the _script alert_ will trigger with the “Go short…” message.
*   Because no argument is specified for the `freq` parameter in the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call, the default value of `alert.freq_once_per_bar` will be used, so the alert will only trigger the first time each of the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls is executed during the realtime bar.
*   The message sent with the alert is composed of two parts: a constant string and then the result of the [str.tostring()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}tostring) call which will include the value of RSI at the moment where the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call is executed by the script. An alert message for a cross up would look like: “Go long (RSI is 53.41)”.
*   Because a _script alert_ always triggers on any occurrence of a call to [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert), as long as the frequency used in the call allows for it, this particular script does not allow a script user to restrict his _script alert_ to longs only, for example.

Note that:

*   Contrary to an [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) call which is always placed at column 0 (in the script’s global scope), the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call is placed in the local scope of an [if](https://www.tradingview.com/pine-script-reference/v5/#op_if) branch so it only executes when our triggering condition is met. If an [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call was placed in the script’s global scope at column 0, it would execute on all bars, which would likely not be the desired behavior.
*   An [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) could not accept the same string we use for our alert’s message because of its use of the [str.tostring()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}tostring) call. [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) messages must be constant strings.

Lastly, because [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) messages can be constructed dynamically at runtime, we could have used the following code to generate our alert events:

```
// Trigger an alert on crosses.
if xUp or xDn
    firstPart = (xUp ? "Go long" : "Go short") + " (RSI is "
    alert(firstPart + str.tostring(r, "#.00)"))

```


#### [Using selective \`alert()\` calls](#id11)

When users create a _script alert_ on _alert() function calls_, the alert will trigger on any call the script makes to the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function, provided its frequency constraints are met. If you want to allow your script’s users to select which [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function call in your script will trigger a _script alert_, you will need to provide them with the means to indicate their preference in your script’s inputs, and code the appropriate logic in your script. This way, script users will be able to create multiple _script alerts_ from a single script, each behaving differently as per the choices made in the script’s inputs prior to creating the alert in the charts UI.

Suppose, for our next example, that we want to provide the option of triggering alerts on only longs, only shorts, or both. You could code your script like this:

```
//@version=5
indicator("Selective `alert()` calls")
detectLongsInput  = input.bool(true,  "Detect Longs")
detectShortsInput = input.bool(true,  "Detect Shorts")
repaintInput      = input.bool(false, "Allow Repainting")

r = ta.rsi(close, 20)
// Detect crosses.
xUp = ta.crossover( r, 50)
xDn = ta.crossunder(r, 50)
// Only generate entries when the trade's direction is allowed in inputs.
enterLong  = detectLongsInput  and xUp and (repaintInput or barstate.isconfirmed)
enterShort = detectShortsInput and xDn and (repaintInput or barstate.isconfirmed)
// Trigger the alerts only when the compound condition is met.
if enterLong
    alert("Go long (RSI is " + str.tostring(r, "#.00)"))
else if enterShort
    alert("Go short (RSI is " + str.tostring(r, "#.00)"))

plotchar(enterLong,  "Go Long",  "▲", location.bottom, color.lime, size = size.tiny)
plotchar(enterShort, "Go Short", "▼", location.top,    color.red,  size = size.tiny)
hline(50)
plot(r)

```


Note how:

*   We create a compound condition that is met only when the user’s selection allows for an entry in that direction. A long entry on a crossover of the centerline only triggers the alert when long entries have been enabled in the script’s Inputs.
*   We offer the user to indicate his repainting preference. When he does not allow the calculations to repaint, we wait until the bar’s confirmation to trigger the compound condition. This way, the alert and the marker only appear at the end of the realtime bar.
*   If a user of this script wanted to create two distinct script alerts from this script, i.e., one triggering only on longs, and one only on shorts, then he would need to:
    *   Select only “Detect Longs” in the inputs and create a first _script alert_ on the script.
    *   Select only “Detect Shorts” in the Inputs and create another _script alert_ on the script.

#### [In strategies](#id12)

[alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function calls can be used in strategies also, with the provision that strategies, by default, only execute on the [close](https://www.tradingview.com/pine-script-reference/v5/#var_close) of realtime bars. Unless `calc_on_every_tick = true` is used in the [strategy()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy) declaration statement, all [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls will use the `alert.freq_once_per_bar_close` frequency, regardless of the argument used for `freq`.

While _script alerts_ on strategies will use _order fill events_ to trigger alerts when the broker emulator fills orders, [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) can be used advantageously to generate other alert events in strategies.

This strategy creates _alert() function calls_ when RSI moves against the trade for three consecutive bars:

```
//@version=5
strategy("Strategy with selective `alert()` calls")
r = ta.rsi(close, 20)

// Detect crosses.
xUp = ta.crossover( r, 50)
xDn = ta.crossunder(r, 50)
// Place orders on crosses.
if xUp
    strategy.entry("Long", strategy.long)
else if xDn
    strategy.entry("Short", strategy.short)

// Trigger an alert when RSI diverges from our trade's direction.
divInLongTrade  = strategy.position_size > 0 and ta.falling(r, 3)
divInShortTrade = strategy.position_size < 0 and ta.rising( r, 3)
if divInLongTrade
    alert("WARNING: Falling RSI", alert.freq_once_per_bar_close)
if divInShortTrade
    alert("WARNING: Rising RSI", alert.freq_once_per_bar_close)

plotchar(xUp, "Go Long",  "▲", location.bottom, color.lime, size = size.tiny)
plotchar(xDn, "Go Short", "▼", location.top,    color.red,  size = size.tiny)
plotchar(divInLongTrade,  "WARNING: Falling RSI", "•", location.top,    color.red,  size = size.tiny)
plotchar(divInShortTrade, "WARNING: Rising RSI",  "•", location.bottom, color.lime, size = size.tiny)
hline(50)
plot(r)

```


If a user created a _script alert_ from this strategy and included both _order fill events_ and _alert() function calls_ in his alert, the alert would trigger whenever an order is executed, or when one of the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls was executed by the script on the realtime bar’s closing iteration, i.e., when [barstate.isrealtime](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isrealtime) and [barstate.isconfirmed](https://www.tradingview.com/pine-script-reference/v5/#var_barstate{dot}isconfirmed) are both true. The _alert() function events_ in the script would only trigger the alert when the realtime bar closes because `alert.freq_once_per_bar_close` is the argument used for the `freq` parameter in the [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) calls.

### [Order fill events](#id13)

When a _script alert_ is created from an indicator, it can only trigger on _alert() function calls_. However, when a _script alert_ is created from a strategy, the user can specify that _order fill events_ also trigger the _script alert_. An _order fill event_ is any event generated by the broker emulator which causes a simulated order to be executed. It is the equivalent of a trade order being filled by a broker/exchange. Orders are not necessarily executed when they are placed. In a strategy, the execution of orders can only be detected indirectly and after the fact, by analyzing changes in built-in variables such as [strategy.opentrades](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}opentrades) or [strategy.position\_size](https://www.tradingview.com/pine-script-reference/v5/#var_strategy{dot}position_size). _Script alerts_ configured on _order fill events_ are thus useful in that they allow the triggering of alerts at the precise moment of an order’s execution, before a script’s logic can detect it.

Pine Script® programmers can customize the alert message sent when specific orders are executed. While this is not a pre-requisite for _order fill events_ to trigger, custom alert messages can be useful because they allow custom syntax to be included with alerts in order to route actual orders to a third-party execution engine, for example. Specifying custom alert messages for specific _order fill events_ is done by means of the `alert_message` parameter in functions which can generate orders: [strategy.close()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}close), [strategy.entry()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry), [strategy.exit()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}exit) and [strategy.order()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}order).

The argument used for the `alert_message` parameter is a “series string”, so it can be constructed dynamically using any variable available to the script, as long as it is converted to string format.

Let’s look at a strategy where we use the `alert_message` parameter in both our [strategy.entry()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry) calls:

```
//@version=5
strategy("Strategy using `alert_message`")
r = ta.rsi(close, 20)

// Detect crosses.
xUp = ta.crossover( r, 50)
xDn = ta.crossunder(r, 50)
// Place order on crosses using a custom alert message for each.
if xUp
    strategy.entry("Long", strategy.long, stop = high, alert_message = "Stop-buy executed (stop was " + str.tostring(high) + ")")
else if xDn
    strategy.entry("Short", strategy.short, stop = low, alert_message = "Stop-sell executed (stop was " + str.tostring(low) + ")")

plotchar(xUp, "Go Long",  "▲", location.bottom, color.lime, size = size.tiny)
plotchar(xDn, "Go Short", "▼", location.top,    color.red,  size = size.tiny)
hline(50)
plot(r)

```


Note that:

*   We use the `stop` parameter in our [strategy.entry()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy{dot}entry) calls, which creates stop-buy and stop-sell orders. This entails that buy orders will only execute once price is higher than the high on the bar where the order is placed, and sell orders will only execute once price is lower than the low on the bar where the order is placed.
*   The up/down arrows which we plot with [plotchar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotchar) are plotted when orders are **placed**. Any number of bars may elapse before the order is actually executed, and in some cases the order will never be executed because price does not meet the required condition.
*   Because we use the same `id` argument for all buy orders, any new buy order placed before a previous order’s condition is met will replace that order. The same applies to sell orders.
*   Variables included in the `alert_message` argument are evaluated when the order is executed, so when the alert triggers.

When the `alert_message` parameter is used in a strategy’s order-generating `strategy.*()` function calls, script users must include the `{{strategy.order.alert_message}}` placeholder in the “Create Alert” dialog box’s “Message” field when creating _script alerts_ on _order fill events_. This is required so the `alert_message` argument used in the order-generating `strategy.*()` function calls is used in the message of alerts triggering on each _order fill event_. When only using the `{{strategy.order.alert_message}}` placeholder in the “Message” field and the `alert_message` parameter is present in only some of the order-generating `strategy.*()` function calls in your strategy, an empty string will replace the placeholder in the message of alerts triggered by any order-generating `strategy.*()` function call not using the `alert_message` parameter.

While other placeholders can be used in the “Create Alert” dialog box’s “Message” field by users creating alerts on _order fill events_, they cannot be used in the argument of `alert_message`.

[\`alertcondition()\` events](#id14)
--------------------------------------------------------------------------------------------

The [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) function allows programmers to create individual _alertcondition events_ in their indicators. One indicator may contain more than one [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) call. Each call to [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) in a script will create a corresponding alert selectable in the “Condition” dropdown menu of the “Create Alert” dialog box.

While the presence of [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) calls in a **strategy** script will not cause a compilation error, alerts cannot be created from them.

The [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) function has the following signature:

```
alertcondition(condition, title, message)

```


`condition`

A “series bool” value (`true` or `false`) which determines when the alert will trigger. It is a required argument. When the value is `true` the alert will trigger. When the value is `false` the alert will not trigger. Contrary to [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) function calls, [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) calls must start at column zero of a line, so cannot be placed in conditional blocks.

`title`

A “const string” optional argument that sets the name of the alert condition as it will appear in the “Create Alert” dialog box’s “Condition” field in the charts UI. If no argument is supplied, “Alert” will be used.

`message`

A “const string” optional argument that specifies the text message to display when the alert triggers. The text will appear in the “Message” field of the “Create Alert” dialog box, from where script users can then modify it when creating an alert. **As this argument must be a “const string”, it must be known at compilation time and thus cannot vary bar to bar.** It can, however, contain placeholders which will be replaced at runtime by dynamic values that may change bar to bar. See this page’s [Placeholders](#placeholders) section for a list.

The [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) function does not include a `freq` parameter. The frequency of _alertcondition() alerts_ is determined by users in the “Create Alert” dialog box.

### [Using one condition](#id15)

Here is an example of code creating _alertcondition() events_:

```
//@version=5
indicator("`alertcondition()` on single condition")
r = ta.rsi(close, 20)

xUp = ta.crossover( r, 50)
xDn = ta.crossunder(r, 50)

plot(r, "RSI")
hline(50)
plotchar(xUp, "Long",  "▲", location.bottom, color.lime, size = size.tiny)
plotchar(xDn, "Short", "▼", location.top,    color.red,  size = size.tiny)

alertcondition(xUp, "Long Alert",  "Go long")
alertcondition(xDn, "Short Alert", "Go short ")

```


Because we have two [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) calls in our script, two different alerts will be available in the “Create Alert” dialog box’s “Condition” field: “Long Alert” and “Short Alert”.

If we wanted to include the value of RSI when the cross occurs, we could not simply add its value to the `message` string using `str.tostring(r)`, as we could in an [alert()](https://www.tradingview.com/pine-script-reference/v5/#fun_alert) call or in an `alert_message` argument in a strategy. We can, however, include it using a placeholder. This shows two alternatives:

```
alertcondition(xUp, "Long Alert",  "Go long. RSI is {{plot_0}}")
alertcondition(xDn, "Short Alert", 'Go short. RSI is {{plot("RSI")}}')

```


Note that:

*   The first line uses the `{{plot_0}}` placeholder, where the plot number corresponds to the order of the plot in the script.
*   The second line uses the `{{plot("[plot_title]")}}` type of placeholder, which must include the `title` of the [plot()](https://www.tradingview.com/pine-script-reference/v5/#fun_plot) call used in our script to plot RSI. Double quotes are used to wrap the plot’s title inside the `{{plot("RSI")}}` placeholder. This requires that we use single quotes to wrap the `message` string.
*   Using one of these methods, we can include any numeric value that is plotted by our indicator, but as strings cannot be plotted, no string variable can be used.

### [Using compound conditions](#id16)

If we want to offer script users the possiblity of creating a single alert from an indicator using multiple [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) calls, we will need to provide options in the script’s inputs through which users will indicate the conditions they want to trigger their alert before creating it.

This script demonstrates one way to do it:

```
//@version=5
indicator("`alertcondition()` on multiple conditions")
detectLongsInput  = input.bool(true, "Detect Longs")
detectShortsInput = input.bool(true, "Detect Shorts")

r = ta.rsi(close, 20)
// Detect crosses.
xUp = ta.crossover( r, 50)
xDn = ta.crossunder(r, 50)
// Only generate entries when the trade's direction is allowed in inputs.
enterLong  = detectLongsInput  and xUp
enterShort = detectShortsInput and xDn

plot(r)
plotchar(enterLong,  "Go Long",  "▲", location.bottom, color.lime, size = size.tiny)
plotchar(enterShort, "Go Short", "▼", location.top,    color.red,  size = size.tiny)
hline(50)
// Trigger the alert when one of the conditions is met.
alertcondition(enterLong or enterShort, "Compound alert", "Entry")

```


Note how the [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) call is allowed to trigger on one of two conditions. Each condition can only trigger the alert if the user enables it in the script’s inputs before creating the alert.

### [Placeholders](#id17)

These placeholders can be used in the `message` argument of [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) calls. They will be replaced with dynamic values when the alert triggers. They are the only way to include dynamic values (values that can vary bar to bar) in [alertcondition()](https://www.tradingview.com/pine-script-reference/v5/#fun_alertcondition) messages.

Note that users creating _alertcondition() alerts_ from the “Create Alert” dialog box in the charts UI are also able to use these placeholders in the dialog box’s “Message” field.

`{{exchange}}`

Exchange of the symbol used in the alert (NASDAQ, NYSE, MOEX, etc.). Note that for delayed symbols, the exchange will end with “\_DL” or “\_DLY.” For example, “NYMEX\_DL.”

`{{interval}}`

Returns the timeframe of the chart the alert is created on. Note that Range charts are calculated based on 1m data, so the placeholder will always return “1” on any alert created on a Range chart.

`{{open}}`, `{{high}}`, `{{low}}`, `{{close}}`, `{{volume}}`

Corresponding values of the bar on which the alert has been triggered.

`{{plot_0}}`, `{{plot_1}}`, \[…\], `{{plot_19}}`

Value of the corresponding plot number. Plots are numbered from zero to 19 in order of appearance in the script, so only one of the first 20 plots can be used. For example, the built-in “Volume” indicator has two output series: Volume and Volume MA, so you could use the following:

```
alertcondition(volume > sma(volume,20), "Volume alert", "Volume ({{plot_0}}) > average ({{plot_1}})")

```


`{{plot("[plot_title]")}}`

This placeholder can be used when one needs to refer to a plot using the `title` argument used in a [plot()](https://www.tradingview.com/pine-script-reference/v5/#fun_plot) call. Note that double quotation marks (`"`) **must** be used inside the placeholder to wrap the `title` argument. This requires that a single quotation mark (`'`) be used to wrap the `message` string:

```
//@version=5
indicator("")
r = ta.rsi(close, 14)
xUp = ta.crossover(r, 50)
plot(r, "RSI", display = display.none)
alertcondition(xUp, "xUp alert", message = 'RSI is bullish at: {{plot("RSI")}}')

```


`{{ticker}}`

Ticker of the symbol used in the alert (AAPL, BTCUSD, etc.).

`{{time}}`

Returns the time at the beginning of the bar. Time is UTC, formatted as `yyyy-MM-ddTHH:mm:ssZ`, so for example: `2019-08-27T09:56:00Z`.

`{{timenow}}`

Current time when the alert triggers, formatted in the same way as `{{time}}`. The precision is to the nearest second, regardless of the chart’s timeframe.

[Avoiding repainting with alerts](#id18)
----------------------------------------------------------------------------------------------------------

The most common instances of repainting traders want to avoid with alerts are ones where they must prevent an alert from triggering at some point during the realtime bar when it would **not** have triggered at its close. This can happen when these conditions are met:

*   The calculations used in the condition triggering the alert can vary during the realtime bar. This will be the case with any calculation using `high`, `low` or `close`, for example, which includes almost all built-in indicators. It will also be the case with the result of any [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security) call using a higher timeframe than the chart’s, when the higher timeframe’s current bar has not closed yet.
*   The alert can trigger before the close of the realtime bar, so with any frequency other than “Once Per Bar Close”.

The simplest way to avoid this type of repainting is to configure the triggering frequency of alerts so they only trigger on the close of the realtime bar. There is no panacea; avoiding this type of repainting **always** entails waiting for confirmed information, which means the trader must sacrifice immediacy to achieve reliability.

Note that other types of repainting such as those documented in our [Repainting](https://tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html#pagerepainting) section may not be preventable by simply triggering alerts on the close of realtime bars.

[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)