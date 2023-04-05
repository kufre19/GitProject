import os
from datetime import datetime, timedelta
import random
from itertools import zip_longest
import math
import random

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

    return lst


def get_numbers_sum_to_count(count, length):
    # Calculate the maximum value for each index in the list to ensure the sum equals count
    max_vals = [count - sum(range(length-i)) for i in range(length)]

    # Replace any negative value with zero and adjust the largest value to make sure the sum equals count
    neg_count = sum(1 for v in max_vals if v < 0)
    if neg_count > 0:
        max_vals = [max(v, 0) for v in max_vals]
        max_vals[-1] += neg_count

    # Ensure the last value is non-negative or zero and adjust it if necessary to make sure the sum equals count
    last_val = max_vals[-1] if max_vals[-1] <= length else length
    if last_val < 0:
        last_val = 0
    elif last_val > count:
        last_val = count
    max_vals[-1] = last_val

    # Create the list with the maximum possible values
    numbers = [max_vals[i] if max_vals[i] <= i+1 else i+1 for i in range(length)]

    # Shuffle the list to make the values appear in random order
    random.shuffle(numbers)

    # Adjust the last value to make sure the sum equals count
    numbers[-1] += count - sum(numbers)

    return split_list(numbers,count)







def makeCommits(num_commits, start_date, days_back):
    
    # convert start_date and stop_date to datetime objects
    start_date = datetime.strptime(start_date, '%d/%m/%Y')
   
    stop_date = start_date - timedelta(days=days_back)


    # create a list of dates to make commits on
    date_list = []
    while start_date >= stop_date:
        date_list.append(start_date)
        start_date -= timedelta(days=1)

    date_list.reverse()
     # remove duplicates
    date_list = list(set(date_list))
   
    date_list.sort()
    date_list.pop(0)
    commit_list = get_numbers_sum_to_count(num_commits,len(date_list))

    # print(date_list)
    # commit_list[-1] = sum(commit_list) - num_commits
    # print(len(commit_list))
    # print(commit_list)
    # quit()

 


    for i, commit_count in enumerate(commit_list):
          
          for s in range(commit_count):
              
            commit_date = date_list[i]
            commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')

            # write commit message to file
            with open('data.txt', 'a') as file:
                    file.write(f'Commit for {commit_date.strftime("%d/%m/%Y")}\n')
                    
            # stage the file
            os.system('git add data.txt')
            
            # commit 
            os.system(f'git commit --date="{commit_date_str}" -m "Commit for {commit_date}"')


    # push changes to remote repository
    os.system('git push')



makeCommits(2000, '01/01/2023',365)
