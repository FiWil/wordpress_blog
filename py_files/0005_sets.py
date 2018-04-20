
# coding: utf-8

# # Sets
# 
# Sets are unordered collections of unique values. Common uses include membership testing, finding overlaps and differences between sets, and removing duplicates from a sequence. 
# 
# Sets, like dictionaries, are defined using curly brackets{}.

# ## Creating sets
# 
# Creating a set directly:

# In[11]:


my_set = {'a','e','i','o','u'}
print (my_set)


# Creating a set from a list:

# In[12]:


my_list = ['a','e','i','o','u']
my_set = set(my_list)
print (my_set)


# Creating an empty set. This cannot be done simply with {}
my_set = set()
print (my_set)
# ## Adding to a set and removing duplicates

# Adding one element to a set:

# In[13]:


my_set.add('y')
print (my_set)


# Adding multiple elements to a set (note that the set has no duplication of entries already present; sets automatically remove duplicate items):

# In[14]:


my_set.update(['x','z','a','x'])
print (my_set)


# ## Analysing the intersection between sets
# 
# Sets may be used to explore the intersection betwen sets. There are usually two orms of syntax which may be used, both of which are given in the examples below.

# In[15]:


set1 = {'a','b','c','d','e','f'}
set2 = {'a','e','i','o','u'}


# The difference between two sets:

# In[16]:


print ('difference')
print (set1.difference(set2))
print (set1 - set2)


# The intersection between two sets:

# In[17]:


print ('Intersection')
print (set1.intersection(set2))
print (set1 & set2)


# Is a subset? Is set 2 wholly included in set 1?

# In[18]:


print ('Is subset?')
print (set1.issubset(set2))
print (set1 <= set2)


# Is a superset? Does set 1 wholly include set 2?

# In[19]:


print ('Is superset?')
print (set1.issuperset(set2))
print (set1 >= set2)


# The union between two sets:

# In[20]:


print ('Union')
print (set1.union(set2))
print (set1 | set2)


# Symmetric difference: in either but not both (equivalent to xor)

# In[21]:


print ('Symmetric difference')
print (set1.symmetric_difference(set2))
print (set1 ^ set2)

