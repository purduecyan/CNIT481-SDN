from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import OVSController

class MyTopo(Topo):
    """
    A simple topology with two hosts and one switch.

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

    Creates an instance of the MyTopo class, initializes the Mininet network with the topology and a default controller,
    starts the network, and opens the Mininet CLI for user interaction. Stops the network after exiting the CLI.
    """
    topo = MyTopo()
    net = Mininet(topo=topo, controller=OVSController)
    net.start()
    CLI(net)
    net.stop()
