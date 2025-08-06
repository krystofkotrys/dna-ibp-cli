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

## Sequence: create

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

## Sequence: show

usage: `dna-ibp sequence show [-h] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence   | Sequence(s) to be processed by related methods. (number, id, tag(s) or `all`)|

## Sequence: delete

usage: `dna-ibp sequence delete [-h] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence   | Sequence(s) to be processed by related methods. (number, id, tag(s) or `all`)|

## Sequence: count

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

## G4Hunter: analyse

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

## G4Hunter: show

usage: `dna-ibp g4hunter show [-h] [--details] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --details, -d  | Show details of the selected analyse result. |

## G4Hunter: delete

usage: `dna-ibp g4hunter delete [-h] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

## G4Hunter: export

usage: `dna-ibp g4hunter export [-h] [--path PATH] [--aggregate | --no-aggregate | -a] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --path PATH, -p PATH             |   Path where the CSV file should be saved. |
|  --aggregate, --no-aggregate, -a  |    Specify whether the CSV file should be grouped or not. Usage: --aggregate or --no-aggregate (default True). |

# R-Loop tracker

usage: `dna-ibp rloop [-h] {analyse,show,delete,export} ...`

**positional arguments:**

|Command            | Description                                        |
|-------------------|-----------------------------------------------------|
|    analyse        |     Analyse the provided sequence by R-loop tracker algorithm               |
|    show           |     Display selected analyse result(s) in the command line            |
|    delete         |     Delete chosen analyse result(s) from your DNA analyser account.   |
|    export         |     Export the provided R-loop tracker result(s) as a CSV file.             |

## Rloop: analyse

usage: `dna-ibp rloop analyse [-h] [--riz3g] [--riz4g] [--tags [TAGS ...]] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence          |    Choose sequence(s) which should be analysed by the R-loop tracker algorithm |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --riz3g          |  Select whether the RIZ 3G-cluster should be used to analyse. |
|  --riz4g          |  Select whether the RIZ 4G-cluster should be used to analyse. |
|  --tags [TAGS ...] |  (OPTIONAL) Add tags to analyse result(s). |

## Rloop: show

usage: `dna-ibp rloop show [-h] [--details] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --details, -d  | Show details of the selected analyse result. |

## Rloop: delete

usage: `dna-ibp rloop delete [-h] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

## Rloop: export

usage: `dna-ibp rloop export [-h] [--path PATH] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --path PATH, -p PATH             |   Path where the CSV file should be saved. |

# Z-DNA hunter

usage: `usage: dna-ibp zdna [-h] {analyse,show,delete,export} ...`

**positional arguments:**

|Command            | Description                                        |
|-------------------|-----------------------------------------------------|
|    analyse        |     Analyse the provided sequence by Z-DNA Hunter algorithm               |
|    show           |     Display selected analyse result(s) in the command line            |
|    delete         |     Delete chosen analyse result(s) from your DNA analyser account.   |
|    export         |     Export the provided Z-DNA Hunter result(s) as a CSV file.             |

## Z-DNA: analyse

usage: ``

**REPAIR AND FILL**

## Z-DNA: show

usage: `dna-ibp zdna show [-h] [--details] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --details, -d  | Show details of the selected analyse result. |

## Z-DNA: delete

usage: `dna-ibp zdna delete [-h] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

## Z-DNA: export

usage: `dna-ibp zdna export [-h] [--path PATH] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --path PATH, -p PATH             |   Path where the CSV file should be saved. |

# CpX Hunter

usage: `dna-ibp cpx [-h] {analyse,show,delete,export} ...`

**positional arguments:**

|Command            | Description                                        |
|-------------------|-----------------------------------------------------|
|    analyse        |     Analyse the provided sequence by CpX Hunter algorithm               |
|    show           |     Display selected analyse result(s) in the command line            |
|    delete         |     Delete chosen analyse result(s) from your DNA analyser account.   |
|    export         |     Export the provided CpX Hunter result(s) as a CSV file.             |

## CpX: analyse

usage: `dna-ibp cpx analyse [-h] [--ws WS] [--gcp GCP] [--o-e-cpg O_E_CPG] [--gap GAP] [--second SECOND] [--tags [TAGS ...]] sequence`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  sequence          |    Choose sequence(s) which should be analysed by the R-loop tracker algorithm |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --ws WS, --window-size WS, -w WS | |
|  --gcp GCP, --gc-percentage GCP, -g GCP | |
|  --o-e-cpg O_E_CPG, --observed-expected-cpg-o O_E_CPG | |
|  --gap GAP, --island-merge-gap GAP, -i GAP | |
|  --second SECOND, -s SECOND | |
|  --tags [TAGS ...], -t [TAGS ...] | (OPTIONAL) Add tags to analyse result(s). |

## CpX: show

usage: `dna-ibp cpx show [-h] [--details] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --details, -d  | Show details of the selected analyse result. |

## CpX: delete

usage: `dna-ibp cpx delete [-h] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

## CpX: export

usage: `dna-ibp cpx export [-h] [--path PATH] result`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  result        | Specify the analyse result(s) to be selected. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|  --path PATH, -p PATH             |   Path where the CSV file should be saved. |

# G4Killer

usage: `dna-ibp g4killer [-h] {run} ...`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|    run      | Run the G4Killer algorithm on the provided sequence.      |

## G4Killer: run

usage: `dna-ibp g4killer run [-h] [--complementary | --no-complementary] [--threshold THRESHOLD] sequence [sequence ...]`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|sequence          |    Specify the sequence(s) to be modified by G4Killer algorithm. |

**options:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
| --complementary, --no-complementary   |  Specify whether the analysed sequence is G-rich (false) or C-rich (true). Usage: --complementary or --no-complementary (default False). |
|  --threshold THRESHOLD, -t THRESHOLD  |  Target G4Hunter score for sequence mutation (default 1.0). |

# P53 Predictor

usage: `dna-ibp p53 [-h] {run} ...`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|    run      | Run the P53 Predictor algorithm on the provided sequence.      |

## P53: run

usage: `dna-ibp p53 run [-h] sequence [sequence ...]`

**positional arguments:**

|Argument            | Description                                        |
|-------------------|-----------------------------------------------------|
|sequence          |    Specify the sequence(s) to be processed by P53 predictor algorithm. |
