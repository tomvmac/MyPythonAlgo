# Tournament Winner
#
#
# There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible.
#
# Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition,
# one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there
# are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.
#
#
#
# Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition,
# write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively.
#
# The competitions array has elements in the form of[homeTeam, awayTeam], where each team is a string of at most 30 characters representing the name of the team.The results array contains information about the winner of each corresponding competition in the competitions array.  Specifically, results[i] denotes the winner of competitions[i], where 1 in the results array means that the home team in the corresponding competition won and a 0 means the away team won.
#
# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once.  ' \
# It's also guaranteed that the tournament will always have at least two teams.
#
# Sample Input:
# compeitions = [
# ["HTML", "C#"],
# ["C#, "Python"],
# ["Python", "HTML"]
#]
#
# results = [0, 0, 1]

# Winner is Python
# C# beats HTML, Python beats C#, and Python beats HTML.
# HTML - points
# C# - 3 points
# Python - 6 points



# General Approach
# Create a scores dictionary keyed by team, update the score for each team
# Iterate through results and competition
# Iterate through dictionary to find the max score and declare the winner


def tournamentWinner(competitions, results):
    theWinner = ""
    currWinner = ""
    scoresDict = {}

    for num in range(len(results)):
        # get competition element
        competition = competitions[num]
        if results[num] == 1:
            # Home team won
            currWinner = competition[0]
        else:
            currWinner = competition[1]
        # track score
        if currWinner in scoresDict:
            scoresDict[currWinner] += 3
        else:
            scoresDict[currWinner] = 3


    # iterate through scores dictionary
    highScore = 0
    for team, score in scoresDict.items():
        if score > highScore:
            highScore = score
            theWinner = team

    return theWinner




# Driver code
competitions = [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
results = [0, 0, 1]

print (tournamentWinner(competitions, results))