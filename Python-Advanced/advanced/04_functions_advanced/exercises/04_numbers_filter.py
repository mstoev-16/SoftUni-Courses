def even_odd_filter(**kwargs):
    dict1 = {}
    for key, value in kwargs.items():
        if key == 'odd':
            value = list(filter(lambda x: x % 2 != 0, value))
        if key == 'even':
            value = list(filter(lambda x: x % 2 == 0, value))
        dict1[key] = value

    sorted_dict = sorted(dict1.items(), key=lambda kvpt: (-len(kvpt[1])))
    print(type(sorted_dict))
    return dict(sorted_dict)


def even_odd_filter(**kwargs):
    if 'odd' in kwargs:
        kwargs['odd'] = list(filter(lambda x: x % 2 != 0, kwargs['odd']))
    if 'even' in kwargs:
        kwargs['even'] = list(filter(lambda x: x % 2 == 0, kwargs['even']))

    sorted_dict = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1])))
    print(type(sorted_dict))
    return dict(sorted_dict)

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
