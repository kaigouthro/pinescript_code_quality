Timestamps can be formatted using [str.format()](https://www.tradingview.com/pine-script-reference/v5/#fun_str{dot}format). These are examples of various formats:

```swift
//@version=5
indicator("", "", true)

print(txt, styl) =>
    var alignment = styl == label.style_label_right ? text.align_right : text.align_left
    var lbl = label.new(na, na, "", xloc.bar_index, yloc.price, color(na), styl, color.black, size.large, alignment)
    if barstate.islast
        label.set_xy(lbl, bar_index, hl2[1])
        label.set_text(lbl, txt)

var string format =
  "{0,date,yyyy.MM.dd hh:mm:ss}\n" +
  "{1,date,short}\n" +
  "{2,date,medium}\n" +
  "{3,date,long}\n" +
  "{4,date,full}\n" +
  "{5,date,h a z (zzzz)}\n" +
  "{6,time,short}\n" +
  "{7,time,medium}\n" +
  "{8,date,'Month 'MM, 'Week' ww, 'Day 'DD}\n" +
  "{9,time,full}\n" +
  "{10,time,hh:mm:ss}\n" +
  "{11,time,HH:mm:ss}\n" +
  "{12,time,HH:mm:ss} Left in bar\n"

print(format, label.style_label_right)
print(str.format(format,
  time, time, time, time, time, time, time,
  timenow, timenow, timenow, timenow,
  timenow - time, time_close - timenow), label.style_label_left)

```
