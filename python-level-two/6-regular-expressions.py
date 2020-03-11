# import re
#
# patterns = ['term1', 'term2']
# text = 'This is a string with term1, not not the other'
# for pattern in patterns:
#     print('I\'m seraching for: '+pattern)
#
#     if re.search(pattern, text):
#         print('MATCH!')
#     else:
#         print('NO MATCH')

# import re
#
# text = 'This is a string with term1, not not the other!'
# match = re.search('term1', text)
# print(match.start())
import re
# split_term = '@'
#
# email = 'user@gmail.com'.split('@')

# print(re.split(split_term, email))

# find all matches
# print(re.findall('match', 'test phrase match in match of the match'))
def multi_re_find(patterns, pharase):
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, pharase))
        print('\n')

test_pharase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
# test_patterns = ['[^!.?]+']
# test_patterns = ['[a-z]+']
test_patterns = [r'\d+'] sequence of digits
test_patterns = [r'\D+'] non digits
test_patterns = [r'\s+'] whitespace
test_patterns = [r'\S+'] non whitespace

multi_re_find(test_patterns, test_pharase)
