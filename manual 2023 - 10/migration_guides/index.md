# Migration guides¶

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

    - Invalid argument 'style'/'linestyle' in 'plot'/'hline' call
    - Undeclared identifier 'input.%input_name%'
    - Invalid argument 'when' in 'strategy.close' call
    - Cannot call 'input.int' with argument 'minval'='%value%'. An argument of 'literal float' type was used but a 'const int' is expected

  - All variable, function, and parameter name changes

    - Removed functions and variables
    - Renamed functions and parameters

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

© Copyright 2024, TradingView.
