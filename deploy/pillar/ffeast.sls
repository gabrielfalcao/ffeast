app_name: ffeast
user: ubuntu

repository: git@github.com:weedlabs/ffeast.git
revision: master

base_path: "/srv"

app_path: "/srv/app"
static_path: "/srv/app/ffeast/static"

etc_path: "/srv/etc"

venv_path: "/srv/venv"

prefix_path: "/srv/usr"
bin_path: "/srv/usr/bin"
lib_path: "/srv/usr/lib"

log_path: "/var/log"

github_users:
  - gabrielfalcao
  - alscardoso
  - clarete

environment:
  PORT: "8000"
  LOGLEVEL: "DEBUG"
  HOST: "ffeast.weedlabs.io"
  DOMAIN: "ffeast.weedlabs.io"
  REDIS_URI: "redis://localhost:6379"
  PATH: "/srv/venv/bin:$PATH"
  PYTHONPATH: "/srv/app:/src/venv:/src/venv/lib/python2.7:$PYTHONPATH"
