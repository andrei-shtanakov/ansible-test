import crypt
d = {}
items = ('alice', 'bob', 'carol')
for i in items:
  pw = i
  cw = crypt.crypt(pw)
  d[pw] = cw
print(d)
with open('passwords.txt','w') as out:
    for key,val in d.items():
        out.write('{}:{}\n'.format(key,val))
