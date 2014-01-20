# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"

  config.vm.provision :salt do |salt|
    salt.always_install = true
    salt.verbose = true

    salt.minion_config = "deploy/minion.conf"
    salt.run_highstate = true  # change to true if you want
                                # `vagrant up` to automatically provision
  end

  config.vm.network :private_network, ip: "192.168.42.2"
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8000, host: 8000

  config.cache.auto_detect = true

  config.vm.synced_folder "deploy/salt", "/srv/salt", :nfs => true
  config.vm.synced_folder "deploy/pillar", "/srv/pillar", :nfs => true

  config.vm.provider :virtualbox do |vb|
    vb.gui = false
  end

  config.vm.provider :aws do |aws, override|

    aws.access_key_id = ENV['AWS_ACCESS_KEY_ID']
    aws.secret_access_key = ENV['AWS_SECRET_ACCESS_KEY']
    aws.keypair_name = "weedlabs-master"

    aws.ami = "ami-a73264ce"
    aws.security_groups = ['sg-b5e0a7de', 'sg-7580be1e']

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "~/.ssh/weedlabs-master.pem"
  end
end


# to run masterless:
# vagrant ssh
# salt-call --local state.highstate -l debug
