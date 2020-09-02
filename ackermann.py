 ############################################################################
#                       ackermann.py                                         #
#                                                                            #
#This py file has function that Calculate Ackermann function for given       #                              
#numbers.                                                                    #
#Input : Interger m (Number) and Integer n                                   #                          
#Output : interger                                                           #
#Dependency : None                                                           #
#                                                                            #
 ############################################################################

def ackermann(m, n):     
    if m == 0: 
        return n + 1
    if n == 0: 
        return ackermann(m - 1, 1) 
    n2 = ackermann(m, n - 1) 
    return ackermann(m - 1, n2) 

#print(ackermann(1, 2)) 
