*********************
Open vSwitch
*********************

This tutorial provides a set of exercises to help you learn and teach Open vSwitch (OVS). It includes installation instructions for Ubuntu, commonly used commands, and a CLI cheat sheet.

.. contents::
   :local:
   :depth: 2


Installation
============

To install Open vSwitch on Ubuntu, follow these steps:

.. code-block:: bash

   sudo apt update
   sudo apt install openvswitch-switch

Verify the installation:

.. code-block:: bash

   sudo systemctl status openvswitch-switch


Commonly Used Commands
======================

Here are some commonly used Open vSwitch commands:

.. code-block:: bash
    :linenos:

    # Show Open vSwitch version
    ovs-vsctl --version

    # Show current configuration
    ovs-vsctl show

    # List all bridges
    ovs-vsctl list-br

    # Add a new bridge
    ovs-vsctl add-br br0

    # Add a port to a bridge
    ovs-vsctl add-port br0 eth0

    # Delete a bridge
    ovs-vsctl del-br br0


CLI Cheat Sheet
===============

This cheat sheet provides a quick reference to the most commonly used Open vSwitch commands:

.. code-block:: bash
    :linenos:

    # Configuration commands
    ovs-vsctl add-br <bridge>          # Create a bridge
    ovs-vsctl del-br <bridge>          # Delete a bridge
    ovs-vsctl add-port <bridge> <port> # Add a port to a bridge
    ovs-vsctl del-port <bridge> <port> # Delete a port from a bridge

    # Monitoring commands
    ovs-vsctl show                     # Show current configuration
    ovs-vsctl list-br                  # List all bridges
    ovs-vsctl list-ports <bridge>      # List all ports on a bridge

    # OpenFlow commands
    ovs-ofctl show <bridge>            # Show OpenFlow information
    ovs-ofctl dump-flows <bridge>      # Dump all flows on a bridge
    ovs-ofctl add-flow <bridge> <flow> # Add a flow to a bridge
    ovs-ofctl del-flows <bridge>       # Delete all flows on a bridge


OVS Basic Configuration
=======================

The following exercises provide hands-on practice with Open vSwitch:


Exercise 1: Basic Configuration
-------------------------------

1. Create a new bridge named ``br0``:

   .. code-block:: bash

      ovs-vsctl add-br br0

2. Add a port named ``eth0`` to the bridge ``br0``:

   .. code-block:: bash

      ovs-vsctl add-port br0 eth0

3. Verify the configuration:

   .. code-block:: bash

      ovs-vsctl show

Exercise 2: OpenFlow Configuration
----------------------------------

1. Show OpenFlow information for the bridge ``br0``:

   .. code-block:: bash

      ovs-ofctl show br0

2. Add a flow to the bridge ``br0``:

   .. code-block:: bash

      ovs-ofctl add-flow br0 "in_port=1,actions=output:2"

3. Verify the flow:

   .. code-block:: bash

      ovs-ofctl dump-flows br0




OVS Advanced Configuration
==========================

This section provides detailed explanations for the configuration commands used in Open vSwitch (OVS) along with examples for each advanced feature.


1. Flow Monitoring and Visibility
---------------------------------

This exercise will guide you through the process of setting up flow monitoring and visibility using Open vSwitch (OVS). You will learn how to use sFlow, NetFlow, and IPFIX to monitor network traffic and analyze flow data.

**Objective**: Configure flow monitoring and visibility using sFlow, NetFlow, and IPFIX on Open vSwitch.


Enabling sFlow
^^^^^^^^^^^^^^

sFlow is a protocol for monitoring network traffic. It provides visibility into inter-VM communication and detailed traffic analysis.

1. **Create a Bridge**:
   
   .. code-block:: bash

      ovs-vsctl add-br br0

   Explanation: This command creates a new bridge named ``br0``.

