import os
from datetime import datetime, timedelta
import random

def makeCommits(num_commits, start_date, days_to_count):
    date_format = '%d/%m/%Y'
    current_date = datetime.strptime(start_date, date_format)
    commit_count = 0

    while commit_count < num_commits:
        num_commits_today = random.randint(1, days_to_count)
        for i in range(num_commits_today):
            if commit_count >= num_commits:
                break
            date_str = current_date.strftime(date_format)
            dates = f"{date_str} at {i}th commit"
            with open('data.txt', 'a') as file:
                file.write(f'{dates} <- this was the commit for the day!!\n')
            # staging 
            os.system('git add data.txt')
            # commit 
            os.system(f'GIT_COMMITTER_DATE="{date_str}T12:00:00" git commit --date="{date_str}T12:00:00" -m "Commit for {date_str}"')
            commit_count += 1
        
        current_date -= timedelta(days=1)

    os.system('git push')

makeCommits(30, '01/01/2023', 10)
