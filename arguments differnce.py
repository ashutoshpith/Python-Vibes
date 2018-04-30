
# coding: utf-8

# # Differnce between args and *args

# In[3]:


def a(arg, *args):
    print('Simple normal arg :', arg)
    for arg in args:
        print('Now *args :',arg)
a('India', 'Usa', 'England', 'Eroupe')


# # Use of **keyWordArgument

# In[10]:


def hello(**keywordargs):
    for key, value in keywordargs.items():
        print('{0} = {1}'.format(key, value))
hello(name='ashutosh')
hello(title='singh')


# # Example for *args

# In[16]:


def testa(a1, a2, a3):
    print('a1',a1)
    print('a2',a2)
    print('a3',a3)
args = ('two', 3, 5)
testa(*args)

