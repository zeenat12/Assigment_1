#!/usr/bin/env python
# coding: utf-8

# Q.1 Create one variable containing following type of data
# (i)    string
# 
# (ii)	list
# 
# (iii)	float
# 
# (iv)	tuple

# In[81]:


#(i) string
str1 = 'Red'
print(str1)


# In[82]:


#(ii) list
lst = [1, 2, 5.6, 'PW skills']
print(lst)


# In[83]:


#(iii) float
x = 75.6
print(x)


# In[84]:


#(iv) tuple
tup1 = ('physics', 'chemistry', 1999, 2000)
print(tup1)


# Q2. Given are some following variables containing data:
# 
# (i)	var1 = ‘ ‘
# 
# (ii)	var2 = ‘[ DS , ML , Python]’
# 
# (iii)	var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# 
# (iv)	var4 = 1
# 
# What will be the data type of the above given variable.

# In[2]:


#(i)
var1 = ''


# In[6]:


type(var1)


# In[1]:


#(ii)
var2='[DS, ML, Python]'


# In[8]:


type(var2)


# In[10]:


#(iii)
var3 = ['DS', 'ML', 'Python']


# In[13]:


type(var3)


# In[14]:


#(iv)
var4 = 1


# In[15]:


type(var4)


# Q3. Explain the use of the following operators using an example:
# 
# (i)	/
# 
# (ii)	% 
# 
# (iii)	//
# 
# (iv)	**

# ### Arithmetic Operators
# (i)
# 
# |Operators|Meaning|
# |-|-|
# |**\** | Division operator to divide left hand operator by right handed operator.

# In[13]:


#Example
x = 90
y = 3
z = x/y
print(int(z))


# (ii)
# 
# |Operators|Meaning|
# |-|-|
# |**%** | Modulus operator to find remainder.

# In[8]:


#Example
x = 90
y = 3
z = x%y
print(int(z))


# (iii)
# 
# |Operators|Meaning|
# |-|-|
# |**//** | Floor division operator to find the quotient and remove the fractional.

# In[9]:


#Example
x = 90
y = 3
z = x//y
print(int(z))


# (iv)
# 
# |Operators|Meaning|
# |-|-|
# |** | Exponential operator to calculate power.
# 

# In[10]:


#Example
x = 90
y = 3
z = x**y
print(int(z))


# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the 
# element and its data type.

# In[19]:


lst1 = [23, 56, 78.67, 'red', 'blue', 45, 678, 34,78, 'purple']


# In[17]:


len(lst1)


# In[80]:


for x in lst1:
    print(x, type(x))


# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many 
# times it can be divisible.

# In[46]:


def count_divisions(a, b):
    count = 0
    while a % b == 0:
        a /= b
        count += 1
    return count


# In[47]:


number_a = 120
number_b = 5

divisions = count_divisions(number_a, number_b)

if divisions > 0:
    print(f'{number_a} is divisible by {number_b} and can be divided {divisions} times.')
else:
    print(f'{number_a} is not divisible by {number_b}.')


# Q.6 Create a list containing 25 int type data. Using for loop and if-else condition print if the element is 
# divisible by 3 or not.

# In[31]:


lst2 = [2, 3, 8, 10, 12, 16, 18, 20, 21, 24, 25, 27, 30, 32, 35, 37, 39, 40, 45, 49, 50, 51, 52, 58, 60]


# In[27]:


len(lst2)


# In[34]:


for x in lst2:
    if x%3==0:
        print('Divisible by 3')
    else:
        print('Not divisible by 3')


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing 
# this property.

# ### Mutable objects are those that allow to change their value or data in place without affecting the object’s identity.
# ### In contrast, immutable objects don’t allow this kind of operation. It's just have the option of creating new objects of the same type with different values.

# In[58]:


# Mutable object
# Example 1


# In[59]:


lst=[23, 56, 789, 'red', 'yellow']


# In[60]:


type(lst)


# In[61]:


lst[3] = 567


# In[62]:


lst


# In[63]:


# Mutable object
# Example 2


# In[64]:


my_dict = {'Name': 'Ramesh', 'age': 21, 'class': 'T.Y.Bsc'}


# In[65]:


type(my_dict)


# In[66]:


my_dict['age'] = 23


# In[57]:


my_dict


# In[67]:


# Immutable object
# Example 3


# In[68]:


my_str = 'Hello World'


# In[69]:


type(my_str)


# In[71]:


my_str[3] = 'r'


# In[76]:


# Immutable object
# Example 4


# In[77]:


tup1 = (12, 23.56, 'abc', 'xyz')


# In[78]:


type(tup1)


# In[79]:


tup1[2] = 100

