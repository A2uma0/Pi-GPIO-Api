### Control the PI GPIO pins via a Flask API, using the RPIO.GPIO library.


⚠ The pin numbers used here are equal to the boards layout **GPIO.setmode(GPIO.BOARD)**. ⚠  
This means that pin 1 is **not equal** to the GPIO pin 1.  
Diagram for the pins:  <a href="https://mlqmtwka8c9g.i.optimole.com/ngiUMAo-2-7SEs6-/w:1024/h:588/q:auto/https://raspberrydiy.com/wp-content/uploads/2020/10/gpio-pin-layout-reference.png">click me!</a> 

# Docs
#### setGpi

Set the specified pin to input and read it. Returns response code 200.

*Example:*  
*/api/v1/setgpi?pin=15*

#### setGpo

Set the specified pin to output and set the specified state, either high or low. Returns response code 200.

*Example:*  
*/api/v1/setgpo?pin=15&state=high*

#### setAll

Set every GPIO pin available on the Board to output and the specified state, either high or low. Returns response code 200.

*Example:*  
*/api/v1/setall?state=high*

# Deploying
### Deploy locally
#### Clone the Repo or download the zip.
```
git clone https://github.com/A2uma0/Pi-GPIO-Api.git
```
#### Run the API locally:
```
cd Pi-GPIO-Api/ && python3 api.py
```
#### You can now access the API at http://127.0.0.1:5000/
### Deploy to public
#### Clone the Repo or download the zip.
```
git clone https://github.com/A2uma0/Pi-GPIO-Api.git
```
#### Install waitress
```
pip install waitress
```
#### Edit the file
```
nano Pi-GPIO-Api/api.py
```
#### Uncomment lines and bind to your IP & Port
```python
...
#from waitress import serve  # uncomment this
#serve(app, host="127.0.0.1", port=5000) # uncomment this, and change IP & Port
app.run(host="127.0.0.1") # comment out this
```
#### Save the file and exit, then start the API
```
python3 Pi-GPIO-Api/api.py
```
#### The API will now be started in a production environment, and can be accessed at your defined IP & Port

# Notes
The Code is very messy, since I wrote it rather quickly.
