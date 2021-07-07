import telebot
import ast
import time
import pandas as pd
from telebot import types

SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
PAYMENTS_PROVIDER_TOKEN = '284685063:TEST:Y2RmY2JjZmM5MDZl'





bot = telebot.TeleBot('1858996616:AAH_YJcU9EiimHjJ5sBxjrX0fxG4CEIWLRo')
menu=pd.read_excel('menu.xlsx')
result = pd.DataFrame(columns=["no"])
provider_token = '1234567890:TEST:AAAABBBBCCCCDDDD'  
global selected
global stringList1
stringList1={}
selected ={}
selected[1] = {'check':0,'name':'mm','phone':'11111111','final':'fffffffff','price':0,'egg':0,'fish':0,'meat':0,'veg':0,'oderid':0,'stringList1':{},'cardno':'','email':'','Month':'','Year':'','cvv':''}
crossIcon = '^^'#u"\u274C"
tickicon='**'#u"\u2713"

cart = '!!' #u"\U0001F6D2"

def makeKeyboard(stringList,flag):


    markup = types.InlineKeyboardMarkup()
    if flag == 1:
        for key, value in stringList.items():
            markup.add(types.InlineKeyboardButton(text=value,callback_data="['value', '" + value + "', '" + key + "']"))
    
    if flag == 6:
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        valuest= stringList.values()
        stringListt = list(valuest)
        t = 0
        while t < len(stringListt):
            
            try:
                markup.add(types.InlineKeyboardButton(text=tickicon+' '+stringListt[t],callback_data="['value', '" + stringListt[t] + "', '" + stringListt[t] + "']"),
                       types.InlineKeyboardButton(text=tickicon+' '+stringListt[t+1],callback_data="['value', '" + stringListt[t+1]+ "', '" + stringListt[t+1] + "']"))
                t = t+2
            except:
                try:
                    markup.add(types.InlineKeyboardButton(text=tickicon+' '+stringListt[t],callback_data="['value', '" + stringListt[t] + "', '" + stringListt[t] + "']"))
                    t = t+1
                except Exception as e:
                    print(e)
                    break
                   
            
                
    elif flag == 2:
        markup = types.InlineKeyboardMarkup(row_width=2)
        #cross
        for key, value in stringList.items():
            markup.add(types.InlineKeyboardButton(text=value,
                                              callback_data="['value', '" + value + "', '" + key + "']"),
            types.InlineKeyboardButton(text=crossIcon,
                                   callback_data="['key', '" + key + "']"))
    elif flag == 4:
        markup = types.InlineKeyboardMarkup(row_width=2)
        #cross
        for key, value in stringList.items():
            markup.add(types.InlineKeyboardButton(text=crossIcon,
                                              callback_data="['value', '" + value + "', '" + key + "']"))
            

    elif flag == 3:
        #tick
        markup = types.InlineKeyboardMarkup(row_width=2)
        for key, value in stringList.items():
             
        
            markup.add(types.InlineKeyboardButton(text=value,callback_data="['value', '" + value + "', '" + key + "']"),
                              
                           types.InlineKeyboardButton(text=crossIcon,
                                   callback_data="['key', '" + key + "']"))
            
        markup.add(types.InlineKeyboardButton(text='CheckOut',callback_data="['value', '" + 'pay' + "', '" + 'pay' + "']") )

    elif flag == 7:
        #tick
        markup = types.InlineKeyboardMarkup(row_width=5)
        for key, value in stringList.items():             
        
            markup.add(types.InlineKeyboardButton(text=value,callback_data="['value', '" + value + "', '" + key + "']"),
                types.InlineKeyboardButton(text=tickicon+'... Eggs',callback_data="['value', '" + value + "', '" + "eggs" + "']"),
                             types.InlineKeyboardButton(text=tickicon+'... Meat',callback_data="['value', '" + value + "', '" + "meat" + "']"),
                               types.InlineKeyboardButton(text=tickicon+'... Fish',callback_data="['value', '" + value + "', '" + "fish" + "']"),
                               types.InlineKeyboardButton(text=tickicon+'... Veg',callback_data="['value', '" + value+ "', '" + "vegetables" + "']"))

            
    elif flag == 8:
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(
                       types.InlineKeyboardButton(text='Customise Pizza',callback_data="['value', '" + "Customize Pizza" + "', '" + "customise" + "']"),
                     types.InlineKeyboardButton(text="Order",callback_data="['value', '" + "Order" + "', '" + "Order" + "']"),
                       
                       types.InlineKeyboardButton(text=cart+' View Cart',callback_data="['value', '" + 'View Cart' + "', '" + "cancel" + "']"))
    
        markup.add(types.InlineKeyboardButton(text='CheckOut',callback_data="['value', '" + 'pay' + "', '" + 'pay' + "']") )
        


            
        
    return markup





