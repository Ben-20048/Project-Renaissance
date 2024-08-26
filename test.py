mylist = [2,4,6,8,10]
newlist = []

for wall in mylist:
    print(wall)
    
#mylist = [wall + 1 for wall in mylist]
for wall in mylist:
    newlist.append(wall+1)
    
for wall in newlist:
    print(wall)