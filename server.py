from flask import Flask, request, render_template
from gpiozero import LED
import time

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

blue_led = LED(17)
blue_led.on()

green_led = LED(27)
green_led.on()

red_led = LED(22)
red_led.on()


@app.route('/')
def start_here():
    """Home page."""

    return render_template("homepage.html")


@app.route("/blue-led")
def change_blue_led_status():
    """Turn the LED on or off."""

    if blue_led.is_lit:
        blue_led.off()

    else:
        blue_led.on()

    return "blue led route accessed"


@app.route("/green-led")
def change_green_led_status():
    """Turn the LED on or off."""

    if green_led.is_lit:
        green_led.off()

    else:
        green_led.on()

    return "green led route accessed"


@app.route("/red-led")
def change_red_led_status():
    """Turn the LED on or off."""

    if red_led.is_lit:
        red_led.off()

    else:
        red_led.on()

    return "green led route accessed"


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.

    app.run(host='192.168.2.163', port=80, debug=True)
