# how to read that file????

def read_file(path):
    try:
        
        with open(path) as file:
            contents = file.read()

        contents += ' - has been read'

        with open('output.txt', 'w') as outputfile:
            outputfile.write(contents)

        print('write complete')

    # what happens if you uncomment below?
    # assert False

    finally:

        print('Always see this')


try:
    read_file('howdy.txt')

except FileNotFoundError as error:

    print('handled error')
    print(error)

except:

    print('something else went wrong')