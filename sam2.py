import os
from datetime import datetime, timedelta
import random

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
        start_date -= timedelta(days=1)
    date_list.reverse()

    # calculate the number of commits needed for each day
    num_days = len(date_list)
    commits_per_day = [1] * num_days
    remaining_commits = num_commits - num_days
    
    # distribute remaining commits evenly across the days
    if remaining_commits > 0:
        commits_per_day = [2] * num_days
        for i in range(remaining_commits):
            commits_per_day[i % num_days] += 1

    # loop through each day and make commits
    for i in range(num_days):
        # get the commit date and format it
        commit_date = date_list[i] + timedelta(hours=12)
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

makeCommits(20, '01/01/2023', 7, '23/12/2022')

# makeCommits(30, '01/01/2023', 10)
