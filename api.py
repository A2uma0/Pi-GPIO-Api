from flask import Flask, request
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


app = Flask(__name__)
app.config["DEBUG"] = False


def setGPI(num):
    # set up input channel without pull-up
    try:
        GPIO.setup(num, GPIO.IN)
        if GPIO.input(num):
            state = "High"
        else:
            state = "Low"
        return state
    # catch exception 
    except ValueError as e:
        state = "Error: Invalid Channel, check if the pin is a GPIO pin. <br>  <img src='https://mlqmtwka8c9g.i.optimole.com/ngiUMAo-2-7SEs6-/w:1024/h:588/q:auto/https://raspberrydiy.com/wp-content/uploads/2020/10/gpio-pin-layout-reference.png'>", 400
    except Exception as s:
        state = "An Error ocurred", 500
    return state

def setGPO(num, state):
    # set channel to output with the specified state
    try:
        GPIO.setup(num, GPIO.OUT)
        GPIO.output(num, state)
        if state == 1:
            state = "High"
        elif state == 0:
            state = "Low"
        print(f" Set state: {state} on port {num}")
        data = f" Set state: {state} on port {num}"
        return data
        
    except ValueError as e:
        state = f"Error: Invalid Channel, check if the pin is a GPIO pin. {e} <br>  <img src='https://mlqmtwka8c9g.i.optimole.com/ngiUMAo-2-7SEs6-/w:1024/h:588/q:auto/https://raspberrydiy.com/wp-content/uploads/2020/10/gpio-pin-layout-reference.png'>", 400
    except Exception as s:
        state = "An Error ocurred", 500
    return state

def setAll(state):
    list = (3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 32, 35, 36, 37, 38, 40)
    GPIO.setup(list, GPIO.OUT)
    GPIO.output(list, state)
    if state == 1:
        state = "High"
    elif state == 0:
        state = "Low"
    return f"Set all pins to {state}"

@app.route('/api/v1/setgpi', methods=['GET'])
def setgpiapi():
        if "pin" in request.args:
            pin = int(request.args["pin"])
            state = setGPI(pin)
            return state
        else:
            return "Error: no pin provided", 400

@app.route('/api/v1/setgpo', methods=['GET'])
def setgpoapi():
        if "pin" in request.args:
            pin = int(request.args["pin"])
        else:
            return "Error: no pin provided"
        if "state" in request.args:
            state = request.args["state"]
            if state == "High" or state == "high":
                state = GPIO.HIGH
            elif state == "Low" or state == "low":
                state = GPIO.LOW
            data = setGPO(pin, state)
            return data
        else:
            return "Error: no state provided", 400

@app.route('/api/v1/setall', methods=['GET'])
def setall():
        if "state" in request.args:
            state = request.args["state"]
            if state == "High" or state == "high":
                state = GPIO.HIGH
            elif state == "Low" or state == "low":
                state = GPIO.LOW
            data = setAll(state)
            return data
        else:
            return "Error: no state provided", 400


if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="127.0.0.1", port=5000)
    app.run(host="127.0.0.1")
