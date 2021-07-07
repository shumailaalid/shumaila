from flask import Flask
from flask import request
from waitress import serve
import json, datetime
from botpizza_21 import botpizza_21
app = Flask(__name__)


################################################ Error Handling Messages #################################################  


def errstr(flag):
    
    e = 'Something went really wrong. Sorry for Inconvenience !!!'
        
    
    return e

########################################## Routing Functions #############################################################
''' This function do the calculations '''
@app.route("/")
def index():
    return(botpizza_21())
    return 'hi'
     


    
        

    
   
    
    return errstr(flag)
        
  
 
###################################################### Main #############################################################
    
''' This is main that invokes the app '''

if __name__ == "__main__":    
    serve(app, host='0.0.0.0', port=5000)
     
    #app.run(threaded=True, port=5000)
    


