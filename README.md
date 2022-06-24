# Git Tools

## pre-commit

First create [.pre-commit-config.yaml](./.pre-commit-config.yaml)

```bash
pip install pre-commit
```
after staging files `git add [filename]`

    pre-commit run --all-files
it will check all files based on hooks defined in `.pre-commit-config.yaml` and fix mistakes.

```
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check for added large files..............................................Passed
seed isort known_third_party.............................................Passed
```
<hr>
automatically find and install setup.cfg or setup.py

```bash
pip install -e .
```
