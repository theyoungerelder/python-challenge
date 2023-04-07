# package 
import csv 

dataset = 'Resources/election_data.csv'

# get data
with open(dataset) as csvfile:
    

    # my variables
    total_votes = 0
    candidate_votes = {}
    candidate_percentages = {}

        # Loop 
    for line in csvfile:
            # Split line into columns
        columns = line.strip().split(",")
            
            # the dcandidate
        candidate_name = columns[2]
            
            # total votes
        total_votes = total_votes + 1
            
            # persons vote
        if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0
            
            # adding to votes
        candidate_votes[candidate_name] =  candidate_votes[candidate_name] + 1

    # percentage for each person. I tghink this is right
    for candidate_name in candidate_votes:
        candidate_percentages[candidate_name] = (candidate_votes[candidate_name] / total_votes) * 100

    # make winner
    winner = max(candidate_votes, key=candidate_votes.get)
    
    # Printthe results
    print("Election Results")
    print('-------------------------------')
    print("Total Votes: ", total_votes)
    for candidate_name in candidate_votes:
        print(candidate_name, " received ", candidate_percentages[candidate_name], candidate_votes[candidate_name])
    print("Winner: ", winner)


with open('results.txt', 'w') as data:

# put in the results file
    data.write("Election Results" + "\n")
    data.write('-------------------------------' + "\n")
    data.write("Total Votes " + str(total_votes) +"\n")
    data.write('-------------------------------' + "\n")
    for candidate_name in candidate_votes:
        data.write(str(candidate_name) + " received " + str(candidate_percentages[candidate_name]) + str(candidate_votes[candidate_name]) + "\n")
    data.write("Winner: "+ str(winner))
