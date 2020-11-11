from flask import Flask
from flask import request
from waitress import serve
import json, datetime
from taxid import checktaxid
from taxid import checkbarcodeid
app = Flask(__name__)


################################################ Error Handling Messages #################################################  


def errstr(flag):
    
    e = 'Something went really wrong. Sorry for Inconvenience !!!'
        
    return json.dumps({'status':'Error')

########################################## Routing Functions #############################################################
''' This function do the calculations '''
@app.route("/")
def index():
    return errstr(0)    
     

@app.route("/search")
def search():
    
    if str(request.args.get('flag')) == '1':
        return(checktaxid(str(request.args.get('taxid'))))
                    
    elif str(request.args.get('flag')) == '2':
        return(checkbarcodeid(str(request.args.get('barcode')),str(request.args.get('name'))))    
    
    
        

    
   
    
    return json.dumps({'status':'Error'})
        
  
 
###################################################### Main #############################################################
    
''' This is main that invokes the app '''

if __name__ == "__main__":    
    serve(app, host='0.0.0.0', port=5000)
    #app.run(threaded=True, port=5000)
    


