[

![Pine Script® logo](https://tradingview.com/pine-script-docs/en/v5/_images/Pine-script-logo.svg)

](https://www.tradingview.com/pine-script-docs/en/v5/Introduction.md)

[Introduction](#id1)
-------------------------------------------------------------------

Session information is usable in three different ways in Pine Script®:

1.  **Session strings** containing from-to start times and day information that can be used in functions such as [time()](https://www.tradingview.com/pine-script-reference/v5/#fun_time) and [time\_close()](https://www.tradingview.com/pine-script-reference/v5/#fun_time_close) to detect when bars are in a particular time period, with the option of limiting valid sessions to specific days. The [input.session()](https://www.tradingview.com/pine-script-reference/v5/#fun_input{dot}session) function provides a way to allow script users to define session values through a script’s “Inputs” tab (see the [Session input](concepts_Inputs.html#pageinputs-sessioninput) section for more information).
2.  **Session states** built-in variables such as [session.ismarket](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}ismarket) can identify which session a bar belongs to.
3.  When fetching data with [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security) you can also choose to return data from _regular_ sessions only or _extended_ sessions. In this case, the definition of **regular and extended sessions** is that of the exchange. It is part of the instrument’s properties — not user-defined, as in point #1. This notion of _regular_ and _extended_ sessions is the same one used in the chart’s interface, in the “Chart Settings/Symbol/Session” field, for example.

The following sections cover both methods of using session information in Pine Script®.

Note that:

*   Not all user accounts on TradingView have access to extended session information.
*   There is no special “session” type in Pine Script®. Instead, session strings are of “string” type but must conform to the session string syntax.

[Session strings](#id2)
-------------------------------------------------------------------------

### [Session string specifications](#id3)

Session strings used with [time()](https://www.tradingview.com/pine-script-reference/v5/#fun_time) and [time\_close()](https://www.tradingview.com/pine-script-reference/v5/#fun_time_close) must have a specific format. Their syntax is:

Where:

*   <time\_period> uses times in “hhmm” format, with “hh” in 24-hour format, so `1700` for 5PM. The time periods are in the “hhmm-hhmm” format, and a comma can separate multiple time periods to specify combinations of discrete periods.

For example, - <days> is a set of digits from 1 to 7 that specifies on which days the session is valid.

1 is Sunday, 7 is Saturday.

Note

**The default days are**: `1234567`, which is different in Pine Script® v5 than in earlier versions where `23456` (weekdays) is used. For v5 code to reproduce the behavior from previous versions, it should explicitly mention weekdays, as in `"0930-1700:23456"`.

These are examples of session strings:

`"24x7"`

A 7-day, 24-hour session beginning at midnight.

`"0000-0000:1234567"`

Equivalent to the previous example.

`"0000-0000"`

Equivalent to the previous two examples because the default days are `1234567`.

`"0000-0000:23456"`

The same as the previous example, but only Monday to Friday.

`"2000-1630:1234567"`

An overnight session that begins at 20:00 and ends at 16:30 the next day. It is valid on all days of the week.

`"0930-1700:146"`

A session that begins at 9:30 and ends at 17:00 on Sundays (1), Wednesdays (4), and Fridays (6).

`"1700-1700:23456"`

An _overnight session_. The Monday session starts Sunday at 17:00 and ends Monday at 17:00. It is valid Monday through Friday.

`"1000-1001:26"`

A weird session that lasts only one minute on Mondays (2) and Fridays (6).

`"0900-1600,1700-2000"`

A session that begins at 9:00, breaks from 16:00 to 17:00, and continues until 20:00. Applies to every day of the week.

### [Using session strings](#id4)

Session properties defined with session strings are independent of the exchange-defined sessions determining when an instrument can be traded. Programmers have complete liberty in creating whatever session definitions suit their purpose, which is usually to detect when bars belong to specific time periods. This is accomplished in Pine Script® by using one of the following two signatures of the [time()](https://www.tradingview.com/pine-script-reference/v5/#fun_time) function:

```swift
time(timeframe, session, timezone) → series int
time(timeframe, session) → series int

```


Here, we use [time()](https://www.tradingview.com/pine-script-reference/v5/#fun_time) with a `session` argument to display the market’s opening [high](https://www.tradingview.com/pine-script-reference/v5/#var_high) and [low](https://www.tradingview.com/pine-script-reference/v5/#var_low) values on an intraday chart:

![../_images/Sessions-UsingSessionStrings-01.png](https://tradingview.com/pine-script-docs/en/v5/_images/Sessions-UsingSessionStrings-01.png)

```swift
//@version=5
indicator("Opening high/low", overlay = true)

sessionInput = input.session("0930-0935")

sessionBegins(sess) =>
    t = time("", sess)
    timeframe.isintraday and (not barstate.isfirst) and na(t[1]) and not na(t)

var float hi = na
var float lo = na
if sessionBegins(sessionInput)
    hi := high
    lo := low

plot(lo, "lo", color.fuchsia, 2, plot.style_circles)
plot(hi, "hi", color.lime,    2, plot.style_circles)

```


Note that:

*   We use a session input to allow users to specify the time they want to detect. We are only looking for the session’s beginning time on bars, so we use a five-minute gap between the beginning and end time of our `"0930-0935"` default value.

*   We create a `sessionBegins()` function to detect the beginning of a session. Its `time("", sess)` call uses an empty string for the function’s `timeframe` parameter, which means it uses the chart’s timeframe, whatever that is. The function returns `true` when:

    > *   The chart uses an intraday timeframe (seconds or minutes).
    > *   The script isn’t on the chart’s first bar, which we ensure with `(not barstate.isfirst)`. This check prevents the code from always detecting a session beginning on the first bar because `na(t[1]) and not na(t)` is always `true` there.
    > *   The [time()](https://www.tradingview.com/pine-script-reference/v5/#fun_time) call has returned [na](https://www.tradingview.com/pine-script-reference/v5/#var_na) on the previous bar because it wasn’t in the session’s time period, and it has returned a value that is not [na](https://www.tradingview.com/pine-script-reference/v5/#var_na) on the current bar, which means the bar is **in** the session’s time period.


[Session states](#id5)
-----------------------------------------------------------------------

Three built-in variables allow you to distinguish the type of session the current bar belongs to. They are only helpful on intraday timeframes:

*   [session.ismarket](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}ismarket) returns `true` when the bar belongs to regular trading hours.
*   [session.ispremarket](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}ispremarket) returns `true` when the bar belongs to the extended session preceding regular trading hours.
*   [session.ispostmarket](https://www.tradingview.com/pine-script-reference/v5/#var_session{dot}ispostmarket) returns `true` when the bar belongs to the extended session following regular trading hours.

[Using sessions with \`request.security()\`](#id6)
-------------------------------------------------------------------------------------------------------------------------

When your TradingView account provides access to extended sessions, you can choose to see their bars with the “Settings/Symbol/Session” field. There are two types of sessions:

*   **regular** (which does not include pre- and post-market data), and
*   **extended** (which includes pre- and post-market data).

Scripts using the [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security) function to access data can return extended session data or not. This is an example where only regular session data is fetched:

![../_images/Sessions-RegularAndExtendedSessions-01.png](https://tradingview.com/pine-script-docs/en/v5/_images/Sessions-RegularAndExtendedSessions-01.png)

```swift
//@version=5
indicator("Example 1: Regular Session Data")
regularSessionData = request.security("NASDAQ:AAPL", timeframe.period, close, barmerge.gaps_on)
plot(regularSessionData, style = plot.style_linebr)

```


If you want the [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security) call to return extended session data, you must first use the [ticker.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker{dot}new) function to build the first argument of the [request.security()](https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}security) call:

![../_images/Sessions-RegularAndExtendedSessions-02.png](https://tradingview.com/pine-script-docs/en/v5/_images/Sessions-RegularAndExtendedSessions-02.png)

```swift
//@version=5
indicator("Example 2: Extended Session Data")
t = ticker.new("NASDAQ", "AAPL", session.extended)
extendedSessionData = request.security(t, timeframe.period, close, barmerge.gaps_on)
plot(extendedSessionData, style = plot.style_linebr)

```


Note that the previous chart’s gaps in the script’s plot are now filled. Also, keep in mind that our example scripts do not produce the background coloring on the chart; it is due to the chart’s settings showing extended hours.

The [ticker.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker{dot}new) function has the following signature:

```swift
ticker.new(prefix, ticker, session, adjustment) → simple string

```


Where:

*   `prefix` is the exchange prefix, e.g., `"NASDAQ"`
*   `ticker` is a symbol name, e.g., `"AAPL"`
*   `session` can be `session.extended` or `session.regular`. Note that this is **not** a session string.
*   `adjustment` adjusts prices using different criteria: `adjustment.none`, `adjustment.splits`, `adjustment.dividends`.

Our first example could be rewritten as:

```swift
//@version=5
indicator("Example 1: Regular Session Data")
t = ticker.new("NASDAQ", "AAPL", session.regular)
regularSessionData = request.security(t, timeframe.period, close, barmerge.gaps_on)
plot(regularSessionData, style = plot.style_linebr)

```


If you want to use the same session specifications used for the chart’s main symbol, omit the third argument in [ticker.new()](https://www.tradingview.com/pine-script-reference/v5/#fun_ticker{dot}new); it is optional. If you want your code to declare your intention explicitly, use the [syminfo.session](https://www.tradingview.com/pine-script-reference/v5/#var_syminfo{dot}session) built-in variable. It holds the session type of the chart’s main symbol:

```swift
//@version=5
indicator("Example 1: Regular Session Data")
t = ticker.new("NASDAQ", "AAPL", syminfo.session)
regularSessionData = request.security(t, timeframe.period, close, barmerge.gaps_on)
plot(regularSessionData, style = plot.style_linebr)

```


[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)
