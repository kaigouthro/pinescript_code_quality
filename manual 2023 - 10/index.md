# Pine Script™ v5 User Manual¶

- Welcome to Pine Script™ v5
- Pine Script™ primer

  - First steps

    - Introduction
    - Using scripts
    - Reading scripts
    - Writing scripts

  - First indicator

    - The Pine Editor
    - First version
    - Second version
    - Next

  - Next steps

    - "indicators" vs "strategies"
    - How scripts are executed
    - Time series
    - Publishing scripts
    - Getting around the Pine Script™ documentation
    - Where to go from here?

- Language

  - Execution model

    - Calculation based on historical bars
    - Calculation based on realtime bars
    - Events triggering the execution of a script
    - More information
    - Historical values of functions

  - Time series
  - Script structure

    - Version
    - Declaration statement
    - Code
    - Comments
    - Line wrapping
    - Compiler annotations

  - Identifiers
  - Operators

    - Introduction
    - Arithmetic operators
    - Comparison operators
    - Logical operators
    - `?:` ternary operator
    - `[ ]` history-referencing operator
    - Operator precedence
    - `=` assignement operator
    - `:=` reassignement operator

  - Variable declarations

    - Introduction
    - Variable reassignment
    - Declaration modes

  - Conditional structures

    - Introduction
    - `if` structure
    - `switch` structure
    - Matching local block type requirement

  - Loops

    - Introduction
    - `for`
    - `while`

  - Type system

    - Introduction
    - Qualifiers
    - Types
    - `na` value
    - Type templates
    - Type casting
    - Tuples

  - Built-ins

    - Introduction
    - Built-in variables
    - Built-in functions

  - User-defined functions

    - Introduction
    - Single-line functions
    - Multi-line functions
    - Scopes in the script
    - Functions that return multiple results
    - Limitations

  - Objects

    - Introduction
    - Creating objects
    - Changing field values
    - Collecting objects
    - Copying objects
    - Shadowing

  - Methods

    - Introduction
    - Built-in methods
    - User-defined methods
    - Method overloading
    - Advanced example

  - Arrays

    - Introduction
    - Declaring arrays
    - Reading and writing array elements
    - Looping through array elements
    - Scope
    - History referencing
    - Inserting and removing array elements
    - Calculations on arrays
    - Manipulating arrays
    - Searching arrays
    - Error handling

  - Matrices

    - Introduction
    - Declaring a matrix
    - Reading and writing matrix elements
    - Rows and columns
    - Looping through a matrix
    - Copying a matrix
    - Scope and history
    - Inspecting a matrix
    - Manipulating a matrix
    - Matrix calculations
    - Error handling

  - Maps

    - Introduction
    - Declaring a map
    - Reading and writing
    - Looping through a map
    - Copying a map
    - Scope and history
    - Maps of other collections

- Concepts

  - Alerts

    - Introduction
    - Script alerts
    - `alertcondition()` events
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
    - Example

  - Chart information

    - Introduction
    - Prices and volume
    - Symbol information
    - Chart timeframe
    - Session information

  - Colors

    - Introduction
    - Constant colors
    - Conditional coloring
    - Calculated colors
    - Mixing transparencies
    - Tips

  - Fills

    - Introduction
    - `plot()` and `hline()` fills
    - Line fills

  - Inputs

    - Introduction
    - Input functions
    - Input function parameters
    - Input types
    - Other features affecting Inputs
    - Tips

  - Levels

    - `hline()` levels
    - Fills between levels

  - Libraries

    - Introduction
    - Creating a library
    - Publishing a library
    - Using a library

  - Lines and boxes

    - Introduction
    - Lines
    - Boxes
    - Polylines
    - Realtime behavior
    - Limitations

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
    - Data feeds
    - `request.security()`
    - `request.security_lower_tf()`
    - Custom contexts
    - Historical and realtime behavior
    - `request.currency_rate()`
    - `request.dividends()`, `request.splits()`, and `request.earnings()`
    - `request.quandl()`
    - `request.financial()`
    - `request.economic()`
    - `request.seed()`

  - Plots

    - Introduction
    - `plot()` parameters
    - Plotting conditionally
    - Levels
    - Offsets
    - Plot count limit
    - Scale

  - Repainting

    - Introduction
    - Historical vs realtime calculations
    - Plotting in the past
    - Dataset variations

  - Sessions

    - Introduction
    - Session strings
    - Session states
    - Using sessions with `request.security()`

  - Strategies

    - Introduction
    - A simple strategy example
    - Applying a strategy to a chart
    - Strategy tester
    - Broker emulator
    - Orders and entries
    - Position sizing
    - Closing a market position
    - OCA groups
    - Currency
    - Altering calculation behavior
    - Simulating trading costs
    - Risk management
    - Margin
    - Strategy Alerts
    - Notes on testing strategies

  - Tables

    - Introduction
    - Creating tables
    - Tips

  - Text and shapes

    - Introduction
    - `plotchar()`
    - `plotshape()`
    - `plotarrow()`
    - Labels

  - Time

    - Introduction
    - Time variables
    - Time functions
    - Formatting dates and time

  - Timeframes

    - Introduction
    - Timeframe string specifications
    - Comparing timeframes

