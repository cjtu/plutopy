# The plutopy repository
Welcome to the **plutopy** Python package! This example package is intended to show you how to craft a Python research package and release it to the community. It also contains examples of planetary image analysis, and reproducible Jupyter notebooks which are a great tool for communicating your research code and analysis.

## Overview
Plutopy is a data analysis package which contains Python functions to download, visualize and manipulate an image of Pluto.

## Tutorial
See the Jupyter Notebook tutorial for the **plutopy** Python package [here](./plutopy/jupyter_notebooks/tutorial.ipynb). This tutorial will be updated as more functions are added to Plutopy.

## Data attribution
The image used is the *Pluto New Horizons Global Mosaic 300m July 2017*. The data was collected by [Moore et al. 2016](https://arxiv.org/abs/1604.05702) and made available by the U.S. Geologic Survey [here](https://astrogeology.usgs.gov/search/map/Pluto/NewHorizons/Pluto_NewHorizons_Global_Mosaic_300m_Jul2017). The first time you import **plutopy**, it will download the image for you.

## Processing
The image handling is done with Python bindings for [GDAL](https://www.gdal.org/index.html), features of interest are read in with [Pandas](https://pandas.pydata.org/pandas-docs/stable/), the analysis is done with [numpy](http://www.numpy.org/) and [scipy](https://www.scipy.org/about.html), and the plotting is done with [matplotlib](https://matplotlib.org/). The tutorial and worked examples are written in [Jupyter](http://jupyter.org/) notebooks. All of these packages are installed and managed with the [Anaconda](https://www.anaconda.com/) package manager.

Some useful tutorials/documentation on the above packages:

- [Getting started with conda](https://conda.io/docs/user-guide/getting-started.html)
- [Python GDAL/OGR Cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/)
- [10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)
- [Numpy Quickstart tutorial](https://docs.scipy.org/doc/numpy-1.15.0/user/quickstart.html)
- [Scipy Tutorials](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html)
- [Matplotlib.pyplot Tutorial](https://matplotlib.org/users/pyplot_tutorial.html)
- [Running the Jupyter Notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html)
