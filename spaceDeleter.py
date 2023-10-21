def func(s):
    s = s.replace('.', '')
    s = s.replace(' ', '_')
    s+='.py'
    return s
while 1:
    print(func(input()))
