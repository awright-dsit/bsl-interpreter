"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
-- Project information -----------------------------------------------------
"""

import os
import sys


def read_poetry_dependencies(file_path):
    # Initialize an empty dictionary to store the dependencies
    dependencies = {}

    # Open the file and read its contents
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Flag to check if we are in the [tool.poetry.dependencies] section
    in_dependencies_section = False

    for line in lines:
        # If we encounter [tool.poetry.dependencies], we start reading the dependencies
        if "[tool.poetry.dependencies]" in line:
            in_dependencies_section = True
            continue

        # If we encounter another section, we stop reading
        if line.startswith("[") and in_dependencies_section:
            break

        # If we are in the dependencies section, we read the dependencies
        if in_dependencies_section:
            if "=" in line:
                package, version = line.split("=")
                dependencies[package.strip()] = version.strip()

    return dependencies


lib_folder = os.path.dirname(os.path.abspath(os.path.join("..")))
requirement_path = lib_folder + "/pyproject.toml"

install_requires = read_poetry_dependencies(requirement_path)

sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "src")))

root_doc = "repo_documentation"

project = "python-template"
copyright = "2024, Advanced-Analytics"
author = "cameron-currie"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_togglebutton",
]
exclude_patterns = ["_build", ".github", "*_test.py", "_*.py"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

autosectionlabel_prefix_document = True

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented_params"
autodoc_mock_imports = install_requires
napoleon_include_init_with_doc = True

# -- Options for HTML output -------------------------------------------------

repo_link = "https://github.com/dsit-advanced-analytics/python-repo-template"

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": repo_link,
    "use_repository_button": True,
    "home_page_in_toc": True,
    "toc_title": "Components in this Module",
    "show_toc_level": 2,
    "use_issues_button": True,
    "use_fullscreen_button": False,
    "repository_branch": "main",
}

html_title = "python-template"
html_last_updated_fmt = ""
html_show_copyright = True
