from pypkgs_db import __version__
from pypkgs_db import pypkgs_db
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    assert ((pypkgs_db.catbind(a, b)).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
    assert (
        (pypkgs_db.catbind(a, b)).categories
        == [
            "but",
            "character",
            "counts",
            "eyeballs",
            "hits",
            "integer",
            "where it",
            "your",
        ]
    ).all()
