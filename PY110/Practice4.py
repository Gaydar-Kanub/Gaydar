import re

# s1 = "251.250.25.250"
# s2 = "266.250.25.250"
#
# pattern = '\d+'
#
# if re.fullmatch(pattern, s1):
#     print('Correct')
#
#
# pat_ip6 = '((^|:)([0-9a-fA-F]{0,4})){1,8}'


pat = r'\b\w+\b'
print(''.join(map(lambda x: x[0].upper(),  re.findall(pat, 'Шла Маша по шоссе'))))