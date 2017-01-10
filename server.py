from flask import Flask, request, render_template
from gpiozero import LED
import time

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

led = LED(17)
led.on()


@app.route('/')
def start_here():
    """Home page."""

    return render_template("homepage.html")


@app.route("/led")
def change_led_status():
    """Turn the LED on or off."""

    if led.is_lit:
        led.off()

    else:
        led.on()

    return "/led"

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    # app.run(host='192.168.3.248', port=80, debug=True)
    app.run(debug=True)
