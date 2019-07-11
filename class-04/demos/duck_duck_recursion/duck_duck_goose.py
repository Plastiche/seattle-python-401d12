from os import listdir
from os.path import isdir, abspath

continue_searching = True

def goose_check(folder):

    global continue_searching

    if not continue_searching:
        return
          
    try:
        with open(folder + '/duck.txt') as f:
            contents = f.read()
            print('duck contents', contents)
            if contents == 'goose':
                print(folder)
                continue_searching = False

    except FileNotFoundError:
  
        folder_path = abspath(folder)
        file_names = listdir(folder_path)
       
        for file_name in file_names:
            file_path = f'{folder_path}/{file_name}'
            if isdir(file_path):
                goose_check(file_path)


















def goose_check_old(folder):
    folder_path = abspath(folder)
    file_names = listdir(folder_path)
    for file_name in file_names:
        file_path = f'{folder_path}/{file_name}'
        if isdir(file_path):
            goose_check(file_path)
        elif file_name == 'duck.txt':
            with open(file_path) as f:
                contents = f.read()
                print(contents)
                if contents == 'goose':
                    print('*******************')
                    print(file_path)
                    print('*******************')
                
            

if __name__ == "__main__":
    goose_check('studs')

