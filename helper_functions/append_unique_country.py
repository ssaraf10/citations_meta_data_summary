def append_unique_items(main_list, returned_list):
    for item in returned_list:
        if item not in main_list:
            main_list.append(item)

    return main_list