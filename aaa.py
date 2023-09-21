from string import digits

s = '/department/transport/2/'.rstrip("/")
remove_digits = str.maketrans('', '', digits)
res = s.translate(remove_digits)
print(res)