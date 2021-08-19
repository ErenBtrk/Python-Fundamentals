import re

result = dir(re)
print(result)


# re module
str1 = "yarasa reis : alemlerin krali : 1993"

#re.findall()
result = re.findall("Yarasa",str1)
print(result)
result = len(result)
print(result)

#re.split()
result = re.split(" ",str1)
print(result)

#re.sub()
result = re.sub(" ","-",str1)
print(result)

#re.search()
result = re.search("Yarasa",str1)
print(result)

# result = result.span() #returns indexes of searching string chars
# print(result)
# result = result.start() #returns index of searching string's first char
# print(result)
# result = result.end() #returns index of searching string's last char
# print(result)
# result = result.group() #returns the string
# print(result)
# result = result.string # returns the string that we search on
# print(result)


# regular expressions

# '[]' expression
result = re.findall("[abc]",str1)
print(result)
result = re.findall("[alem]",str1)
print(result)
result = re.findall("[a-e]",str1)
print(result)
result = re.findall("[a-z]",str1)
print(result)
result = re.findall("[1-5]",str1)
print(result)
result = re.findall("[^abc]",str1)
print(result)
result = re.findall("[^0-9]",str1)
print(result)

# '.' expression

result = re.findall("...",str1)
print(result)
result = re.findall("ya..sa",str1)
print(result)


# '^' expression

result = re.findall("^a",str1)
print(result)
result = re.findall("^y",str1)
print(result)

# '$' expression

result = re.findall("1993$",str1)
print(result)

# '*' expression

result = re.findall("19*3",str1)
print(result)

# '+' expression

result = re.findall("18+3",str1)
print(result)

# '?' expression

result = re.findall("19?3",str1) 
print(result)

# '{}' expression

result = re.findall("9{2,3}",str1)
print(result)
result = re.findall("[0-9]{2}",str1)
print(result)

# '|' expression
result = re.findall("a|r",str1)
print(result)

# '()' expression
result = re.findall("(a|b|c)xz",str1)
print(result)

# '\' expression
result = re.findall("\$a",str1)
print(result)

# '\A' expression
result = re.findall("\Ayarasa",str1)
print(result)

# '\Z' expression
result = re.findall("1992\Z",str1)
print(result)

# '\b' #expression #searches char in every words of string
# '\B' #expression opposite of \b
# '\d' #expression same as [0-9]
# '\D' #expression same as [^0-9]
# '\s' #searchs white-space chars.
# '\S' #searchs chars except white-space
# '\w' #searchs alpha,digits and underscores
# '\W' #opposite of '\w'