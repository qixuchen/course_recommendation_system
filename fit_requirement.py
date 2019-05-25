# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:49:22 2019

@author: qchen
"""
import copy
from rule_base_predictor import rule_base_predictor

def fit_basic_requirement(R,C):
    '''
    select all the courses in c_set of requirement
    
    R: requirement
    C: circumstance
    '''
    course_set = copy.deepcopy(R.c_set)
    for i in course_set:
        C.add(i)
        R.update(i)
        
        
        
        
def fit_pool_requirement(R,C,stuinfo):
    '''
    This function tries to fit all pool requirements
    '''
    def sort_score(val):# this function sort the courses by its scores
        return val[1]
    
    pool_dict = R.p_dict #pool_dict is the dict of all pools
    for i in pool_dict.keys():
        if(pool_dict[i].fulfilled==False):
            scores=[]   #scores is the list of (course, score) tuple
            for course in pool_dict[i].course_set:
                success,grad,conf = predict(stuinfo,course)
                if(success!= False):
                    score=grad*conf
                    scores.append((course,score))
            scores.sort(key=sort_score,reverse=True)
                
            j=0; # j is the current course index
            while(pool_dict[i].fulfilled ==False and j<len(scores)): #add courses until it is fulfilled
                course, score = scores[j]
                if(C.available(course)):
                    C.add(course)
                    R.update(course)

                j +=1
            
    
    
def fit_module_requirement(R,C,stuinfo):
    '''
    This function tries to fit all the module requirements
    '''
    module_dict = copy.deepcopy(R.m_dict) #module_dict is the dict of all modules
    for i in module_dict.keys():                           
        if(module_dict[i].fulfilled==False):
            max_score = 0.0
            max_path = -1
            c_set=set()
            for j in range(len(module_dict[i].path)): #predict the score along each path
                score=0.0
                path_credit=0
                for course in module_dict[i].path[j]: #predict the grad of a course in this path
                    success,grad,conf = predict(stuinfo,course)
                    if(success==False): #if prediction unsuccessful, we won't choose this path for now
                        score=-1
                        break
                    score += grad * conf * R.curriculum[course].credit
                    path_credit+=R.curriculum[course].credit
                score /= (path_credit*1.0)
                if (score>max_score):
                    max_score = score
                    max_path=j
            if (max_path != -1):
                for course in module_dict[i].path[max_path]:
                    c_set.add(course)
                for i in c_set:
                    C.add(i)
                    R.update(i)

def fit_elective_requirement(R,C,stuinfo):
    '''
    This function tries to fit all the elective requirements
    '''
    def sort_score(val):# this function sort the courses by its scores
        return val[1]
    
    def e_predict(course,course_set):
        '''
        predict the score of a course. The score take consider in the other elective prerequiste
        '''
        nonlocal R
        nonlocal C
        nonlocal stuinfo

        success, grade,conf = predict(stuinfo,course)
        if(success==False):
            return (False,0,0,[])
        total_score = grade*conf*R.curriculum[course].credit
        total_credit =  R.curriculum[course].credit
        if( len(R.curriculum[course].prerequisite)==0):
            return(True,total_score,total_credit,[])
        pre_List=[]
        path_score = -1
        path_credit = 0

        for pre_path in R.curriculum[course].prerequisite:
            this_path_list = []
            score = 0
            credit = 0
            for pre in pre_path:
                if(pre in course_set):  # the prerequisite is one of the electives,
                    s,g,c = predict(stuinfo,pre)
                    if(s==False):
                        score = -2
                        credit =1
                        break
                    this_path_list.append(pre)
                    score += g*c*R.curriculum[pre].credit
                    credit+= R.curriculum[pre].credit
            if(credit == 0):
                path_score =0
            elif(score * 1.0 /credit > path_score):
                path_score = score * 1.0 /credit
                pre_List= copy.deepcopy(this_path_list)
                path_credit = credit
        if(path_score<0): #no path available, course cant be chosen
            return (False,0,0,[])
        total_credit += path_credit
        total_score += path_score * path_credit
        return(True,total_score,total_credit,pre_List)
    
    def add_prereq(R,C,pre_List):
        '''
        This function adds all the prerequiste of the elective course to the list
        '''
        for pre in pre_List:
            if(pre in course_set and C.available(pre)):
                C.add(pre)
                R.update(pre)
                
            
                
    e_dict = R.e_dict
    for i in e_dict.keys():
        if(e_dict[i].fulfilled==False):
            course_set = e_dict[i].course_set
            scores = []
            for area in e_dict[i].areas: # this two-level for loop get scores for each course
                for course in area:
                    success,total_score,total_credit,pre_List = e_predict(course,course_set)
                    if(success):
                        scores.append((course,total_score/total_credit,pre_List))
            scores.sort(key=sort_score,reverse=True)
            #keep update until requirement met
            j=0
            while((max(e_dict[i].course_num)<e_dict[i].num1 or sum(e_dict[i].course_num)<e_dict[i].total_num) and j<len(scores)):
                course,_,pre_List = scores[j]
                if(C.available(course)):
                    C.add(course)
                    R.update(course)
                    add_prereq(R,C,pre_List)
                j+=1;
            
            

def predict(stuinfo,course):
    result = rule_base_predictor(stuinfo,course)
    if (float(result[2])==0.0):
        return (False,0.0,0.0)
    else:
        grad_dict = {'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0.0}
        return (True,grad_dict[result[0]],float(result[2]))