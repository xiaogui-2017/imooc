import functools

sorted_ignore_case = functools.partial(sorted, key=str.lower)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])