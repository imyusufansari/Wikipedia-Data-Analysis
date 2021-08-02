import os
count = 1
for i in os.listdir():
    os.rename(i,'page_'+str(count)+ '.txt')
    count+=1
