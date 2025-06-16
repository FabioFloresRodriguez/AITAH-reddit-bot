import re
lst_test = [
    "test 1", "test 5","test 2", "test3", "test: 4"
]
dct_test = {
    "test4": "value",
    "test 1": "value",
    "[test 2]": "value",
    "test: 3": "value"
}


res_1 = sorted(lst_test, key=lambda x: int(re.search(r'\d+', x).group()))

print(res_1)

res_2 = sorted(dct_test, key=lambda x: int(re.search(r'\d+', x).group()))

print(res_2)