Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04" 

  config.vm.define "server1" do |server1|
    server1.vm.network "private_network", ip: "10.10.10.11"
    server1.vm.provider "virtualbox" do |server1|
      server1.memory = 1024
    end  
    server1.vm.provision "ansible_local" do |ansible|
      ansible.playbook = 'api/playbook.yml'
      ansible.become = true
      #ansible.verbose = true
    end
  end

  config.vm.define "server2" do |server2|
    server2.vm.network "private_network", ip: "10.10.10.12"
    server2.vm.provider "virtualbox" do |server2|
      server2.memory = 2024
    end  
    server2.vm.provision "ansible_local" do |ansible|
      ansible.playbook = 'zabbix/playbook.yml'
      ansible.become = true
      #ansible.verbose = true
    end
    server2.vm.provision "file", source: "./script/hosts.py", destination: "$HOME//script/hosts.py"
    server2.vm.provision "shell", inline: "python3 /home/vagrant/script/hosts.py"
  end
end
