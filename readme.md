# Vote Digger

It takes legislators, votes results, votes, and bills provided as CSV data.



## Dependencies
For running this code

You will need to have Python 3, I used version **3.11.3** for this one.
For the other dependencies, you just load from **requirements.txt** file.

If you are using PIP:
```Bash
$ pip install -r requirements.txt
```
If you are using 'Conda':
```Bash
$ conda install --file requirements.txt
```





# CODE CHALLENGE

## The problem
In "./sample_data" folder, there are CSV files:

- Person - An individual legislator elected to government. This includes everyone from President Joe Biden to Representative. David McKinley from West Virginia.
- Bill - A piece of legislation introduced in the United States Congress.
- Vote - A vote on a particular Bill. Bills can be voted on multiple times, as the Bill itself can undergo changes over the course of its life. For the purposes of this challenge, there will only be up to 1 Vote provided for each Bill.
- VoteResult - A vote cast by an individual legislator for or against a piece of legislation. Each vote cast is associated with a specific Vote.
See the provided data for schema information for each of the data models.



## Changelog

### v0
Initial file and tooling, just the minimal to load the CSV files into data, for beginning operations.
Initially, I think of 2 simple ways to do that:
1. Load the data into variables and just iterate the collections.
2. Load the data in SQLite and just query the tables

As there (challenge proposal) explicitly tells "but you should not need anything complicated such as a database"(i.e.), I'll just go by **option 1**.