#!/usr/bin/python
from app import app
#app.run(host='0.0.0.0', debug=True)

#to run locally, uncomment and comment the one above and run the app
app.debug = True
app.run()
