import json, codecs
import os
from task import *

class task_manage(Tasks):
        
    def __init__(self):
        
        self.file_path = "data.json"
        self.user_file_path = "users.json"

    def get_file_path(self):
        return self.file_path

    def get_user_file_path(self):
        return self.user_file_path

    def set_file_path(self,file_path):
        self.file_path = file_path

    def set_user_file_path(self,user_file_path):
        self.user_file_path = user_file_path

    def create_json(self):
        self.todo = {"task_list":[],"complete_task" : []}
        #check data.json is exist.
        if not os.path.exists(self.file_path):
    
            with open(self.file_path, 'ab+') as write:
              json.dump(self.todo, codecs.getwriter('utf-8')(write), ensure_ascii=False)

    def create_user_json(self):
       
        self.fill_user = {"Users":[]}
        if not os.path.exists(self.user_file_path):
    
            with open(self.user_file_path, 'ab+') as write:
              json.dump(self.fill_user, codecs.getwriter('utf-8')(write), ensure_ascii=False)

    def load_json(self):
        with open(self.file_path, 'r+') as read:
            self.data = json.load(read)
        return self.data

    def append_json(self,folder,inx,username,data_append):
        with open(self.file_path,'r+') as file:
            self.data = json.load(file)
            self.data[folder][inx][username].append(data_append)
            file.seek(0)
            json.dump(self.data, file, indent = 4)

    def write_json(self,x):
        with open(self.file_path,'w') as write:
            json.dump(x, write, indent = 4)
    
    def new_task(self,taskname,note,date):
        Tasks.set_taskname(self,taskname)
        Tasks.set_note(self,note)
        Tasks.set_date(self,date)
        Tasks.set_not_complete(self)

    def create_user(self,username,password):
        Tasks.set_username(self,username)
        Tasks.set_password(self,password)
    



