import os, shutil
path=r"" # place the directory path
file_name=os.listdir(path)
folder_name = ['word_file','image file','pdf file'] # change the folder name based on requirements
for loop in range(0,3): #size based on folder count
    if not os.path.exists(path + folder_name[loop]):
        os.makedirs(path + folder_name[loop])

for file in file_name:
    if ".docx" in file and not os.path.exists(path +"word_file/" + file):
        shutil.move(path +file ,path+ "word_file/" + file)
    elif ".jpg" in file and not os.path.exists(path +"image file/" + file):
        shutil.move(path +file ,path+ "image file/" + file)
    elif ".pdf" in file and not os.path.exists(path +"pdf file/" + file):
        shutil.move(path +file ,path+ "pdf file/" + file)
