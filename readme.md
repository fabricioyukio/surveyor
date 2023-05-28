# VOTES SURVEYOR

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
## Running this project
Just run
```Bash
$ python surveyor.py
# depending of your system configurations,
# you might use "python3" instead of "python"
# to run with version 3.x
```


# CODE CHALLENGE

Repository at https://github.com/fabricioyukio/surveyor.

## The problem
In "./sample_data" folder, there are CSV files:

- Person - An individual legislator elected to government. This includes everyone from President Joe Biden to Representative. David McKinley from West Virginia.
- Bill - A piece of legislation introduced in the United States Congress.
- Vote - A vote on a particular Bill. Bills can be voted on multiple times, as the Bill itself can undergo changes over the course of its life. For the purposes of this challenge, there will only be up to 1 Vote provided for each Bill.
- VoteResult - A vote cast by an individual legislator for or against a piece of legislation. Each vote cast is associated with a specific Vote.
See the provided data for schema information for each of the data models.


## Considerations

As previously stated, I coded this project for a code challenged proposed by Quorum for a Software Engineer position.

### Tradeoffs

I could've implemented this project with just CSV lib instead of using PANDAS lib.
The code performance would be a little better. However, it's my opinion that by using Pandas the code becomes more readable, understandable and maintainable.
And returning to the performance issue, for such a small volume of data, the difference is not humanly perceptible.

### Solution's complexity
Talking about complexity, just some methods are worthy of note:
1. Method congress.Base.**__init__**:
	* This method loads the associated CSV file, to every Child class. And we can say that its complexity is (O)<sup>1</sup> as the loadings are only single direct instructions.
2. Method congress.Legislator.**alignment_report**:
	* On this method, there are some orderings and queryings. As some of the operations occur under the hood,  there is some guessing. Considering the code alone:
		* It iterates the Legislators (n), where "**n**" is the number of legislators.
		* At each iteration, it queries for both "yea votes" and "nay votes", supposing the search is optimal, let's be optimistic and say it can be (log(m)), where "**m**" is the total votes.
		* And then, there is the time needed to write the CSV file for the report
	* With that in mind, I might think it would be: ```((O)n)*log(m)```
3. Method congress.Bill.**popularity_report**:
	* On this method, there are some orderings and queryings. As some of the operations occur under the hood,  there is some guessing. Considering the code alone:
		* It iterates the Bills (n), where "**n**" is the number of bills.
		* It iterates the Votes sessions (m), where "**m**" is the number of votes sessions with said Bill.
		* It queries the Sponsor (a legislator) of the Bill. Supposing the search is optimal, let's be optimistic and say it can be (log(k)), where "**k**" is the total of legislators.
		* At each iteration, it queries for both "yea votes" and "nay votes", supposing the search is optimal, let's be optimistic and say it can be (log(l)), where "**l**" is the total votes.
		* And then, there is the time needed to write the CSV file for the report
	* With that in mind, I might think it would be: ```((O)n)*log(m)*log(k)*log(l)```

### Possible future implementations
*How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?*
It would be just to add the new column in the CSV or have it to be got from another CSV.
In the first case, just be sure to add a column with the proper values in the CSV and update the affected Methods.
In the second case, one must add the proper columns to the CSV files, and maybe add similar classes and methods.

*How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?*
It depends on how frequently one would be responsible for such a task:
* If not that frequently, I would just convert the files to CSV and use this tool.
* If so, I would create methods to read the files and parse the contents to the proper format.
* Or even using Pentaho or MS Power BI, and create a procedure to do so.

*How long did you spend working on the assignment?*
* about 1 hour and 30 minutes on coding.
* some 1 or 2 hours thinking how I should do it. The challenge per se was not difficult, it just


## Changelog

### v4
Updated readme and a time for linting.
Also, restored CSV files in "./source_data" folder.

### v3
Added bill's report (opposers and supporters).

### v2
Added some more lines on CSV files just to be extra sure it would work properly.
Properly calculating for the first deliverable: "legislators and how many bills one supported and how many opposed". Will take some tests to check out.

### v1
Added this project to a Github Repo:
https://github.com/fabricioyukio/surveyor

### v0
Initial file and tooling, just the minimal to load the CSV files into data, for beginning operations.
Initially, I think of 2 simple ways to do that:
1. Load the data into variables and just iterate the collections.
2. Load the data in SQLite and just query the tables

As there (challenge proposal) explicitly tells "but you should not need anything complicated such as a database"(i.e.), I'll just go by **option 1**.