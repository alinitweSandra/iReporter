import datetime

def check_type_date(self, input_date):
             
        day,month,year = input_date.split('/') 
        
        x=datetime.datetime(int(year),int(month),int(day))
        
        if(x) :
                return True
        else :
                return False
            
def check_type_string(self, input_type):
 
    x= isinstance(input_type, str)
    if(x) :
        return True
    else :
        return False

def check_type_list(self, input_type):
     
    x= isinstance(input_type, (list,))
    if(x) :
        return True
    else :
        return False
    
def check_type_int(self, input_type):
         
    x= isinstance(input_type, int)
    if(x) :
        return True
    else :
        return False

def check_type_bool(self, input_type):
        x= isinstance(input_type,bool)
        if(x):
                return True
        else:
                return False

                
            