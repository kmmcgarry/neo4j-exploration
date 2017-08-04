import csv

def execute(i_file, o_file):
    out_file = open(o_file,'w')
    with open(i_file,"rU") as csvfile:
        spamreader= csv.reader(csvfile,delimiter=",")
        for row in spamreader:
            gvkey = row[0]
            conml = row[1]
            naics = row[2]
            tic = row[3]
            exchg = row[4]
            adr = row[5]
            atq = row[6]
            saleq = row[7]
            annualSale = row[8]
            year = row[9]
            runDateTime = row[10]
            finalRank = row[11]
            finalRankYr = row[12]
            busdesc = row[13]

            # create features for entity
            if gvkey != "GVKEY":
                tic = tic.replace(".","")
                for i in tic:
                    try:
                        i = int(i)
                        tic = 'NULL'
                        break
                    except:
                        continue
                if tic != 'NULL':
                    features = 'gvkey: "' + gvkey + '", conml: "' + conml + '", naics: "' + naics + '", exchg:"' + exchg + '"'
                    # + ', adr: ' + adr + ', atq:' + atq + ', saleq: ' +saleq + ', annualSale: ' + annualSale + ', year: ' + year + ', runDateTime: ' + runDateTime + ', finalRank: ' + finalRank + ', finalRankYr' + finalRankYr + ', busdesc: '  + busdesc
                    entity = 'CREATE (' + tic + ':Company {' + features + '})'
                    out_file.write(entity + '\n')
    return "done"

def getComp(i_file,o_file):
    companies = []
    out_file = open(o_file,'w')
    with open(i_file,"rU") as csvfile:

        spamreader= csv.reader(csvfile,delimiter=",")
        for row in spamreader:
            conml = row[1]

            if conml not in companies:
                companies.append(conml)

    out_file.write(str(companies))
    out_file.close()




# execute("C:\Users\mcgark9\Documents\main-project\data\Top3000.csv", "C:\Users\mcgark9\Documents\main-project\data\compEntity.txt")
getComp("C:\Users\mcgark9\Documents\main-project\data\Top3000.csv", "C:\Users\mcgark9\Documents\main-project\data\companies.txt")
