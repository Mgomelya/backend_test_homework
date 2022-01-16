def we_crash_all(name):
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crash_all('Наташа'))
print(we_crash_all(True))
>>> TypeError: can only concatenate str (not "bool") to str 