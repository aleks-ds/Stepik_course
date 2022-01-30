def chunked(string, n):
    list_start = [[i] for i in string.split(' ')]
    lst = []
    for i in range(0, len(list_start), n):
        lst.append(list_start[i])
        for j in range(1 + i, i + n):
            if j >= len(list_start):
                break
            else:
                print(lst)
                lst[len(lst) - 1].append(list_start[j][0])
    return print(lst)


chunked(input(), int(input()))

#[[a], [b], [c], [d], [e], [f]]


