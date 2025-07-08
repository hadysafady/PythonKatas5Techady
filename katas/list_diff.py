def find_difference(numbers):
    
   # Finds the difference between the largest and smallest numbers in the list.
    
    return max(numbers)-min(numbers)

    

    


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed