import math

def split_list(lst, target_sum):
    # Remove all zero items from the list
    nums = [num for num in lst if num != 0]

    

    # Replace all negative numbers with zero
    nums = [max(num, 0) for num in nums]
   

    # Divide all items by 2 until the sum is less than or equal to the target
    while sum(nums) > target_sum:
        nums = [max(math.ceil(num / 2), 0) for num in nums]
       

    # Calculate the difference between the sum and the target
    diff = target_sum - sum(nums)
  

    # Find the first item with a value of zero and replace it with the difference
    for i in range(len(lst)):
        if nums[i] == 0:
            nums[i] = diff
            break
          

    # Replace non-zero items in the original list with items from the new list
    j = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[i] = nums[j]
            j += 1
            if j == len(nums):
                break

       # Check if the last element is divisible by 2 and greater than or equal to 100
    if lst[-1] % 2 == 0 and lst[-1] <= 100:
        half = lst[-1] // 2
        lst[-1] = half
        zeros = [i for i in range(len(lst)) if lst[i] == 0]
        half_idx = 0
        while half > 0 and half_idx < len(zeros):
            if half >= 100:
                lst[zeros[half_idx]] = half
                half_idx += 1
            half = half // 2

    return lst







lst = [0, 0, 170, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 350, 0, 0, 0, 0, 326, 0, 0, 0, 0, 0, 0, 313, 0, 0, 0, 0, 330, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 343, 0, 0, 0, 0, 316, 0, 0, 0, 0, 0, 0, 0, 0, 0, 365, 0, 0, 0, 0, 342, 344, 0, 0, 0, 0, 355, 0, 319, 0, 359, 0, 0, 0, 0, 331, 0, 0, 0, 318, 334, 0, 0, 0, 0, 0, 0, 0, 0, 320, 309, 349, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 341, 0, 0, 327, 0, 0, 0, 0, 0, 336, 0, 0, 0, 0, 337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 348, 0, 0, 0, 0, 0, 351, 0, 0, 0, 339, 230, 315, 0, 0, 0, 338, 322, 0, 0, 0, 323, 0, 0, 0, 335, 0, 0, 0, 0, 352, 0, 0, 0, 328, 346, 0, 0, 311, 0, 0, 0, 0, 0, 0, 0, 332, 364, 0, 363, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 321, 324, 0, 0, 0, 0, 0, 0, 0, 0, 0, 325, 0, 0, 0, 0, 0, 362, 0, 0, 0, 0, 0, 0, 0, 0, 0, 360, 0, 0, 0, 358, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 314, 0, 0, 357, 0, 0, 0, 354, 0, 0, 0, 0, 109, 0, 0, 0, 0, 0, 0, 289, 0, 0, 0, 308, 0, 347, 0, 0, 0, 0, 0, 0, 0, 310, 0, 0, 0, 0, 317, 0, 0, 0, 361, 0, 312, 0, 0, 0, 0, 0, 356, 0, 0, 0, 0, 0, 353, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 345, 0, 0, 0, 0, 0, 0, 0, 329, 0, 0, 0, 0, 0, 340, 0, 0, 333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 0, 0, -18362]
target_sum = 2000

adjusted_lst = split_list(lst, target_sum)
print(adjusted_lst)
print(sum(adjusted_lst))
