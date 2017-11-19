
# coding: utf-8

# While Loops in Python
# 
# simple example of using a while loop in python

# In[ ]:


i = 0
while(i < 21):
    i = i+1
    print(i)
    


# Temperature While Loop

# In[ ]:


temp = 250
while(temp > 212):
    temp = temp - 2
    print("the temperature is too hot!")
    print("it's at", temp)
   


# Using the Appending method of a list in a While Loop

# In[1]:


nums = list()
i = 4
while (i < 9):
    nums.append(i)
    i = i+2
print(nums)


# In[2]:


thirty = list()
i = 0
while (i < 31):
    thirty.append(i)
    i = i+1
print(thirty)


# While Loops using the Range Function

# In[3]:


nums = range(4,9,2)
print(list(nums))


# In[5]:


thirty = range(0,31,1)
print(list(thirty))


# In[6]:


list(range(10,0,-1))


# Create a list of boiling temperature going down 1 degree at a time until it no longer boils.

# In[10]:


boiling = list(range(275,211,-1))
print (boiling)


# Blastoff Timer 

# In[12]:


#Blastoff

for i in range(10,0, -1):
    print(i)
print("blastoff!")


# lines in a list

# In[3]:


lines = list() #create a new list
n = int(input("How many lines do you want to enter?")) #define n as an integer input from user 
for i in range(n):  #n is number of lines to input
    line = input("next line: ")  #line = variable that takes input of user's line
    lines.append(line)  #take the value of the line input and add it to the list of inputs the user entered
    
print("your lines were:") #check the user's lines.  
for line in lines:  #for loop to print all the lines in the list lines
    print(line)


# Monthly Activities

# In[4]:


monthly_activities = list() #create a list of monthly activites

n = int(input("how many activities do you have?"))
for i in range(n):
    
    activity = input("what activity this month? ")  #store an input activity into the variable activity
    monthly_activities.append(activity)  #store the input activity into a the list monthly activites
    
print("your activites are")
for activity in monthly_activities: 
    print(activity)



    


# input lines until user hits enter

# In[5]:


lines = list()  #create a list named:  lines
print('Enter lines of text.')   
print('enter an empty line to quit.')

line = input('next line: ')  #create a user input variable line

while line != '':  #while loop:  so long as the user input variable line doesn't blank
    lines.append(line) #append the list lines with the user input variable line
    line = input('next line: ')

print("your lines are:", lines)


# In[ ]:


lines = list()
print("enter your line")

line = input("enter your line: ")

while line != '':
    lines.append(line)
    line = (input('next line please: '))

