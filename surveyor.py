import os
import sys
from congress.classes import Bill, Legislator, Vote, VoteResult


bills = Bill()
legislators = Legislator()
vote_results = VoteResult()
votes = Vote()


# preparing for the Popularity Report
bills.load_votes_results(vote_results)
bills.load_legislators(legislators)
bills.load_votes(votes)
# with source data loaded, we can now run this report
bills.popularity_report()


# preparing for the Legislator Alignment Report
legislators.load_votes_results(vote_results)
# with source data loaded, we can now run this report
legislators.alignment_report()
