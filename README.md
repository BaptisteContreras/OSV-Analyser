# OsvAnalyzer

A simple Python tool to analyse your deps file (for example composer.lock in a PHP application) and querying the awesome [OSV vuln database](https://osv.dev/) to check if one of your dependency is affected by a known vulnerability.


## Installation
Python >= 3.7 is advised.

You only need [**requests**](https://fr.python-requests.org/en/latest/) package, which can be installed with **pip**

```shell
curl https://github.com/BaptisteContreras/OSV-Analyser.git
pip install
chmod +x OsvAnalyzer.py
```

## Usage

```shell

python3 OsvAnalyzer.py -a analyze -l PHP -f /path/to/composer.lock

```

When you run the **analyze** action, it generates a cache file for the others actions.


## TODO

- Support for others languages (only PHP is supported for the moment)
- Add visual result display
- Add support for CI/CD
- Add possibility to get more detail about the vulns found
- Add possibility to ignore some vulns