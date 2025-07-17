import pytest
from dna_ibp.cli import DnaCli
from argparse import Namespace
from pandas import DataFrame, Series
from pathlib import Path

@pytest.fixture(scope="module")
def cli():
    CLI = DnaCli(email="host", password="host")
    return CLI

def test_sequence_show_all(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="show",
        sequence="all",
        verbose=None
    )

    result = cli.sequence_logic(args)

    assert isinstance(result, DataFrame)
    assert len(result) == 8     # update if number of public sequences changes
    
def test_sequence_show_indices(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="show",
        sequence="0",
        verbose=None
    )

    result = cli.sequence_logic(args)

    assert isinstance(result, Series)

@pytest.mark.skip(reason="Impossible to test on public sequences, due to sequence IDs changing on each host login.")
def test_sequence_show_by_id(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="show",
        sequence="05f472d3-19e2-4cf1-b791-096d4c841201",
        verbose=None
    )

    result = cli.sequence_logic(args)

    assert isinstance(result, Series)

@pytest.mark.skip(reason="Impossible to test on public sequences, due to them not having any tags.")
def test_sequence_show_tags(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="show",
        sequence="test",
        verbose=None
    )

    result = cli.sequence_logic(args)

    assert isinstance(result, Series)

def test_sequence_show_data(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="data",
        sequence="-1",
        length=50,
        position=0
    )

    result = cli.sequence_logic(args)

    assert isinstance(result, str)
    assert len(result) == 50

def test_sequence_create_text(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="create",
        file=None,
        id=None,
        text="ATTACTATGCAGGGA",
        circular=True,
        tags=["pytest1"],
        nucleic="DNA",
        name="Pytest_Text_created_sequence"
    )

    cli.sequence_logic(args)
    result = cli.sequence_logic(Namespace(command="sequence", subcommand="show", sequence="pytest1", verbose=None))

    result = result.iloc[0]

    assert isinstance(result, Series)
    assert result["length"] == 15
    assert result["name"] == "Pytest_Text_created_sequence"

def test_sequence_create_ncbi(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="create",
        file=None,
        id="NC_003065.1",
        text=None,
        circular=True,
        tags=["pytest2"],
        nucleic="DNA",
        name="Pytest_ID_created_sequence"
    )

    cli.sequence_logic(args)
    result = cli.sequence_logic(Namespace(command="sequence", subcommand="show", sequence="pytest2", verbose=None))

    result = result.iloc[0]

    assert isinstance(result, Series)
    assert result["length"] == 214331
    assert result["name"] == "Pytest_ID_created_sequence"

def test_sequence_create_file(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="create",
        file=Path(__file__).parent / "sequence_samples/fasta_test.fasta",
        id=None,
        text=None,
        circular=True,
        tags=["pytest3"],
        nucleic="DNA",
        name="Pytest_file_created_sequence"
    )

    cli.sequence_logic(args),
    result = cli.sequence_logic(Namespace(command="sequence", subcommand="show", sequence="pytest3", verbose=None))

    result = result.iloc[0]

    assert isinstance(result, Series)
    assert result["length"] == 1565
    assert result["name"] == "Pytest_file_created_sequence"


def test_sequence_count(cli: DnaCli):
    args = Namespace(
        command="sequence",
        subcommand="count",
        sequence="all"
    )

    cli.sequence_logic(args)
    result = cli.sequence_logic(Namespace(command="sequence", subcommand="show", sequence="all", verbose=None))

    assert not result["nucleic_count"].isnull().any()