#!/bin/bash
echo "Installing poetry"
pip install --upgrade poetry
echo "Installing project requirements"
python -m poetry install
echo "Activating venv"
source ./.venv/bin/activate
pre-commit install
deactivate
