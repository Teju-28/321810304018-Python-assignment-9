#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a Python program to read an entire text file

# In[ ]:


def file_read(fname):
    txt=open(fname)
    print(txt.read())
file_read('python.txt')


# ## 2.Write a python program to read first n lines of a file.

# In[ ]:


def file_read_from_head(fname,nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f,nlines):
                        print(line)
file_read_from_head('python.txt',2)


# ## 3.Write a python program to append text to a file and display the text

# In[ ]:


def read(a):
        from itertools import islice
        with open(a,"w") as file:
                file.write("Python Exercises\n")
                file.write("Java Exercises")
        txt=open(a)
        print(txt.read())
read('python.txt')


# ## 4.Write a python program to read last n lines of a file.

# In[ ]:


def LastNLines(f,n):
    with open(f) as file:
        print('Last',n,"lines from file:",f)
        for line in (file.readlines() [-n:]):
            print(line,end=' ')
name=input("enter the file name:" )
n=int(input("no of last lines to read:"))
try:
    LastNLines(name,n)
except:
    print("file error.....")


# ## 5.Write a python program to read a file line by line store it into a variable.

# In[ ]:


def read(a):
        with open (a) as file:
                cse=file.readlines()
                print(cse)
a=input("enter the file name:")
read(a)


# ## 6.Write a python program to read a file line by line and store it into a list.

# In[ ]:


def read(a):
        with open(a) as file:
                list=file.readlines()
                print(list)
a=input("enter the file name:")
read(a)

