"""
source from:A.M. Kuchling <amk@amk.ca>

1.metacharacters
. ^ $ * + ? { } [ ] \ | ( )
1.1     []
1.1.1   They’re used for specifying a character class, which is a set of characters that you wish to match
eg.1     match only lowercase letters,RE would be [a-z]
1.1.2   Metacharacters are not active inside classes
eg.2    [akm$] will match any of the characters 'a', 'k', 'm', or '$'
1.1.3   ^
eg.3     [^5] will  match any character except '5'.

1.2     \
\d
Matches any decimal digit; this is equivalent to the class [0-9].
\D
Matches any non-digit character; this is equivalent to the class [^0-9].
\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
"""