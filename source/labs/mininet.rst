*******
Mininet
*******


Introduction to Mininet
=======================

Mininet is a network emulator that creates a network of virtual hosts, switches, controllers, and links. It supports OpenFlow for software-defined networking (SDN) and allows you to run real Linux network software on a single machine [7]_. Mininet is widely used for research, development, learning, prototyping, testing, and debugging network applications [8]_.

Main Features
-------------

1. **Network Emulation**: Mininet creates a network of virtual hosts, switches, controllers, and links, allowing you to run real Linux network software on a single machine [7]_.

2. **OpenFlow Support**: It supports OpenFlow, enabling highly flexible custom routing and software-defined networking (SDN) [3]_.

3. **Lightweight Virtualization**: Mininet uses lightweight containers (network namespaces) instead of full virtual machines, which allows for the creation of large networks with minimal resource consumption [7]_.

4. **Realistic Network Topologies**: You can create realistic network topologies and test them in a controlled environment [2]_.

5. **Extensive CLI and API**: Mininet provides a command-line interface (CLI) and a Python API for easy network creation, management, and automation [2]_.

6. **Integration with Tools**: It integrates well with other network tools like Wireshark for packet analysis and debugging [2]_.


Advanced Features 
-----------------

1. **Custom Topologies**: Mininet allows you to create custom network topologies using Python scripts, enabling complex and specific network configurations [2]_.

2. **Link Variations**: You can emulate different link characteristics such as bandwidth, delay, and packet loss to test network performance under various conditions [2]_.

3. **Multiple Controllers**: Mininet supports multiple controllers, including remote controllers, which allows for testing distributed control scenarios [2]_.

4. **XTerm Integration**: You can open terminal windows for each host and switch, providing a convenient way to interact with the network elements [2]_.

5. **Benchmarking**: Mininet includes benchmarking tools to measure the performance of the network and its components [2]_.


Use Cases
---------

1. **Research and Development**: Enabling experimentation with new network services and protocols, such as OpenFlow case studies [1]_.

2. **Education**: Providing a hands-on learning environment for students to understand networking concepts and SDN [3]_.

3. **Prototyping and Testing**: Allowing developers to prototype and test network applications and configurations before deploying them in a real-world environment [1]_.

4. **Network Function Virtualization (NFV)**: Implementing and testing NFV scenarios, such as virtualized network functions and service chaining [1]_.


Installing Mininet
==================

Mininet runs on Linux-based systems and requires Python and a few other dependencies. This guide will focus on installing Mininet on Ubuntu. For other distributions, refer to the official Mininet documentation [8]_.
Here are the steps to install Mininet on Ubuntu:

1. **Update your package list:**

   .. code-block:: bash

      sudo apt update

2. **Install Mininet:**

   .. code-block:: bash

      sudo apt install mininet

3. Install Open vSwitch Test Controller:

   .. code-block:: bash

      sudo apt install openvswitch-testcontroller

4. **Verify the installation:**

   .. code-block:: bash

      sudo mn --test pingall

This will create a simple network and test connectivity between hosts.



Mininet CLI [9]_
================

Mininet provides a command-line interface (CLI) that allows you to interact with the network elements and perform various operations. The Mininet CLI is a powerful tool for creating, managing, and testing network topologies. Here are some common commands and operations you can perform using the Mininet CLI:


Exercise 1: Basic Commands in Mininet
-------------------------------------

Objective: Learn the basic commands in Mininet.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      $ sudo mn

2. List the nodes in the network:
   
   .. code-block:: bash

      mininet> nodes

3. Display the links in the network:
   
   .. code-block:: bash

      mininet> net

4. Test connectivity between hosts:
   
   .. code-block:: bash

      mininet> pingall


Exercise 2: Teardown and Cleanup
--------------------------------

Objective: Learn how to teardown and cleanup a Mininet network.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      $ sudo mn

2. Stop the network and cleanup resources:
   
   .. code-block:: bash

      mininet> exit

3. Verify that the network has been stopped and resources have been cleaned up.
    
   .. code-block:: bash

      $ sudo mn -c


Exercise 3: Exploring Network Topology
--------------------------------------

Objective: Use Mininet CLI commands to explore the network topology.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      sudo mn

2. Display the network topology:
   
   .. code-block:: bash

      mininet> net

