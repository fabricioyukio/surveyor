import os
import sys

from congress.classes import Bill, Legislator, Vote, VoteResult

bills = Bill()
legislators = Legislator()
vote_results = VoteResult()
votes = Vote()

bills.load_votes_results(vote_results)
bills.load_legislators(legislators)
bills.load_votes(votes)

bills.popularity_report()
# legislators.load_votes_results(vote_results)
# legislators.alignment_report()
