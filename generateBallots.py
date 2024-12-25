import random
import numpy as np


general_list_of_parties = ['Crown Union', 'Britain First', 'People\'s Choice', 'Frontier Coalition', 'Greenfield Society', 'Liberty Forward', 'Seafarers Alliance']

random.seed(42)

# correct ballots

# here you can assign some distribution to party votes, e.g. based on the last elections. 
# If you want to underline the ambiguity about the best system for counting votes, it is better to make probabilities almost equal.
prob_weights = np.array([0.20, 0.20, 0.20, 0.19, 0.19, 0.01, 0.01])

# generating votes_names
votes = []
for i in range(3,8):
    for k in range(random.randint(1000,1500)):
        votes.append([str(i) for i in list(np.random.choice(general_list_of_parties, size=i, replace=False, p=prob_weights))])

# generating votes_ranks
votes2 = []
for i in range(2,8):
    for k in range(random.randint(1000,1500)):
        comb = [str(i) for i in list(np.random.choice(general_list_of_parties, size=i, replace=False, p=prob_weights))]
        newlist = []
        for party in general_list_of_parties:
            if party in comb:
                newlist.append(comb.index(party)+1)
            else:
                newlist.append(0)
        votes2.append(newlist)

votes += votes2
random.shuffle(votes)

len(votes)

# incorrect ballots
general_list_of_parties_d = ['Go Grass!', 'Advertisement Party', 'Pink Party', 'Justice and Teeth', 'SDP', 'Party like a Racoon', 'Pickle Ricks', 'Princess Party']

names_d = []
for i in range(3,8):
    for k in range(random.randint(5, 25)):
        names_d.append([str(i) for i in list(np.random.choice(general_list_of_parties, size=8, replace=True, p=[1/7] * 7))])

len(names_d)

ranks_d = []

for k in range(random.randint(20, 40)):
    sample = list(np.random.choice(general_list_of_parties, size=7, replace=False, p=prob_weights))
    comb = [str(i) for i in sample]
    newlist = []
    for party in general_list_of_parties:
        newlist.append(comb.index(party)+2)
    ranks_d.append(newlist)

for k in range(random.randint(20, 40)):
    sample = list(np.random.choice(general_list_of_parties, size=random.randint(3,7), replace=False, p=prob_weights))
    comb = [str(i) for i in sample]
    newlist = []
    for party in general_list_of_parties:
        if party in comb:
            newlist.append(0)
        else:
            newlist.append(0)
    ranks_d.append(newlist)

for k in range(random.randint(20, 40)):
    sample = list(np.random.choice(general_list_of_parties, size=random.randint(3,7), replace=False, p=prob_weights))
    comb = [str(i) for i in sample]
    newlist = []
    for party in general_list_of_parties:
        if party in comb:
            newlist.append(0)
        else:
            newlist.append(0)
    newlist.append(random.randint(0,1))
    ranks_d.append(newlist)

len(ranks_d)

votes = votes + names_d + ranks_d
random.shuffle(votes)
len(votes)

# saving data
import csv
with open("votes.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerows(votes)