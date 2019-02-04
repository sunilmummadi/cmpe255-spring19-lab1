#!/usr/bin/env python
# coding: utf-8

# In[1]:


users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

for i in users:
    i['friends']=0
    count=0
    for x in friendship:
        if x[0]== i["id"] or x[1]== i["id"]:
            count +=1
    i['friends']=count
        
def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    # TODO
    for i in users:
        if i['name'] == user:
            print(i["friends"])

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    # TOOD
    sorted_users=sorted(users, key = lambda p: p['friends'],reverse=True)
    for i in sorted_users:
            print(i["name"] , i["friends"] )


# In[2]:


num_friends("Thor")


# In[3]:


sort_by_num_friends()


# In[ ]:




