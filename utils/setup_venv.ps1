Write-Output "Installing poetry"
pip install --upgrade poetry
Write-Output "Installing project requirements"
python -m poetry install
Write-Output "Activating venv"
.\.venv\Scripts\activate
#pre-commit install
deactivate
