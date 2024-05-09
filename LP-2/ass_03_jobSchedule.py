# Ask user to input the number of jobs
n = int(input("Enter number of jobs: "))

# Create an empty list to store job details
jobs = []

# Get job details from the user
print("Enter ID, deadline, and profit for each job:")
for i in range(n):
    job = input(f"Job {i+1}: ").split()  # Split the input into a list
    jobs.append(job)  # Add job details to the list

# Sort jobs based on profit (descending order)
def get_profit(job):
    return int(job[2])

jobs.sort(key=get_profit, reverse=True)


# Schedule jobs based on deadlines and profit
scheduled = []
time = 0
for job in jobs:
    if time < int(job[1]):  # Check if deadline is not yet reached
        scheduled.append(job[0])  # Add job ID to the schedule
        time += 1  # Increment time

# Print scheduled jobs
print("Jobs are scheduled as:")
print(scheduled)
