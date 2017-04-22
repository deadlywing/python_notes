"""
re fundamental knowledge test
source : https://docs.python.org/3.5/library/re.html#re.X

1. re.compile(pattern, flags=0)
flag:
re.A --- re.ASCII
re.DEBUG
re.I --- re.IGNORECASE
re.M --- re.MULTILINE
re.S --- re.DOTALL
re.X ---- re.VERBOSE

prog = re.compile(pattern)
result = prog.match(string)
is equivalent to
result = re.match(pattern, string)

2.   re.search(pattern, string, flags=0)
Scan through string looking for the first location where the regular expression pattern produces a match,
and return a corresponding match object

3.    re.match(pattern, string, flags=0)
If zero or more characters at the beginning of string match the regular expression pattern,
return a corresponding match object

even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
If want to locate a match anywhere in string, use search() instead
compare re.search() vs. re.match()

4.    re.fullmatch(pattern, string, flags=0)
If the whole string matches the regular expression pattern, return a corresponding match object

5.    re.split(pattern, string, maxsplit=0, flags=0)
Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list.
If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.

6.  re.findall(pattern, string, flags=0)
Return all non-overlapping matches of pattern in string, as a list of strings.
If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group

7.  re.finditer(pattern, string, flags=0)

8.  re.sub(pattern, repl, string, count=0, flags=0)
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl
If the pattern isn’t found, string is returned unchanged.
Unmatched groups are replaced with an empty string.

repl can be a string or a function; if it is a string, any backslash escapes in it are processed
\g<name> will use the substring matched by the group named name, as defined by the (?P<name>...) syntax. \g<number> uses the corresponding group number; \g<2> is therefore equivalent to \2, but isn’t ambiguous in a replacement such as \g<2>0.
The backreference \g<0> substitutes in the entire substring matched by the RE.


If repl is a function, it is called for every non-overlapping occurrence of pattern. The function takes a single match object argument, and returns the replacement string

The optional argument count is the maximum number of pattern occurrences to be replaced; count must be a non-negative integer. If omitted or zero, all occurrences will be replaced
 Empty matches for the pattern are replaced only when not adjacent to a previous match, so sub('x*', '-', 'abc') returns '-a-b-c-'.

9.  re.subn(pattern, repl, string, count=0, flags=0)
Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made).

10. re.escape(pattern)
Escape all the characters in pattern except ASCII letters, numbers and '_'.

11. re.purge()
Clear the regular expression cache.

"""
import re

# compare re.match and re.search
# print(re.match('c', 'abc'))
# print(re.search('c', 'abc'))
# print(re.match('X', 'A\nB\nX', re.M))
# print(re.search('^X', 'A\nB\nX', re.M))



# print(re.match('..', 'abcdef'))
# r = re.match('(..)\w+?(.+)', 'abcdef')
# print(r.groups())
# print(re.search('..', 'abcdef'))
# print(re.search('(..)', 'abcdef'))
# r = re.search('(..)\w+?(.+)', 'abcdef')
# print(r.groups())





# have warning
# print(re.split('x*', 'axbc'))
# print(re.split('x+', 'axbc'))
# print(re.findall(r'\d+', 'one1two2three3'))



# compare following three examples
# s = "adfad asdfasdf asdfas asdfawef asd adsfas "
# print(re.findall(r'((\w+)\s+\w+)', s))
# print(re.findall(r'(\w+)\s+\w+', s))
# print(re.findall(r'\w+\s+\w+', s))





# re.sub() when repl is a string
# print(re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
#              r'static PyObject*\npy_\1(void)\n{',
#              'def myfunc():'))

# print(re.sub(r'def\s+(a+)\s*\(\s*\):',
#              r'static PyObject*\npy_\1(void)\n{',
#              'def myfunc():'))

# re.sub() when repl is a function
# def dashrepl(matchobj):
#     if matchobj.group(0) == '-':
#         return ' '
#     else:
#         return '-'


# print(re.sub('-{1,2}', dashrepl, 'pro----gram-files'))

# print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.I))


# If the pattern isn’t found, string is returned unchanged.
# Unmatched groups are replaced with an empty string.
# print(re.sub('x*', '-', 'abc'))
# print(re.sub("foo(?:b(ar)|baz)", "\\1", "foobaz123"))
# print(re.sub("foo(b(ar)|baz)", "\\1", "foobaz123"))


# re.subn()
# print(re.subn(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.I))
