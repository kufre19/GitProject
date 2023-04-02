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

    # create a dictionary to store the commits for each date
    commits_per_date = {}

    # loop through the days and assign a random number of commits for each day
    while start_date >= stop_date:
        if start_date not in commits_per_date:
            commits_per_date[start_date] = random.randint(0, num_commits)
        num_commits -= commits_per_date[start_date]
        start_date -= timedelta(days=1)

    # distribute any remaining commits evenly across the days
    if num_commits > 0:
        num_days = len(commits_per_date)
        for i in range(num_commits):
            date = random.choice(list(commits_per_date.keys()))
            commits_per_date[date] += 1

    # loop through each date and make commits
    for date, num_commits in commits_per_date.items():
        # get the commit date and format it
        commit_date_str = date.strftime('%Y-%m-%dT%H:%M:%S')

        # loop through each commit for the current day
        for i in range(num_commits):
            # write commit message to file
            with open('data.txt', 'a') as file:
                file.write(f'Commit for {date.strftime("%d/%m/%Y")}\n')

            # stage the file
            os.system('git add data.txt')

            # commit
            os.system(f'git commit --date="{commit_date_str}" -m "Commit for {date.strftime("%d/%m/%Y")}"')

    # push changes to remote repository
    os.system('git push')



makeCommits(30, '01/01/2023', 2, '23/12/2022')
