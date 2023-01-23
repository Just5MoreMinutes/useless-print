-> uprint v0.0.1
# useless-print (`uprint`)
useless-print (`uprint`) is a python package for styling outputs and a lot of other fairly useless functionalities for print statements.

## Using `uprint`
useless-print can be found on [PyPi](https://pypi.org/) and can therefore be installed using `pip`:
```
pip install uprint
```
After installing and importing the package you first want to set up `uprint`. The function `uprint.setup()` does everything for you, so you don't have to worry about taking the right steps:
```python
import uprint

uprint.setup()
```
After you added the `setup` function you can start working with `uprint`. `uprint` has a plethora of useless functionalities:
#### Functions
- **`uprint(<txt>)`**: This is the standard `uprint` function. You can use [styling](#styling) in this function, however, other functionalities can't be used with this plain `uprint` function.
- **`uprint.custom(<dict>)`**: Add custom tags that can be used within the `uprint` functions for improved [styling](#styling).
- **`uprint.call(<txt>, <func>, <delay>)`**: Call a function together with an output. You can [style](#styling) the output regularly, however, you can add a function which will be called once the `uprint` function is called. The function can also be delayed, so it will be called `<delay>` seconds after the output has been rendered.
- **`uprint.modify(<txt>, <var/func-arg>, <val>)`**: Modify the value of a function argument or variable.
- **`block_print()`**: Blocks any output.
- **`enable_print()`**: Re-enables outputs.
- **`uprint.bypass_self()`**: Regular print statements will be blocked. Modified `uprint` outputs are allowed.

## Styling 
*(Considering that this is far from being finished, the below list of possible styling is still WIP.)*
- `[<color>]`: The following characters will be colored in the given color. As of right now these brackets also accept `RGB` and `HEX` values. (*`HSL` will be added soon*).
- `**<txt>**`: Make a text snippet bold.
- `*<txt>*`: Make a text snippet italic.
- `__<txt>__`: Underline a text snippet.
- `~~<txt>~~`: Strike out a text snippet. ***(NOT widely supported)***
- `[<color>:bg]`: Set background color.
- ...and more to come
