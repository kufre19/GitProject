import os
from datetime import datetime, timedelta
import random


def makeCommits(num_commits: int, start_date: str, days_count_back: int):
    # Convert start_date to datetime object
    start_datetime = datetime.strptime(start_date, '%d/%m/%Y')

    for i in range(num_commits):
        # Generate a random number of commits for each day
        num_commits_per_day = random.randint(1, 10)

        # Format date in required format
        commit_date = start_datetime.strftime('%Y-%m-%dT%H:%M:%S')

        with open('data.txt', 'a') as file:
            date_obj = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%S')
            formatted_date = date_obj.strftime('%m/%d/%Y')
            file.write(f'Commit for {formatted_date}\n')

        # staging
        os.system('git add data.txt')
        # commit 
        os.system(f'GIT_COMMITTER_DATE="{commit_date}" git commit -m "Commit for {commit_date}"')

        # Move start_datetime back by days_count_back days
        start_datetime -= timedelta(days=days_count_back)

makeCommits(30, '01/01/2023', 10)
