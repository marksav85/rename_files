import os
import string
def rename_files():
    #get filenames from folder
    file_list = os.listdir(r"D:\OneDrive\Programming and Data Science\Projects\rename_files\pictures")
    #print (file_list)
    saved_path = os.getcwd()
    print ("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\marks\Desktop\Intro to Programming\prank")
    print (os.getcwd())
    

