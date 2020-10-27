FROM jupyter/base-notebook:9e8682c9ea54

USER root
RUN apt-get update 
RUN apt-get install -y --no-install-recommends gcc g++ make
RUN apt-get clean
WORKDIR /usr/share
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN tar -xzf ta-lib-0.4.0-src.tar.gz
RUN rm -f ta-lib-0.4.0-src.tar.gz
WORKDIR /usr/share/ta-lib
RUN ./configure --prefix=/usr
RUN make
RUN make install

USER $NB_UID
# Using pip install instead of conda since zipline has conda version issues, see:
# https://github.com/quantopian/zipline/issues/2514
RUN pip install --no-cache pip==9.0.1
RUN pip install --no-cache --upgrade setuptools pip wheel
RUN pip install --no-cache zipline alphalens pyfolio
# Add permanent pip/conda installs here
# e.g., RUN conda install -f -y -q -c conda-forge dask=2.6.0
RUN pip install --no-cache TA-Lib

# Add permanent apt-get installs and other root commands here
# e.g., RUN apt-get install npm nodejs
RUN conda clean --all -y
WORKDIR /home/$NB_USER
