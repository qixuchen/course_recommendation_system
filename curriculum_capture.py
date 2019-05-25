# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:23:17 2019

@author: qchen
"""

from course_classes import *

class requirement:
    def __init__(self,curriculum,num_credits,c_set,p_dict,m_dict,e_dict):
        '''
        graduation requirement capture
        
        curriculum: dict of all the courses offered by school
        num_credits: total credits needed to graduation
        c_set: course must taken to graduate
        p_dict: dictionaries of requirements that can be captrued by 'pool' structure
        m_dict: ------------------------------------------------- by 'module' structure
        e_dict: ------------------------------------------------- by 'elective' structure
        '''
        self.curriculum=curriculum
        self.num_credits= num_credits
        self.c_set=c_set
        self.p_dict = p_dict
        self.m_dict = m_dict
        self.e_dict = e_dict
        
    def setup(self,circumstance):
        '''
        set up the requirement based on taken course upon creation
        '''
        # update credits
        course_taken = circumstance.taken
        for i in course_taken:
            self.num_credits -= self.curriculum[i].credit
        
        # update mandatory course list
        self.c_set -= course_taken
        
        # update pools
        for i in self.p_dict.keys():
            
            pool_course_taken = self.p_dict[i].course_set.intersection(course_taken)
            for j in pool_course_taken:
                self.p_dict[i].total_credit -= self.curriculum[j].credit
            
            if (self.p_dict[i].total_credit<=0):#already fulfilled
                self.p_dict[i].fulfilled =True
                continue
            
            self.p_dict[i].course_set -= course_taken
            self.p_dict[i].course_set -= circumstance.excluded

        # update modules
        for i in self.m_dict.keys():
            rm_path=[]
            for j in range(len(self.m_dict[i].path)):
                if(course_taken.issuperset(self.m_dict[i].path[j])):#already fulfilled
                    self.m_dict[i].fulfilled=True
                    break
                if(self.m_dict[i].path[j].isdisjoint(circumstance.excluded)==False):
                    rm_path.append(j)
                    continue
                self.m_dict[i].path[j] -= course_taken
            for p in range(len(rm_path)-1,-1,-1):
                self.m_dict[i].path.remove(self.m_dict[i].path[rm_path[p]])
        # update electives
        # count how many elective course already taken
        # and delete them from areas        
        for i in self.e_dict.keys():
            for j in range(len(self.e_dict[i].areas)):
                course_from_area = course_taken.intersection(self.e_dict[i].areas[j])
                self.e_dict[i].course_num[j]=len(course_from_area)
                self.e_dict[i].areas[j] -= course_from_area
                    
                
                
                
    def update(self,course):
        '''
        update the requirement of a course if selected
        '''
        c = set({course})
        c_e = set(self.curriculum[course].exclusion)
        
        # update mandatory course set 
        self.num_credits -= self.curriculum[course].credit
        self.c_set -= c;
         
        # update pool---------
        for i in self.p_dict:
            if (self.p_dict[i].fulfilled == False):
                if(course in self.p_dict[i].course_set):
                    self.p_dict[i].total_credit -= self.curriculum[course].credit            
                    if (self.p_dict[i].total_credit<=0):#already fulfilled
                        self.p_dict[i].fulfilled =True
                        break     #under the assumption that one course can't be used
                                  #two CCC requirement
                    self.p_dict[i].course_set -= c
                    self.p_dict[i].course_set -= c_e
        # update pool-----------
        
        # update module---------
        for i in self.m_dict.keys():
            rm_path=[]
            if(self.m_dict[i].fulfilled == False):
                for j in range(len(self.m_dict[i].path)):
                    if(c.issuperset(self.m_dict[i].path[j])):#fulfilled
                        self.m_dict[i].fulfilled=True
                        break
                    if(self.m_dict[i].path[j].isdisjoint(c_e)==False):
                        rm_path.append(j)
                        continue
                    self.m_dict[i].path[j] -= c
            for p in range(len(rm_path)-1,-1,-1):
                self.m_dict[i].path.remove(self.m_dict[i].path[rm_path[p]])             
        # update module----------
                
        # update electives---------
        for i in self.e_dict.keys():
            for j in range(len(self.e_dict[i].areas)):
                course_from_area = c.intersection(self.e_dict[i].areas[j])
                self.e_dict[i].course_num[j]+=len(course_from_area)
                self.e_dict[i].areas[j] -= course_from_area  
                self.e_dict[i].areas[j] -= c_e.intersection(self.e_dict[i].areas[j])        

                
class circumstance:
    def __init__(self,curriculum,taken):
        '''
        THe curcumstance of a student
        
        curriculum: dict of all the courses offered by school
        taken: courses the student already taken
        excluded: course that are exclusion of some of the taken course
        selected: courses that will be selected
        '''
        self.curriculum=curriculum
        self.taken = taken
        self.excluded=set()
        self.exclusion_setup()
        self.selected = set()
        
    def available(self,course_name):
        '''
        Check the availability of a course
        '''
        if (course_name in self.taken):
            return False
        if (course_name in self.excluded):
            return False
        if (course_name in self.selected):
            return False
        return True
    
    def add(self,course):
        '''
        add a course to the selected list
        '''
        self.selected.add(course)
        for i in self.curriculum[course].exclusion:
            self.excluded.add(i)
    
    def exclusion_setup(self):
        '''
        Called in __init__ to set up exclusion set
        '''
        for c in self.taken:
            for e in self.curriculum[c].exclusion:
                self.excluded.add(e)
    
    def is_excluded(self,course_name):
        return (course_name in self.excluded)
                 
        