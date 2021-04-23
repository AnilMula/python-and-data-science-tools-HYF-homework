# try and catch to avoid Index out of range exception

try:
    lst= [5, 10, 20]
    print(lst[len(lst)])
except IndexError as e:
    print(e)
    