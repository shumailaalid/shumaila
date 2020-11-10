from flask import Flask
from flask import request
from waitress import serve
import json, datetime
from taxid import taxid
app = Flask(__name__)


################################################ Error Handling Messages #################################################  


def errstr(flag):
    
    e = 'Something went really wrong. Sorry for Inconvenience !!!'
        
    return json.dumps({'status':'Error',"Message":e})

########################################## Routing Functions #############################################################
''' This function do the calculations '''
@app.route("/")
def index():
    return errstr(0)    
     

@app.route("/search")
def search():
    flag = 0
    
    return(taxid(str(request.args.get('search')),str(request.args.get('type'))))
    #print(request.args.get('barcode'))
   
    #print(request.args.get('name'))
    
        

    
   
    
    return errstr(flag)
        
  
 
###################################################### Main #############################################################
    
''' This is main that invokes the app '''

if __name__ == "__main__":    
    serve(app, host='0.0.0.0', port=5000)
    #app.run(threaded=True, port=5000)
    


