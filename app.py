import os
import random
from datetime import datetime, timedelta

def makeCommits(numCommits, startDateStr, maxCommitsPerDay):
    startDate = datetime.strptime(startDateStr, '%d/%m/%Y')
    currDate = datetime.now()
    if startDate > currDate:
        print("Start date is in the future. No commits will be made.")
        return
    endDate = startDate - timedelta(days=numCommits-1)
    while currDate >= endDate:
        numCommitsToday = random.randint(1, maxCommitsPerDay)
        for j in range(numCommitsToday):
            commitDate = currDate - timedelta(days=random.randint(0, numCommits-1))
            commitMessage = f"Commit for {commitDate.strftime('%d/%m/%Y')} ({j+1}/{numCommitsToday})"
            commitDatetime = commitDate + timedelta(minutes=random.randint(0, 1439))
            commitDatetimeStr = commitDatetime.strftime('%Y-%m-%d %H:%M:%S')
            with open('data.txt', 'a') as file:
                file.write(f'{commitDatetimeStr} <- {commitMessage}\n')
            os.system(f'git add data.txt')
            os.system(f'git commit --date="{commitDatetimeStr}" -m "{commitMessage}"')
        currDate -= timedelta(days=1)


makeCommits(30, '01/01/2023', 10)