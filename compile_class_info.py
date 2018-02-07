import pandas as pd
import json
import numpy
CamelCount = 0
SpaceCount = 0

def main():
    filenames = collect_csv_files()
    CheckedFiles = read_csv(filenames)
    student_data = cat_data(CheckedFiles)
    write_data(student_data)
    #STDOUT
    print(CamelCount)

def collect_csv_files():
    import glob
    filelist = glob.glob('*.csv')
    #make JSON here before I remove anything
    write_JSONs(filelist)
    if 'mlp6.csv' in filelist:
        filelist.remove('mlp6.csv')
    if 'everyone.csv' in filelist:
        filelist.remove('everyone.csv')
    return filelist

def read_csv(filenames):
    global CamelCount
    global SpaceCount
    for files in filenames:
        temp = pd.read_csv(files,delimiter=',')
        NoSpaces = check_no_spaces(temp.columns[4:5].values[0])
        Camels = check_camel_case(temp.columns[4:5].values[0])
       # if NoSpaces == False or Camels == False:
           ##Uncomment to throw out csv files that have false from the cases
        #    filenames.remove(files)
        if Camels == True:
            CamelCount += 1
        if NoSpaces == True:
            SpaceCount += 1
    return filenames

def check_no_spaces(teamname):
    count = 0
    lastchar = len(teamname)-1
    for i,character in enumerate(teamname):
        if count == 0:
            if character.isspace() == False: #if this is not a space (so beginning of word)
                count += 1 #add 1 to count (so we know we're in the word)
        if count == 1:
            if character.isspace() ==True: #once we detect word, if there is a space
                count += 1 #add 1 so now we have count=2
            if i == lastchar:
                return True #don't care about last character whether space or not
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
        elif count == 0 and character.isdigit()==True: # this is a number
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

def cat_data(CheckedFiles):
    FullList = [] #initiate
    cols = ['First Name','Last Name','NET ID','Git User','Team']
    for files in CheckedFiles:
        temp = pd.read_csv(files,header=None)
        FullList.append(temp)
    CatFullList = pd.concat(FullList,axis=0,ignore_index=True)
    CatFullList.columns = cols
    return CatFullList

def write_data(CatList):
    #CSV
    EveryoneFile = ('~/bme590s18_lecture03/everyone.csv')
    CatList.to_csv(EveryoneFile,index=None)

def write_JSONs(totalFiles):
    labels = ['First Name','Last Name','NET ID','Git User','Team']
    data = dict.fromkeys(labels)
    for files in totalFiles:
        temp = pd.read_csv(files,delimiter=',')
        NetID = temp.columns[2:3].values[0]
        #OutputFile = ('~/bme590s18_lecture03/'+NetID+'.json')
        OutputFile = NetID+'.json'
        for i,tag in enumerate(labels):
            data[labels[i]] = temp.columns[i:i+1].values[0]
        with open(OutputFile,'w') as outfile:
            json.dump(data,outfile)

if __name__ == "__main__":
    main()