3. List the hosts in the network:
   
   .. code-block:: bash

      mininet> hosts

4. List the switches in the network:
   
   .. code-block:: bash

      mininet> switches

5. List the links in the network:
   
   .. code-block:: bash

      mininet> links


Exercise 4: Running Commands on Hosts
-------------------------------------

Objective: Run various commands on hosts using the Mininet CLI.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      $ sudo mn

2. Run a command on a specific host:
   
   .. code-block:: bash

      mininet> h1 ifconfig

3. Run a ping test between two hosts:
   
   .. code-block:: bash

      mininet> h1 ping -c 3 h2

4. Run a bandwidth test between two hosts:
   
   .. code-block:: bash

      mininet> iperf h1 h2

Exercise 5: Configuring Link Parameters
---------------------------------------

Objective: Configure link parameters such as bandwidth, delay, and loss using the Mininet CLI.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      sudo mn --link tc,bw=10,delay=5ms,loss=1

In the above command, we set the bandwidth to 10 Mbps, delay to 5 ms, and packet loss to 1%.

2. Test connectivity and observe the effects of the link parameters:
   
   .. code-block:: bash

      mininet> pingall

3. Run a bandwidth and latency test between the two hosts:
   
   .. code-block:: bash

      mininet> iperfudp
      mininet> h1 ping -c 10 h2

Exercise 6: Using XTerm for Hosts
---------------------------------

Objective: Open XTerm windows for hosts to interact with them using a graphical interface.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      sudo mn

2. Open an XTerm window for a specific host:
   
   .. code-block:: bash

      mininet> xterm h1

3. Run commands in the XTerm window on the host ``h1``:
   
   .. code-block:: bash

      ifconfig
      ping -c 3 h2

Exercise 7: Capturing Packets with Wireshark
--------------------------------------------

Objective: Capture and analyze network packets using Wireshark.

Steps:
1. Start a simple network topology:
   
   .. code-block:: bash

      sudo mn

2. Start Wireshark on a specific interface:
   
   .. code-block:: bash

      mininet> h1 wireshark &

3. Capture packets and analyze them in Wireshark.



Mininet Python API
==================

Exercise 1: Creating Custom Topologies
--------------------------------------

Objective: Learn how to create custom network topologies in Mininet.

Steps:
1. Create a Python script to define a custom topology:

.. literalinclude:: code/mn/mytopo.py
   :language: python
   :linenos:
   :caption: mytopo.py
   

2. Run the script to start the custom topology:
   
   .. code-block:: bash

      sudo python3 mytopo.py

3. Test connectivity between hosts using the Mininet CLI:
   
   .. code-block:: bash

      mininet> pingall

Exercise 2: Emulating Link Characteristics
------------------------------------------

Objective: Emulate different link characteristics such as bandwidth, delay, and packet loss.

Steps:
1. Create a Python script to define a topology with link characteristics:

.. literalinclude:: code/mn/linktopo.py
   :language: python
   :linenos:
   :caption: linktopo.py
   

1. Run the script to start the topology with link characteristics:
   
   .. code-block:: bash

      sudo python3 linktopo.py

2. Test connectivity and observe the effects of the link characteristics:
   
   .. code-block:: bash

      mininet> pingall

Exercise 3: Using Multiple Controllers
--------------------------------------

Objective: Configure and use multiple controllers in Mininet.

Steps:
1. Create a Python script to define a topology with multiple controllers:
   
.. literalinclude:: code/mn/multicontroller.py
   :language: python
   :linenos:
   :caption: multicontroller.py

2. Run the script to start the topology with multiple controllers:
   
   .. code-block:: bash

      sudo python3 multicontroller.py

3. Test connectivity and observe the behavior with multiple controllers:
   
   .. code-block:: bash

      mininet> pingall


.. note:: Highly Recommended Reading: Mininet Walkthrough [2]_
      
      This guide provides a detailed walkthrough of Mininet, including basic commands, custom topologies, advanced features, and Python API usage. It is an excellent resource for beginners to get started with Mininet.



Advanced Network Topologies
===========================

Mininet allows you to create complex and realistic network topologies using Python scripts. You can define custom topologies, configure link characteristics, use multiple controllers, and integrate with other tools for network analysis and debugging. Here are some examples of advanced network topologies you can create in Mininet:

1. **Fat-Tree Topology**: Implement a fat-tree network topology with multiple switches and hosts.

2. **Spine-Leaf Topology**: Create a spine-leaf network topology with spine and leaf switches.

3. **Data Center Network**: Emulate a data center network with multiple racks, switches, and hosts.

4. **Software-Defined WAN (SD-WAN)**: Implement an SD-WAN topology with multiple sites and controllers.

5. **Network Function Virtualization (NFV)**: Create an NFV topology with virtualized network functions and service chaining.

6. **Internet of Things (IoT) Network**: Simulate an IoT network with edge devices, gateways, and cloud servers.



The following exercises demonstrate how to create advanced network topologies in Mininet using Python scripts:


Exercise 4: Fat Tree Topology
-----------------------------

In this exercise, you will create a fat tree topology in Mininet using a Python script.


The fat tree topology is a network design that enhances the traditional tree structure by increasing the bandwidth at higher levels of the hierarchy. This design helps to eliminate bottlenecks and improve overall network performance.

Key Characteristics
^^^^^^^^^^^^^^^^^^^

1. **Uniform Bandwidth**: Each layer of the network has the same aggregated bandwidth, ensuring that there are no bottlenecks at any point in the network.

2. **Scalability**: Fat tree topologies can scale efficiently, making them suitable for large data centers and high-performance computing environments.

3. **Redundancy and Fault Tolerance**: The multiple paths available in a fat tree topology provide redundancy, enhancing fault tolerance and reliability.

4. **Cost-Effectiveness**: Fat tree networks can be built using commodity switches, which are cheaper and more power-efficient than high-end modular switches.

Applications
^^^^^^^^^^^^

Fat tree topologies are commonly used in data centers and supercomputers to ensure efficient and scalable communication. They are particularly well-suited for environments that require high bandwidth and low latency, such as cloud computing and large-scale scientific simulations.