- Writing scripts

  - Style guide

    - Introduction
    - Naming Conventions
    - Script organization
    - Spacing
    - Line wrapping
    - Vertical alignment
    - Explicit typing

  - Debugging

    - Introduction
    - The lay of the land
    - Numeric values
    - Conditions
    - Strings
    - Pine Logs
    - Debugging functions
    - Debugging loops
    - Tips

  - Publishing scripts

    - Script visibility and access
    - Preparing a publication
    - Publishing a script
    - Updating a publication

  - Limitations

    - Introduction
    - Time
    - Chart visuals
    - `request.*()` calls
    - Script size and memory
    - Other limitations

- FAQ

  - Get real OHLC price on a Heikin Ashi chart
  - Get non-standard OHLC values on a standard chart
  - Plot arrows on the chart
  - Plot a dynamic horizontal line
  - Plot a vertical line on condition
  - Access the previous value
  - Get a 5-days high
  - Count bars in a dataset
  - Enumerate bars in a day
  - Find the highest and lowest values for the entire dataset
  - Query the last non-na value

- Error messages

  - The if statement is too long
  - Script requesting too many securities
  - Script could not be translated from: null
  - line 2: no viable alternative at character '$'
  - Mismatched input <...> expecting <???>
  - Loop is too long (> 500 ms)
  - Script has too many local variables
  - Pine Script™ cannot determine the referencing length of a series. Try using max_bars_back in the indicator or strategy function

- Release notes

  - 2024

    - March 2024
    - February 2024
    - January 2024

  - 2023

    - December 2023
    - November 2023
    - October 2023
    - September 2023
    - August 2023
    - July 2023
    - June 2023
    - May 2023
    - April 2023
    - March 2023
    - February 2023
    - January 2023

  - 2022

    - December 2022
    - November 2022
    - October 2022
    - September 2022
    - August 2022
    - July 2022
    - June 2022
    - May 2022
    - April 2022
    - March 2022
    - February 2022
    - January 2022

  - 2021

    - December 2021
    - November 2021
    - October 2021
    - September 2021
    - July 2021
    - June 2021
    - May 2021
    - April 2021
    - March 2021
    - February 2021
    - January 2021

  - 2020

    - December 2020
    - November 2020
    - October 2020
    - September 2020
    - August 2020
    - July 2020
    - June 2020
    - May 2020
    - April 2020
    - March 2020
    - February 2020
    - January 2020

  - 2019

    - December 2019
    - October 2019
    - September 2019
    - July-August 2019
    - June 2019

  - 2018

    - October 2018
    - April 2018

  - 2017

    - August 2017
    - June 2017
    - May 2017
    - April 2017
    - March 2017
    - February 2017

  - 2016

    - December 2016
    - October 2016
    - September 2016
    - July 2016
    - March 2016
    - February 2016
    - January 2016

  - 2015

    - October 2015
    - September 2015
    - July 2015
    - June 2015
    - April 2015
    - March 2015
    - February 2015

  - 2014

    - August 2014
    - July 2014
    - June 2014
    - April 2014
    - February 2014

  - 2013

- Migration guides

  - To Pine Script™ version 5

    - Introduction
    - v4 to v5 converter
    - Renamed functions and variables
    - Renamed function parameters
    - Removed an `rsi()` overload
    - Reserved keywords
    - Removed `iff()` and `offset()`
    - Split of `input()` into several functions
    - Some function parameters now require built-in arguments
    - Deprecated the `transp` parameter
    - Changed the default session days for `time()` and `time_close()`
    - `strategy.exit()` now must do something
    - Common script conversion errors
    - All variable, function, and parameter name changes

  - To Pine Script™ version 4

    - Converter
    - Renaming of built-in constants, variables, and functions
    - Explicit variable type declaration

  - To Pine Script™ version 3

    - Default behaviour of security function has changed
    - Self-referenced variables are removed
    - Forward-referenced variables are removed
    - Resolving a problem with a mutable variable in a security expression
    - Math operations with booleans are forbidden

- Where can I get more information?

  - External resources
  - Download this manual

© Copyright 2024, TradingView.
