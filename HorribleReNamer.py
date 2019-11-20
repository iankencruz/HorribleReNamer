import os

directory = os.getcwd()




def main():
    print("Main Function")

    for f in os.listdir(directory):
        file_name, file_ext = os.path.splitext(f)
        
        try:
            h_sub, f_title = file_name.split('] ')
        
            #Get all necessary file paths
            old_name = '{}\{}{}'.format(directory, file_name, file_ext)
            new_name = '{}\{}{}'.format(directory, f_title, file_ext)
            os.rename(old_name,new_name)
        except:
            print("ERROR: Name does not match")








if __name__ == "__main__": 
    main()