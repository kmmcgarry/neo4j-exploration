import re

def cleanhtml(raw_html,outFile):
    table_cleaner = re.compile('(?i)<table.*?</table>')
    regexs = [table_cleaner, '<.*?>', '\n', '\t', '&nbsp', '&#']
    for regex in regexs:
        raw_html = re.sub(regex, ' ', raw_html)

    print type(raw_html)
    out_file = open(outFile,"w")
    out_file.write(raw_html)
    print "done"
    return raw_html

#in_file = open("C:/dev/EDO-Intern-Project/Kristen/nlp/data/appl-secfiling.htm","r")
#raw_html = in_file.read()
#cleanhtml(raw_html,"C:/dev/EDO-Intern-Project/Kristen/nlp/data/appl-secfiling.txt")