2. **Enable sFlow on the Bridge**:
   
   .. code-block:: bash

      ovs-vsctl -- --id=@sflow create sflow agent=eth0 target=\"192.168.1.1:6343\" \
      sampling=64 polling=10 -- set bridge br0 sflow=@sflow

   Explanation: This command creates an sFlow configuration with the specified agent, target, sampling rate, and polling interval, and then applies it to the bridge ``br0``.

3. **Verify sFlow Configuration**:
   
   .. code-block:: bash

      ovs-vsctl list sflow

   Explanation: This command displays the current sFlow configuration.


Enabling NetFlow
^^^^^^^^^^^^^^^^

NetFlow is another protocol supported by Open vSwitch for traffic analysis.

1. **Enable NetFlow on the Bridge**:
   
   .. code-block:: bash

      ovs-vsctl -- --id=@netflow create netflow targets=\"192.168.1.1:2055\" \
      active-timeout=60 -- set bridge br0 netflow=@netflow

   Explanation: This command creates a NetFlow configuration with the specified target and active timeout, and then applies it to the bridge ``br0``.

2. **Verify NetFlow Configuration**:
   
   .. code-block:: bash

      ovs-vsctl list netflow

   Explanation: This command displays the current NetFlow configuration.


Enabling IPFIX
^^^^^^^^^^^^^^

IPFIX (IP Flow Information Export) is a protocol for exporting flow information from routers, switches, and other devices.

1. **Enable IPFIX on the Bridge**:
   
   .. code-block:: bash

      ovs-vsctl -- --id=@ipfix create ipfix targets=\"192.168.1.1:4739\" \
      sampling=128 -- set bridge br0 ipfix=@ipfix

   Explanation: This command creates an IPFIX configuration with the specified target and sampling rate, and then applies it to the bridge ``br0``.

2. **Verify IPFIX Configuration**:
   
   .. code-block:: bash

      ovs-vsctl list ipfix

   Explanation: This command displays the current IPFIX configuration.


Monitoring OpenFlow Flows
^^^^^^^^^^^^^^^^^^^^^^^^^

OpenFlow is a protocol used by Open vSwitch to manage and control the flow of network traffic.

1. **Display OpenFlow Flows**:
   
   .. code-block:: bash

      ovs-ofctl dump-flows br0

   Explanation: This command displays all the OpenFlow flows configured on the bridge ``br0``.

2. **Add an OpenFlow Rule**:
   
   .. code-block:: bash

      ovs-ofctl add-flow br0 "priority=100,in_port=1,actions=output:2"

   Explanation: This command adds an OpenFlow rule to forward traffic from port 1 to port 2.

3. **Verify the OpenFlow Rule**:
   
   .. code-block:: bash

      ovs-ofctl dump-flows br0

   Explanation: This command displays the current OpenFlow rules on the bridge ``br0``.


Using OVS-DPCTL for Datapath Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``ovs-dpctl`` command is used to monitor and manage Open vSwitch datapaths.

1. **Display Datapath Statistics**:
   
   .. code-block:: bash

      ovs-dpctl show

   Explanation: This command displays statistics for all datapaths.

2. **Display Port Statistics**:
   
   .. code-block:: bash

      ovs-dpctl dump-ports br0

   Explanation: This command displays statistics for all ports on the bridge ``br0``.


This exercise demonstrates how to set up flow monitoring and visibility using sFlow, NetFlow, and IPFIX on Open vSwitch. By following these steps, you can effectively monitor network traffic and analyze flow data to gain insights into network performance and behavior.





2. Link Aggregation
-------------------

**LACP (IEEE 802.1AX-2008)**: Link Aggregation Control Protocol allows for the bundling of multiple physical links into a single logical link to increase bandwidth and provide redundancy.This exercise will guide you through the process of setting up link aggregation with LACP (Link Aggregation Control Protocol) using Open vSwitch (OVS). You will learn how to configure LACP to aggregate multiple network interfaces into a single logical link to increase bandwidth and provide redundancy.


**Objective**: Configure link aggregation with LACP on Open vSwitch to combine multiple network interfaces into a single logical link.

