"""
sources from : https://docs.python.org/3.5/library/re.html#regular-expression-examples
some examples:
1.poker
2.phone number
3.Text Munging
4.Finding all Adverbs

"""
import random
import re


# a graceful display for match object
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


# valid = re.compile(r'^[a2-9tjqk]{5}$')
# print(displaymatch(valid.match("akt5q")))
# pair = re.compile(r".*(.).*\1")
# print(displaymatch(pair.match("717ak")))

# re.search() vs re.match()
# print(re.match('X', 'A\nB\nX', re.MULTILINE))  # No match
# print(re.search('^X', 'A\nB\nX', re.MULTILINE))  # Match

# phone number
text = """Ross McFluff: 834.345.1254 155 Elm Street

 Ronald Heathmore: 892.345.3428 436 Finley Avenue
 Frank Burger: 925.541.7625 662 South Dogwood Way


 Heather Albrecht: 548.326.4584 919 Park Place"""
print(re.split('\n+', text))
entries = re.split('\n+', text)
li = [re.split(':? ', item, maxsplit=3) for item in entries]
print(li)


#  Text Munging
def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)


text = "Professor Abdolmalek, please report your absences promptly."
print(re.sub(r"(\w)(\w+)(\w)", repl, text))

# Finding all Adverbs
text = "He was carefully disguised but captured quickly by police."
print(re.findall(r'\w+ly', text))
print(re.findall(r'(?<! )\w+ly', text))
print(re.findall(r'(?<= )\w+ly', text))
