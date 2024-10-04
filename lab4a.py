#!/usr/bin/env python3

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/10/03

def join_sets(s1, s2):
    return s1 | s2

def match_sets(s1, s2):
    return s1 & s2

def diff_sets(s1, s2):
    return s1 ^ s2

if __name__ == '__main__':
    set1 = set(range(1, 10))
    set2 = set(range(5, 15))

    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))

