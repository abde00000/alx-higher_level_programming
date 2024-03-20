#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    index_list = my_list.index(search)
    new_list[index_list] = replace
    return new_list
