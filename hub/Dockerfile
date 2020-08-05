FROM jupyterhub/jupyterhub

USER root

RUN python3 -m pip install --upgrade setuptools pip wheel
RUN python3 -m pip install jupyterhub-ldapauthenticator dockerspawner

USER $NB_UID