@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_command_adminwindow(message):
    global selected
    global stringList1
    if len(selected) == 1:   
       
        chatid=message.chat.id       
        
        markup = types.InlineKeyboardMarkup(row_width=3)     
        
        markup.add(types.InlineKeyboardButton(text="Order",callback_data="['value', '" + "Order" + "', '" + "Order" + "']"),
                       types.InlineKeyboardButton(text="Opening hours",callback_data="['value', '" + "Opening hours" + "', '" + "Hours" + "']"),
                     types.InlineKeyboardButton(text="Menu",callback_data="['value', '" + "Menu" + "', '" + "Menu" + "']"))

        temp = {chatid:{'check':0,'name':'','phone':'','final':'','price':0,'oderid':0,'stringList1':{},'cardno':'','email':'','Month':'','Year':'','cvv':''}}
        bot.send_message(chat_id=message.chat.id,text="Hello ! Welcome ! I am your personal virtual assistance",reply_markup=markup,parse_mode='HTML')
        selected.update(temp)
    else:
        try:
            if selected[message.chat.id]['check'] == 1:
                selected[message.chat.id]['name'] = message.json["text"]
                bot.send_message(message.chat.id,'Please Enter Your Phone Number')
                selected[message.chat.id]['check'] = 2

            elif selected[message.chat.id]['check'] == 2:
                selected[message.chat.id]['phone'] = str(message.json["text"])
                bot.send_message(message.chat.id,'Please Enter Your Email')
                selected[message.chat.id]['check'] = 3
            elif selected[message.chat.id]['check'] == 3:
                selected[message.chat.id]['email'] = str(message.json["text"])
                prices = [
        types.LabeledPrice(label='Pizza Bot', amount=(int)(selected[message.chat.id]['price'])*100),
       
    ]
                m= bot.send_invoice(chat_id=message.chat.id, title='Pizza',
                               description=selected[message.chat.id]['final'],
                               provider_token=PAYMENTS_PROVIDER_TOKEN,
                               currency='usd',
                               photo_url='https://media-cdn.tripadvisor.com/media/photo-s/0a/c0/7c/98/best-pizza-in-lahore.jpg',
                               photo_height=None,  # !=0/None or picture won't be shown
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=prices,
                                 start_parameter='pizza',
                               invoice_payload='HAPPY'
                               )
                print(m)
                m = str(m).split("'pay': ",1)[1].split('}',1)[0]
                if m == 'True':
                    print("Payment Successfull")
                else:
                    print('ERror in payment')
                
          
                ######## Absar add here ###########
                #bot.send_message(message.chat.id,'Please Enter Your Phone Number')
        except:
            chatid=message.chat.id       
        
            markup = types.InlineKeyboardMarkup(row_width=3)     
            
            markup.add(types.InlineKeyboardButton(text="Order",callback_data="['value', '" + "Order" + "', '" + "Order" + "']"),
                           types.InlineKeyboardButton(text="Opening hours",callback_data="['value', '" + "Opening hours" + "', '" + "Hours" + "']"),
                         types.InlineKeyboardButton(text="Menu",callback_data="['value', '" + "Menu" + "', '" + "Menu" + "']"))

            temp = {chatid:{'check':0,'name':'','phone':'','final':'','price':0,'oderid':0,'stringList1':{},'cardno':'','email':'','Month':'','Year':'','cvv':''}}
            bot.send_message(chat_id=message.chat.id,text="Hello ! Welcome ! I am your personal virtual assistance",reply_markup=markup,parse_mode='HTML')
            selected.update(temp)


            ##########after finishng everythng###########    
            #selected.pop(selected[call.message.chat.id], None)
                
            

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global selected
    
    if (call.data.startswith("['value'")):
        print('here1')
        #print(f"call.data : {call.data} , type : {type(call.data)}")
        #print(f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
        valueFromCallBack = ast.literal_eval(call.data)[1]
        keyFromCallBack = ast.literal_eval(call.data)[2]
        print(keyFromCallBack)
        try:
            if keyFromCallBack.isdigit():
                print('mmmmmhere')
                val =selected[call.message.chat.id]['stringList1'][keyFromCallBack]
                print(val)
               # bot.send_message(call.message.chat.id,val)
                bot.answer_callback_query(callback_query_id=call.id,
                              show_alert=True,
                              text=val)


                
            
        except Exception as e:
            print('m',e)
            pass
        
        if 'Order' in keyFromCallBack or 'Add' in keyFromCallBack :
            print('dddd',keyFromCallBack)
            markup = types.InlineKeyboardMarkup(row_width=3)     
        
            markup.add(types.InlineKeyboardButton(text='Veg',callback_data="['value', '" + 'Veg' + "', '" + "Vegetarian" + "']"),
                       types.InlineKeyboardButton(text='Non Veg',callback_data="['value', '" + 'Non Veg' + "', '" + "Viande" + "']"),
                     types.InlineKeyboardButton(text="More",callback_data="['value', '" + "More" + "', '" + "mer" + "']"))
            bot.send_message(chat_id=call.message.chat.id,text="What kind of Pizza do you want",reply_markup=markup,parse_mode='HTML')

        elif 'again' in keyFromCallBack:
            bot.send_message(call.message.chat.id,'Enter Your 16 Digit Card Number')
            selected[call.message.chat.id]['check'] = 5
            
        elif 'Start' in keyFromCallBack:
            stringList = {"Order": "Order", "Hours": "Opening hours", "Menu": "Menu"}
            bot.send_message(chat_id=call.message.chat.id,text="Hello ! Welcome ! I am your personal virtual assistance",reply_markup=makeKeyboard(stringList,1),parse_mode='HTML')
            temp = {'check':0,'name':'','phone':'','final':'','price':0,'egg':0,'fish':0,'meat':0,'veg':0,'stringList1':{},'cardno':'','email':'','Month':'','Year':'','cvv':''}
            del selected[call.message.chat.id]
            selected[call.message.chat.id]=temp
        elif 'Veg' in keyFromCallBack:
            now1= len(menu)
            stringList ={}
            
            for x in range(0,len(menu)):
                markup = types.InlineKeyboardMarkup(row_width=3)
                if 'Veg' in menu['Veg and Non Veg'][x]:
                   stringList[menu['Pizza name'][x]]=menu['Pizza name'][x]
                    

            bot.send_message(chat_id=call.message.chat.id,text="Okay! So look more at our pizzas",reply_markup=makeKeyboard(stringList,6),parse_mode='HTML')
           
        elif 'Viande' in keyFromCallBack:
            stringList ={}
           
            myval = ''
            for x in range(0,len(menu)):
                
                if 'Viande' in menu['Veg and Non Veg'][x]:
                    
                    stringList[menu['Pizza name'][x]]=menu['Pizza name'][x]
                    

            bot.send_message(chat_id=call.message.chat.id,text="Okay! So look more at our pizzas",reply_markup=makeKeyboard(stringList,6),parse_mode='HTML')
                      
        elif 'mer' in keyFromCallBack:
            stringList ={}
            
            for x in range(0,len(menu)):
               
                if 'me' in menu['Veg and Non Veg'][x]:
                   stringList[menu['Pizza name'][x]]=menu['Pizza name'][x]
                    

            bot.send_message(chat_id=call.message.chat.id,text="Okay! So look more at our pizzas",reply_markup=makeKeyboard(stringList,6),parse_mode='HTML')
     

            
        
        elif 'Menu' in keyFromCallBack :
            stringList = {}
            for x in range(0,len(menu)):
                if 'Veg' or 'mer' or 'Viande' in menu['Veg and Non Veg'][x]:
                    stringList[menu['Pizza name'][x]]=menu['Pizza name'][x]
                    

            bot.send_message(chat_id=call.message.chat.id,text="Okay! So look more at our pizzas",reply_markup=makeKeyboard(stringList,6),parse_mode='HTML')
           
          ###################################
        elif 'customise' in keyFromCallBack:
            
          # bot.send_message(chat_id=call.message.chat.id,text="Choose what you want to do?",reply_markup=makeKeyboard(stringList,7),parse_mode='HTML')
            checklist =selected[call.message.chat.id]['final'].strip().split('\n')
            print('len=',len(checklist))
            if len(checklist) > 0:
                mystringList1 ={}
                templist = {}
            
                for m in range(0,len(checklist)):

                    mystringList1[str(m)]=checklist[m].split(',',1)[0]
                    templist[str(m)]=checklist[m]
                    
                    
                bot.send_message(chat_id=call.message.chat.id,text="Add Toppings to pizza",reply_markup=makeKeyboard(mystringList1,7),parse_mode='HTML')

            else:
                bot.send_message(chat_id=call.message.chat.id,text='Cart is Empty')
            
                
            
            
                               
        elif 'vegetables' in keyFromCallBack:
                rate = 0        
                for x in range(0,len(menu)):
                    if 'vegetab' in menu['Customize Pizza'][x]:
                        rate = menu['Rate'][x]
                        break
                    
                 
                
                pname= keyFromCallBack = ast.literal_eval(call.data)[1]
                nall='N/A'
                try:
                    nall=selected[call.message.chat.id]['final'].split(pname,1).split('price',1)[0]
                except:
                    nall='N/A'
                if 'veg' in nall :
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Vegetables already added to '+pname)
                else:
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace(pname,pname+', veg = ' + str(rate))
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace('\nTopping',', Topping')
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Vegetables Added to '+pname)
                    bot.send_message(chat_id=call.message.chat.id,text='Vegetables Added to '+pname)
                    
                    print(selected[call.message.chat.id]['final'])
               

            
        elif 'meat' in keyFromCallBack:
                rate = 0        
                for x in range(0,len(menu)):
                    if 'meat' in menu['Customize Pizza'][x]:
                        rate = menu['Rate'][x]
                        break
                    
                              
                nall='N/A'
                pname= keyFromCallBack = ast.literal_eval(call.data)[1]
                try:
                    nall=selected[call.message.chat.id]['final'].split(pname,1).split('price',1)[0]
                except:
                    nall='N/A'
                if 'meat' in nall:
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Meat already added to '+pname)
                else:
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace(pname,pname+', meat = ' + str(rate))
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace('\nmeat',', meat')
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Meat Added to '+pname)
                    bot.send_message(chat_id=call.message.chat.id,text='Meat Added to '+pname)
                    
                print(selected[call.message.chat.id]['final'])
                
        elif 'fish' in keyFromCallBack:
                rate = 0        
                for x in range(0,len(menu)):
                    if 'fish' in menu['Customize Pizza'][x]:
                        rate = menu['Rate'][x]
                        break
                    
                        
                
                pname= keyFromCallBack = ast.literal_eval(call.data)[1]
                nall='N/A'
                try:
                    nall=selected[call.message.chat.id]['final'].split(pname,1).split('price',1)[0]
                except:
                    nall='N/A'
                if 'fish' in nall:
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Fish already added to '+pname)
                else:
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace(pname,pname+',fish = ' + str(rate))
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace('\nfish',', fish')
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Fish Added to '+pname)
                    bot.send_message(chat_id=call.message.chat.id,text='Fish Added to '+pname)
                    
                print(selected[call.message.chat.id]['final'])


        elif 'eggs' in keyFromCallBack:
                rate = 0        
                for x in range(0,len(menu)):
                    if 'egg' in menu['Customize Pizza'][x]:
                        rate = menu['Rate'][x]
                        break
                    
                nall ='N/A'
                
                pname= keyFromCallBack = ast.literal_eval(call.data)[1]
                try:
                    nall=selected[call.message.chat.id]['final'].split(pname,1).split('price',1)[0]
                except:
                    nall='N/A'
                if 'egg' in nall:
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Eggs already added to '+pname)
                else:
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace(pname,pname+', egg = ' + str(rate))
                    selected[call.message.chat.id]['final']= selected[call.message.chat.id]['final'].replace('\negg',', egg')
                    bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text='Eggs Added to '+pname)
                    bot.send_message(chat_id=call.message.chat.id,text='Eggs Added to '+pname)
        
                    
                print(selected[call.message.chat.id]['final'])
