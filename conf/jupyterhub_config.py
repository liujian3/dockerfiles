c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.server_address = 'x.x.x.x'

c.LDAPAuthenticator.lookup_dn = True
c.LDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
c.LDAPAuthenticator.lookup_dn_search_user = 'xdn'
c.LDAPAuthenticator.lookup_dn_search_password = 'xpassword'
c.LDAPAuthenticator.user_search_base = 'ydn'
c.LDAPAuthenticator.user_attribute = 'sAMAccountName'
c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'
c.LDAPAuthenticator.escape_userdn = False
#c.LDAPAuthenticator.bind_dn_template = '{username}'

c.Spawner.default_url = '/lab'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jh'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = 'jupyter/base-notebook'

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub'

# delete containers when the stop

c.DockerSpawner.remove = True
