from flask import Flask
from flask import request
from waitress import serve
from fibonacci import fibonacci
from ackermann import ackermann
from factorial import factorial
import json

app = Flask(__name__)

################################################ Calculate ###############################################################

''' This function do the calculations '''

@app.route("/calculate")
def calculate():
    if request.args.get('operation') == 'fibonacci' or request.args.get('operation') == 'fib': 
        try:
            n =(int)(request.args.get('n'))
            if n < 1:
                retstr(1)                  
            return json.dumps({'result':fibonacci(n)})
                
        except:
            retstr(1)                
           
    elif request.args.get('operation') == 'ackermann' or request.args.get('operation') == 'ack':
        try:
            n1 =(int)(request.args.get('n1'))
            if n1 < 1:
                retstr(1)  
            n2 =(int)(request.args.get('n2'))
            if n2 < 1:
                retstr(1)                
            return json.dumps({'result':ackermann(n1,n2)})                
        except:
            retstr(1)  
        
    elif request.args.get('operation') == 'factorial' or request.args.get('operation') == 'fac':
        try:
            n =(int)(request.args.get('n'))
            if n < 1:
                retstr(1)                
            return json.dumps({'result':factorial(n)})                
        except:
            retstr(1)                 
    else:
        retstr(2)
        
###################################################### restr ############################################################
        
''' This function returns error messages '''
        
def retstr(i):
    if i == 1:
        return json.dumps({'error':'Enter a Valid Positive Integer'})
    elif i == 2:
        return json.dumps({'error':'Please enter a valid operation type'})

   
 
###################################################### Main #############################################################
    
''' This is main that invokes the app '''

if __name__ == "__main__":    
    app.run()
    


