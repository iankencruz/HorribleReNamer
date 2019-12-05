#Batch Renames Horrible subs videos to remove "[HorribleSubs]" in file name
#Instructions
#   1. Make sure python is installed in your computer
#   2. Copy and Paste this file into target folder
#   3. Right click and select "Open with" then select python
#   4. Move to next folder then just double click


import os

directory = "M:\Media\Anime"






def main():
    
     
  





    # # Preset selections 
    # try:

    #     user_input = input("1. HorribleSubs \n2. Kaya \n3. Cleo \n4. Custom ")

    #     val = int(user_input)
    #     print("Input is {}".format(user_input))
    #     if (val == 1):
    #         title = "HorribleSubs"
    #     elif (val == 2):
    #         title = "Kaya"
    #     elif (val == 3):
    #         title = "Cleo"
    #     elif (val == 4):
    #         title = input("Input Text to replace: ")
    # except ValueError:
    #     print("Not a valid input! Try again")



    #  Try Walking through folders
    for root, dirs, files in os.walk(directory):
        for name in files:
            if ("[HorribleSubs]" in name):
                # print (name)
                file_name, file_ext = os.path.splitext(name)
                print("FileName: " + file_name)
                print ("FileExt: " + file_ext)

 

    

    # # walk through current directory of file
    # for f in os.listdir(directory):
    #     file_name, file_ext = os.path.splitext(f)       #split name from extension (filename & .mkv)
        
    #     try:
    #         h_sub, f_title = file_name.split('[{}]'.format(title))      #seperate [HorribleSubs] from name
        
    #         #Get all necessary file paths
    #         old_name = '{}\{}{}'.format(directory, file_name, file_ext) #Store old name
    #         new_name = '{}\{}{}'.format(directory, f_title, file_ext)   #Create New Name
    #         os.rename(old_name,new_name)                                #Rename
    #     except:
    #         print("ERROR: Name does not match")                         #Will Fail and print this if filename does not contain [HorribleSubs]








if __name__ == "__main__": 
    main()