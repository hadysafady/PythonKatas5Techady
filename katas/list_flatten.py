def flatten_list(nested_list):
    """
    Flattens a nested list into a single list of integers.

    Args:
        nested_list: the input nested list

    Returns:
        a flat list containing all integers from the nested structure
    """
    # hint: isinstance()
    print(nested_list)
    flatt_list = []

    def loop_list(list_in_list):
        for i in range(len(list_in_list)):
            if isinstance(list_in_list[i],list):
                 loop_list(list_in_list[i])
            else :
                flatt_list.append(list_in_list[i])

    if isinstance(nested_list,list):
        for i in range(len(nested_list)):
            if isinstance(nested_list[i],list):
                 loop_list(nested_list[i])
            else :
                 flatt_list.append(nested_list[i])
    else :
         raise TypeError(f"Expected list, got {type(nested_list)}")
        
    return flatt_list


if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]