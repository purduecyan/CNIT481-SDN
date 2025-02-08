from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info


class SpineLeafTopo:
    def __init__(self, num_spines=2, num_leaves=2):
        self.num_spines = num_spines
        self.num_leaves = num_leaves
        self.net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)

    def build(self):
        info('*** Adding controller\n')
        self.net.addController('c0')

        info('*** Adding spine switches\n')
        spines = [self.net.addSwitch(f's{i+1}') for i in range(self.num_spines)]

        info('*** Adding leaf switches\n')
        leaves = [self.net.addSwitch(f'l{i+1}') for i in range(self.num_leaves)]

        info('*** Creating links between spine and leaf switches\n')
        for spine in spines:
            for leaf in leaves:
                self.net.addLink(spine, leaf)

        info('*** Adding hosts and connecting them to leaf switches\n')
        for i, leaf in enumerate(leaves):
            host = self.net.addHost(f'h{i+1}')
            self.net.addLink(host, leaf)

    def start(self):
        self.net.start()
        CLI(self.net)
        self.net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    num_spines = int(input("Enter the number of spine switches: "))
    num_leaves = int(input("Enter the number of leaf switches: "))
    topo = SpineLeafTopo(num_spines, num_leaves)
    topo.build()
    topo.start()
