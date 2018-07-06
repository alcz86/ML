import pandas as pd
import numpy as np
import csv

#read the survey

for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
    line = line.strip()
    parts = line.split(" - ")
    name = parts[0]
    vote = parts[1]
    print(name + " voted for " + vote)

print "\ninspecting votes\n"


for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
   line = line.strip()
   parts = line.split(" - ")
   name, vote = parts
   if vote == "White Icicle":
      print(name + " likes White Icicle!")

print "\ncounting votes\n"

print("Counting votes for White Icicle...")
count = 0
for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
   line = line.strip()
   name, vote = line.split(" - ")
   if vote == "White Icicle":
      count = count + 1
print(count)

print "\ngeneric function\n"

def count_votes(radish):
    print("Counting votes for " + radish + "...")
    count = 0
    for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
        line = line.strip()
        name, vote = line.split(" - ")
        if vote == radish:
            count = count + 1
    return count

print(count_votes("White Icicle"))

print(count_votes("Daikon"))

print(count_votes("Sicily Giant"))

print "\ncounting all the votes\n"

# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    if vote not in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] = counts[vote] + 1
print(counts)


print "\ncleaning data\n"

# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # munge the vote string to clean it up
    vote = vote.strip().capitalize()
    if not vote in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] = counts[vote] + 1
print(counts)


print "\nChecking if anyone voted twice\n"

# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # clean up the person's name
    name = name.strip().capitalize().replace("  "," ")
    # check if this person already voted
    if name in voted:
        print(name + " has already voted! Fraud!")
        continue
    voted.append(name)
    # munge the vote string to clean it up
    vote = vote.strip().capitalize().replace("  "," ")
    if not vote in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] += 1

print("Results:")
print()
for name in counts:
    print(name + ": " + str(counts[name]))

print "\nrefactoring\n"

#Create an empty dictionary for associating radish names
#with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []


#Clean up (munge) a string so it's easy to match against other     strings
def clean_string(s):
    return s.strip().capitalize().replace("  ", " ")


#Check if someone has voted already and return True or False
    def has_already_voted(name):
        if name in voted:
            print(name + " has already voted! Fraud!")
            return True
        return False


    # Count a vote for the radish variety named 'radish'
    def count_vote(radish):
        if not radish in counts:
            # First vote for this variety
            counts[radish] = 1
        else:
            # Increment the radish count
            counts[radish] = counts[radish] + 1


    for line in open("C:\Users\Aleksandra\Desktop\python/radishsurvey.txt"):
        line = line.strip()
        name, vote = line.split(" - ")
        name = clean_string(name)
        vote = clean_string(vote)

        if not has_already_voted(name):
            count_vote(vote)
        voted.append(name)

    print("Results:")
    print()
    for name in counts:
        print(name + ": " + str(counts[name]))

#/refactoring


print "\nwinner\n"

#Record the winning name and the votes cast for it
winner_name = "No winner"
winner_votes = 0

for name in counts:
    if counts[name] > winner_votes:
        winner_votes = counts[name]
        winner_name = name

print("The winner is: " + winner_name)