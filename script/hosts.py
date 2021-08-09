from pyzabbix import ZabbixAPI
api = ZabbixAPI ("http://10.10.10.12")
api.login("Admin", "zabbix")

# Cria um host
host = api.host.create (
{
        "host": "API - Server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "10.10.10.11",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }]
}
)

# Teste de conexão do Server API
item = api.item.create (
    {
        "name": "Teste de conexão",
        "key_": "agent.ping",
        "hostid": "10416",
        "type": 0,
        "interfaceid": "2",
        "value_type": 3,
        "delay": "1m",   
    }
)

####### Memória RAM #########
# Quantidade de memoria ram 

qmram = api.item.create (
    {
        "name": "Quantidade de memória disponível",
        "key_": "vm.memory.size[available]",
        "hostid": "10416",
        "type": 0,
        "interfaceid": "2",
        "value_type": 3,
        "units": "M",
        "delay": "1m",
        "description": "",   
    }
)

# Percentual de memória disponível 
pmram = api.item.create (
    {
        "name": "Percentual de memória disponível",
        "key_": "vm.memory.size[inactive]",
        "hostid": "10416",
        "type": 0,
        "interfaceid": "2",
        "value_type": 3,
        "units": "%",
        "delay": "1m",
        "description": "",   
    }
)

# Média de memória utilizada
mmram = api.item.create (
    {
        "name": "Média de memória utilizada",
        "key_": "vm.memory.[pused]",
        "hostid": "10416",
        "type": 0,
        "interfaceid": "2",
        "value_type": 0,
        "units": "%",
        "delay": "1m",
        "description": "",   
    }
)



############# Disco ##############
# Quantidade de volume disponível em disco
qtddisk = api.item.create (
    {
        "name": "Quantidade de volume disponível em disco",
        "key_": "vfs.fs.size[/,free]",
        "hostid": "10416",
        "type": 0,
        "value_type": 3,
        "units": "G",
        "interfaceid": "2",
        "delay": "1m",
        "description": "",
    }
)



############# Processos #############
# Quantidade de processos associados ao zabbix
qtdproczb = api.item.create (
    {
        "name": "Quantidade de processos associados ao zabbix",
        "key_": "proc.num[zabbix]",
        "hostid": "10416",
        "type": 0,
        "value_type": 3,
        "interfaceid": "2",
        "delay": "1m",
        "description": "Este item mede a Quantidade de processos associados ao zabbix",
    }
)


# Quantidade de memória utilizada pelo serviço do zabbix
qtdmemzb = api.item.create (
    {
        "name": "Quantidade de memória utilizada pelo serviço do zabbix",
        "key_": "proc.mem[zabbix]",
        "hostid": "10416",
        "type": 0,
        "value_type": 3,
        "units": "M",
        "interfaceid": "2",
        "delay": "1m",
        "description": "",
    }
)


# Quantidade de memória utilizada pelo serviço da API
qtdmemapi = api.item.create (
    {
        "name": "Quantidade de memória utilizada pelo serviço da API",
        "key_": "proc.mem[nginx]",
        "hostid": "10416",
        "type": 0,
        "value_type": 3,
        "units": "M",
        "interfaceid": "2",
        "delay": "1m",
        "description": "",
    }

)

####### CPU #########
# Quantidade de CPU em Uso

qtdcpu = api.item.create (
    {
        "name": "Quantidade de CPU em uso",
        "key_": "system.cpu.util[,user]",
        "hostid": "10416",
        "type": 0,
        "interfaceid": "2",
        "value_type": 0,
        "units": "%",
        "delay": "1m",
        "description": "",   
    }
)

############# Serviços #############
# Média do tempo de resposta da API
timeapi = api.item.create (
    {
        "name": "Média do tempo de resposta da API",
        "key_": "net.tcp.service.perf[http,10.10.10.11,80]",
        "hostid": "10416",
        "type": 0,
        "value_type": 0,
        "units": "s",
        "interfaceid": "2",
        "delay": "1m",
        "description": "",
    }
)

############# Triggers #############
# Aumento de memória em mais de 65%
aumem = api.trigger.create (
    {
        "description": "Aumento de memória em mais de 65%",
        "expression": "{API - Server:vm.memory.size[available].count(#1)}>65",
        "priority": "3",
    }
)

# Aumento de disco em mais de 70%
audisk = api.trigger.create (
    {
        "description": "Aumento de disco em mais de 70%",
        "expression": "{API - Server:vfs.fs.size[/,free].count(#1)}>70",
        "priority": "3",
    }
)

# Quantidade de CPU em Uso
aucpu = api.trigger.create (
    {
        "description": "Quantidade de CPU em Uso",
        "expression": "{API - Server:system.cpu.util[,user].count(1)}>85",
        "priority": "4",
    }
)

print (item)
print (host)
print (qmram)
print (pmram)
print (mmram)
print (qtddisk)
print (qtdmemzb)
print (qtdmemapi)
print (qtdcpu)
print (timeapi)
print (aumem)
print (audisk)
print (aucpu)
