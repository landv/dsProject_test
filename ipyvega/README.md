# IPython Vega
[![PyPI](https://img.shields.io/pypi/v/vega.svg)](https://pypi.python.org/pypi/vega)
[![Build Status](https://github.com/vega/ipyvega/workflows/Test/badge.svg)](https://github.com/vega/ipyvega/actions)

IPython/Jupyter notebook module for [Vega 5](https://github.com/vega/vega), and [Vega-Lite 4](https://github.com/vega/vega-lite). Notebooks with embedded visualizations can be viewed on [GitHub](https://github.com/vega/ipyvega/blob/master/notebooks/VegaLite.ipynb) and [nbviewer](https://nbviewer.jupyter.org/github/vega/ipyvega/blob/master/notebooks/VegaLite.ipynb). If you use JupyterLab (not the notebook), you don't need to install this extension since JupyterLab comes with built-in support for Vega and Vega-Lite.

Available on [pypi](https://pypi.python.org/pypi/vega) and [Conda Forge](https://anaconda.org/conda-forge/vega) as `vega`.

<img src="screenshot.png" width="500">

## Install and run

### Python Package Index

To install `vega` and its dependencies from the Python Package Index using
`pip`, use the following commands:

```sh
pip install jupyter pandas vega
pip install --upgrade notebook  # need jupyter_client >= 4.2 for sys-prefix below
jupyter nbextension install --sys-prefix --py vega  # not needed in notebook >= 5.3
```

### Conda Forge

If you use Conda, you probably already have the latest versions of the notebook and pandas installed. To install `vega` extension run:

```sh
conda install vega
```

## Usage

Once the package is installed, run
```sh
jupyter notebook
```
to launch the Jupyter notebook server, and use `vega` within the notebook.
See the example notebooks for [Vega-Lite](https://github.com/vega/ipyvega/blob/master/notebooks/VegaLite.ipynb) and [Vega](https://github.com/vega/ipyvega/blob/master/notebooks/Vega.ipynb).

To run the notebooks yourself, you need to get the file [`cars.json`](https://raw.githubusercontent.com/vega/ipyvega/master/notebooks/cars.json).


## Developers

This project uses [Poetry](https://python-poetry.org/). If you prefer a local virtual environment, run `poetry config virtualenvs.in-project true` first. Install requirements: `poetry install`.

Then activate the virtual environment with `poetry shell`.

Symlink files instead of copying files:

```sh
jupyter nbextension install --py --symlink vega
```

Run kernel with `jupyter notebook`. Run the tests with `pytest vega`.

To rebuild the JavaScript continuously, run `yarn watch`.

### How to make a release

* Update the JavaScript dependencies by changing `package.json` (e.g. with [ncu](https://www.npmjs.com/package/npm-check-updates)).
* Run `yarn`.
* Rebuild the JavaScript with `yarn build`.
* Make sure that everything still works (launch notebook and try the examples).
* Update the version number in `pyproject.toml` (with `poetry version [VERSION]`), `package.json`, and `__init__.py` and add a git tag.
* `git push --tags`.
* Then run `poetry publish --build` to update https://pypi.python.org/pypi/vega.

The Conda feedstock for this package is at https://github.com/conda-forge/vega-feedstock. It should update automatically but we may need to merge a pull request with the updates. 
