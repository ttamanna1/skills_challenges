def count_words(string):
    if string == '':
        return 0
    elif len(string.split(' ')) >= 2:
        return len(string.split(' '))
    else:
        return 1

print(count_words('hi'))