###################################


        elif 'pay' in keyFromCallBack:
            finalprice=0
            pricelist = selected[call.message.chat.id]['final'].split('Price = ')[1:]
            print(pricelist)
            
            for pr in pricelist:
                print(pr)
                pr=pr.split(', ',1)[0]
                try:
                    pr=pr.split('\n',1)[0]
                except:
                    pass
                print(pr)
                finalprice=finalprice + (float)(pr)

            pricelist = selected[call.message.chat.id]['final'].split('egg = ')[1:]
            print(pricelist)
            
            for pr in pricelist:
                print(pr)
                pr=pr.split(',',1)[0]
                try:
                    pr=pr.split('\n',1)[0]
                except:
                    pass
                print(pr)
                finalprice=finalprice + (float)(pr)

            pricelist = selected[call.message.chat.id]['final'].split('meat = ')[1:]
            print(pricelist)
            
            for pr in pricelist:
                print(pr)
                pr=pr.split(',',1)[0]
                try:
                    pr=pr.split('\n',1)[0]
                except:
                    pass
                print(pr)
                finalprice=finalprice + (float)(pr)
            pricelist = selected[call.message.chat.id]['final'].split('fish = ')[1:]
            print(pricelist)
            
            for pr in pricelist:
                print(pr)
                pr=pr.split(',',1)[0]
                try:
                    pr=pr.split('\n',1)[0]
                except:
                    pass
                print(pr)
                finalprice=finalprice + (float)(pr)
            selected[call.message.chat.id]['price']=finalprice
            
            pricelist = selected[call.message.chat.id]['final'].split('veg = ')[1:]
            print(pricelist)
            
            for pr in pricelist:
                print(pr)
                pr=pr.split(', ',1)[0]
                try:
                    pr=pr.split('\n',1)[0]
                except:
                    pass
                print(pr)
                finalprice=finalprice + (float)(pr)
                
            bot.send_message(chat_id=call.message.chat.id,text='Details:\n '+selected[call.message.chat.id]['final']+'\nTotal Price:'+str(finalprice))
            
            
            bot.send_message(chat_id=call.message.chat.id,text='Enter Full Name')
            selected[call.message.chat.id]['check'] = 1
            
            
        elif 'cancel' in keyFromCallBack:
            
      
            ############### calculating price #############
            
            checklist =selected[call.message.chat.id]['final'].strip().split('\n')
            print('len=',len(checklist))
            if len(checklist) > 0:
                mystringList1 ={}
                templist = {}
            
                for m in range(0,len(checklist)):
                    mystringList1[str(m)]=checklist[m].split(',',1)[0]
                    templist[str(m)]=checklist[m]
                    
                    
                bot.send_message(chat_id=call.message.chat.id,text="Cart",reply_markup=makeKeyboard(mystringList1,3),parse_mode='HTML')

            else:
                bot.send_message(chat_id=call.message.chat.id,text='Cart is Empty')
            
                
                           
                
          
           
        
