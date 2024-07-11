## Installing repository requirements
When using this repo, it is necessary to install some packages. As a default, this repo will require you to install pre-commit & ruff. It is likely that your code will fail automated pull review checks if you do not install these.

To assist the creation of your virtual environment for this project, there are two scripts in `utils`, one for Unix systems (`bash`) and one for Windows (`PowerShell`).

### On Windows:
```console
.\utils\setup_venv.ps1
```
### On Unix
```sh
source ./utils/setup_venv.sh
```
These will set up Poetry (for package management) and a virtual environment with all the required dependencies in your repo's directory called `.venv`. Additionally, it will install your pre-commit hooks and activate your virtual environment.


## Adding (main) Branch Protection

When using a GitHub repository, you should use branch protection to ensure that no-one is able to make changes to your ```main``` branch without first having their code review by another person in a pull request. Do enable branch protection, a repo admin should first navigate to the branch protection under settings: 
![image](https://github.com/dsit-advanced-analytics/python-repo-template/assets/104204485/032e4134-ecd7-427c-8b9d-3429510433da)

Then click "Add branch protection rule". You will then need to type in the name of your branch - in this example we have used ```main```. Tick the option requiring a pull request before merging. There are a range of other options you may want to tick, feel free to use and experiment with them to meet your specific project needs. 
![image](https://github.com/dsit-advanced-analytics/python-repo-template/assets/104204485/2772ddbd-630f-41e6-9be8-f169ef08b6e6)





## Documentation
This repo uses Sphinx to automatically generate documentation which is hosted locally. You can access this documentation locally by using:

### On Windows:

```console
.\utils\open_docs.ps1
```

### On Unix
```sh
source ./utils/open_docs.sh
```

When code is approved after a PR, a GitHub action will run to update documentation based on the docStrings within your codebase. Consult the README.md in the doc subfolder. 
