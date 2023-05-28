import os
import sys

from congress.classes import Bill, Legislator, Vote, VoteResult

bills = Bill()
legislators = Legislator()
votes = Vote()
vote_results = VoteResult()

legislators.load_bills(bills)

legislators.load_votes_results(vote_results)
legislators.alignment_report()
