# def get_keys_nd_values(dictionary: dict):
#     return dictionary.keys(), dictionary.values()
#
#
# keys, values = get_keys_nd_values({"a": 3, "b": 5})
#
# print(values)
#
#
# arr = ["meaningful", "information", "extra", "extra"]
# important, info, *_ = arr
#
# print(important, info)
#
#
# my_tuple = (1, 2, 3)
#
# print((0, *my_tuple, 4))
#
# my_dict = {"one": 1, "two":2, "three": 3}
#
# print({"zero": 0, **my_dict, "five": 5})
#
#
# def unlimited_args(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# print(unlimited_args(first=1, sec=2, third=3, fth=4))


def add(required: int, optional: int=0, *args, **kwargs) -> int:
    print(required)
    print(optional)
    print(args)
    print(kwargs)
    return required + optional + sum(args) + sum(kwargs.values())

list_to_add = [1, 2, 3, 4, 5, 6, 7, 8]
print(add(*list_to_add))
