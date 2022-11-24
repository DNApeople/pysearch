import os

global path_with_file

# the location where you want to save the file (change as you pleas) eg- "H:\FoldeName" + "FileName.txt"
path_with_file = "F:\pysearch/"+ 'urls.txt'

def make_a_file():
    ALL_urls  = input('paste all urls:\t')
    List_urls = ALL_urls.split(' ')
    
    with open(path_with_file ,'w+') as url_file:
        for items in List_urls:
            url_file.write('%s\n' %items)
            print("saved url:")
        url_file.close()

def search():
    with open(path_with_file) as search_urls:
        for line in search_urls:
            start = 'start ' + line
            os.system(start)

def rep():
    make_a_file()
    ask_for_search = input('\nDo you require immediat search ? [y,n]\t')
    ask_ = ask_for_search.lower()
    if ask_ == 'y':
        search()
    else:
        exit()

    repeat = input('Do you want to repeat ? [y,n]')
    repeat_ = repeat.lower()

    if repeat_ == "y":
        rep()
    else:
        exit()

rep()

        