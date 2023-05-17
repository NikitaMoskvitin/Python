def number_count(stroka):
    dict = {}
    for i in range(len(stroka)):
        k = int(stroka[i])
        dict.setdefault(k)
        if dict[k] == None:
            dict[k] = 1
        else:
            dict[k] = dict[k] + 1
    return dict
stroka = input()
print(number_count(stroka))
