# Packages Comparator

## What It Does

This tool gets packages from the branches "sisyphus" and "p11", classifies them by architechture, and checks which branch each package belongs to. If a package belongs to both branches, it is compared by version. If the version in `"sisyphus"` is newer, it is added to the `"newer_in_sisyphus"` section. All results are saved in `"result.json"` and are available for viewing. 

## How to Run

Run the tool by executing bash-script:

```bash
./run.sh
```

This script installs the required dependencies and runs tests.

If you don't want to use `run.sh`, you can install dependencies manually:
```bash
pip3 install -r requirements.txt
sudo apt-get install -y python3-module-rpm
sudo apt-get install -y python3-module-pip
```
and use `python3 cli.py --branch1 branch_name_1 --branch2 branch_name_2 result.json` with all the available branches you have. 

## Tested On
This tool was tested on `ALT Linux 11.0 Workstation (x86_64)`