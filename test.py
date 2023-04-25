import os
import json, codecs



with open('data.json', 'r') as read:
            data = json.load(read)
        
            x = data['task_list']
            x.pop(0)
            
            print(x)

with open('data.json','w') as write:
            json.dump(x, write, indent = 4)


