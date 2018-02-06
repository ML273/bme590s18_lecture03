import pandas as pd
import numpy

def main():
    filenames = collect_csv_files()
    print(filenames)
    read_csv(filenames)
    student_data = cat_data()
    write_data()

def collect_csv_files():
    import glob
    print(globals()) #DELETE LATER
    return glob.glob('*.csv')
# Am I correct in thinking that filenames is a variable with all the csv files?

def read_csv(filenames):
    for files in filenames
        temp = pd.read_csv(files,delimiter=',')
        print(type(temp))
        check_no_spaces(temp[5])
        check_camel_case(temp[5])
        #throw out csv files that have false from the cases
        #and create a list of the names of files that failed

def check_no_spaces(teamname):
    count = 0
    lastchar = len(teamname)-1
    for i,character in enumerate(teamname):
        while count == 0:
            if character.isspace() == False: #if this is not a space (so beginning of word)
                count += 1 #add 1 to count (so we know we're in the word)
        while count == 1:
            if character.isspace() ==True: #once we detect word, if there is a space
                count += 1 #add 1 so now we have count=2
        if count ==2 and character.isspace() == False:
            return False
        elif count ==2 and i == lastchar:
            return True

def check_camel_case(teamname):
    #assuming camel case allows for ONLY letters and numbers (no spaces or underscores)
    #where if there is a letter first, it must be uppercase
    #but if there is a number first, that is okay
    count = 0
    for character in teamname:
        # This block of if cases will ignore leading spaces
        if count == 0 and character.isupper()==True: #this is a letter that is uppercase
            count +=1
        elif count == 0 and character.digit()==True: # this is a number
            count +=1
        elif count == 0 and character.islower()==True: # this is a letter that is lowercase
            count +=1
        elif count == 0 and character.isspace()==False: #not a space or any of the above
            return False
        if count == 1 and character.isspace() ==True:
            #logic: assume a space after having one alphanumeric character means end of teamname
                #even if it is not the end, check_no_spaces() will return False
            return True
        if count == 1 and character.isalnum() ==False:
            #So if it's not the end of the word, and there is a non-alphanumeric character, then false. Else True.
            return False
        else:
            return True

def cat_data():
    pass

def write_():
    # CSV or JSON
    pass

if __name__ == "__main__":
    main()
