import re

log = "July 31 the is just a date i want to use in python [1235]: ERROR peforming package upgrade"
index = log.index('[')
print(log[index+1:index+5])
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])