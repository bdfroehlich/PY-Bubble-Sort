# write your bubble sort algorithm below
def bubble_sort(lst):
    #FOR loop to run the bubble sort algorithm as many times as there are elements in the list
    for i in range(len(lst)-1):
        swapped = False
        print(f"iteration {i}")
        #FOR loop to compare all the values in the list for each pass
        for j in range(len(lst)-1):
            print(f"comparing {lst[j], lst[j+1]}")
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        #"if not swapped" checks if swap was set to True for any iteration through the inner loop
        #if swapped was ever True you go back to the outter for loop and continue until swapped is never set to True
        #when is never set to True you end your for loops and return lst
        if not swapped:
            return
    return lst


sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
