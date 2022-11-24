import os 


# if you have a text file (option: 1)
def I_have_a_file():
    path_with_folder = input("path to folder:\t")
    file_name = input("name of file:\t")
    
    # Using readlines()
    youre_url_file = open(path_with_folder + file_name, 'r')
    Lines = youre_url_file.readlines()
    
    # Strips the newline character
    for line in Lines:
        start = 'start ' + line
        os.system(start)       
       

def make_a_new_file():
    # the location where you want to save the file (change as you pleas) eg- "H:\FoldeName" + "FileName.txt".
    # below is default location.
    path_for_file = "F:\pysearch/"+ "urls.txt"

    ALL_urls = input('past urls:\t') 
    List_urls = ALL_urls.split(' ')

    with open(path_for_file ,'w+') as url_file:
        for items in List_urls:
            url_file.write('%s\n' %items)
            print("saved url:")
        url_file.close()
    
    opt = input('i - instant search\ns - save file for later\n')
    
    if opt == 'i':
        with open(path_for_file, 'r') as search_urls:
            for line in search_urls:
                start = 'start ' + line
                os.system(start)
    elif opt == 's':
        print('\nOK !!!!')


def ask_for_option():
    # do you have a file ? / do you want to make one ?
    ask_for_option = input('1 - I have a url file.\n2 - Instantly create a file\n')
    if ask_for_option == str(1):
        I_have_a_file()
    elif ask_for_option == str(2):
        make_a_new_file()


def rep():
    ask_for_option()
    repeat = input("Do you want to repear ? [y/n]")
    repear_ = repeat.lower()
    if repear_ == 'y':
        rep()
rep()