FROM jupyterhub/jupyterhub
#USER root
RUN python3 -m pip install --no-cache --upgrade setuptools pip wheel
RUN python3 -m pip install --no-cache jupyterhub-ldapauthenticator dockerspawner
#USER $NB_UID
