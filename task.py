
import json, codecs
import os
from pickle import FALSE, TRUE
from user import *

class Tasks(User):
    def __init__(self,taskname,note,date,complete):
        self.name = taskname
        self.note = note
        self.date = date
        self.complete = complete
    
    def get_taskname(self):
        return self.name
    
    def get_note(self):
        return self.note
    
    def get_date(self):
        return self.date

    def get_complete(self):
        return self.complete

    def set_taskname(self,taskname):
        self.name = taskname

    def set_note(self,note):
        self.note = note

    def set_date(self,date):
        self.date = date

    def set_not_complete(self):
        self.complete = False

    def set_complete(self):
        self.complete = True

    def convert_dict(self):
        self.todict = {"Taskname": self.name , "Note" : self.note,"Date" : self.date,"Complete" : self.complete}
        return self.todict

        
    



  
        





   

       
        

   


