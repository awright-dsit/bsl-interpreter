import json
import os
import subprocess


def create_notebook_with_output():
    """Create a Jupyter notebook with output cells."""
    notebook_content = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": ["Hello, world!\n"],
                    }
                ],
                "source": ["print('Hello, world!')\n"],
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.10",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    with open("tests/test_notebook.ipynb", "w") as f:
        json.dump(notebook_content, f, indent=1)


def test_nbstripout():
    """Test nbstripout hook."""
    create_notebook_with_output()

    # Run nbstripout on the notebook
    subprocess.run(["nbstripout", "tests/test_notebook.ipynb"], check=True)

    # Check if outputs have been stripped
    with open("tests/test_notebook.ipynb") as f:
        notebook_data = json.load(f)
        for cell in notebook_data["cells"]:
            if "outputs" in cell:
                outputs = cell["outputs"]
                if any(
                    output.get("output_type") == "stream"
                    and output.get("name") == "stdout"
                    for output in outputs
                ):
                    raise AssertionError(
                        "Outputs were not stripped successfully"
                    )

    print("nbstripout hook test passed successfully")

    # Remove the notebook file after the test
    os.remove("tests/test_notebook.ipynb")
    print("Removed test_notebook.ipynb")


if __name__ == "__main__":
    test_nbstripout()