.. graphviz::
   :caption: Fat Tree Topology, ``k=4``
   :align: center

      digraph FatTree {
         rankdir=LR;
         nodesep=0.2
         node [shape=ellipse];

         // Legend
         subgraph cluster_legend {
            label = "Legend";
            height=0;
            style=invis;
            cs [label="CS: Core Switch", shape=plaintext, height=0.0];
            as [label="AS: Aggregation Switch", shape=plaintext, height=0.0];
            es [label="ES: Edge Switch", shape=plaintext, height=0.0];
            h [label="H: Host", shape=plaintext, height=0.0];
         }

         // Core switches
         subgraph cluster_core {
            label = "Core Layer";
            style=filled;
            color=lightblue;
            CS1 [label="CS1"];
            CS2 [label="CS2"];
            CS3 [label="CS3"];
            CS4 [label="CS4"];
         }

         // Pod 1
         subgraph cluster_pod1 {
            label = "Pod 1";
            style=filled;
            color=lightgrey;
            AS11 [label="AS1-1"];
            AS12 [label="AS1-2"];
            ES11 [label="ES1-1"];
            ES12 [label="ES1-2"];
         }

         // Pod 2
         subgraph cluster_pod2 {
            label = "Pod 2";
            style=filled;
            color=lightgrey;
            AS21 [label="AS2-1"];
            AS22 [label="AS2-2"];
            ES21 [label="ES2-1"];
            ES22 [label="ES2-2"];
         }

         // Pod 3
         subgraph cluster_pod3 {
            label = "Pod 3";
            style=filled;
            color=lightgrey;
            AS31 [label="AS3-1"];
            AS32 [label="AS3-2"];
            ES31 [label="ES3-1"];
            ES32 [label="ES3-2"];
         }

         // Pod 4
         subgraph cluster_pod4 {
            label = "Pod 4";
            style=filled;
            color=lightgrey;
            AS41 [label="AS4-1"];
            AS42 [label="AS4-2"];
            ES41 [label="ES4-1"];
            ES42 [label="ES4-2"];
         }

         // Hosts
         H111 [label="H1-1-1"];
         H112 [label="H1-1-2"];
         H121 [label="H1-2-1"];
         H122 [label="H1-2-2"];
         H211 [label="H2-1-1"];
         H212 [label="H2-1-2"];
         H221 [label="H2-2-1"];
         H222 [label="H2-2-2"];
         H311 [label="H3-1-1"];
         H312 [label="H3-1-2"];
         H321 [label="H3-2-1"];
         H322 [label="H3-2-2"];
         H411 [label="H4-1-1"];
         H412 [label="H4-1-2"];
         H421 [label="H4-2-1"];
         H422 [label="H4-2-2"];

         // Core to Aggregation links
         CS1 -> AS11 [color=red];
         CS1 -> AS21 [color=red];
         CS1 -> AS31 [color=red];
         CS1 -> AS41 [color=red];
         CS2 -> AS12 [color=blue];
         CS2 -> AS22 [color=blue];
         CS2 -> AS32 [color=blue];
         CS2 -> AS42 [color=blue];
         CS3 -> AS11 [color=yellow];
         CS3 -> AS21 [color=yellow];
         CS3 -> AS31 [color=yellow];
         CS3 -> AS41 [color=yellow];
         CS4 -> AS12 [color=cyan];
         CS4 -> AS22 [color=cyan];
         CS4 -> AS32 [color=cyan];
         CS4 -> AS42 [color=cyan];

         // Aggregation to Edge links
         AS11 -> ES11;
         AS11 -> ES12;
         AS12 -> ES11;
         AS12 -> ES12;
         AS21 -> ES21;
         AS21 -> ES22;
         AS22 -> ES21;
         AS22 -> ES22;
         AS31 -> ES31;
         AS31 -> ES32;
         AS32 -> ES31;
         AS32 -> ES32;
         AS41 -> ES41;
         AS41 -> ES42;
         AS42 -> ES41;
         AS42 -> ES42;

         // Edge to Host links
         ES11 -> H111;
         ES11 -> H112;
         ES12 -> H121;
         ES12 -> H122;
         ES21 -> H211;
         ES21 -> H212;
         ES22 -> H221;
         ES22 -> H222;
         ES31 -> H311;
         ES31 -> H312;
         ES32 -> H321;
         ES32 -> H322;
         ES41 -> H411;
         ES41 -> H412;
         ES42 -> H421;
         ES42 -> H422;

         {
            rank = same;
            // Here you enforce the desired order with "invisible" edges and arrowheads
            edge[ style=invis];
            CS1 -> CS2 -> CS3 -> CS4 ;
            rankdir = LR;
         }
      }


Topology Design
^^^^^^^^^^^^^^^

Objective: Create a fat tree topology by extending the ``Topo`` class.

Steps:
1. Create a Python script to define a fat tree topology:


.. literalinclude:: code/mn/fattreetopo.py
   :language: python
   :linenos:
   :caption: fattreetopo.py

2. Run the script with the desired value of ``k``:

   .. code-block:: bash

      sudo python fattreetopo.py 4

3. Use the Mininet CLI to interact with the network:

   .. code-block:: bash

      mininet> pingall

Explanation
-----------

In this exercise, you will create a fat tree topology by extending the ``Topo`` class in Mininet. The parameter ``k`` is made user-configurable by taking it as a command-line argument. The script creates core switches, aggregation switches, edge switches, and hosts, and then links them according to the fat tree design.




Exercise 5: Leaf Spine Topology (Clos)
--------------------------------------

In this exercise, you will create a leaf-spine (Clos) topology in Mininet using a Python script. The leaf-spine topology is a popular network design for data centers that provides high bandwidth, low latency, and fault tolerance. It consists of two layers: leaf switches and spine switches. The leaf switches are connected to the spine switches, and the hosts are connected to the leaf switches. This design allows for non-blocking, full-mesh connectivity between hosts and provides scalability and redundancy. 

.. note:: Switch oversubscription can create bottlenecks in the network. Therefore, the leaf and spine switch configurations should be carefully planned to avoid congestion.


Key Characteristics
^^^^^^^^^^^^^^^^^^^

1. **Scalability**: The leaf-spine topology is highly scalable and can accommodate a large number of hosts and switches.

2. **High Bandwidth**: The full-mesh connectivity between leaf and spine switches ensures high bandwidth and low latency.

3. **Redundancy**: The multiple paths between hosts and switches provide redundancy and fault tolerance.



See the data center network lecture for more information on the leaf-spine topology.


