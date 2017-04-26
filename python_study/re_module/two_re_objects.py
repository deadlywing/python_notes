"""
the following source is from :
https://docs.python.org/3.5/library/re.html#regular-expression-objects
http://www.cnblogs.com/fkissx/p/3932841.html


I.Regular Expression Objects
Compiled regular expression objects support the following methods and attributes:
1.  regex.search(string[, pos[, endpos]])
Scan through string looking for the first location where this regular expression produces a match, and return a corresponding match object

notes on optional parameters:
The optional second parameter pos gives an index in the string where the search is to start; it defaults to 0
the '^' pattern character matches at the real beginning of the string and at positions just after a newline, but not necessarily at the index where the search is to start.
endpos limits how far the string will be searched.so only the characters from pos to endpos - 1 will be searched for a match

2.  regex.match(string[, pos[, endpos]])
If zero or more characters at the beginning of string match this regular expression, return a corresponding match object

The optional pos and endpos parameters have the same meaning as for the search() method.

If you want to locate a match anywhere in string, use search() instead

3.  regex.fullmatch(string[, pos[, endpos]])
If the whole string matches this regular expression, return a corresponding match object.

The optional pos and endpos parameters have the same meaning as for the search() method.

4.  others
regex.split(string, maxsplit=0)
Identical to the split() function, using the compiled pattern.

regex.findall(string[, pos[, endpos]])
Similar to the findall() function, using the compiled pattern, but also accepts optional pos and endpos parameters that limit the search region like for match().

regex.finditer(string[, pos[, endpos]])
Similar to the finditer() function, using the compiled pattern, but also accepts optional pos and endpos parameters that limit the search region like for match().

regex.sub(repl, string, count=0)
Identical to the sub() function, using the compiled pattern.

regex.subn(repl, string, count=0)
Identical to the subn() function, using the compiled pattern.

regex.flags
The regex matching flags. This is a combination of the flags given to compile(), any (?...) inline flags in the pattern, and implicit flags such as UNICODE if the pattern is a Unicode string.

regex.groups
The number of capturing groups in the pattern.

regex.groupindex
A dictionary mapping any symbolic group names defined by (?P<id>) to group numbers. The dictionary is empty if no symbolic groups were used in the pattern.

regex.pattern
The pattern string from which the RE object was compiled.





II.Match Objects
Match objects always have a boolean value of True.

1.  match.expand(template)
Return the string obtained by doing backslash substitution on the template string template, as done by the sub() method.

2.  match.group([group1, ...])
If there is a single argument, the result is a single string; if there are multiple arguments, the result is a tuple with one item per argument. Without arguments, group1 defaults to zero (the whole match is returned).
 If a group is contained in a part of the pattern that matched multiple times, the last match is returned.

3.  match.groups(default=None)
Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern. The default argument is used for groups that did not participate in the match; it defaults to None.

4.  match.groupdict(default=None)
Return a dictionary containing all the named subgroups of the match, keyed by the subgroup name. The default argument is used for groups that did not participate in the match; it defaults to None. For example:

5.  match.start([group])
    match.end([group])
Return the indices of the start and end of the substring matched by group; group defaults to zero (meaning the whole matched substring). Return -1 if group exists but did not contribute to the match. For a match object m, and a group g that did contribute to the match, the substring matched by group g (equivalent to m.group(g)) is m.string[m.start(g):m.end(g)]
Besides, m.start(group) will equal m.end(group) if group matched a null string

6.  match.span([group])
For a match m, return the 2-tuple (m.start(group), m.end(group)). Note that if group did not contribute to the match, this is (-1, -1). group defaults to zero, the entire match.

7.  match.pos
The value of pos which was passed to the search() or match() method of a regex object. This is the index into the string at which the RE engine started looking for a match.

8.  match.endpos
The value of endpos which was passed to the search() or match() method of a regex object. This is the index into the string beyond which the RE engine will not go.

9.  match.lastindex
The integer index of the last matched capturing group, or None if no group was matched at all.

For example, the expressions (a)b, ((a)(b)), and ((ab)) will have lastindex == 1 if applied to the string 'ab', while the expression (a)(b) will have lastindex == 2, if applied to the same string.

10. match.lastgroup
The name of the last matched capturing group, or None if the group didn’t have a name, or if no group was matched at all.

11.  match.re
The regular expression object whose match() or search() method produced this match instance.

12.  match.string
The string passed to match() or search().
"""

import re

# 1.examples of Regular Expression Objects

# regex.search()
# patten = re.compile('d')
# print(patten.search("dog"))
# print(patten.search('dog', pos=1))

# regex.match()
# patten = re.compile('o', flags=re.I)
# print(patten.flags)
# print(patten.match('dog'))
# print(patten.match('dog', pos=1))

# regex.fullmatch
# pattern = re.compile("(o[gh])")
# print(pattern.groups)
# print(pattern.groupindex)
# print(pattern.pattern)
# print(pattern.fullmatch("dog"))  # No match as "o" is not at the start of "dog".
# print(pattern.fullmatch("ogre"))  # No match as not the full string matches.
# print(pattern.fullmatch("doggie", 1, 3))  # Matches within given limits.

# print some regex attributes
# pattern = re.compile(r'def\s+(?P<group1>a+)\s*\(\s*\):')
# print(pattern.flags)
# print(pattern.pattern)
# print(pattern.groupindex)
# print(pattern.groups)
# print(pattern.sub(r'static PyObject*\npy_\1(void)\n{', 'def myfunc():'))


# examples of  Match Objects
# example info
pattern = re.compile(r'<p.*?>#(\d*)(\w+) (\w+)(?P<sign>.*)#.*?', flags=re.I | re.M)
strs = "<p style='font-family:arial;color:red;font-size:20px;'>#6748hello word!#6748</p>"
Match = pattern.match(strs)

# some Match Object's attr and method
print(Match.expand(r'\2 \3 \4 \1'))  # also can change the interval " "
print(Match.group())  # the entire matched strings
print(Match.group(1, 2))
print(Match.pos)
print(Match.endpos)
print(Match.lastindex)  # compare with following m.lastindex
print(Match.lastgroup)
print(Match.re)
print(Match.string)
# a group matches multiple times
m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
print(m.group(1))
# match.groupdict() only return named group
print(Match.groupdict())
m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', "Malcolm Reynolds")
print(m.groupdict())
# match.start() and match.end()
print(Match.start(2))
print(Match.end(2))
# return -1 if group not matched
m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.lastindex)  # compare with the above Match.lastindex
print(m.start(2))
print(m.end(2))
# match.span()
print(Match.span())
print(Match.span(2))
