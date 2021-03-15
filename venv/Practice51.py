"""
Regular Expressions -> Searching and filtering of data

"""

import re

quote = "Change the world by being yourself."
#result = re.match("Change",quote) # 0 - 6
result = re.match("being", quote) # None , this is because the match matches from the beginning
#print(result,type(result))

result = re.search("being",quote)
#print(result)

message = "PB 09 Z 8430"
answer = bool(re.match("^[A-Z]{2}\s[0-9]{2}\s[A-Z]{1}\s[0-9]{4}$",message))
print(answer)