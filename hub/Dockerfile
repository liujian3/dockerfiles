FROM jupyterhub/jupyterhub

USER root

RUN pip3 install --upgrade pip3 \
 && pip3 install jupyterhub-ldapauthenticator
 && pip3 install dockerspawner
 && pip3 install jupyterhub-systemdspawner

USER $NB_UID
