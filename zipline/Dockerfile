FROM jupyter/base-notebook:9e8682c9ea54

USER jovyan

# Using pip install instead of conda since zipline has conda version issues, see:
# https://github.com/quantopian/zipline/issues/2514
RUN apt-get update 
RUN apt-get install gcc g++ make
RUN apt-get clean
RUN pip install --no-cache pip==9.0.1
RUN pip install --no-cache --upgrade setuptools pip wheel
RUN pip install --no-cache zipline alphalens pyfolio
# Add permanent pip/conda installs here
# e.g., RUN conda install -f -y -q -c conda-forge dask=2.6.0
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN cd ta-lib/
RUN ./configure --prefix=/usr
RUN make
RUN make install
RUN rm -f ta-lib-0.4.0-src.tar.gz
RUN pip install --no-cache TA-Lib

USER root

# Add permanent apt-get installs and other root commands here
# e.g., RUN apt-get install npm nodejs

RUN conda clean --all -y
