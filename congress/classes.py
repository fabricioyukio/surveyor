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
        print(f"loaded {csv_file_name}, with {self.fields} with {len(self.data)} rows")

    def __repr__(self) -> str:
        return self.data.to_string()

    def check_fields(self, field: str) -> bool:
        if field not in self.data.columns:
            raise ValueError(f"{field} is not a valid field")

    def snakefy(self) -> str:
        name = self.__class__.__name__
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


class Bill(Base):
    fields = ["id", "title", "sponsor_id"]

    def __init__(self) -> None:
        super().__init__()


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
    bills = None
    votes = None

    def __init__(self) -> None:
        super().__init__()

    def load_bills(self, bills: Bill) -> None:
        self.bills = bills.data

    def load_votes_results(self, votes: VoteResult) -> None:
        self.votes = votes.data

    def alignment_report(self) -> pd.DataFrame:
        assert self.votes is not None, "Votes must be loaded first"

        pass
