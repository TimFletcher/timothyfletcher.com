from fabric.api import *

env.project_name = 'timothyfletcher.com'
env.hosts = ['78.129.251.161:32214']
env.user = 'wind'
env.path = '/home/{user}/www/{project_name}'.format(**env)

def update():
    with cd(env.path):
        run('git pull')
    restart_webserver()

# -------------------------
# --- Utility functions ---
# -------------------------

def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/uwsgi reload')
