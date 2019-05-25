# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:46:07 2019

@author: qchen
"""

class course:
    '''
    basic info of a course
    
    '''
    def __init__(self,name,term,credit,prerequisite,exclusion):
        '''
         name : name of the course, i.e 'MATH1013'
        term: term in which the course is offered, i.e "S"(spring), "F"(fall), "A"(all)
        credit: num of credit of the course
        prerequiste: set of the prerequisites of the course
        exclusion: set of exclusion of the course
        '''
        self.name = name
        self.term = term
        self.credit = credit
        self.prerequisite = prerequisite
        self.exclusion = exclusion
        
class pool:
    '''
    A pool which stores all the course could be used to fulfill a requirement
    i.e A huma pool stores all the huma ccc courses
    
    A pool will be fuifilled if fuifilled==True
    '''
    def __init__(self,course_set,total_credit):
        '''
         course_list: set of courses belong to the pool
         total_credit: num of credits needed from the pool to fulfill the requirement
        '''
        self.course_set = course_set
        self.total_credit = total_credit
        self.fulfilled = False
        
        
class module:
    '''
    A module stores all the possible combination which could be used 
    to fulfill a requirement
    i.e to fulfill c++ requirement, a student can take comp2011+2012 or comp2012h
    
    A module will be fuifilled if fuifilled==True
    '''
    def __init__(self,course_set,path):
        '''
        course list: list of all courses involved in this module
        path: list of all possible paths
        i.e c++ module has path [ {'COMP2011','COMP2012'},{'COMP2012H'} ] 
        '''
        self.course_set=course_set
        self.path = path
        self.fulfilled=False
        
    
class elective:
    '''
    A elective is used to catch the requirement of CSE electives
    
    '''
    
    def __init__(self,course_set,areas,total_num,num1):
        '''
        course_set: All courses in this elective
        areas: set of courses in different areas
        total_num:total number of courses needs to take from all the electives
        num1: num of course should take from major area 
        course_num: list of intergers indicating how many courses have been taken from each area
        '''
        self.course_set = course_set
        self.areas=areas
        self.total_num=total_num
        self.num1=num1
        self.fulfilled=False
        
        self.course_num=[];
        for i in range(len(areas)):
            self.course_num.append(0)
    
        
        
        
        
        
        
        
        
        
        
        
        
        