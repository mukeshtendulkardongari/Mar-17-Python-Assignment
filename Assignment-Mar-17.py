# swapcase()

def my_swapcase(s):
    res=""
    for ch in s:
        if "A" <= ch <= "Z":
            res+=chr(ord(ch)+32)

        elif "a" <= ch <= "z":
            res+=chr(ord(ch)-32)
        
        else:
            res+=ch
    return res

s="ManJunaDH"
print(my_swapcase(s))
print(s.swapcase())

# output:
# mANjUNAdh
# mANjUNAdh


# strip()

def my_strip(s):
    start=0
    end=len(s)-1
    while start<end and s[start]==" ":
        start+=1
    while start<end and s[end]==" ":
        end-=1
    return s[start:end+1]

s="   manjunadh   "
print(99,my_strip(s),99)
print(99,s.strip(),99)        

# output:
# 99 manjunadh 99
# 99 manjunadh 99


# lstrip()

def my_lstrip(s):
    start=0

    while start<len(s) and s[start]==" ":
        start+=1
    return s[start:]

s="   manjunadh   "
print(99,my_lstrip(s),99)
print(99,s.lstrip(),99) 

# output:
# 99 manjunadh    99
# 99 manjunadh    99


# rstrip()


def my_rstrip(s):
    end=len(s)-1

    while end>=0 and s[end]==" ":
        end-=1
    return s[:end+1]

s="   manjunadh   "
print(99,my_rstrip(s),99)
print(99,s.rstrip(),99) 

# output:
# 99    manjunadh 99
# 99    manjunadh 99


# replace()

def my_replace(s, old, new):
    res=""
    i=0
    
    while i<len(s):
        if s[i:i+len(old)]==old:
            res+=new
            i+=len(old)
        else:
            res+=s[i]
            i+=1
    return res

s="python snake is not python lang"
print(my_replace(s,"python", "java"))

# output:
# java snake is not java lang