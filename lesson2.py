from copy import deepcopy

# # set collection
# set = {44,"fff", (22)}
# print(type(set))
# print(set)
# list_set = list(set)

student= {
    "name": "Aimarzhan",
    "age": 21,
    "year" : None
    "subject": {
        "math":(80,47,68,100),
        "python": (67,88,97,82),
        "html": (67,80,97,82),
        "css" : (67,88,92,88),
    },
    "total": None
}
student["year"]=2022 - student['aga']
for key ,value in student["subject"].items() :
    student['subject'][key] = sum(value)/ len(value)
    print(student)