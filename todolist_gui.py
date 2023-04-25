from ast import Lambda
import tkinter as tk
from tkinter import *
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from PIL import Image,ImageTk
from task import *
import json, codecs
from tkinter import ttk
from tkcalendar import *
from todo_mang import *
from tkinter import messagebox
from user import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import datetime as DT
from tkinter import ttk
from calendar import monthrange
import datetime

class GuiApp(tk.Frame):
    
    def __init__(self,logwin):
        tk.Frame.__init__(self,logwin)
        #self.file_path="data.json"
        #self.user_file_path="users.json"
        task_manage.set_file_path(self,'data.json')
        task_manage.get_file_path(self)

        task_manage.set_user_file_path(self,'users.json')
        task_manage.get_user_file_path(self)
        
        lambda: task_manage.create_user_json(self)
        
        self.logwin = logwin
        self.logwin.geometry('620x280')

        self.login_frame  =tk.Frame(self.logwin,bg ='firebrick',highlightbackground="black",highlightthickness= 0.1,width = 620,height=280)
        self.login_frame.grid(row = 0 ,column = 0)
        self.login_frame.grid_propagate(0)

        self.topic_label = tk.Label(self.login_frame,text = 'To DO List',width =30,font = "Helvetica 16 bold italic")
        self.topic_label.grid(row = 0,column=0,pady =30,columnspan=3,padx = 80)

        self.username_label  = tk.Label(self.login_frame,text = "Username",width = 15)
        self.username_label.grid(row=1,column =0,columnspan=2,sticky = tk.W,pady =10,padx = 20)

        self.username_entry = tk.Entry(self.login_frame,width=50)
        self.username_entry.grid(row =1,column=1,sticky=tk.W,pady =10)

        self.password_label  = tk.Label(self.login_frame,text = "Password",width = 15)
        self.password_label.grid(row=2,column =0,columnspan=2,sticky = tk.W,pady =10,padx =20)

        self.password_entry = tk.Entry(self.login_frame,width=50)
        self.password_entry.grid(row =2,column=1,sticky=tk.W,pady =10)

        self.login_button = tk.Button(self.login_frame,text = 'Login',width =20,command = lambda: Todo_manager.check_user(self))
        self.login_button.grid(row=3,column = 0,pady=20,padx=5)

        self.Register_button = tk.Button(self.login_frame,text = 'Register',width =20,command = self.register_page)
        self.Register_button.grid(row=3,column = 1,pady =10)

        self.exit_button = tk.Button(self.login_frame,text = 'Exit',width =20,command = lambda: Todo_manager.exit_login(self))
        self.exit_button.grid(row=3,column = 2,pady =10,padx=5)

     
    def main_gui(self):
        
        lambda: task_manage.get_file_path(self)
        lambda: task_manage.get_user_file_path(self)

        # Create Main Window
        self.master = tk.Toplevel(self.master)
        self.master.geometry("450x650")

        
        ### Top frame 
        self.top_frame = tk.Frame(self.master,bg ='firebrick',highlightbackground="black",highlightthickness= 0.1,width = 450,height=50)
        self.top_frame.grid(row = 0 ,column = 0,columnspan=6)
        self.top_frame.grid_propagate(0)

        # Resize image a

        self.img =(Image.open("check.png"))
        self.resize_img = self.img.resize((30,30),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.resize_img)

        self.img2 =(Image.open("bars.png"))
        self.resize_img2 = self.img2.resize((25,25),Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.resize_img2)

        self.img3 =(Image.open("search.png"))
        self.resize_img3 = self.img3.resize((20,20),Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.resize_img3)



        
        #Button
        #add menu to button
        self.bars_button =tk.Menubutton(self.top_frame,image = self.photo2,width = 25,height=25,bg = 'firebrick')
        self.bars_button.grid(row=0,column = 0,pady = 20,padx = 5)

        self.bars_button.menu =  tk.Menu(self.bars_button,tearoff=0)
        self.bars_button["menu"] = self.bars_button.menu

        editVar = IntVar()
        self.bars_button.menu.add_command(label = "Edit",command =self.Edit_task) #command = lambda: Todo_manager.get_lb_item(self)
        self.bars_button.menu.add_command(label = 'Delete',command = lambda: Todo_manager.remove_task(self))
        self.bars_button.menu.add_command(label = "Complete History",command = self.com_history)
        self.bars_button.menu.add_command(label = "Import",command = lambda: Todo_manager.import_file(self))
        self.bars_button.menu.add_command(label = "Export",command = lambda: Todo_manager.export_file(self))
        

        


        self.cb_box = ttk.Combobox(self.top_frame,values=["Graph1","Graph2","Graph3"],width=30)
        self.cb_box.grid(row = 0,column=3,padx=10)

        self.cb_button = tk.Button(self.top_frame,text = 'Choose Graph Display',command = lambda: Todo_manager.graph_callback(self))
        self.cb_button.grid(row= 0,column =5,padx=10)

        
        ### Middle Frame
        self.mid_frame = tk.Frame(self.master,bg = 'navajowhite',highlightbackground="black",highlightthickness= 0.1,width = 450,height=560)
        self.mid_frame.grid(row = 1,column =0,columnspan = 6)
        self.mid_frame.grid_propagate(0)

        #self.lb = tk.Listbox(self.mid_frame,width =  60 ,height= 30,fg = 'blue')
        #self.lb.grid(row = 0 ,column = 0 ,pady = 40,padx = 40)

        self.tv = ttk.Treeview(self.mid_frame,height=23)
        self.tv['columns']=('ID', 'TaskName', 'Note','Date')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('ID', anchor=CENTER, width=70)
        self.tv.column('TaskName', anchor=CENTER, width=70)
        self.tv.column('Note', anchor=CENTER, width=200)
        self.tv.column('Date', anchor=CENTER, width=70)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('ID', text='ID', anchor=CENTER)
        self.tv.heading('TaskName', text='TaskName', anchor=CENTER)
        self.tv.heading('Note', text='Note', anchor=CENTER)
        self.tv.heading('Date', text='Date', anchor=CENTER)

        self.tv.grid(row = 0,column = 0,pady = 20 ,padx = 20 )

        #Check button
        self.check_button = tk.Button(self.mid_frame,image = self.photo,width = 25,height=25,bg = 'navajowhite',command = lambda: Todo_manager.markasdone(self))
        self.check_button.grid(row =1,column=0)

     
        ### Bot Frame
        self.bot_frame = tk.Frame(self.master,bg = 'firebrick',highlightbackground="black",highlightthickness= 0.1,width = 450,height=40)
        self.bot_frame.grid(row = 2,column =0,columnspan = 6)
        self.bot_frame.grid_propagate(0)
        
        #Resize img
        self.img4 =(Image.open("plus.png"))
        self.resize_img4 = self.img4.resize((35,35),Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(self.resize_img4)

        #Button
        self.add_button =tk.Button(self.bot_frame,image = self.photo4,width = 35,height=35,bg = 'firebrick',command = self.newwin)
        self.add_button.grid(row=0,column = 0,padx = 205)

      
        


        Todo_manager.load_task(self)

        
        

    def newwin(self):
        self.new = tk.Toplevel(self.master)

        
       
        self.new.geometry("500x350")
        self.frame = tk.Frame(self.new,bg = "firebrick",highlightbackground="black",highlightthickness= 0.1,width=500,height=350)
        self.frame.grid(row = 0 ,column = 0)
        self.frame.grid_propagate(0)

        self.label = tk.Label(self.frame,text = "TaskName")
        self.label.grid(row =0,column = 0,pady = 20)

        self.entry1 = tk.Entry(self.frame,width = 65)
        self.entry1.grid(row = 0,column =1,pady = 20,padx = 10,sticky = tk.W)

        self.tb = tk.Text(self.frame,width= 50 ,height=10)
        self.tb.grid(row =1 ,column = 1 ,pady = 10,sticky = tk.W)

        self.date_entry =tk.Entry(self.frame)
        self.date_entry.grid(row = 2 ,column = 1,pady = 5)

        self.date_button = tk.Button(self.frame,text = 'Set Date',command = self.calendar_frame)
        self.date_button.grid(row= 3 ,column = 1,pady=5)

        self.save_button = tk.Button(self.frame,width=20,text= 'Save',command = lambda: Todo_manager.save_task(self))
        self.save_button.grid(row=4,column =1)

    def calendar_frame(self):
        self.w = tk.Toplevel(self.master)
        self.w.geometry('450x350')
        self.w.config(bg="firebrick")

        self.frame_date = tk.Frame(self.w,bg = 'navajowhite',width = 350,height=300)
        self.frame_date.grid(row=0,column = 0,padx = 50,pady = 20)
        self.frame_date.grid_propagate(0)
        self.cal = Calendar(self.frame_date, selectmode="day", year=2022, month=1,day=16)
        self.cal.grid(row = 0,column = 0,pady = 10,padx = 50)

        self.get_date_button = tk.Button(self.frame_date,text= 'Get Date',command = lambda: Todo_manager.get_date(self))
        self.get_date_button.grid(row= 1,column =0,pady = 10 )
    def Edit_task(self):

        self.root = tk.Toplevel(self.master)
        self.root.geometry("500x300")
        self.frame = tk.Frame(self.root,bg = "firebrick",highlightbackground="black",highlightthickness= 0.1,width=500,height=300)
        self.frame.grid(row = 0,column=1)
        self.frame.grid_propagate(0)

        Todo_manager.tree_selected(self)
       
        self.name_label = tk.Label(self.frame,text = 'TaskName')
        self.name_label.grid(row=0,column=0)
        self.entry_name = tk.Entry(self.frame,width = 50)
        self.entry_name.insert(0,self.get_name)
        self.entry_name.grid(row=0,column=1,padx = 20,pady = 10)

        self.note_label = tk.Label(self.frame,text = 'Note',width = 8)
        self.note_label.grid(row= 1,column =0)
        self.text_box = tk.Text(self.frame,width = 50 ,height=8)
        self.text_box.grid(row=1,column=1,padx = 20,pady =10)
        self.text_box.insert(END, self.get_note)

        self.date_label =tk.Label(self.frame,text= 'Date',width = 8)
        self.date_label.grid(row=2,column = 0)
        self.edit_entry_date = tk.Entry(self.frame,width = 20)
        self.edit_entry_date.grid(row =2 ,column = 1)
        self.edit_entry_date.insert(0,self.get_tree_date)

        self.save_button= tk.Button(self.frame,text = 'Save',command = lambda: Todo_manager.edit(self))
        self.save_button.grid(row=3,column =1,padx=20,pady=10)

    def com_history(self):
        self.root = tk.Toplevel(self.master)
        self.root.geometry('400x500')
        self.root.title("Complete Tasks")

        self.frame = tk.Frame(self.root,width = 400,height=600,bg = 'navajowhite')
        self.frame.grid(row= 0,column =0)
        self.frame.grid_propagate(0)

        self.tv2 = ttk.Treeview(self.frame,height=20)
        self.tv2['columns']=('ID', 'TaskName', 'Note','Date')
        self.tv2.column('#0', width=0, stretch=NO)
        self.tv2.column('ID', anchor=CENTER, width=70)
        self.tv2.column('TaskName', anchor=CENTER, width=70)
        self.tv2.column('Note', anchor=CENTER, width=150)
        self.tv2.column('Date', anchor=CENTER, width=70)

        self.tv2.heading('#0', text='', anchor=CENTER)
        self.tv2.heading('ID', text='ID', anchor=CENTER)
        self.tv2.heading('TaskName', text='TaskName', anchor=CENTER)
        self.tv2.heading('Note', text='Note', anchor=CENTER)
        self.tv2.heading('Date', text='Date', anchor=CENTER)

        self.tv2.grid(row = 0,column = 0,pady = 20 ,padx = 20 )

        Todo_manager.show_complete(self)
    
    def register_page(self):
        self.root = tk.Toplevel(self.logwin)
        self.root.geometry('350x250')
        self.frame = tk.Frame(self.root,width = 350,height=250,bg = "firebrick")
        self.frame.grid(row = 0,column=0)
        self.frame.grid_propagate(0)

        self.label1 = tk.Label(self.frame,text = 'REGISTER',width =15,font = "Helvetica 16 bold italic")
        self.label1.grid(row=0,column=0,padx=10,columnspan=3,pady =20)

        self.regis_username_label  = tk.Label(self.frame,text = "Username",width = 15)
        self.regis_username_label.grid(row=1,column =0,pady =10,padx =  10)

        self.regis_username_entry = tk.Entry(self.frame,width=30)
        self.regis_username_entry.grid(row =1,column=1,pady =10,padx=10)

        self.regis_password_label  = tk.Label(self.frame,text = "Password",width = 15)
        self.regis_password_label.grid(row=2,column =0,pady =10,padx=10)

        self.regis_password_entry = tk.Entry(self.frame,width=30)
        self.regis_password_entry.grid(row =2,column=1,pady =10,padx=10)

        self.regis_button = tk.Button(self.frame,text = 'Register.',width = 20,command = lambda: Todo_manager.register(self))
        self.regis_button.grid(row= 3,column=0,columnspan=3,pady = 20)
    
    



class Todo_manager(task_manage):

    def graph_callback(self):
        if self.cb_box.get() == "Graph1":
            Todo_manager.get_graph(self)
        
        elif self.cb_box.get() == "Graph2":
            Todo_manager.get_graph7days(self)

        elif self.cb_box.get() == "Graph3":
            Todo_manager.get_graph3(self)

        else:
            messagebox.showerror("showerror", "You Must Choose One.")

    def get_fp(self):
        task_manage.get_file_path(self)
        self.fp = self.file_path

    def exit_login(self):
        self.logwin.destroy()

    # This func is use to convert to dict and save as json then display on listbox
    def save_task(self):
        task_manage.create_json(self)

        self.topic = self.entry1.get()
        
    

        if self.topic != "":
            #self.todict = {"Taskname": self.entry1.get() , "Note" : self.tb.get("1.0","end-1c"),"Date" : self.date_entry.get()}
            task_manage.new_task(self,self.entry1.get(),self.tb.get("1.0","end-1c"),self.date_entry.get())
            task_manage.convert_dict(self)
            task_manage.append_json(self,"task_list",self.inx,self.user,self.todict)
            print(self.count)
            self.tv.insert(parent='', index= self.count , iid= self.count, text='', values=(self.count,self.data['task_list'][self.inx][self.user][self.count]['Taskname'],self.data['task_list'][self.inx][self.user][self.count]['Note'],self.data['task_list'][self.inx][self.user][self.count]['Date']))
            #self.lb.insert("end",self.todict['Taskname'])อ
            self.entry1.delete(0, "end")
            self.tb.delete("1.0",'end-1c')
            self.date_entry.delete(0,"end")
            
            self.count +=1
            print(self.count)
            print(self.todict)
        else:
            messagebox.showerror("showerror", "You must to insert Taskname . ")

        return self.count
    def load_task(self):
        lambda: task_manage.create_json(self)
        

        self.count = 0 
        with open(self.file_path, 'r+') as read:
            self.data = json.load(read)
            for i in range(len(self.data['task_list'][self.inx][self.user])):
                
                print(self.data['task_list'][self.inx][self.user][self.count]['Taskname'])
                self.tv.insert(parent='', index= i , iid= i, text='', values=(i,self.data['task_list'][self.inx][self.user][i]['Taskname'],self.data['task_list'][self.inx][self.user][i]['Note'],self.data['task_list'][self.inx][self.user][i]['Date']))
                self.count +=1
                
        return self.count

    def tree_selected(self):
        for selected_item in self.tv.selection():
            self.item_iid = self.tv.selection()[0]
            print(self.item_iid)
            self.get_name =self.data['task_list'][self.inx][self.user][int(self.item_iid)]['Taskname']
            self.get_note =self.data['task_list'][self.inx][self.user][int(self.item_iid)]['Note']
            self.get_tree_date = self.data['task_list'][self.inx][self.user][int(self.item_iid)]['Date']
            self.get_tree_complete = self.data['task_list'][self.inx][self.user][int(self.item_iid)]['Complete']

    def update_tree(self,task,note,date):
        self.selected = self.tv.focus()
        self.temp = self.tv.item(self.selected, 'values')
        
        self.tv.item(self.selected, values=(self.temp[0], task, note,date))

    def clear_tree(self):
        for self.item in self.tv.get_children():
            self.tv.delete(self.item)

    def get_date(self):
        self.date = self.cal.get_date()
        if self.date_entry != "":
            self.date_entry.delete(0,"end")
        self.date_entry.insert(0,self.date)
        self.w.destroy()


    def edit(self):
        self.name_val = self.entry_name.get()
        self.note_val = self.text_box.get("1.0","end-1c")
        self.date_val = self.edit_entry_date.get()
        
        #self.data['task_list'][int(self.item_iid)]['Taskname'] = self.name_val
        #self.data['task_list'][int(self.item_iid)]['Note'] = self.note_val 
        with open(self.file_path, 'r') as f:
            self.json_data = json.load(f)
            self.json_data['task_list'][self.inx][self.user][int(self.item_iid)]['Taskname'] = self.entry_name.get()
            self.json_data['task_list'][self.inx][self.user][int(self.item_iid)]['Note'] = self.text_box.get("1.0","end-1c")
            self.json_data['task_list'][self.inx][self.user][int(self.item_iid)]['Date'] = self.edit_entry_date.get()
            Todo_manager.update_tree(self,self.name_val,self.note_val,self.date_val)

        with open(self.file_path, 'w') as f:
            json.dump(self.json_data, f, indent = 4)

        self.root.destroy()

    def remove_task(self):
        self.selected_item = self.tv.selection()[0]    
        self.tv.delete(self.selected_item)
        with open(self.file_path, 'r+') as read:
            self.data = json.load(read)
            self.x = self.data['task_list'][self.inx][self.user]
            self.x.pop(int(self.selected_item))
            
        task_manage.write_json(self,self.data)    
        Todo_manager.clear_tree(self)   
        Todo_manager.load_task(self)
        #self.count -= 1

        return self.count

    def show_complete(self):
        task_manage.load_json(self)
        for i in range(len(self.data['complete_task'][self.inx][self.user])):
                
            print(self.data['complete_task'][self.inx][self.user][i]['Taskname'])
            self.tv2.insert(parent='', index= i , iid= i, text='', values=(i,self.data['complete_task'][self.inx][self.user][i]['Taskname'],self.data['complete_task'][self.inx][self.user][i]['Note'],self.data['complete_task'][self.inx][self.user][i]['Date']))



    def check_user(self):
        self.username_list = []
        self.password_list = []
        self.user = self.username_entry.get()
        self.password = self.password_entry.get()
        with open(self.user_file_path, 'r+') as read:
            self.userdata = json.load(read)
            for i in self.userdata["Users"]:
                self.username_list.append(i["Username"])
                self.password_list.append(i["Password"])
                print(self.username_list)
            if self.user not in self.username_list or self.password not in self.password_list:
                messagebox.showerror("showerror", "Invalid username or password")
            else:
                print("Login Sucess!!.")
                
                self.inx = self.username_list.index(self.user)
                print(self.inx)
                task_manage.create_user(self,self.user,self.password)
                self.logwin.withdraw()
                GuiApp.main_gui(self)

    def markasdone(self):
        Todo_manager.tree_selected(self)
        self.selected_item = self.tv.selection()[0]    
        self.tv.delete(self.selected_item)
    
        with open(self.file_path, 'r') as f:
            self.json_data = json.load(f)
            self.json_data['task_list'][self.inx][self.user][int(self.item_iid)]['Complete'] = True
            self.json_data["complete_task"][self.inx][self.user].append(self.json_data["task_list"][self.inx][self.user][int(self.item_iid)])
            f.seek(0)
            y = self.json_data["task_list"][self.inx][self.user]
            y.pop(int(self.selected_item))
        task_manage.write_json(self,self.json_data)
        Todo_manager.clear_tree(self)
        Todo_manager.load_task(self)

    def register(self):
        self.regis_user = self.regis_username_entry.get()
        self.regis_password = self.regis_password_entry.get()
        task_manage.create_user(self,self.regis_user,self.regis_password)
        User.convert_user_dict(self)
        print(self.user_dict)
        
        with open(self.file_path,'r+') as file:
           self.data = json.load(file)
           self.data["task_list"].append({self.regis_user : []})
           self.data["complete_task"].append({self.regis_user : []})
           file.seek(0)
           json.dump(self.data, file, indent = 4)
  
        with open(self.user_file_path,'r+') as file:
            self.user_data = json.load(file)
            self.user_data["Users"].append(self.user_dict)
            file.seek(0)
            json.dump(self.user_data, file, indent = 4)
        
        self.root.destroy()
    
    def import_file(self):
        file_path = filedialog.askopenfilename(title ='Select Data File To Import.',filetypes=[("Json files","*.json")])
        if file_path:
            task_manage.set_file_path(self,file_path)
            
        
        user_path = filedialog.askopenfilename(title ='Select User File To Import.',filetypes=[("Json files","*.json")])
        if user_path:
            task_manage.set_user_file_path(self,user_path)
        Todo_manager.clear_tree(self)
        Todo_manager.load_task(self)


    def export_file(self):
        file_path = filedialog.asksaveasfilename(title = 'Select Data File To Export.',filetypes=[("Json files","*.json")])
        if file_path:
            with open(self.file_path,'r+') as file:
                self.data = json.load(file)
            
            with open(file_path,'w') as write:
                json.dump(self.data, write, indent = 4)

        user_path = filedialog.asksaveasfilename(title = 'Select User File To Export.',filetypes=[("Json files","*.json")])
        if user_path:
            with open(self.user_file_path,'r+') as file:
                self.data = json.load(file)
            
            with open(user_path,'w') as write:
                json.dump(self.data, write, indent = 4)
    
    def get_graph(self):
        with open(self.file_path, 'r+') as read:
            self.data = json.load(read)

            mylabels =["uncomplete_task","complete_task"]
            y = np.array([len(self.data["task_list"][self.inx][self.user]),len(self.data["complete_task"][self.inx][self.user])])
            fig, ax = plt.subplots()
            ax.set_title('complete and incomplete task')
            plt.pie(y, labels = mylabels,autopct='%1.2f%%')
            plt.show()
        

    def get_graph7days(self):
        with open(self.file_path, 'r+') as read:
            self.data = json.load(read)
            mylabels = {}
            mylabels2 = {}
            for i in range(7):
                today = DT.date.today()
                days_ago = today - DT.timedelta(days=i)
                mylabels[(days_ago.strftime("%#m/%#d/%y"))]=0
                mylabels2[(days_ago.strftime("%#m/%#d/%y"))]=0
                for y in range(len(self.data["complete_task"][self.inx][self.user])):
                    if days_ago.strftime("%#m/%#d/%y") in self.data["complete_task"][self.inx][self.user][y]['Date']:
                        mylabels[(days_ago.strftime("%#m/%#d/%y"))] += 1
                for x in range(len(self.data["task_list"][self.inx][self.user])):
                    if days_ago.strftime("%#m/%#d/%y") in self.data["task_list"][self.inx][self.user][x]['Date']:
                        mylabels2[(days_ago.strftime("%#m/%#d/%y"))] += 1


            names = list(mylabels.keys())
            names2 = list(mylabels2.keys())
            values = list(mylabels.values())
            values2 = list(mylabels2.values())
            
            x = np.arange(len(names))  # the label locations
            width = 0.35  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(x - width/2, values, width, label='Complete_task')
            rects2 = ax.bar(x + width/2, values2, width, label='Incomeplete_task')

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_ylabel('Tasks')
            ax.set_title('ALL TASKS IN 7 DAYs AGO')
            ax.set_xticks(x, names)
            ax.legend()

            ax.bar_label(rects1, padding=3)
            ax.bar_label(rects2, padding=3)

            fig.tight_layout()

            plt.show()

    def get_graph3(self):
        with open(self.file_path, 'r+') as read:

            self.data = json.load(read)
            #sorted_date = sorted(self.data["complete_task"][self.inx][self.user], key=lambda x: datetime.strptime(x['Date'], ('%m/%d/%y')))
            today = DT.date.today()
            month_now = today.strftime("%Y,%#m")
            
            year_now = today.strftime("%Y")
            month_now = today.strftime("%#m")
            mr = monthrange(int(year_now),int(month_now))
            mylabels = {}
            mylabels2 = {}

            #All_days = self.data["task_list"][self.inx][self.user][0]['Date'] - self.data["task_list"][self.inx][self.user][len-1]['Date']
            for x in range(1,int(mr[1])+1):
                mylabels[x]=0
                for i in range(len(self.data["complete_task"][self.inx][self.user])):
                    month = self.data["complete_task"][self.inx][self.user][i]['Date']
                    m = month.split("/") 
                    if str(x) == m[1] and today.strftime("%#m") == m[0]:
                        mylabels[x]+= 1
            
            for x in range(1,int(mr[1])+1):
                mylabels2[x]=0
                for i in range(len(self.data["task_list"][self.inx][self.user])):
                    month = self.data["task_list"][self.inx][self.user][i]['Date']
                    m = month.split("/") 
                    if str(x) == m[1] and today.strftime("%#m") == m[0]:
                        mylabels2[x]+= 1

            fig, ax = plt.subplots()
            ax.set_ylabel('Tasks')
            ax.set_xlabel('Days')
            values = list(mylabels.values())
            values2 = list(mylabels2.values())  
            sum1 = np.array(values)
            sum2 = np.array(values2)
            ax.set_title('Tasks in 1 month')
            #plt.legend(['complete_task','uncomplete_task'], loc='upper right')
            plt.plot(sum1, color = 'b',label = "complete_task")
            plt.plot(sum2, color = 'r',label = "incomplete_task")
            plt.legend()
            plt.show()
  

        


        


def main():
    root = tk.Tk() 
    app =GuiApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()