from calendar import c
import os
import pandas as pd
import re


class Base:
    fields = []

    def __init__(self) -> None:
        csv_file_name = self.snakefy() + "s.csv"
        path = os.path.join(os.path.dirname(__file__), "..", "source_data")
        csv_path = f"{path}/{csv_file_name}"

        assert (  # the file exists
            os.path.exists(csv_path) is True
        ), f"../sample_data/{csv_file_name} does not exist"

        assert (  # the file is a file
            os.path.isfile(csv_path) is True
        ), f"../sample_data/{csv_file_name} is not a file"

        assert (  # there are fields to extract defined
            len(self.fields) > 0
        ), f"no columns to extract"

        self.data = pd.read_csv(csv_path, index_col="id", usecols=self.fields)
        assert self.data.shape[0] > 0, "There is no data in the file"

    def __repr__(self) -> str:
        return self.data.to_string()

    def check_fields(self, field: str) -> bool:
        if field not in self.data.columns:
            raise ValueError(f"{field} is not a valid field")

    def snakefy(self) -> str:
        name = self.__class__.__name__
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


class Vote(Base):
    fields = ["id", "bill_id"]

    def __init__(self) -> None:
        super().__init__()


class VoteResult(Base):
    fields = ["id", "legislator_id", "vote_id", "vote_type"]

    def __init__(self) -> None:
        super().__init__()


class Legislator(Base):
    fields = ["id", "name"]
    votes = None

    def __init__(self) -> None:
        super().__init__()

    def load_votes_results(self, votes: VoteResult) -> None:
        self.votes = votes.data

    def alignment_report(self) -> None:
        # making sure the votes are loaded
        assert self.votes is not None, "Votes must be loaded first"
        results = []

        for lid, legislator in self.data.sort_values(
            by=["name"], ascending=True
        ).iterrows():
            votes_yea = self.votes.query(f"legislator_id == {lid} & vote_type == 1")
            votes_nay = self.votes.query(f"legislator_id == {lid} & vote_type == 2")

            results.append(
                {
                    "id": lid,
                    "name": legislator["name"],
                    "num_supported_bills": votes_yea.shape[0],
                    "num_opposed_bills": votes_nay.shape[0],
                }
            )
        votes_alignments = pd.DataFrame(results)
        path = os.path.join(os.path.dirname(__file__), "..", "results")
        votes_alignments.to_csv(
            f"{path}/legislators-support-oppose-count.csv", index=False
        )
        print("Generated CSV file legislators-support-oppose-count.csv")


class Bill(Base):
    fields = ["id", "title", "sponsor_id"]
    votes = None
    votes_results = None
    legislators = None

    def __init__(self) -> None:
        super().__init__()

    def load_legislators(self, legislators: Legislator) -> None:
        self.legislators = legislators.data

    def load_votes(self, votes: Vote) -> None:
        self.votes = votes.data

    def load_votes_results(self, votes_results: VoteResult) -> None:
        self.votes_results = votes_results.data

    def popularity_report(self) -> None:
        # making sure the votes are loaded
        assert self.votes is not None, "Votes must be loaded first"
        # making sure the legislators are loaded
        assert self.legislators is not None, "Votes must be loaded first"

        results = []
        for bid, bill in self.data.sort_values(by=["title"], ascending=True).iterrows():
            votes = self.votes.query(f"bill_id == {bid}")

            votes_yea, votes_nay = 0, 0

            sponsors = self.legislators.query(f"id == {bill['sponsor_id']}")
            if sponsors.shape[0] > 0:
                sponsor_name = sponsors.iloc[0]["name"]
            else:
                sponsor_name = "Unknown"

            for vid, vote in votes.iterrows():
                votes_yea += self.votes_results.query(
                    f"vote_id == {vid} & vote_type == 1"
                ).shape[0]
                votes_nay += self.votes_results.query(
                    f"vote_id == {vid} & vote_type == 2"
                ).shape[0]

            results.append(
                {
                    "id": bid,
                    "title": bill["title"],
                    "supporter_count": votes_yea,
                    "opposer_count": votes_nay,
                    "primary_sponsor": sponsor_name,
                }
            )

        popularity_report = pd.DataFrame(results)
        path = os.path.join(os.path.dirname(__file__), "..", "results")
        popularity_report.to_csv(f"{path}/bills.csv", index=False)
        print("Generated CSV file bills.csv")
