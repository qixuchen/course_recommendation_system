# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:38:18 2018

@author: qchen
"""


def rule_base_predictor(stuInfo,course):
    import time
    import os.path
    import re
    targetFile= "dir_of_pre/"+course+"_predictor.txt"
    if(os.path.exists(targetFile)):
        file=open("dir_of_pre/"+course+"_predictor.txt","r")
        raw=file.read()
        file.close()
    else:
        return ["Invalid course name","0","0"]
        
    
    if "Cumulative GPA" in stuInfo:
        from math import floor
        CGA = float(stuInfo["Cumulative GPA"])
        stuInfo["Cumulative GPA"]=str((floor(CGA)+floor(float(CGA)+0.5))/2)
        
    for key in stuInfo.keys():
        if(re.match("\\w{3,4}\\d{3,4}",key)):
            if("A" in stuInfo[key]): stuInfo[key]="A"
            if("B" in stuInfo[key]): stuInfo[key]="B"
            if("C" in stuInfo[key]): stuInfo[key]="C"
            if("D" in stuInfo[key]): stuInfo[key]="D"

    rule_index = raw.split("__INDEX__")
    rulelist = rule_index[0].split(";")
    expr_list= [rule.split("-->") for rule in rulelist]
    
    rawindexlist = eval(rule_index[1])
    indexlist = [index.split(" || ") for index in rawindexlist]   
    indexfound =[]

        
    for i in range(len(indexlist)):
        if stuInfo.__contains__(indexlist[i][0]) and stuInfo[indexlist[i][0]] == indexlist[i][1]:
            indexfound += eval(indexlist[i][2])
            
    indexfound = sorted(set(indexfound))
    
    
    for i in indexfound:
        try:
            if eval(expr_list[i][0]):
                if ((expr_list[i][1][-2:-1]=="A") or (expr_list[i][1][-2:-1]=="B") or (expr_list[i][1][-2:-1]=="C") or (expr_list[i][1][-2:-1]=="D") or (expr_list[i][1][-2:-1]=="F")):
                    return [(expr_list[i][1][-2:-1]),expr_list[i][2],expr_list[i][3]]
        except KeyError:
            continue
    return ["Insufficent information to predict","0","0"]
