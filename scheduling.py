# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:01:41 2019

@author: qchen
"""
from fit_requirement import predict
def check_satisfy_pre(major,ccc,course):
    for i in major:
        if(course == i[0]):
            return False
    for i in ccc:
        if(course == i[0]):
            return False
    return True
def recur_prior(cd, priority, course_map, cur_course, cur_prior):
    i = course_map[cur_course]
    c,p=priority[i]
    if(p>cur_prior): 
        return
    else:
        priority[i] = (c,cur_prior)
    for pre_path in cd[c].prerequisite:
        for pre in pre_path:
            if (pre in course_map.keys()):
                recur_prior(cd,priority,course_map,pre,cur_prior+1)
            

def cal_priority(course_set,cd):
    '''
    This function calculates priority for each course
    The course with the most course following it(the prerequisite of prerequisite)
    has the highest priority, CCC has priority 0.
    course_set: set of course to compute priority
    cd: dictionary of courses
    '''
    priority = []
    course_map={}
    index = 0
    for course in course_set:
        priority.append((course,-1))
        course_map[course] = index
        index+=1
        
    for i in range(len(priority)):
        c, p = priority[i]
        if(p==-1):
            if(len(cd[c].prerequisite)==0): #an CCC/equavilent
                priority[i]=(c,0)
            else:
                cur_course=c
                cur_prior=1
                recur_prior(cd, priority, course_map,cur_course,cur_prior)
    return priority
                
def scheduling(stuinfo,priority_list,cd,sem_remain):
    '''
    This function schedules the list of course into a valid time table
    priority_list: (course_name,priority) tuples
    cd: course dictionary
    sem_remain: how many semesters remain before graduation
    '''
    from copy import deepcopy
    from math import ceil,floor
    term_dict = {0:'F',1:'S'}
    def get_priority(val):
        return val[1]
    
    major = []
    ccc = []
    for i in range(len(priority_list)):
        c,p = priority_list[i]
        if(p==0):
            ccc.append((c,p))
        else:
            major.append((c,p))
    course_per_sem = ceil(len(priority_list)/sem_remain)
    major_per_sem = course_per_sem-floor(len(ccc)/sem_remain)
    time_table = []
    cur_sem = sem_remain%2  # cur_sem indicates Spring or Fall, 0 is fall
    for t in range(sem_remain):
        schedule = set({})
        m = deepcopy(major)
        for i in range(len(m)): #update priority to record term info
            c, p = m[i]
            if (cd[c].term == term_dict[cur_sem]):
                m[i] = (c,p+0.3)
            elif (cd[c].term == term_dict[1-cur_sem]):
                m[i] = (c,-1)
                
        m.sort(key=get_priority,reverse = True) # sort the priority list
        count = 0
        index = 0
        while(count<major_per_sem and index < len(m)): # select major courses
            c, p = m[index]
            if( p!= -1):
                available = True
                for pre_path in cd[c].prerequisite:
                    for pre in pre_path:
                        if(check_satisfy_pre(major,ccc,pre) == False):
                            available = False
                            break;
                if(available) :
                    _,grad,conf = predict(stuinfo,c)
                    schedule.add((c,grad,conf))
                    #schedule.add(c)
                    count+=1
            index+=1
        for i in schedule:   #update course list
            for j in range(len(major)):
                if(major[j][0]==i[0]):
                    major.remove(major[j])
                    break
        while(count < course_per_sem): #select ccc courses
            if(len(ccc)<=0):
                break
            else:
                c, p = ccc[0]
                _,grad,conf = predict(stuinfo,c)
                schedule.add((c,grad,conf))
                #schedule.add(c)
                count +=1
                ccc.remove(ccc[0])
        time_table.append(schedule)
        cur_sem = 1-cur_sem
    print(time_table)
                
                
                
                
                
                
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    



    