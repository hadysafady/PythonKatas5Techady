def count_true_values(array):
    """
    Counts the number of True values in the given boolean list.

    Args:
        array: the boolean list to check

    Returns:
        the count of True values in the list
    """
    sum_true = 0
    for i in array:
        if i == True:
            sum_true = sum_true + 1 
    return sum_true


if __name__ == '__main__':
    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed