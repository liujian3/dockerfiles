FROM jupyter/base-notebook:9e8682c9ea54

USER jovyan

# Using pip install instead of conda since zipline has conda version issues, see:
# https://github.com/quantopian/zipline/issues/2514

RUN python3 -m pip install --no-cache --upgrade setuptools pip wheel
RUN python3 -m pip install --no-cache zipline TA-Lib alphalens pyfolio
# Add permanent pip/conda installs here
# e.g., RUN conda install -f -y -q -c conda-forge dask=2.6.0



USER root

# Add permanent apt-get installs and other root commands here
# e.g., RUN apt-get install npm nodejs

RUN conda clean --all -y
