# urop

All python codes are written under python version 3.7.2 

The "course_classes.py" defines classes for courses and basic requirement such as the pool requirements.

The "fit_requirement.py" implements the algorithms to fit each requirement defined in "course_classes.py"

The "course_dict.py" consists of all the courses offered by school. For now, it has only some of the courses.

The "curriculum_capture.py" defines two classes: Requirements, which is used to construct the whole requirement. And Curriculum, which maintain the status of each courses(available, excluded etc)

The "course_selection.py" is the main program and you can run it to generate a schedule. It takes all the requirements and the student profile(hard-coded for now) and generate the schedule based on the requirments.

The "scheduling.py" implements the course scheduling algorithm. For now it only has one algorithm, that is evenly distribute the workload for each semester.

The "rule_base_predictor.py" is the association rule based predictor. It has a rule_base_predictor class which does the prediction.

Although the system is functioning. It is still far from complete, A lot of amending and improvement are needed to make it more robust and more generic. Good Luck!