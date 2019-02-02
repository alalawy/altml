from sys import *

def altmlfile(filename, **altmlstate):

    altmlf = open(filename,"r+")

    altmlfRead = altmlf.read()

    altmlfSplit = altmlfRead.split()

    arrStyleCek = []

    tagTemp = []

    tagPosTmp = []

    codeList = []

    altmlfStrr = ""

    for code in range(len(altmlfSplit)):
        codeList.append(altmlfSplit[code])

    for x in range(len(altmlfSplit)):
        if altmlfSplit[x][-1] == "{": #tag awal
            tagTemp.append("<" + altmlfSplit[x][0:len(altmlfSplit[x])-1] + ">")
            tagPosTmp.append(x)

            if tagTemp[-1] == "<>":
                tagTemp.pop()
            
            #print(openTag)
        elif altmlfSplit[x][:1] == "}": #tag akhir
            if tagTemp[-1] == "</>":
                tagTemp.pop()
            #print(tagPosTmp[-1])
            if altmlfSplit[tagPosTmp[-1]+1][-1] == "[": 
                for a in range(tagPosTmp[-1],x):
                    if altmlfSplit[a][-1] == "[":
                        if altmlfSplit[a][0:len(altmlfSplit[a])-1] == "text":
                            for b in range(a+1,x):
                                if altmlfSplit[b][:1] != "]" and altmlfSplit[b] != "\\n" and altmlfSplit[b][0:2] != "{{":
                                    if altmlfSplit[b][-1] == "{":
                                        tagTemp.pop()
                                        tagTemp.pop()
                                        tagTemp.append(altmlfSplit[b] + " ")
                                    else:
                                        tagTemp.append(altmlfSplit[b] + " ")
                                elif altmlfSplit[b] == "\\n" :
                                    tagTemp.append("<br>")
                                elif altmlfSplit[b][0:2] == "{{":
                                    exec(altmlfSplit[b][2:-2])
                                    #tagTemp.append(str(altmlstate))
                                else:
                                    continue
                        elif altmlfSplit[a][0:len(altmlfSplit[a])-1] == "attr":
                            tagTempLast = tagTemp[-1][0:len(tagTemp[-1])-1]
                            tagTemp.pop()
                            tagTemp.append(tagTempLast)
                            for b in range(a+1,x):
                                if altmlfSplit[b][:1] != "]" and altmlfSplit[b][-1] != "{" and altmlfSplit[b][:1] != "}":
                                    tagTemp.append(" " + altmlfSplit[b])
                                elif altmlfSplit[b][:1] == "]":
                                    tagTemp.append(">")
                                    break
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue

            tagTemp.append("</" + codeList[tagPosTmp[-1]][0:len(codeList[tagPosTmp[-1]])-1] + ">")
            tagPosTmp.pop()
               
    for i in range(len(tagTemp)):
        altmlfStrr += tagTemp[i]

    return altmlfStrr