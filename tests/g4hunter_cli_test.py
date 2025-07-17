import pytest
from dna_ibp.cli import DnaCli
from argparse import Namespace
from pandas import DataFrame, Series
from pathlib import Path

@pytest.fixture(scope="module")
def cli():
    CLI = DnaCli(email="host", password="host")
    return CLI

def test_g4hunter_analyse_and_show(cli: DnaCli):
    args_analyse = Namespace(
        command="g4hunter",
        subcommand="analyse",
        sequence="all",
        threshold=1.0,
        windowsize=25,
        tags=["pytest"]
    )

    args_show = Namespace(
        command="g4hunter", 
        subcommand="show", 
        result="all", 
        verbose=None, 
        details=None
    )

    cli.g4hunter_logic(args_analyse)
    result = cli.g4hunter_logic(args_show)

    assert result["result_count"].sum() == 450


def test_g4hunter_show_details(cli: DnaCli):
    args = Namespace(
        command="g4hunter",
        subcommand="show",
        result=0,
        verbose=None,
        details=True
    )

    result = cli.g4hunter_logic(args)

    assert isinstance(result, DataFrame)
    assert len(result.columns) == 8
