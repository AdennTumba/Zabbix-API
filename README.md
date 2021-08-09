Projeto 
=========

O Projeto tem o objetivo de criar uma solução automatizada que hospede uma API no mesmo servidor do Zabbix ou
outro para consumir o serviço dos correios e retornar para o usuário os dados solicitados. Monitorar o servidor web / API desenvolvida com a ferramenta Zabbix.


Instalação
------------
<pre>
<b>Instala virtualbox</b>
Siga o passo a passo: https://www.virtualbox.org/wiki/Linux_Downloads

<b>Instala o Vagrant</b>
apt get install vagrant

<b>Clona o projeto</b>
git clone https://github.com/viniciustbitencourt/crud-apizabbix.git
</pre>

Como usar
--------------
* Acessa o diretorio raiz do repositório baixado
<pre>
<b>Em seu terminal usa o seguinte comando: </b>

vagrant up
</pre>

Comandos Essenciais 
------------
<pre>
vagrant up (Para subir as Máquinas Virtuais )
vagrant destroy (Para destruir as Máquinas Virtuais)
vagrant ssh (Para acessar uma Máquina Virtual)
  - ex: vagrant ssh < nome da máquina virtual >
</pre>

License
-------

MIT License

Informação do Autor
-------------------
I am a Cloud Computing enthusiast and IaC, I love contribute and help environments with infrastructure automation.

