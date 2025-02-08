import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class FatTreeTopo(Topo):
    """
    A fat tree topology with a configurable number of pods.

    Methods
    -------
    build(k=4):
        Builds the network topology by adding core, aggregation, and edge switches, and hosts, and linking them.
    """
    def build(self, k=4):
        """
        Build the network topology.

        Parameters
        ----------
        k : int, optional
            The number of pods in the fat tree topology (default is 4).

        Creates core switches, aggregation switches, edge switches, and hosts, and links them according to the fat tree design.
        """
        core_switches = []
        agg_switches = []
        edge_switches = []
        hosts = []

        # Create core switches
        for i in range((k//2)**2):
            core_switches.append(self.addSwitch(f'cs{i+1}'))

        # Create aggregation and edge switches
        for pod in range(k):
            agg_switches.append([])
            edge_switches.append([])
            for i in range(k//2):
                agg_switches[pod].append(self.addSwitch(f'as{pod+1}{i+1}'))
                edge_switches[pod].append(self.addSwitch(f'es{pod+1}{i+1}'))

        # Create hosts and link them to edge switches
        for pod in range(k):
            hosts.append([])
            for i in range(k//2):
                hosts[pod].append([])
                for j in range(k//2):
                    host = self.addHost(f'h{pod+1}{i+1}{j+1}')
                    hosts[pod][i].append(host)
                    self.addLink(host, edge_switches[pod][i])

        # Connect edge switches to aggregation switches
        for pod in range(k):
            for i in range(k//2):
                for j in range(k//2):
                    self.addLink(edge_switches[pod][i], agg_switches[pod][j])

        # Connect aggregation switches to core switches
        for i in range(k//2):
            for j in range(k//2):
                for pod in range(k):
                    self.addLink(agg_switches[pod][i], core_switches[i*(k//2)+j])

if __name__ == '__main__':
    """
    Main function to create and start the Mininet network.

    Checks if the correct number of command-line arguments is provided. If not, prints usage instructions and exits.
    Creates an instance of the FatTreeTopo class with a specified number of pods (k), initializes the Mininet network with the topology,
    starts the network, opens the Mininet CLI for user interaction, and stops the network after exiting the CLI.
    """
    if len(sys.argv) != 2:
        print("Usage: sudo python fattreetopo.py <k>")
        sys.exit(1)

    k = int(sys.argv[1])
    topo = FatTreeTopo(k=k)
    net = Mininet(topo=topo)
    net.start()
    CLI(net)
    net.stop()
