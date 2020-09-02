### imports #####
import decimal


 ############################################################################
#                       factorial.py                                         #
#                                                                            #
#This py file has function that Calculates the factorial for given number.   #                             
#Input : Interger n (Number)                                                 #                          
#Output : Integer (factorial). If output is a large number,its rounded off   #
#         to exponential form upto 5 digits.                                 #
#Dependency : Uses internal library decimal.py                               #
#                                                                            #
 ############################################################################


############################## factorial ####################################

def factorial(n):    
    fact = 1      
    for i in range(1,n+1): 
        fact = fact * i
    if fact > 10000:
        fact = format(decimal.Decimal(fact),'.5e')         
    return fact



############################ END of factorial ###############################
