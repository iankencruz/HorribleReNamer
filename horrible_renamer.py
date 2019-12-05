#Batch Renames Horrible subs videos to remove "[HorribleSubs]" in file name
#Instructions
#   1. Make sure python is installed in your computer
#   2. Copy and Paste this file into target folder
#   3. Right click and select "Open with" then select python
#   4. Move to next folder then just double click


import os

directory = "M:\Media\Anime"






def main():

    # Preset selections 
    try:
        print("Select which tag to clear...")
        print("1. HorribleSubs")
        print("2. Kaya")
        print("3. Cleo")
        print("4. Custom?")
        user_input = input("Select Choice...")

        val = int(user_input)                                               #Store input to integer
        print("Input is {}".format(user_input))
        if (val == 1):
            title = "HorribleSubs"
        elif (val == 2):
            title = "Kaya"
        elif (val == 3):
            title = "Cleo"
        elif (val == 4):
            title = input("Input Text to replace: ")                        #Custom Tag
    except ValueError:
        print("Not a valid input! Try again")



    #  Try Walking through folders
    for root, dirs, files in os.walk(directory):
        for name in files:
            if ('[{}]'.format(title) in name):                              #Only iterate through files with tag
                file_name, file_ext = os.path.splitext(name)                #Split from extension
                f_tag, f_title = file_name.split('[{}]'.format(title))      #seperate [HorribleSubs] from name
                
                #Get all necessary file paths
                try:
                    old_name = '{}\{}{}'.format(root, file_name, file_ext) #Store old name
                    new_name = '{}\{}{}'.format(root, f_title, file_ext)   #Create New Name
                    os.rename(old_name, new_name)                          #Renaming
                except FileNotFoundError:
                    print("ERROR: Name does not match")                    #Error check




if __name__ == "__main__": 
    main()