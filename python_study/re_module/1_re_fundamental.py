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

"""


