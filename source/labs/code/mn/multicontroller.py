from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

class MultiControllerTopo(Topo):
    """
    A topology with two hosts and one switch, using multiple remote controllers.

    Methods
    -------
    build():
        Builds the network topology by adding hosts and switches and linking them.
    """
    def build(self):
        """
        Build the network topology.

        Adds two hosts and one switch, then creates links between the hosts and the switch.
        """
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

if __name__ == '__main__':
    """
    Main function to create and start the Mininet network.

    Creates an instance of the MultiControllerTopo class, initializes the Mininet network with the topology and two remote controllers.
    Starts the network, opens the Mininet CLI for user interaction, and stops the network after exiting the CLI.
    """
    topo = MultiControllerTopo()
    c0 = RemoteController('c0', ip='127.0.0.1', port=6633)
    c1 = RemoteController('c1', ip='127.0.0.1', port=6634)
    net = Mininet(topo=topo, controllers=[c0, c1])
    net.start()
    CLI(net)
    net.stop()
