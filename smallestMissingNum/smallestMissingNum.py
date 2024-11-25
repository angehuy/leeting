def solution(A):
    # Filter only positive numbers and sort them
    A = sorted([x for x in A if x > 0])
    
    smallest_num = 1  # Start with the smallest positive integer
    for num in A:
        if num == smallest_num: # if smallest_num found in num
            smallest_num += 1  # Increment if the number is found in the list
        elif num > smallest_num: # if smallest_num not found in num and is smaller than the current num
            break  # No need to check further if `num` is greater
    
    return smallest_num