#!/usr/bin/env python
# coding: utf-8

# 1. Write four functions that directly mutate a list:
# 1. repeat(lst, n): Repeat lst n times.
# 2. add(lst, x): Adds x to the end of the lst.
# 3. remove(lst, m, n): Removes all elements between indices m and n
# inclusive in lst.
# 4. concat(lst, x): concatenates lst with x (another list).
# Examples
# lst = [1, 2, 3, 4]
# repeat(lst, 3) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# add(lst, 1) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1]
# remove(lst, 1, 12) ➞ [1]
# concat(lst, [3, 4]) ➞ [1, 3, 4]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


lst = [1, 2, 3, 4]

def repeat(in_num):
    global lst
    lst = lst*in_num
    return lst

def add(in_num):
    global lst
    lst.append(in_num)
    return lst

def remove(start,end):
    global lst
    for ele in lst[start:end+1]:
        lst.remove(ele)
    return lst

def concat(in_list):
    global lst
    lst = lst+in_list
    return lst

print(f'repeat(3) ➞ {repeat(3)}')
print(f'add(1) ➞ {add(1)}')
print(f'remove(lst, 1, 12) ➞ {remove(1,12)}')
print(f'concat([3, 4]) ➞ {concat([3, 4])}')


# 2. The classic game of Mastermind is played on a tray on which the
# Mastermind conceals a code and the Guesser has 10 tries to guess it. The
# code is a sequence of 4 (or 6, sometimes more) pegs of different colors. Each
# guess is a corresponding sequence of 4 (or more) pegs of different colors. A
# guess is &quot;correct&quot; when the color of every peg in the guess exactly matches
# the corresponding peg in the Mastermind&#39;s code.
# After each guess by the Guesser, the Mastermind will give a score comprising
# black &amp; white pegs, not arranged in any order:
# - Black peg == guess peg matches the color of a code peg in the same
# position.
# - White peg == guess peg matches the color of a code peg in another
# position.
# Create a function that takes two strings, code and guess as arguments, and
# returns the score in a dictionary.
# - The code and guess are strings of numeric digits
# - The color of the pegs are represented by numeric digits
# - no &quot;peg&quot; may be double-scored
# Examples
# guess_score(&quot;1423&quot;, &quot;5678&quot;) ➞ {&quot;black&quot;: 0, &quot;white&quot;: 0}
# 
# guess_score(&quot;1423&quot;, &quot;2222&quot;) ➞ {&quot;black&quot;: 1, &quot;white&quot;: 0}
# guess_score(&quot;1423&quot;, &quot;1234&quot;) ➞ {&quot;black&quot;: 1, &quot;white&quot;: 3}
# guess_score(&quot;1423&quot;, &quot;2211&quot;) ➞ {&quot;black&quot;: 0, &quot;white&quot;: 2}
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def guess_score(code,guess):
    output = {"black":0,"white":0}
    for ele in range(len(code)): 
        if code[ele] == guess[ele]:
            output['black'] += 1
        elif code[ele] in guess and ele != guess.index(code[ele]):
            output['white'] += 1
    print(f'guess_score{code,guess} ➞ {output}')
        
guess_score("1423", "5678")
guess_score("1423", "2222")
guess_score("1423", "1234") 
guess_score("1423", "2211")


# 3. Create a function that takes a list lst and a number N and returns a list of
# two integers from lst whose product equals N.
# Examples
# two_product([1, 2, -1, 4, 5], 20) ➞ [4, 5]
# two_product([1, 2, 3, 4, 5], 10) ➞ [2, 5]
# two_product([100, 12, 4, 1, 2], 15) ➞ None
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def two_product(in_list,in_num):
    output = None
    for num_1 in in_list:
        for num_2 in in_list:
            if num_1*num_2 == in_num:
                output = sorted([num_1,num_2])
                break
    print(f'two_product({in_list}) ➞ {output}')
    
two_product([1, 2, -1, 4, 5], 20)
two_product([1, 2, 3, 4, 5], 10)
two_product([100, 12, 4, 1, 2], 15)


# 4. In this challenge, sort a list containing a series of dates given as strings.
# Each date is given in the format DD-MM-YYYY_HH:MM:
# &quot;12-02-2012_13:44&quot;
# The priority of criteria used for sorting will be:
# - Year
# - Month
# - Day
# - Hours
# - Minutes
# Given a list lst and a string mode, implement a function that returns:
# - if mode is equal to &quot;ASC&quot;, the list lst sorted in ascending order.
# - if mode is equal to &quot;DSC&quot;, the list lst sorted in descending order.
# Examples
# sort_dates([&quot;10-02-2018_12:30&quot;, &quot;10-02-2016_12:30&quot;, &quot;10-02-2018_12:15&quot;],
# &quot;ASC&quot;) ➞ [&quot;10-02-2016_12:30&quot;, &quot;10-02-2018_12:15&quot;, &quot;10-02-2018_12:30&quot;]
# sort_dates([&quot;10-02-2018_12:30&quot;, &quot;10-02-2016_12:30&quot;, &quot;10-02-2018_12:15&quot;],
# &quot;DSC&quot;) ➞ [&quot;10-02-2018_12:30&quot;, &quot;10-02-2018_12:15&quot;, &quot;10-02-2016_12:30&quot;]
# 
# sort_dates([&quot;09-02-2000_10:03&quot;, &quot;10-02-2000_18:29&quot;, &quot;01-01-1999_00:55&quot;],
# &quot;ASC&quot;) ➞ [&quot;01-01-1999_00:55&quot;, &quot;09-02-2000_10:03&quot;, &quot;10-02-2000_18:29&quot;]
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


from datetime import datetime
def sort_dates(in_list,sort_by):
    in_list_clone = in_list.copy()
    in_list_unix = []
    for ele in in_list:
        in_list_unix.append(datetime.strptime(ele, "%d-%m-%Y_%H:%M").timestamp())
    in_list_unix = sorted(in_list_unix) if sort_by == 'ASC' else sorted(in_list_unix, reverse=True)
    output = []
    for ele in in_list_unix:
        output.append(datetime.fromtimestamp(ele).strftime("%d-%m-%Y_%H:%M"))
    print(f'sort_dates{in_list,sort_by}➞ {output}')

sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC")
sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC")
sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC")


# 5. Write a function that selects all words that have all the same vowels (in any
# order and/or number) as the first word, including the first word.
# Examples
# same_vowel_group([&quot;toe&quot;, &quot;ocelot&quot;, &quot;maniac&quot;]) ➞ [&quot;toe&quot;, &quot;ocelot&quot;]
# same_vowel_group([&quot;many&quot;, &quot;carriage&quot;, &quot;emit&quot;, &quot;apricot&quot;, &quot;animal&quot;]) ➞
# [&quot;many&quot;]
# same_vowel_group([&quot;hoops&quot;, &quot;chuff&quot;, &quot;bot&quot;, &quot;bottom&quot;]) ➞ [&quot;hoops&quot;, &quot;bot&quot;,
# &quot;bottom&quot;]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def same_vowel_group(in_list):
    vowels = ['a','e','i','o','u']
    first_ele = sorted(set([x for x in in_list[0] if x in vowels]))
    output = []
    for ele in range(0,len(in_list)):
        vowels_in_word = [x for x in in_list[ele] if x in first_ele]
        if sorted(first_ele) == sorted(set(vowels_in_word)):
            output.append(in_list[ele])
    print(f'same_vowel_group({in_list}) ➞ {output}')
    
same_vowel_group(["toe", "ocelot", "maniac"])
same_vowel_group(["many", "carriage", "emit", "apricot", "animal"])
same_vowel_group(["hoops", "chuff", "bot", "bottom"])


# 6. Create a function that takes a list of more than three numbers and returns
# the Least Common Multiple (LCM).
# Examples
# lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520
# lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340
# lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[6]:


import math
def lcm_of_list(in_list):
    output = in_list[0]
    for ele in range(1,len(in_list)):
        output = (output*in_list[ele])//math.gcd(output,in_list[ele])
    print(f'lcm_of_list({in_list}) ➞ {output}')
    
lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lcm_of_list([13, 6, 17, 18, 19, 20, 37])
lcm_of_list([44, 64, 12, 17, 65])

