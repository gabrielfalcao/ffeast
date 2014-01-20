ssh_config:
  file.managed:
    - name: /root/.ssh/config
    - source: salt://ffeast/ssh_config
    - makedirs: True

deploykey:
  file.managed:
    - name: /root/.ssh/github
    - source: salt://ffeast/id_rsa
    - makedirs: True
    - mode: 600

publickey:
  file.managed:
    - name: /root/.ssh/github.pub
    - source: salt://ffeast/id_rsa.pub
    - makedirs: True
    - mode: 600


/etc/nginx/conf.d/{{ pillar['app_name'] }}.conf:
  file:
    - managed
    - template: jinja
    - source: salt://ffeast/nginx.conf
    - require:
      - pkg: nginx


/etc/supervisor/conf.d/{{ pillar['app_name'] }}.conf:
  file:
    - managed
    - template: jinja
    - source: salt://supervisor/application.conf
    - require:
      - pkg: supervisor


reread-supervisor:
  cmd.run:
    - name: supervisorctl reread


update-supervisor:
  cmd.run:
    - name: supervisorctl update


reload-supervisor:
  cmd.run:
    - name: supervisorctl reload all


start-{{ pillar['app_name'] }}:
  cmd.run:
    - name: supervisorctl restart {{ pillar['app_name'] }} || echo "running"
