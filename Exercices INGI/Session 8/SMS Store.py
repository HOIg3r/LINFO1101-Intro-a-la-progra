class SMSStore:
    
    def __init__(self):
        self.sms_lst = []
    
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        has_been_viewed = False
        self.sms_lst.append((has_been_viewed, from_number, time_arrived, text_of_SMS))
        
    def message_count(self):
        return len(self.sms_lst)
    
    def get_unread_indexes(self):
        count = 0
        for sms in self.sms_lst:
            if sms[0] == False:
                count += 1
        return count
    
    def get_message(self, i):
        try: 
            self.sms_lst[i] = (True, self.sms_lst[i][1], self.sms_lst[i][2], self.sms_lst[i][3] )
            return (self.sms_lst[i][1], self.sms_lst[i][2], self.sms_lst[i][3])
        except IndexError:
            return None
            
    def delete(self,i):
        try:
            del self.sms_lst[i]
        except:
            return None
    def clear(self):
        self.sms_lst = []
        