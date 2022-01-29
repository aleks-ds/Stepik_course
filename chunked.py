def chunked(string, n):
    list_start = [[i] for i in string.split(' ')]
    lst = []
    for i in range(0, len(list_start), n):
        lst.append(list_start[i])
        for j in range(i, n):
            lst[i].append(list_start[j])
    return print(lst)


chunked(input('Введите символы через пробел: '), int(input('Введите длину куска: ')))

#[[a], [b], [c], [d], [e], [f]]


