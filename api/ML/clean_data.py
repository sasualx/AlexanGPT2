import re
lyrics = []
with open('clean_data.txt', 'r') as f:
    lyrics = f.readlines()

train = []
test = []

for i in range(0,len(lyrics),200):
    train += lyrics[i:i+190]
    test += lyrics[i+190:i+200]

with open('train.txt','w') as f:
    f.writelines(train)

with open('test.txt', 'w') as f:
    f.writelines(test)
