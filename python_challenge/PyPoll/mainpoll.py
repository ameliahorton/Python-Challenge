import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

candidate_votes= {}
vote_percent={}
candidate_names=[]
total_votes=0
with open(election_data) as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")
    header=next(election_csv)
    for row in election_csv:
        total_votes=total_votes+1
        candidate=row[2]
        if candidate not in candidate_names:
            candidate_names.append(candidate)
            candidate_votes[candidate]=0   

        candidate_votes[candidate] = candidate_votes[candidate]+1 

    print(candidate_votes) 
    print("Total Votes: " , total_votes) 
    for candidate in candidate_votes:
        vote_percent[candidate]=(candidate_votes[candidate]/total_votes)*100
    
    print(vote_percent)
    winner=max(candidate_votes, key=candidate_votes.get)
    print("The winner is " , winner)
