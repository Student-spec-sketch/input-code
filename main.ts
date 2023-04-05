basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P1) < 350) {
        basic.showIcon(IconNames.Happy)
    } else if (pins.analogReadPin(AnalogPin.P1) > 1000) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
