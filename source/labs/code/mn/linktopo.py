from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.node import OVSController

class LinkTopo(Topo):
    """
    A topology with two hosts and one switch, using TCLink to specify link parameters.

    Methods
    -------
    build():
        Builds the network topology by adding hosts and switches and linking them with specified parameters.
    """
    def build(self):
        """
        Build the network topology.

        Adds two hosts and one switch, then creates links between the hosts and the switch with specified bandwidth, delay, and packet loss.
        """
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1, cls=TCLink, bw=10, delay='5ms', loss=1)
        self.addLink(h2, s1, cls=TCLink, bw=10, delay='5ms', loss=1)

if __name__ == '__main__':
    """
    Main function to create and start the Mininet network.

    Creates an instance of the LinkTopo class, initializes the Mininet network with the topology, TCLink for link parameters, and a default controller.
    Starts the network, opens the Mininet CLI for user interaction, and stops the network after exiting the CLI.
    """
    topo = LinkTopo()
    net = Mininet(topo=topo, link=TCLink, controller=OVSController)
    net.start()
    CLI(net)
    net.stop()
