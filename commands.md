<h1>FULL COMMAND LIST</h1>

This document contains all valid commands, sub-commands and arguments for the dna-ibp Python CLI application. This information can be also obtained by using the `--help`/`-h` argument e.g.: `>dna-ibp sequence show --help`

 # General commands

These commands follow the command for DNA IBP CLI program execution `dna-ibp`. They specify which tool should be used to process further arguments.

usage: `dna-ibp [-h] [--version] [--reset] {sequence,g4hunter,rloop,zdna,cpx,g4killer,p53} ...`

**positional arguments:**

|Command            | Description                                         |
|-------------------|-----------------------------------------------------|
|    sequence       |     Parser for sequence related operations.         |
|    g4hunter       |     Parser for methods of the G4Hunter tool.        |
|    rloop          |     Parser for methods of the R-loop tracker tool.  |
|    zdna           |     Parser for methods of the Z-DNA hunter tool.    |
|    cpx            |     Parser for methods of the CpX hunter tool.      |
|    g4killer       |     Parser for methods of the G4Killer tool.        |
|    p53            |     Parser for methods of the P53 predictor tool.   |

**options:**
|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  -h, --help       |     show this help message and exit                 |
|  --version, -v    |     show program's version number and exit          |
|  --reset, -r      |     Log out of your DNA analyser account            |

# Sequence

usage: `dna-ibp sequence [-h] {create,show,data,delete,count} ...`

**positional arguments:**

|Command            | Description                                                     |
|-------------------|-----------------------------------------------------            |
|    create         |     Parser for uploading sequences to your DNA analyser.        |
|    show           |     Load sequence(s) uploaded in your DNA analyser account.     |
|    delete         |     Delete chosen sequence(s) from your DNA analyser account.   |
|    count          |     Recount nucleotides for a given sequence.                   |

## Create

usage: `dna-ibp sequence create [-h] (--file FILE | --id ID | --text TEXT) [--circular | --no-circular] [--tags [TAGS ...]] [--nucleic {DNA,RNA}] [--name NAME]`

**options:**
|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --file FILE, -f FILE      |    Upload a sequence by providing path to a file (.txt of FASTA)
|  --id ID, -i ID            |    Upload a sequence via NCBI ID.
|  --text TEXT, -t TEXT       |   Upload a sequence via pasting a string.
|  --circular, --no-circular  |   Specify whether the sequence is circular or not (--circular or --no-circular).
|  --tags [TAGS ...]          |   (OPTIONAL) Specify tags associated with the uploaded sequence.
|  --nucleic {DNA,RNA}        |   Specify whether the sequence nucleic type (choices: DNA, RNA, default val: DNA).
|  --name NAME, -n NAME       |   Specify name of the uploaded sequence.

## Show

usage: `dna-ibp sequence show [-h] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence   | Sequence(s) to be processed by related methods. (number, id, tag(s) or `all`)|

## Delete

usage: `dna-ibp sequence delete [-h] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence   | Sequence(s) to be processed by related methods. (number, id, tag(s) or `all`)|

## Count

usage: `dna-ibp sequence count [-h] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence   | Sequence(s) to be processed by related methods. (number, id, tag(s) or `all`)|

# G4Hunter

usage: `dna-ibp g4hunter [-h] {analyse,show,delete,export} ...`

**positional arguments:**

|Command            | Description                                        |
|-------------------|-----------------------------------------------------|
|    analyse        |     Analyse the provided sequence by G4Hunter algorithm               |
|    show           |     Display selected analyse result(s) in the command line            |
|    delete         |     Delete chosen analyse result(s) from your DNA analyser account.   |
|    export         |     Export the provided G4Hunter result(s) as a CSV file.             |

## Analyse

usage: `dna-ibp g4hunter analyse [-h] [--tags [TAGS ...]] [--threshold THRESHOLD] [--windowsize WINDOWSIZE] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence          |    Choose sequence(s) which should be analysed by the G4 Hunter algorithm |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --tags [TAGS ...]     (OPTIONAL)      | Add tags to analyse result(s).                                                      |
|  --threshold THRESHOLD, -t THRESHOLD   | Minimal G4Hunter score to be classified as a hit.                                   |
|  --windowsize WINDOWSIZE, -w WINDOWSIZE | Minimal required number of consecutive nucleotide bases to be classified as a hit. |
