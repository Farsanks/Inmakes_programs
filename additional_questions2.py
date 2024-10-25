# famly=['farsan','aseena','shihab','riya','ransil','zayan']
# print(famly)
# new=[i for i in famly if 'r' in i]
# print(new)
# scores=[100,101,102,103,104,105,106,107,108,109,110]
# print(scores[2:6])
relation=("father","mother","sister","brother","son","daughter")
print(relation)
new=list(relation)
print(new)
new.append("uncle")
print(new)
new.insert(0,"grand father")
print(new)
relation=tuple(new)
print(relation)
print(new[6])