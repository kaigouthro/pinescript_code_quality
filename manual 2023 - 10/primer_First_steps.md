[Introduction](#id1)
-------------------------------------------------------------------

Welcome to the Pine Script® [v5 User Manual](https://www.tradingview.com/pine-script-docs/en/v5/index.md), which will accompany you in your journey to learn to program your own trading tools in Pine Script®. Welcome also to the very active community of Pine Script® programmers on TradingView.

In this page, we present a step-by-step approach that you can follow to gradually become more familiar with indicators and strategies (also called _scripts_) written in the Pine Script® programming language on [TradingView](https://www.tradingview.com/). We will get you started on your journey to:

1.  **Use** some of the tens of thousands of existing scripts on the platform.
2.  **Read** the Pine Script® code of existing scripts.
3.  **Write** Pine Script® scripts.

If you are already familiar with the use of Pine scripts on TradingView and are now ready to learn how to write your own, then jump to the [Writing scripts](#pagefirstindicator-writingscripts) section of this page.

If you are new to our platform, then please read on!

[Using scripts](#id2)
---------------------------------------------------------------------

If you are interested in using technical indicators or strategies on TradingView, you can first start exploring the thousands of indicators already available on our platform. You can access existing indicators on the platform in two different ways:

*   By using the chart’s “Indicators & Strategies” button, or
*   By browsing TradingView’s [Community Scripts](https://www.tradingview.com/scripts/), the largest repository of trading scripts in the world, with more than 100,000 scripts, most of which are free and open-source, which means you can see their Pine Script® code.

If you can find the tools you need already written for you, it can be a good way to get started and gradually become proficient as a script user, until you are ready to start your programming journey in Pine Script®.

### [Loading scripts from the chart](#id3)

To explore and load scripts from you chart, use the “Indicators & Strategies” button:

![../_images/FirstSteps-LoadingScriptsFromTheChart-01.png](https://tradingview.com/pine-script-docs/en/v5/_images/FirstSteps-LoadingScriptsFromTheChart-01.png)

The dialog box presents different categories of scripts in its left pane:

*   **Favorites** lists the scripts you have “favorited” by clicking on the star that appears to the left of its name when you mouse over it.
*   **My scripts** displays the scipts you have written and saved in the Pine Script® Editor. They are saved in TradingView’s cloud.
*   **Built-ins** groups all TradingVIew built-ins organized in four categories: indicators, strategies, candlestick patterns and volume profiles. Most are written in Pine Script® and available for free.
*   **Community Scripts** is where you can search from the 100,000+ published scripts written by TradingView users.
*   **Invite-only scripts** contains the list of the invite-only scripts you have been granted access to by their authors.

Here, the section containing the TradingView built-ins is selected:

![../_images/FirstSteps-LoadingScriptsFromTheChart-02.png](https://tradingview.com/pine-script-docs/en/v5/_images/FirstSteps-LoadingScriptsFromTheChart-02.png)

When you click on one of the indicators or strategies (the ones with the green and red arrows following their name), it loads on your chart.

### [Changing script settings](#id5)

Once a script is loaded on the chart, you can double-click on its name (#1) to bring up its “Settings/Inputs” tab (#2):

![../_images/FirstSteps-ChangingScriptSettings-01.png](https://tradingview.com/pine-script-docs/en/v5/_images/FirstSteps-ChangingScriptSettings-01.png)

The “Inputs” tab allows you to change the settings which the script’s author has decided to make editable. You can configure some of the script’s visuals using the “Style” tab of the same dialog box, and which timeframes the script should appear on using the “Visibility” tab.

Other settings are available to all scripts from the buttons that appear to the right of its name when you mouse over it, and from the “More” menu (the three dots):

![../_images/FirstSteps-ChangingScriptSettings-02.png](https://tradingview.com/pine-script-docs/en/v5/_images/FirstSteps-ChangingScriptSettings-02.png)

[Reading scripts](#id6)
-------------------------------------------------------------------------

Reading code written by **good** programmers is the best way to develop your understanding of the language. This is as true for Pine Script® as it is for all other programming languages. Finding good open-source Pine Script® code is relatively easy. These are reliable sources of code written by good programmers on TradingView:

*   The TradingView built-in indicators
*   Scripts selected as [Editors’ Picks](https://www.tradingview.com/scripts/editors-picks/)
*   Scripts by the [authors the PineCoders account follows](https://www.tradingview.com/u/PineCoders/#following-people)
*   Many scripts by authors with high reputation and open-source publications.

Reading code from [Community Scripts](https://www.tradingview.com/scripts/) is easy; if you don’t see a grey or red “lock” icon in the upper-right corner of the script’s widget, this indicates the script is open-source. By opening its script page, you will be able to see its source.

To see the code of TradingView built-ins, load the indicator on your chart, then hover over its name and select the “Source code” curly braces icon (if you don’t see it, it’s because the indicator’s source is unavailable). When you click on the icon, the Pine Script® Editor will open and from there, you can see the script’s code. If you want to play with it, you will need to use the Editor’s “More” menu button at the top-right of the Editor’s pane, and select “Make a copy…”. You will then be able to modify and save the code. Because you will have created a different version of the script, you will need to use the Editor’s “Add to Chart” button to add that new copy to the chart.

This shows the Pine Script® Editor having just opened after we selected the “View source” button from the indicator on our chart. We are about to make a copy of its source because it is read-only for now (indicated by the “lock” icon near its filename in the Editor):

![../_images/FirstSteps-ReadingScripts-01.png](https://tradingview.com/pine-script-docs/en/v5/_images/FirstSteps-ReadingScripts-01.png)

You can also open TradingView built-in indicators from the Pine Script® Editor (accessible from the “Pine Script® Editor” tab at the bottom of the chart) by using the “Open/New default built-in script…” menu selection.

[Writing scripts](#id7)
-------------------------------------------------------------------------

We have built Pine Script® to empower both budding and seasoned traders to create their own trading tools. We have designed it so it is relatively easy to learn for first-time programmers — although learning a first programming language, like trading, is rarely **very** easy for anyone — yet powerful enough for knowledgeable programmers to build tools of moderate complexity.

Pine Script® allows you to write three types of scripts:

*   **Indicators** like RSI, MACD, etc.
*   **Strategies** which include logic to issue trading orders and can be backtested and forward-tested.
*   **Libraries** which are used by more advanced programmers to package oft-used functions that can be reused by other scripts.

The next step we recommend is to write your [first indicator](primer/First_indicator.html#pagefirstindicator).

[

![../_images/TradingView-Logo-Block.svg](https://tradingview.com/pine-script-docs/en/v5/_images/TradingView-Logo-Block.svg)

](https://www.tradingview.com/)