.. graphviz:: 
   :caption: Clos Topology
   :align: center

      digraph LeafSpine {
         rankdir=TB;
         node [shape=ellipse];

         // Spine switches
         subgraph cluster_spine {
            label = "Spine Layer";
            style=filled;
            color=lightblue;
            SP1 [label="Spine 1"];
            SP2 [label="Spine 2"];
         }

         // Leaf switches
         subgraph cluster_leaf {
            label = "Leaf Layer";
            style=filled;
            color=lightgreen;
            LF1 [label="Leaf 1"];
            LF2 [label="Leaf 2"];
            LF3 [label="Leaf 3"];
            LF4 [label="Leaf 4"];
         }

         // Hosts
         H1 [label="Host 1"];
         H2 [label="Host 2"];
         H3 [label="Host 3"];
         H4 [label="Host 4"];
         H5 [label="Host 5"];
         H6 [label="Host 6"];
         H7 [label="Host 7"];
         H8 [label="Host 8"];

         // Spine to Leaf links
         SP1 -> LF1 [dir="both",color=red];
         SP1 -> LF2 [dir="both",color=red];
         SP1 -> LF3 [dir="both",color=red];
         SP1 -> LF4 [dir="both",color=red];
         SP2 -> LF1 [dir="both",color=blue];
         SP2 -> LF2 [dir="both",color=blue];
         SP2 -> LF3 [dir="both",color=blue];
         SP2 -> LF4 [dir="both",color=blue];

         // Leaf to Host links
         LF1 -> H1;
         LF1 -> H2;
         LF2 -> H3;
         LF2 -> H4;
         LF3 -> H5;
         LF3 -> H6;
         LF4 -> H7;
         LF4 -> H8;
      }


Topology Design
^^^^^^^^^^^^^^^

Objective: Create a leaf-spine (Clos) topology by extending the ``Topo`` class.

Steps:
1. **Import Required Libraries**

   First, import the necessary libraries for Mininet and network configuration.

   .. code-block:: python

      from mininet.net import Mininet
      from mininet.node import Controller, OVSSwitch
      from mininet.link import TCLink
      from mininet.cli import CLI
      from mininet.log import setLogLevel, info

2. **Define the Spine-Leaf Topology Class**

   Create a class for the spine-leaf topology. This class will initialize the network and configure the switches and hosts.

   .. code-block:: python

      class SpineLeafTopo:
         def __init__(self, num_ports=2):
            self.num_spines = num_spines
            self.num_leaves = num_leaves
            self.net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)


          def build(self):
               info('*** Adding controller\n')
               self.net.addController('c0')

               info('*** Adding spine switches\n')
               # Add spine switches logic here.

               info('*** Adding leaf switches\n')
               # Add leaf switches logic here.

               info('*** Creating links between spine and leaf switches\n')
               # Add links between spine and leaf switches logic here.

               info('*** Adding hosts and connecting them to leaf switches\n')
               # Add hosts and connect them to leaf switches logic here.

          def start(self):
              self.net.start()
              CLI(self.net)
              self.net.stop()

3. **Run the Topology**

   Instantiate the topology class with user-defined port numbers and build the network.

   .. code-block:: python

      if __name__ == '__main__':
          setLogLevel('info')
          num_ports = int(input("Enter the number of ports for each switch: "))
          topo = SpineLeafTopo(num_ports)
          topo.build()
          topo.start()

4. Run the script with the desired value of ``k``:

   .. code-block:: bash

      sudo python spineleaftopo.py

5. Use the Mininet CLI to interact with the network:

   .. code-block:: bash

      mininet> pingall



Expected Outcome
----------------
By the end of this exercise, you should be able to create a spine-leaf network topology using the Mininet Python API with user-configurable ports for both the spine and leaf switches. You will also gain hands-on experience with Mininet's CLI for network management.






References
----------

.. [1] Network Topology Implementations in Mininet. Available at: https://github.com/CynicDog/network-topology-implementations-in-mininet
.. [2] Mininet Walkthrough. Available at: http://mininet.org/walkthrough/
.. [3] Mininet Blog. Available at: http://mininet.org/blog/
.. [7] Mininet Overview. Available at: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet
.. [8] Mininet Documentation. Available at: https://mininet.org/
.. [9] Introduction to Mininet. Available at: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet








