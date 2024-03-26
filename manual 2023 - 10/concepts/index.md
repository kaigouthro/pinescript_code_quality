# Concepts¶

- Alerts

  - Introduction

    - Background
    - Which type of alert is best?

  - Script alerts

    - `alert()` function events
    - Order fill events

  - `alertcondition()` events

    - Using one condition
    - Using compound conditions
    - Placeholders

  - Avoiding repainting with alerts

- Backgrounds
- Bar coloring
- Bar plotting

  - Introduction
  - Plotting candles with `plotcandle()`
  - Plotting bars with `plotbar()`

- Bar states

  - Introduction
  - Bar state built-in variables

    - `barstate.isfirst`
    - `barstate.islast`
    - `barstate.ishistory`
    - `barstate.isrealtime`
    - `barstate.isnew`
    - `barstate.isconfirmed`
    - `barstate.islastconfirmedhistory`

  - Example

- Chart information

  - Introduction
  - Prices and volume
  - Symbol information
  - Chart timeframe
  - Session information

- Colors

  - Introduction

    - Transparency
    - Z-index

  - Constant colors
  - Conditional coloring
  - Calculated colors

    - color.new()
    - color.rgb()
    - color.from_gradient()

  - Mixing transparencies
  - Tips

    - Designing usable colors schemes
    - Plot crisp lines
    - Customize gradients
    - Color selection through script settings

- Fills

  - Introduction
  - `plot()` and `hline()` fills
  - Line fills

- Inputs

  - Introduction
  - Input functions
  - Input function parameters
  - Input types

    - Simple input
    - Integer input
    - Float input
    - Boolean input
    - Color input
    - Timeframe input
    - Symbol input
    - Session input
    - Source input
    - Time input

  - Other features affecting Inputs
  - Tips

- Levels

  - `hline()` levels
  - Fills between levels

- Libraries

  - Introduction
  - Creating a library

    - Library functions
    - Qualified type control
    - User-defined types and objects

  - Publishing a library

    - House Rules

  - Using a library

- Lines and boxes

  - Introduction
  - Lines

    - Creating lines
    - Modifying lines
    - Line styles
    - Reading line values
    - Cloning lines
    - Deleting lines

  - Boxes

    - Creating boxes
    - Modifying boxes
    - Box styles
    - Reading box values
    - Cloning boxes
    - Deleting boxes

  - Polylines

    - Creating polylines
    - Deleting polylines
    - Redrawing polylines

  - Realtime behavior
  - Limitations

    - Total number of objects
    - Future references with `xloc.bar_index`
    - Other contexts
    - Historical buffer and `max_bars_back`

- Non-standard charts data

  - Introduction
  - `ticker.heikinashi()`
  - `ticker.renko()`
  - `ticker.linebreak()`
  - `ticker.kagi()`
  - `ticker.pointfigure()`

- Other timeframes and data

  - Introduction
  - Common characteristics

    - Usage
    - `gaps`
    - `ignore_invalid_symbol`
    - `currency`
    - `lookahead`

  - Data feeds
  - `request.security()`

    - Timeframes
    - Requestable data

  - `request.security_lower_tf()`

    - Requesting intrabar data
    - Intrabar data arrays
    - Tuples of intrabar data
    - Requesting collections

  - Custom contexts
  - Historical and realtime behavior

    - Avoiding Repainting

  - `request.currency_rate()`
  - `request.dividends()`, `request.splits()`, and `request.earnings()`
  - `request.quandl()`
  - `request.financial()`

    - Calculating financial metrics
    - Financial IDs

  - `request.economic()`

    - Country/region codes
    - Field codes

  - `request.seed()`

- Plots

  - Introduction
  - `plot()` parameters
  - Plotting conditionally

    - Value control
    - Color control

  - Levels
  - Offsets
  - Plot count limit
  - Scale

    - Merging two indicators

- Repainting

  - Introduction

    - For script users
    - For Pine Script™ programmers

  - Historical vs realtime calculations

    - Fluid data values
    - Repainting `request.security()` calls
    - Using `request.security()` at lower timeframes
    - Future leak with `request.security()`
    - `varip`
    - Bar state built-ins
    - `timenow`
    - Strategies

  - Plotting in the past
  - Dataset variations

    - Starting points
    - Revision of historical data

- Sessions

  - Introduction
  - Session strings

    - Session string specifications
    - Using session strings

  - Session states
  - Using sessions with `request.security()`

- Strategies

  - Introduction
  - A simple strategy example
  - Applying a strategy to a chart
  - Strategy tester

    - Overview
    - Performance summary
    - List of trades
    - Properties

  - Broker emulator

    - Bar magnifier

  - Orders and entries

    - Order types
    - Order placement commands

  - Position sizing
  - Closing a market position
  - OCA groups

    - `strategy.oca.cancel`
    - `strategy.oca.reduce`
    - `strategy.oca.none`

  - Currency
  - Altering calculation behavior

    - `calc_on_every_tick`
    - `calc_on_order_fills`
    - `process_orders_on_close`

  - Simulating trading costs

    - Commission
    - Slippage and unfilled limits

  - Risk management
  - Margin
  - Strategy Alerts
  - Notes on testing strategies

    - Backtesting and forward testing
    - Lookahead bias
    - Selection bias
    - Overfitting

- Tables

  - Introduction
  - Creating tables

    - Placing a single value in a fixed position
    - Coloring the chart's background
    - Creating a display panel
    - Displaying a heatmap

  - Tips

- Text and shapes

  - Introduction
  - `plotchar()`
  - `plotshape()`
  - `plotarrow()`
  - Labels

    - Creating and modifying labels
    - Positioning labels
    - Reading label properties
    - Cloning labels
    - Deleting labels
    - Realtime behavior

- Time

  - Introduction

    - Four references
    - Time built-ins
    - Time zones

  - Time variables

    - `time` and `time_close`
    - `time_tradingday`
    - `timenow`
    - Calendar dates and times
    - `syminfo.timezone()`

  - Time functions

    - `time()` and `time_close()`
    - Calendar dates and times
    - `timestamp()`

  - Formatting dates and time

- Timeframes

  - Introduction
  - Timeframe string specifications
  - Comparing timeframes

© Copyright 2024, TradingView.
