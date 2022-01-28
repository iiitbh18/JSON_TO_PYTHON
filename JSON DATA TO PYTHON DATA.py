#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
response = requests.get('https://codingninjas.in/api/v3/courses')
print(response.status_code)
print(response.encoding)
#print(response.text)
print(response.url)
#print(response.headers)


# In[5]:


import json
json_data = '{"student": "Mohit"}'
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))
print(python_data['student'])


# In[9]:


json_data  = '{"roll_number" : null}'
python_data = json.loads(json_data)
print(python_data['roll_number'])
print(type(python_data['roll_number']))


# In[23]:


"""
JSON -------------------------------------------> PYTHON
object                  dict
number                  int ,float
boolean                 boolean
string                  str
array                   list,tuple
null                    None
"""


# In[29]:


json_data = '{"student" : {"Name" : "Mohit", "Roll_NO" : 101}}'
python_data = json.loads(json_data)
student_details = python_data['student']
print(student_details['Name'])
print(student_details['Roll_NO'])


# In[33]:


import json

array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
print(type(data))
print(type(data['fruits']))
for i in data['fruits']:
  print(i)


# In[ ]:




