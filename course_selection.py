# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:14:47 2019

@author: qchen
"""

from course_classes import course,pool,module,elective
from curriculum_capture import requirement,circumstance
from course_dict import cd
from fit_requirement import *
from scheduling import cal_priority, scheduling

stuinfo = {'Gender':'M','Citizenship':'China','MATH1013':'A-','COMP1021':'A','LANG1002S':'B','LANG1003S':'B-',
           'ELEC1100':'A+','PHYS1112':'A','COMP1942':'A','COMP2021':'A','MATH1014':'A+','COMP2711':'A+','SOSC1960':'A','Cumulative GPA':3.91}

huma_ssc_p = pool(set({'HUMA1000'}),3)
huma_p = pool(set({'HUMA1001','HUMA1010','HUMA1020','HUMA1720','HUMA1300','HUMA1440','HUMA1620','HUMA1650','HUMA1810'}),3)
sosc_p = pool(set({'SOSC1440','SOSC1350','ECON2103','ENVR1050','FINA1303','ISOM1090'}),3)
sosc_ssc_p = pool(set({'SOSC1960'}),3)
st_p = pool(set({'PHYS1112','PHYS1114','PHYS1312','CENG1600','CHEM1004','CIVL1140','CIVL1160'}),3)
st_ssc_p = pool(set({'PHYS1003'}),3)

math1_m = module(set({'MATH1013','MATH1023'}),[{'MATH1013'},{'MATH1023'}])
math2_m = module(set({'MATH1014','MATH1024'}),[{'MATH1014'},{'MATH1024'}])
algo_m = module(set({'COMP3711','COMP3711H'}),[{'COMP3711'},{'COMP3711H'}])

probMath_m = module(set({'MATH2411','ELEC2600'}),[{'MATH2411'},{'ELEC2600'}])
c_m = module(set({'COMP2011','COMP2012','COMP2012H'}),[{'COMP2011','COMP2012'},{'COMP2012H'}])
c_e = elective(set({'COMP2021','COMP3211','COMP4211','COMP4221','COMP3311','COMP4331','COMP4332','COMP4411','COMP4441','COMP4451' 'COMP4451', 'COMP4511','COMP4621','COMP4641','COMP4901J'}),
               [set({'COMP3211','COMP4211','COMP4221','COMP4901J'}),set({'COMP3311','COMP4331','COMP4332'}),set({'COMP4411','COMP4441','COMP4451'}),set({'COMP4621','COMP4641','COMP2021'})],5,3)
course_set = set({'LANG1002S','LANG1003S','LANG2030','LANG4030','MATH2111','COMP2611','COMP2711','COMP3111','COMP3511','LANG1118'})

p_dict = {'huma_p':huma_p,'sosc_p':sosc_p,'st_p':st_p,'huma_ssc_p':huma_ssc_p,'sosc_ssc_p':sosc_ssc_p,'st_ssc_p':st_ssc_p}
m_dict = {'math1_m':math1_m,'math2_m':math2_m,'probMath_m':probMath_m,'c_m':c_m,'algo_m':algo_m}
e_dict={'c_e':c_e}
R = requirement(cd,80,course_set,p_dict,m_dict,e_dict)

taken =  set({'MATH1013','COMP1021','LANG1002S','LANG1003S',
           'ELEC1100','PHYS1112','COMP1942','COMP2021','MATH1014','COMP2711','SOSC1960'})
C = circumstance(cd,taken)

#selection
R.setup(C)
fit_basic_requirement(R,C)
fit_pool_requirement(R,C,stuinfo)
fit_module_requirement(R,C,stuinfo)
fit_elective_requirement(R,C,stuinfo)

#scheduling
priority = cal_priority(C.selected,cd)
scheduling(stuinfo,priority, cd,4)