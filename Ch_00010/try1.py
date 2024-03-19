living_beings= {"Reptile":"Snake","mammal":"whale", "Other":"bird"}
new_dict = {kind.replace('a', '/a'): animal.replace('a', '/a') for kind, animal in living_beings.items()}
# new_dict: {"Reptile":"Sn/ake","m/amm/al":"wh/ale", "Other":"bird"}
print('Old Version:', living_beings)
print('New Version:', new_dict)
