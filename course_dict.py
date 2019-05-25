# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:20:33 2019

@author: qchen
"""
from course_classes import course
cd = {'MATH1013': course('MATH1013','A',3,[],[]),
      'MATH1014': course('MATH1014','A',3,[['MATH1013']],[]),
      'MATH1023': course('MATH1023','A',3,[],[]),
      'MATH1024': course('MATH1024','A',3,[['MATH1023']],[]),
      'MATH2111': course('MATH2111','A',3,[['MATH1014']],[]),
      'MATH2411': course('MATH2411','A',4,[['MATH1014']],['ELEC2600']),
      'ELEC1100': course('ELEC1100','A',4,[],[]),
      'ELEC2600': course('ELEC2600','F',4,[['MATH1014']],['MATH2411']),
      
      'LANG1002S': course('LANG1002S','A',3,[],[]),
      'LANG1003S': course('LANG1003S','A',3,[['LANG1002S']],[]),     
      'LANG2030': course('LANG2030','A',3,[['LANG1003S']],[]), 
      'LANG4030': course('LANG4030','A',3,[['LANG2030']],[]), 
      'LANG1118': course('LANG1118','A',3,[],[]),
      
      'COMP1021': course('COMP1021','A',3,[],[]),
      'COMP1942': course('COMP1942','S',3,[],[]),
      'COMP2011': course('COMP2011','A',4,[['COMP1021']],['COMP2012H']), 
      'COMP2012': course('COMP2012','A',4,[['COMP2011']],['COMP2012H']), 
      'COMP2012H': course('COMP2012H','A',5,[['COMP1021']],['COMP2011','COMP2012']), 
      'COMP2611': course('COMP2611','A',4,[['COMP2011','COMP2012'],['COMP2012H']],[]), 
      'COMP2711': course('COMP2711','A',3,[],['COMP2711H']), 
      'COMP2711H': course('COMP2711H','A',3,[],['COMP2711']),       
      'COMP3111': course('COMP3111','A',4,[['COMP2012']],[]), 
      'COMP3511': course('COMP3511','A',3,[['COMP2611']],[]), 
      'COMP3711': course('COMP3711','A',3,[['COMP2011','COMP2711']],['COMP3711H']), 
      'COMP3711H': course('COMP3711H','F',3,[['COMP2011','COMP2711']],['COMP3711']), 

      'HUMA1000': course('HUMA1000','A',3,[],[]),
      'HUMA1001': course('HUMA1001','A',3,[],[]),
      'HUMA1010': course('HUMA1010','A',3,[],[]),
      'HUMA1020': course('HUMA1020','A',3,[],[]),
      'HUMA1720': course('HUMA1720','A',3,[],[]),
      'HUMA1300': course('HUMA1300','A',3,[],[]),
      'HUMA1440': course('HUMA1440','A',3,[],[]),
      'HUMA1620': course('HUMA1620','A',3,[],[]),
      'HUMA1650': course('HUMA1650','A',3,[],[]),
      'HUMA1810': course('HUMA1810','A',3,[],[]),

      'ECON2103': course('ECON2103','A',3,[],['SOSC1440']),
      'ECON2123': course('ECON2123','A',3,[],['SOSC1440']),
      'SOSC1440': course('SOSC1440','A',3,[],['ECON2103']),
      'ENVR1050': course('ENVR1050','A',3,[],['ENVR1050']),
      'SOSC1960': course('SOSC1960','A',3,[],[]),
      'SOSC1350': course('SOSC1350','A',3,[],[]),
      'FINA1303': course('FINA1303','A',3,[],[]),
      'ISOM1090': course('ISOM1090','A',3,[],[]),

      'PHYS1003': course('PHYS1003','A',3,[],[]),
      'PHYS1112': course('PHYS1112','A',3,[],['PHYS1312']),
      'PHYS1114': course('PHYS1114','A',3,[],[]),
      'PHYS1312': course('PHYS1312','A',3,[],['PHYS1112']),     
      'CENG1600': course('CENG1600','A',3,[],[]),     
      'CHEM1004': course('CHEM1004','A',3,[],[]),     
      'CIVL1140': course('CHEM1140','A',3,[],[]),     
      'CIVL1160': course('CHEM1160','A',3,[],[]),     

      'COMP2021': course('COMP2021','A',3,[['COMP1021']],[]), 
      'COMP3211': course('COMP3211','A',3,[['COMP2012']],[]), 
      'COMP4211': course('COMP4211','A',3,[['COMP2012','ELEC2600'],['COMP2012','MATH2411']],['COMP4331']), 
      'COMP4221': course('COMP4221','A',3,[['COMP3211','COMP2012H']],[]), 
      'COMP3311': course('COMP3311','A',3,[['COMP2012']],[]), 
      'COMP4331': course('COMP4331','A',3,[['COMP2012']],['COMP4211']), 
      'COMP4332': course('COMP4332','A',3,[['COMP4331']],['COMP4211']), 
      'COMP4411': course('COMP4411','A',3,[['COMP2011','COMP3711'],['COMP2012','COMP3711']],[]), 
      'COMP4441': course('COMP4441','A',3,[['COMP2011'],['COMP2012'],['COMP2012H']],[]), 
      'COMP4451': course('COMP4451','A',3,[['COMP4411']],[]), 
      'COMP4511': course('COMP4511','S',3,[['COMP3511','COMP4621']],[]),
      'COMP4621': course('COMP4621','S',3,[['COMP3511']],[]),
      'COMP4641': course('COMP4641','S',3,[['COMP2011','MATH2111'],['COMP2012H','MATH2111']],[]),
      'COMP4901J': course('COMP4901J','A',3,[['COMP2012'],['COMP2012H']],[])
      }