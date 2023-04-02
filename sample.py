import os
from datetime import datetime, timedelta
import random
from itertools import zip_longest

import random

def get_numbers_sum_to_count(count, length):
    numbers = []
    while len(numbers) < length:
        num = random.randint(1, count)
        if sum(numbers) + num > count:
            continue
        numbers.append(num)
    if sum(numbers) < count:
        numbers[-1] += count - sum(numbers)
    return numbers


def makeCommits(num_commits, start_date, days_back, stop_date=None):
    # convert start_date and stop_date to datetime objects
    start_date = datetime.strptime(start_date, '%d/%m/%Y')
    if stop_date:
        stop_date = datetime.strptime(stop_date, '%d/%m/%Y')
    else:
        stop_date = start_date - timedelta(days=days_back)

    # create a list of dates to make commits on
    date_list = []
  
    while start_date >= stop_date:
        date_list.append(start_date)
        if start_date != stop_date:
            start_date -= timedelta(days=days_back)
        else:
            date_list.append(start_date)

    date_list.reverse()
     # remove duplicates
    date_list = list(set(date_list))
   
    date_list.sort()
    commit_list = get_numbers_sum_to_count(num_commits,len(date_list))

    print(date_list)
    print(commit_list)
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



makeCommits(50, '01/01/2023', 2, '23/12/2022')