Prerequisites
^^^^^^^^^^^^^

Before starting, ensure you have the following:

- Open vSwitch installed on your system.
- Two or more network interfaces available for aggregation.
- A switch that supports LACP.


Configuring the Switch for LACP (OPTIONAL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Access the Switch Configuration**:
   
   Access the CLI of your switch and configure the ports for LACP. The exact commands may vary depending on your switch model.

   Example for a Dell switch:

   .. code-block:: none

      S4048-ON-sw#config t
      S4048-ON-sw(conf)#int range te1/2,te1/7
      S4048-ON-sw(conf-if-range-te-1/2,te-1/7)#port-channel-protocol lacp
      S4048-ON-sw(conf-if-range-te-1/2,te-1/7-lacp)#port-channel 1 mode active
      S4048-ON-sw(conf-if-range-te-1/2,te-1/7-lacp)#end

   Explanation: These commands configure the switch ports ``te1/2`` and ``te1/7`` for LACP and create a port channel in active mode.


Configuring Open vSwitch for LACP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Create a Bridge**:
   
   .. code-block:: bash

      ovs-vsctl add-br br0

   Explanation: This command creates a new bridge named ``br0``.

2. **Add Ports to the Bridge**:
   
   .. code-block:: bash

      ovs-vsctl add-port br0 eth1
      ovs-vsctl add-port br0 eth2

   Explanation: These commands add the network interfaces ``eth1`` and ``eth2`` to the bridge ``br0``.

3. **Configure LACP on the Ports**:
   
   .. code-block:: bash

      ovs-vsctl set port eth1 lacp=active
      ovs-vsctl set port eth2 lacp=active

   Explanation: These commands enable LACP in active mode on the ports ``eth1`` and ``eth2``.

4. **Create a Bond with LACP**:
   
   .. code-block:: bash

      ovs-vsctl add-bond br0 bond0 eth1 eth2 -- set port bond0 \
      lacp=active -- set port bond0 bond_mode=balance-tcp

   Explanation: This command creates a bond named ``bond0`` on the bridge ``br0`` using the interfaces ``eth1`` and ``eth2``, sets LACP to active mode, and configures the bond mode to ``balance-tcp``.


Verifying the Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Check the Bridge Configuration**:
   
   .. code-block:: bash

      ovs-vsctl show

   Explanation: This command displays the current configuration of Open vSwitch, including the bridge and bond settings.

2. **Check the LACP Status**:
   
   .. code-block:: bash

      ovs-appctl bond/show br0

   Explanation: This command displays the status of the LACP bond on the bridge ``br0``.


Testing the Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Generate Traffic**:
   
   Use a traffic generator or network testing tool to generate traffic across the aggregated link.

2. **Monitor the Traffic**:
   
   .. code-block:: bash

      ovs-ofctl dump-ports br0

   Explanation: This command displays the traffic statistics for all ports on the bridge ``br0``.



3. VLAN Support
---------------

- **Standard 802.1Q VLAN model with trunking**: This feature supports VLAN tagging and trunking, which is essential for network segmentation and isolation.

  *Example*: Adding a VLAN to a port

  .. code-block:: bash

     ovs-vsctl add-br br0
     ovs-vsctl add-port br0 eth0 tag=10

  *Explanation*: The first command creates a new bridge named ``br0``. The second command adds the port ``eth0`` to the bridge ``br0`` and assigns it to VLAN 10.


4. Multicast Support
--------------------

- **Multicast snooping**: This feature optimizes multicast traffic by ensuring that multicast packets are only forwarded to ports that have interested receivers.

  *Example*: Enabling IGMP snooping

  .. code-block:: bash

     ovs-vsctl set Bridge br0 other-config:mcast-snooping-enable=true

  *Explanation*: This command enables IGMP snooping on the bridge ``br0``, which helps optimize multicast traffic by forwarding packets only to interested receivers.


5. Link and Fault Management
----------------------------

- **BFD (Bidirectional Forwarding Detection) and 802.1ag link monitoring**: These protocols provide rapid detection of link failures and help maintain network stability.

  *Example*: Configuring BFD

  .. code-block:: bash

     ovs-vsctl set interface eth0 bfd:enable=true bfd:min_rx=300 \
     bfd:min_tx=300 bfd:decay_min_rx=300

  *Explanation*: This command enables BFD on the interface ``eth0`` with specified minimum receive and transmit intervals, and decay minimum receive interval.


6. Spanning Tree Protocols
--------------------------

- **STP (IEEE 802.1D-1998) and RSTP (IEEE 802.1D-2004)**: These protocols prevent network loops by creating a loop-free logical topology.

  *Example*: Enabling STP

  .. code-block:: bash

     ovs-vsctl set Bridge br0 stp_enable=true

  *Explanation*: This command enables the Spanning Tree Protocol (STP) on the bridge ``br0``, which helps prevent network loops.


7. Quality of Service (QoS)
---------------------------

**Fine-grained QoS control**: This feature allows for precise control over traffic prioritization and bandwidth allocation.This exercise will guide you through the process of setting up Quality of Service (QoS) using Open vSwitch (OVS). You will learn how to configure both ingress policing and egress traffic shaping to manage network traffic effectively.


**Objective**: Configure QoS on Open vSwitch to control the rate of traffic ingress and egress on network interfaces.


Prerequisites
^^^^^^^^^^^^^

Before starting, ensure you have the following:

- Open vSwitch installed on your system.
- Network interfaces available for QoS configuration.


Configuring Ingress Policing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ingress policing limits the rate at which traffic is allowed to enter a network interface.


1. **Add a Port to the Bridge**:
   
   .. code-block:: bash

      ovs-vsctl add-port br0 eth0

   Explanation: This command adds the network interface ``eth0`` to the bridge ``br0``.

2. **Set Ingress Policing Rate and Burst**:
   
   .. code-block:: bash

      ovs-vsctl set interface eth0 ingress_policing_rate=1000
      ovs-vsctl set interface eth0 ingress_policing_burst=100

   Explanation: These commands set the ingress policing rate to 1000 Kbps (1 Mbps) and the burst size to 100 Kb on the interface ``eth0``.

3. **Verify Ingress Policing Configuration**:
   
   .. code-block:: bash

      ovs-vsctl list interface eth0

   Explanation: This command displays the current configuration of the interface ``eth0``, including the ingress policing settings.


Configuring Egress Traffic Shaping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Egress traffic shaping controls the rate at which traffic is allowed to leave a network interface.

1. **Create a QoS Policy**:
   
   .. code-block:: bash

      ovs-vsctl set port eth0 qos=@newqos -- --id=@newqos create qos type=linux-htb \
      other-config:max-rate=1000000000 queues:0=@q0 -- --id=@q0 create queue \
      other-config:min-rate=1000000 other-config:max-rate=5000000

   Explanation: This command sets up a QoS policy on the port ``eth0`` with a maximum rate of 1 Gbps and creates a queue with a minimum rate of 1 Mbps and a maximum rate of 5 Mbps.

2. **Verify QoS Configuration**:
   
   .. code-block:: bash

      ovs-vsctl list qos
      ovs-vsctl list queue

   Explanation: These commands display the current QoS and queue configurations.



Applying QoS to Specific Traffic Flows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Add OpenFlow Rules to Direct Traffic to Queues**:
   
   .. code-block:: bash

      ovs-ofctl add-flow br0 "in_port=1,actions=set_queue:0,normal"

   Explanation: This command adds an OpenFlow rule to direct traffic from port 1 to the queue with ID 0.

2. **Verify OpenFlow Rules**:
   
   .. code-block:: bash

      ovs-ofctl dump-flows br0

   Explanation: This command displays the current OpenFlow rules on the bridge ``br0``.


Testing the Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Generate Traffic**:
   
   Use a traffic generator or network testing tool to generate traffic on the interface ``eth0``.

2. **Monitor the Traffic**:
   
   .. code-block:: bash

      ovs-dpctl dump-ports br0

   Explanation: This command displays the traffic statistics for all ports on the bridge ``br0``.


This exercise demonstrates how to configure Quality of Service (QoS) using Open vSwitch. By following these steps, you can effectively manage network traffic by setting ingress policing and egress traffic shaping policies.




8. Security and Tunneling
-------------------------

- **IPsec and SSL/TLS**: These protocols provide secure communication channels for OVS management and data traffic.

  *Example*: Configuring an IPsec tunnel

  .. code-block:: bash

     ovs-vsctl add-port br0 ipsec0 -- set interface ipsec0 type=gre \
     options:remote_ip=192.168.1.2 options:psk=swordfish

  *Explanation*: This command adds an IPsec tunnel port named ``ipsec0`` to the bridge ``br0``, using GRE tunneling with the specified remote IP and pre-shared key.

- **LISP tunneling**: Locator/ID Separation Protocol (LISP) tunneling supports scalable and flexible network architectures.

  *Example*: Configuring a LISP tunnel

  .. code-block:: bash

     ovs-vsctl add-port br0 lisp0 -- set interface lisp0 type=lisp \
     options:remote_ip=192.168.1.3

  *Explanation*: This command adds a LISP tunnel port named ``lisp0`` to the bridge ``br0``, using the specified remote IP.


9. OpenFlow Extensions
----------------------

- **Advanced flow table management**: OVS extends OpenFlow capabilities with features like multiple flow tables, group tables, and meter tables for more complex flow processing.

  *Example*: Adding a flow with OpenFlow

  .. code-block:: bash

     ovs-ofctl add-flow br0 "priority=100,in_port=1,actions=output:2"

  *Explanation*: This command adds a flow to the bridge ``br0`` with a priority of 100, matching packets coming in on port 1 and forwarding them to port 2.

.. warning:: OpenFlow is obsolete and is considered to have been replaced by P4Runtime in modern SDN architectures.


OVS Programming
===============

Open vSwitch provides a rich set of APIs for programming and automation. The following sections provides an example of how to use Python to interact with Open vSwitch. Open vSwitch provides language bindings for Python, Lua and Go. More information can be found in the Open vSwitch Language Bindings [1]_ and ``ovs`` Python library [2]_.

These exercises will help you gain hands-on experience with Open vSwitch (OVS) in real-world scenarios. They cover advanced topics such as network automation, traffic engineering, and integration with SDN controllers.


1. Automating Network Configuration with Python
-----------------------------------------------

Objective: Use Python to automate the configuration of Open vSwitch bridges and ports.

.. warning:: Before installing the required python libraries, make sure to create a virtual environment to avoid conflicts with system packages.


1. **Install Required Libraries**:
   
   .. code-block:: bash

      sudo apt install python3-pip
      pip3 install ovs

   Explanation: This command installs the necessary Python libraries for interacting with Open vSwitch.

2. **Create a Python Script**:
   
   .. code-block:: python
        :linenos:

         import subprocess

         def create_bridge(bridge_name):
            subprocess.run(["ovs-vsctl", "add-br", bridge_name], check=True)
            print(f"Bridge {bridge_name} created.")

         def add_port(bridge_name, port_name):
            subprocess.run(["ovs-vsctl", "add-port", bridge_name, port_name], check=True)
            print(f"Port {port_name} added to bridge {bridge_name}.")

         if __name__ == "__main__":
            create_bridge("br0")
            add_port("br0", "eth0")

   Explanation: This script uses the ``subprocess.run`` function to execute the ``ovs-vsctl`` commands. The ``check=True`` argument ensures that an exception is raised if the command returns a non-zero exit status, which helps in error handling. An alternative approach is to use the ``ovs`` library to interact with Open vSwitch. The library provides a higher-level interface for managing OVS and it is available as a Python package here [2]_

3. **Run the Script**:
   
   .. code-block:: bash

      python3 script.py

   Explanation: This command runs the Python script to automate the network configuration.


2. Traffic Engineering with OpenFlow
------------------------------------

Objective: Use OpenFlow to implement traffic engineering policies in Open vSwitch.

1. **Install OpenFlow Controller**:
   
   .. code-block:: bash

      sudo apt install openvswitch-testcontroller

   Explanation: This command installs the OpenFlow controller provided by Open vSwitch.

2. **Create a Bridge and Connect to the Controller**:
   
   .. code-block:: bash

      ovs-vsctl add-br br0
      ovs-vsctl set-controller br0 tcp:127.0.0.1:6633

   Explanation: These commands create a bridge and connect it to the local OpenFlow controller.

3. **Add OpenFlow Rules**:
   
   .. code-block:: bash

      ovs-ofctl add-flow br0 "priority=100,in_port=1,actions=output:2"
      ovs-ofctl add-flow br0 "priority=100,in_port=2,actions=output:1"

   Explanation: These commands add OpenFlow rules to forward traffic between ports 1 and 2.

4. **Verify the Configuration**:
   
   .. code-block:: bash

      ovs-ofctl dump-flows br0

   Explanation: This command displays the current OpenFlow rules on the bridge `br0`.



3. Open vSwitch Advanced Features tutorial
------------------------------------------

Complete the Open vSwitch Advanced Features Tutorial [3]_.

.. note:: This tutorial covers multi-table processing to demonstrate advanced OpenFlow features in Open vSwitch. Further the tutorial covers group tables, and provides an example of how to use group tables to implement a MAC learning switch.



Client-Server Model: Automating OVS Network Configuration
=========================================================

**Objective:**
Test advanced programming knowledge of Open vSwitch (OVS) for automating network configuration in a simple Python client-server model.

**Scenario:**

- One server: ``s1``
- Two clients: ``c1`` and ``c2``
- Traffic from ``c1`` to ``s1`` should be processed normally.
- Traffic from ``c2`` to ``s1`` should have Quality of Service (QoS) applied.


.. graphviz::
    :align: center
    :caption: Network Topology

    digraph G {
        node [shape=box, style=filled, color=lightgrey];
        br0 [label="Bridge: br0", color=lightcoral];
        s1 [label="Server (s1)", color=lightblue];
        c1 [label="Client (c1)", color=lightyellow];
        c2 [label="Client (c2)", color=lightyellow];

        br0 -> s1;
        br0 -> c1;
        br0 -> c2;

        s1 -> c1 [label="Normal Traffic", color=blue];
        s1 -> c2 [label="QoS Traffic", color=red];

        c1 -> s1 [color=blue];
        c2 -> s1 [color=red];
    }

**Requirements:**

1. Install and configure Open vSwitch on the server and clients.
2. Write a Python script to automate the network configuration using OVS commands.
3. Ensure that traffic from ``c1`` to ``s1`` is processed normally.
4. Apply QoS to all traffic from ``c2`` to ``s1``.


Solution Blueprint:
-------------------

.. code-block:: python
    :linenos:

      import subprocess

      def create_bridge(bridge_name):
         # Add code to create a bridge.

      def add_port(bridge_name, port_name):
         # Add code to add a port to a bridge.

      def add_openflow_rule(bridge_name, rule):
         # Add code to add an OpenFlow rule.

      def apply_qos(port_name, max_rate, min_rate):
         # Add code to apply QoS to a port.

      if __name__ == "__main__":
         # Create OVS bridge

         # Add interfaces to the bridge

         # Set up normal traffic flow from c1 to s1

         # Apply QoS to traffic from c2 to s1

         # Add flow for QoS traffic



**Testing:**

1. Verify the OVS bridge and ports are correctly configured.
2. Check that traffic from ``c1`` to ``s1`` is processed normally.
3. Ensure QoS is applied to traffic from ``c2`` to ``s1`` by monitoring traffic rates.

**Expected Outcome:**

- Traffic from ``c1`` to ``s1`` should flow without any QoS restrictions.
- Traffic from ``c2`` to ``s1`` should have QoS applied, ensuring bandwidth limits are enforced.




Virtual Network Function: Firewall
==================================

**Objective:**
Test advanced programming knowledge of Open vSwitch (OVS) for implementing a firewall with MAC learning and Quality of Service (QoS) features.

**Scenario:**

The network topology includes two ports (``eth0`` and ``eth1``) connected to the firewall through Open vSwitch bridge ``br0``. 

- Implement a firewall using Open vSwitch with the following features:

  - VLAN Tagging
  - MAC Learning
  - IP Routing
  - Firewall Rules
  - Quality of Service (QoS)


.. graphviz::
   :caption: Open vSwitch Firewall
   :align: center

      digraph OVS_Firewall {
         rankdir=TB;
         node [shape=box, style=filled, color=lightgrey];

         // Define nodes for each table
         Table0 [label="Table 0: VLAN Tagging", color=lightblue];
         Table1 [label="Table 1: MAC Learning",color=lightblue];
         Table2 [label="Table 2: IP Routing", color=lightblue];
         Table3 [label="Table 3: Firewall Rules", color=lightblue];
         Table4 [label="Table 4: QoS", color=lightblue];
         Table5 [label="Table 5: NAT", color=lightblue];
         Table6 [label="Table 6: Final Output Processing", color=lightblue];

         // Define edges to show the flow of packets
         Table0 -> Table1 [label="resubmit(,1)"];
         Table1 -> Table2 [label="resubmit(,2)"];
         Table2 -> Table3 [label="resubmit(,3)"];
         Table3 -> Table4 [label="resubmit(,4)"];
         Table4 -> Table5 [label="resubmit(,5)"];
         Table5 -> Table6 [label="resubmit(,6)"];

         // Define additional edges for specific actions
         Table3 -> Table6 [label="drop"];
         Table6 -> Output [label="output:NORMAL"];

         // Define input and output nodes
         Input1 [label="eth1", shape=ellipse, color=lightcoral];
         Input2 [label="eth2", shape=ellipse, color=lightcoral];
         Output [label="Output", shape=ellipse, color=lightcoral];

         // Connect input nodes to Table 0
         Input1 -> Table0 [label="in_port=1"];
         Input2 -> Table0 [label="in_port=2"];
      }


**Requirements:**

1. Implement VLAN tagging (Table 0) to separate traffic. Use VLAN 10 for internal traffic and VLAN 20 for external traffic.
2. Implement MAC learning (Table 1) to build a forwarding table. Use the first packet to learn the source MAC address and port.
3. Implement IP routing (Table 2) to forward packets based on IP addresses. Use the destination IP address to determine the output port.
4. Implement firewall rules (Table 3) to filter traffic. Allow traffic from internal to external networks and block traffic from external to internal networks. Further, allow HTTP traffic (port 80) and block SSH traffic (port 22).
5. Implement Quality of Service (QoS) (Table 4) to prioritize traffic from port 1 over port 2.
6. Implement Network Address Translation (NAT) (Table 5) for outbound traffic. In this case, translate the source IP address of packets from internal address (private IP) to external address (public IP).
7. Implement final output processing (Table 6) for packet forwarding.


**Testing:**

1. Verify bridge and port configurations using ``ovs-vsctl`` commands.
2. Use tools like ``ping``, ``iperf``, or ``hping3`` to generate test traffic and verify the firewall rules.



References
==========

.. [1] Open vSwitch Language Bindings: https://docs.openvswitch.org/en/latest/topics/language-bindings/
.. [2] ovs Python package: https://github.com/openvswitch/ovs/tree/main/python/ovs
.. [3] Open vSwitch Advanced Features Tutorial: https://docs.openvswitch.org/en/latest/tutorials/ovs-advanced/


