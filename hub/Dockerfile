FROM jupyterhub/jupyterhub

USER root

RUN pip install --upgrade pip \
 && pip install jupyterhub-ldapauthenticator
 && pip install dockerspawner
 && pip install jupyterhub-systemdspawner

USER $NB_UID
