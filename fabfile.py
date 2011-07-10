# globals
env.project_name = 'timothyfletcher.com'

def production():
    env.hosts = ['78.129.251.161']
    env.user = 'wind'
    env.path = '/home/%(user)s/workspace/%(project_name)s' % env
    # env.virtualhost_path = env.path


def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/uwsgi reload', pty=True)