#######################################

           

#####strip

        elif 'Credit card' in keyFromCallBack:
            ###Add strip
                selected[call.message.chat.id]['check'] = 1
############selected[call.message.chat.id]['price']=finalprice    
            
            
            
            ############### 3333333333 #############
        elif 'Hours' in keyFromCallBack :
             bot.send_message(chat_id=call.message.chat.id,text="Monday :  6.00pm – 22pm\nTuesday :  6.00pm – 22pm\nWednesday : 6.00pm – 22pm\nThursday : 6.00pm – 22pm\nFriday : 6.00pm – 22pm\nSaturday : 6.00pm – 22pm\nSunday : 6.00pm – 22pm\n")



       
            
                
            
        else:
            myval=''
            print('ghghg',keyFromCallBack)
            for x in range(0,len(menu)):
                stringList={}
                markup = types.InlineKeyboardMarkup(row_width=3)
                if keyFromCallBack in menu['Pizza name'][x]:
                   stringList[menu['Pizza name'][x]]=menu['Pizza name'][x]
                   markup.add(
                                        types.InlineKeyboardButton(text=cart+' Pocket  ',
                                                               callback_data="['key1', '" + menu['Pizza name'][x] + "']"),
                                        types.InlineKeyboardButton(text=cart+' Petite  ',
                                                               callback_data="['key2', '" + menu['Pizza name'][x] + "']"),
                                       types.InlineKeyboardButton(text=cart+' Moyenne  ',
                                                               callback_data="['key3', '" + menu['Pizza name'][x] + "']"),
                                        
                                        types.InlineKeyboardButton(text="Menu",callback_data="['value', '" + "Menu" + "', '" + "Menu" + "']"))
                   bot.send_photo(chat_id=call.message.chat.id, photo=open('pixxa.jpg','rb'),caption=menu['Pizza name'][x]+'\nComposition:\n'+menu['Composition'][x],reply_markup=markup,parse_mode='HTML')
                   break
      
            
    if (call.data.startswith("['key1'")):
        print('clicked pocket')
        
        myval = ''
        stringList={}
        for x in range(0,len(menu)):
            if ast.literal_eval(call.data)[1] in menu['Pizza name'][x].strip():
                     
                selected[call.message.chat.id]['selected'] =x
                stringList[menu['Pizza name'][x]]=menu['Pizza name'][x]
                break

        price = menu['Pocket'][selected[call.message.chat.id]['selected']]          
        name = menu['Pizza name'][selected[call.message.chat.id]['selected']]
        selected[call.message.chat.id]['final'] = selected[call.message.chat.id]['final'] + name +', Size = Pocket'+ ', Price = '+str(price) + '\n'
        #bot.send_message(chat_id=call.message.chat.id,text='So You have Selected Pizza = " '+ selected[call.message.chat.id]['final'])
        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=False,
                                  text='Added to Cart: '+name+', Size = Pocket')
        bot.send_message(chat_id=call.message.chat.id,text='Added to Cart: '+name+', Size = Pocket',parse_mode='HTML')
         #types.InlineKeyboardButton(text='Customise Pizza',callback_data="['value', '" + "Customize Pizza" + "', '" + "customise" + "']"),
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton(text='Customise Pizza',callback_data="['value', '" + "Customize Pizza" + "', '" + "customise" + "']"),
                      
                     types.InlineKeyboardButton(text="Add another Pizza",callback_data="['value', '" + "Menu" + "', '" + "Menu" + "']"),
                       
                       types.InlineKeyboardButton(text=cart+' View Cart',callback_data="['value', '" + 'View Cart' + "', '" + "cancel" + "']"))
    
        markup.add(types.InlineKeyboardButton(text='CheckOut',callback_data="['value', '" + 'pay' + "', '" + 'pay' + "']") )
        

        bot.send_message(chat_id=call.message.chat.id,text="Choose what you want to do?",reply_markup=markup,parse_mode='HTML') 
        
        
               
    if (call.data.startswith("['key2'")):
        print('clicked petite')
        
        myval = ''   
        for x in range(0,len(menu)):
            if ast.literal_eval(call.data)[1] in menu['Pizza name'][x].strip():
                     
                selected[call.message.chat.id]['selected'] =x
                break

        price = menu[' Petite (29 cm)'][selected[call.message.chat.id]['selected']]          
        name = menu['Pizza name'][selected[call.message.chat.id]['selected']]
        selected[call.message.chat.id]['final'] = selected[call.message.chat.id]['final'] + name +', Size =  Petite (29 cm)'+ ', Price = '+str(price) + '\n'
        #bot.send_message(chat_id=call.message.chat.id,text='So You have Selected Pizza = " '+ selected[call.message.chat.id]['final'])
        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=False,
                                  text='Added to Cart: '+name+', Size =  Petite (29 cm)')
        bot.send_message(chat_id=call.message.chat.id,text='Added to Cart: '+name+', Size = Petite (29 cm)',parse_mode='HTML')
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(
            types.InlineKeyboardButton(text='Customise Pizza',callback_data="['value', '" + "Customize Pizza" + "', '" + "customise" + "']"),
                                          types.InlineKeyboardButton(text="Add another Pizza",callback_data="['value', '" + "Menu" + "', '" + "Menu" + "']"),
                       
                       types.InlineKeyboardButton(text=cart+' View Cart',callback_data="['value', '" + 'View Cart' + "', '" + "cancel" + "']"))
    
        markup.add(types.InlineKeyboardButton(text='CheckOut',callback_data="['value', '" + 'pay' + "', '" + 'pay' + "']") )
        

        bot.send_message(chat_id=call.message.chat.id,text="Choose what you want to do?",reply_markup=markup,parse_mode='HTML') 
        
    if (call.data.startswith("['key3'")):
        print('clicked petite')
        
        myval = ''   
        for x in range(0,len(menu)):
            if ast.literal_eval(call.data)[1] in menu['Pizza name'][x].strip():
                     
                selected[call.message.chat.id]['selected'] =x
                break

        price = menu['Moyenne (40 cm)'][selected[call.message.chat.id]['selected']]          
        name = menu['Pizza name'][selected[call.message.chat.id]['selected']]
        selected[call.message.chat.id]['final'] = selected[call.message.chat.id]['final'] + name +', Size =  Moyenne (40 cm)'+ ', Price = '+str(price) + '\n'
        #bot.send_message(chat_id=call.message.chat.id,text='So You have Selected Pizza = " '+ selected[call.message.chat.id]['final'])
        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=False,
                                  text='Added to Cart: '+name+', Size = Moyenne (40 cm)')
        bot.send_message(chat_id=call.message.chat.id,text='Added to Cart: '+name+', Size = Moyenne (40 cm)',parse_mode='HTML')
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton(text='Customise Pizza',callback_data="['value', '" + "Customize Pizza" + "', '" + "customise" + "']"),
                      
                     types.InlineKeyboardButton(text="Add another Pizza",callback_data="['value', '" + "Menu" + "', '" + "Menu" + "']"),
                       
                       types.InlineKeyboardButton(text=cart+' View Cart',callback_data="['value', '" + 'View Cart' + "', '" + "cancel" + "']"))
    
        markup.add(types.InlineKeyboardButton(text='CheckOut',callback_data="['value', '" + 'pay' + "', '" + 'pay' + "']") )
        

        bot.send_message(chat_id=call.message.chat.id,text="Choose what you want to do?",reply_markup=markup,parse_mode='HTML') 
        
  
    if (call.data.startswith("['key'")):
        #print('mnoe',ast.literal_eval(call.data)[2])
        keyFromCallBack = ast.literal_eval(call.data)[1]
        print('thissssssss',keyFromCallBack)
        
        print('1',selected[call.message.chat.id]['stringList1'])
        val =selected[call.message.chat.id]['stringList1'][keyFromCallBack]
        
        del selected[call.message.chat.id]['stringList1'][keyFromCallBack]
        
        print('2',selected[call.message.chat.id]['stringList1'])
        selected[call.message.chat.id]['final']=selected[call.message.chat.id]['final'].replace(val+'\n','')
        print('final',selected[call.message.chat.id]['final'])
        bot.edit_message_text(chat_id=call.message.chat.id,
                              text="Choose what You want to do",
                              message_id=call.message.message_id,
                              reply_markup=makeKeyboard(selected[call.message.chat.id]['stringList1'],2),
                              parse_mode='HTML')
        if len(selected[call.message.chat.id]['stringList1']) == 0:
            temp = {call.message.chat.id:{'check':0,'name':'','phone':'','final':'','price':0,'egg':0,'fish':0,'meat':0,'veg':0,'stringList1':{},'cardno':'','email':'','Month':'','Year':'','cvv':''}}

     
        
def botpizza_21():
    
    
    if True:
        try:            
            retrun bot.polling(none_stop=True, interval=0)
            #executor.start_polling(dp, skip_updates=True)
        except Exception as e:
            retrun e
            
        
#botpizza_21()



