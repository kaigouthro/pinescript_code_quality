```swift
//@version=5
indicator('Linear Regression', shorttitle='LinReg', overlay=true)

upperMult = input(title='Upper Deviation', defval=2)
lowerMult = input(title='Lower Deviation', defval=-2)

useUpperDev = input(title='Use Upper Deviation', defval=true)
useLowerDev = input(title='Use Lower Deviation', defval=true)
showPearson = input(title='Show Pearson\'s R', defval=true)
extendLines = input(title='Extend Lines', defval=false)

len = input(title='Count', defval=100)
src = input(title='Source', defval=close)

extend = extendLines ? extend.right : extend.none

calcSlope(src, len) =>
    if not barstate.islast or len <= 1
        [float(na), float(na), float(na)]
    else
        sumX = 0.0
        sumY = 0.0
        sumXSqr = 0.0
        sumXY = 0.0
        for i = 0 to len - 1 by 1
            val = src[i]
            per = i + 1.0
            sumX := sumX + per
            sumY := sumY + val
            sumXSqr := sumXSqr + per * per
            sumXY := sumXY + val * per
            sumXY
        slope = (len * sumXY - sumX * sumY) / (len * sumXSqr - sumX * sumX)
        average = sumY / len
        intercept = average - slope * sumX / len + slope
        [slope, average, intercept]

[s, a, intercpt] = calcSlope(src, len)

startPrice = intercpt + s * (len - 1)
endPrice = intercpt
var line baseLine = na

if na(baseLine) and not na(startPrice)
    baseLine := line.new(bar_index - len + 1, startPrice, bar_index, endPrice, width = 1, extend=extend, color = color.red)
    baseLine
else
    line.set_xy1(baseLine, bar_index - len + 1, startPrice)
    line.set_xy2(baseLine, bar_index, endPrice)
    na

calcDev(src, len, slope, average, intercept) =>
    upDev = 0.0
    dnDev = 0.0
    stdDevAcc = 0.0
    dsxx = 0.0
    dsyy = 0.0
    dsxy = 0.0

    periods = len - 1

    daY = intercept + slope * periods / 2
    val = intercept

    for i = 0 to periods by 1
        price = high[i] - val
        if price > upDev
            upDev := price
            upDev

        price := val - low[i]
        if price > dnDev
            dnDev := price
            dnDev

        price := src[i]
        dxt = price - average
        dyt = val - daY

        price := price - val
        stdDevAcc := stdDevAcc + price * price
        dsxx := dsxx + dxt * dxt
        dsyy := dsyy + dyt * dyt
        dsxy := dsxy + dxt * dyt
        val := val + slope
        val

    stdDev = math.sqrt(stdDevAcc / (periods == 0 ? 1 : periods))
    pearsonR = dsxx == 0 or dsyy == 0 ? 0 : dsxy / math.sqrt(dsxx * dsyy)
    [stdDev, pearsonR, upDev, dnDev]

[stdDev, pearsonR, upDev, dnDev] = calcDev(src, len, s, a, intercpt)

upperStartPrice = startPrice + (useUpperDev ? upperMult * stdDev : upDev)
upperEndPrice = endPrice + (useUpperDev ? upperMult * stdDev : upDev)
var line upper = na

lowerStartPrice = startPrice + (useLowerDev ? lowerMult * stdDev : -dnDev)
lowerEndPrice = endPrice + (useLowerDev ? lowerMult * stdDev : -dnDev)
var line lower = na

if na(upper) and not na(upperStartPrice)
    upper := line.new(bar_index - len + 1, upperStartPrice, bar_index, upperEndPrice, width=1, extend=extend, color=#0000ff)
    upper
else
    line.set_xy1(upper, bar_index - len + 1, upperStartPrice)
    line.set_xy2(upper, bar_index, upperEndPrice)
    na

if na(lower) and not na(lowerStartPrice)
    lower := line.new(bar_index - len + 1, lowerStartPrice, bar_index, lowerEndPrice, width=1, extend=extend, color=#0000ff)
    lower
else
    line.set_xy1(lower, bar_index - len + 1, lowerStartPrice)
    line.set_xy2(lower, bar_index, lowerEndPrice)
    na

// Pearson's R
var label r = na
transparent = color.new(color.white, 100)
label.delete(r[1])
if showPearson and not na(pearsonR)
    r := label.new(bar_index - len + 1, lowerStartPrice, str.tostring(pearsonR, '#.################'), color=transparent, textcolor=#0000ff, size=size.normal, style=label.style_label_up)
    r

```
