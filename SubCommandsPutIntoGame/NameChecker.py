import pickle
file = 'Halogen.txt'
gudlist = []
Points = 654432
Name = input("Please input a 5 character name: ")
def checknames(Name):
    if len(Name) == 5:
        return (Name)
    else:
       Name = input("Please input a 5 character name this time: ")
       checknames(Name)




namepoints = {'Name': Name, 'Points': Points}
with open (file, 'rb') as file_handler:
    gudlist = pickle.load(file_handler)
print(gudlist)
gudlist.append(namepoints)
checknames(Name)
with open(file,'wb') as file_handler:
    pickle.dump((gudlist),(file_handler))

    
