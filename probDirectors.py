import csv
import re
def getDirectors():
    out_file = open("C:\Users\mcgark9\Documents\main-project\directors.txt","w")
    with open("C:\Users\mcgark9\Documents\main-project\ProblemDirectors.csv","rU") as csvfile:
        spamreader= csv.reader(csvfile,delimiter=",")
        ProblemDirectors = []
        entity = ""
        pattern = "^[a-zA-Z'-]+, .*$"
        # 1328 rows
        for row in spamreader:
            if row != "DirLName, DirFName":
                try:
                    f_name = row[1]
                    l_name = row[2]
                    name = (l_name + ", " + f_name)
                    if re.match(pattern,name,flags=0) != None:
                        if name not in ProblemDirectors:
                            ProblemDirectors.append(name)
                            identifier = l_name + f_name[0]
                            entity = ('CREATE (' + identifier + ':Person {name: "' + name + '", fName:"' + f_name + '", lName:"' + l_name + '"})')
                            out_file.write((entity+"\n"))
                    else:
                        print name

                except (IndexError):
                    continue
    print (len(ProblemDirectors))
    return "Done"

# Get directors with cleaned data, v2
def getDirectorsClean():
    out_file = open("C:\Users\mcgark9\Documents\main-project\data\DirectorEntity_v2.txt","w")
    with open("C:\Users\mcgark9\Documents\main-project\data\ProblemDirectors_v2.csv","rU") as csvfile:
        spamreader= csv.reader(csvfile,delimiter=",")
        ProblemDirectors = []
        entity = ""
        uniqueId = []
        # 1328 rows
        for row in spamreader:
                try:
                    f_name = row[1]
                    l_name = row[2]
                    if (f_name != "DirFName") and (f_name != ""):
                        name = (l_name + ", " + f_name)
                        if name not in ProblemDirectors:
                            ProblemDirectors.append(name)
                            identifier = str(row[0])
                            entityId = ((l_name.replace(" ","")).replace("'","")).replace("-","")
                            i=0
                            myBool = True
                            while (myBool == True):
                                if entityId in uniqueId:
                                    entityId = entityId + f_name[i]
                                    i+=1
                                else:
                                    myBool= False
                                    break
                            uniqueId.append(entityId)
                            entity = ('CREATE (' + entityId + ':Person {name: "' + name + '", fName:"' + f_name + '", lName:"' + l_name + '", identifier:"' + identifier + '"})')
                            out_file.write((entity+"\n"))
                except (IndexError):
                    continue
    return "Done"
#getDirectors()
getDirectorsClean()
