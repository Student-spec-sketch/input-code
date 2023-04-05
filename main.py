def on_forever():
    if pins.analog_read_pin(AnalogPin.P1) < 350:
        basic.show_icon(IconNames.HAPPY)
    elif pins.analog_read_pin(AnalogPin.P1) > 1000:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
