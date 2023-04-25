import shutil
source_file = open('data.json', 'rb')
dest_file = open('data_cpy.json', 'wb')

shutil.copyfileobj(source_file, dest_file)