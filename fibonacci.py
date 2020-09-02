 ############################################################################
#                       Fibonacci.py                                         #
#                                                                            #
#This py file has function that Calculate Fibonacci series for given number. #                             
#Input : Interger (Number), n                                                #                          
#Output : Fibonacci Series (list)                                            #
#Dependency : None                                                           #
#                                                                            #
 ############################################################################



def calfib(n):
    if n <= 1:
       return n
    else:        
        return calfib(n-1)+calfib(n-2)
    
def fibonacci(n):
    seq = []
   
    if n==1: 
        return str(0)
    elif n==2: 
        return str(1)
    else:
        for i in range(n):
            seq.append(str(calfib(i)))

    #print(seq)
    return ', '.join(seq)
        
        


#fibonacci(2.50)
