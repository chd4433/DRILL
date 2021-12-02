import pickle

# data = [1,2,3,4]
#
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data,f)
#
# with open('data.pickle', 'rb') as f:
#     read_data = pickle.load(f)
#
#
# print(type(read_data))
# print(read_data)

class npc:
    def __init__(self, name,x,y):
        self.name,self.x,self.y, = name,x,y
yuri = npc('yuri', 100,200)

with open('yuri.pickle', 'wb') as f:
    pickle.dump(yuri,f)

with open('yuri.pickle', 'rb') as f:
    read_yuri = pickle.load(f)

print(read_yuri)