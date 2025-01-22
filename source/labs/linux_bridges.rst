*********************************
Linux Bridges and TUN/TAP Devices
*********************************

Linux bridges and TUN/TAP devices are used to create virtual networks.


TUN/TAP Devices
===============

TUN and TAP devices are virtual network kernel devices in Linux that provide different types of network interfaces.

TUN Devices
-----------

**TUN (Network TUNnel) devices** operate at the network layer (Layer 3). They simulate a network layer device and handle IP packets. TUN devices are used to route packets between different network interfaces or to create virtual network interfaces.

**Example Use Cases for TUN Devices**:

1. **VPNs (Virtual Private Networks)**: TUN devices are commonly used in VPNs to tunnel IP packets securely over the internet.
2. **Routing**: They can be used to route traffic between different subnets or networks.
3. **Network Emulation**: TUN devices can be used to create virtual networks for testing and development purposes.

TAP Devices
-----------

**TAP (Network TAP) devices** operate at the data link layer (Layer 2). They simulate an Ethernet device and handle Ethernet frames. TAP devices are used to bridge Ethernet frames between different network interfaces or to create virtual Ethernet interfaces.

**Example Use Cases for TAP Devices**:

1. **Bridging**: TAP devices are often used to bridge virtual machines to the host network, allowing VMs to appear as if they are on the same physical network.
2. **Network Emulation**: TAP devices can be used to create virtual Ethernet networks for testing and development.
3. **Network Simulation**: They are useful for simulating network environments and testing network protocols.

Key Differences
---------------

- **Layer of Operation**:
  
  - **TUN**: Operates at Layer 3 (Network Layer) and handles IP packets.
  - **TAP**: Operates at Layer 2 (Data Link Layer) and handles Ethernet frames.

- **Use Cases**:
  
  - **TUN**: Ideal for routing and VPNs.
  - **TAP**: Ideal for bridging and network emulation.

Example Commands
----------------

Here are some example commands to create and manage TUN and TAP devices:

**Creating a TUN Device**:

.. code-block:: bash
    
    $ sudo ip tuntap add dev tun0 mode tun
    $ sudo ip addr add 10.0.0.1/24 dev tun0
    $ sudo ip link set dev tun0 up


**Creating a TAP Device**:

.. code-block:: bash
    
    $ sudo ip tuntap add dev tap0 mode tap
    $ sudo ip addr add 192.168.1.100/24 dev tap0
    $ sudo ip link set dev tap0 up

By understanding the differences and use cases for TUN and TAP devices, you can choose the appropriate type for your specific networking needs.



TUN/TAP Devices in Linux using iproute2
=======================================

Exercise 1: Creating a TUN Device
---------------------------------

**Objective**: Create a TUN device and bring it up.

**Steps**:

1. Create a TUN Device:

   .. code-block:: bash

      $ sudo ip tuntap add dev tun0 mode tun

   This command creates a TUN device named ``tun0``.

2. Bring Up the TUN Device:
   
   .. code-block:: bash

      $ sudo ip link set dev tun0 up

**Verification**: Use ``ip link show tun0`` to verify the TUN device configuration.

Exercise 2: Assigning an IP Address to a TUN Device
---------------------------------------------------

**Objective**: Assign a static IP address to the TUN device.

**Steps**:

1. Assign an IP Address:
   
   .. code-block:: bash

      $ sudo ip addr add 10.0.0.1/24 dev tun0

2. Bring Up the TUN Device:
   
   .. code-block:: bash

      $ sudo ip link set dev tun0 up

**Verification**: Use ``ip addr show tun0`` to verify the IP address assignment.

Exercise 3: Creating a TAP Device
---------------------------------

**Objective**: Create a TAP device and bring it up.

**Steps**:

1. Create a TAP Device:
   
   .. code-block:: bash

      $ sudo ip tuntap add dev tap0 mode tap

   This command creates a TAP device named ``tap0``.

2. Bring Up the TAP Device:
   
   .. code-block:: bash

      $ sudo ip link set dev tap0 up

**Verification**: Use ``ip link show tap0`` to verify the TAP device configuration.

Exercise 4: Assigning an IP Address to a TAP Device
---------------------------------------------------

**Objective**: Assign a static IP address to the TAP device.

**Steps**:

1. Assign an IP Address:
   
   .. code-block:: bash

      $ sudo ip addr add 192.168.1.100/24 dev tap0

2. Bring Up the TAP Device:
   
   .. code-block:: bash

      $ sudo ip link set dev tap0 up

**Verification**: Use ``ip addr show tap0`` to verify the IP address assignment.

Exercise 5: Adding a TAP Device to a Bridge
-------------------------------------------

**Objective**: Add a TAP device to a Linux bridge.

**Steps**:

1. Create a Bridge Interface:
   
   .. code-block:: bash

      $ sudo ip link add name br0 type bridge

2. Add the TAP Device to the Bridge:
   
   .. code-block:: bash

      $ sudo ip link set dev tap0 master br0

3. Bring Up the Bridge and TAP Device:
   
   .. code-block:: bash

      $ sudo ip link set dev br0 up
      $ sudo ip link set dev tap0 up

**Verification**: Use ``bridge link`` to verify that ``tap0`` is part of the bridge ``br0``.

Exercise 6: Monitoring Traffic on TUN/TAP Devices
-------------------------------------------------

**Objective**: Monitor traffic on TUN/TAP devices.

**Steps**:

1. Install ``tcpdump``
   
   .. code-block:: bash

      $ sudo apt install tcpdump

2. Monitor Traffic on TUN Device:
   
   .. code-block:: bash

      $ sudo tcpdump -i tun0

3. Monitor Traffic on TAP Device:
   
   .. code-block:: bash

      $ sudo tcpdump -i tap0

**Verification**: Observe the traffic being captured on the TUN/TAP devices.



Exercise 7: Creating a TUN Device with Custom MTU
-------------------------------------------------

**Objective**: Create a TUN device with a custom Maximum Transmission Unit (MTU) size.

**Steps**:

1. Create a TUN Device:
   
   .. code-block:: bash

      $ sudo ip tuntap add dev tun0 mode tun

2. Set Custom MTU:
   
   .. code-block:: bash

      $ sudo ip link set dev tun0 mtu 1400

3. Bring Up the TUN Device:
   
   .. code-block:: bash

      $ sudo ip link set dev tun0 up

**Verification**: Use ``ip link show tun0`` to verify the MTU size and TUN device configuration.

Exercise 8: Creating a TAP Device with VLAN Tagging
---------------------------------------------------

**Objective**: Create a TAP device and configure VLAN tagging.

**Steps**:

1. Create a TAP Device:
   
   .. code-block:: bash

      $ sudo ip tuntap add dev tap0 mode tap

2. Create a VLAN Interface:
   
   .. code-block:: bash

      $ sudo ip link add link tap0 name tap0.100 type vlan id 100

3. Bring Up the TAP and VLAN Interfaces:
   
   .. code-block:: bash

      $ sudo ip link set dev tap0 up
      $ sudo ip link set dev tap0.100 up

**Verification**: Use ``ip link show`` to verify the TAP and VLAN interface configuration.

Exercise 9: Configuring a TUN Device with IP Forwarding
-------------------------------------------------------

**Objective**: Configure a TUN device with IP forwarding to route traffic between networks.

**Steps**:

1. Create a TUN Device:
   
   .. code-block:: bash

      $ sudo ip tuntap add dev tun0 mode tun

2. Assign IP Addresses:
   
   .. code-block:: bash

      $ sudo ip addr add 10.0.0.1/24 dev tun0
      $ sudo ip addr add 10.0.1.1/24 dev eth0

3. Enable IP Forwarding:
   
   .. code-block:: bash

      $ sudo sysctl -w net.ipv4.ip_forward=1

4. Set up IP Forwarding Rules:
   
   .. code-block:: bash

      $ sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
      $ sudo iptables -A FORWARD -i eth0 -o tun0 -m state --state RELATED,ESTABLISHED -j ACCEPT
      $ sudo iptables -A FORWARD -i tun0 -o eth0 -j ACCEPT

**Verification**: Use ``ping`` to test connectivity between devices on different networks.

Exercise 10: Bridging TAP Devices with Network Namespaces
---------------------------------------------------------

**Objective**: Create TAP devices and bridge them with network namespaces.

**Steps**:

1. Create Network Namespaces:
   
   .. code-block:: bash

      $ sudo ip netns add ns1
      $ sudo ip netns add ns2

2. Create TAP Devices:
   
   .. code-block:: bash

      $ sudo ip tuntap add dev tap1 mode tap
      $ sudo ip tuntap add dev tap2 mode tap

3. Create a Bridge Interface:
   
   .. code-block:: bash

      $ sudo ip link add name br0 type bridge

4. Add TAP Devices to the Bridge:
   
   .. code-block:: bash

      $ sudo ip link set dev tap1 master br0
      $ sudo ip link set dev tap2 master br0

5. Move TAP Devices to Network Namespaces:
   
   .. code-block:: bash

      $ sudo ip link set tap1 netns ns1
      $ sudo ip link set tap2 netns ns2

6. Bring Up the Bridge and TAP Devices:
   
   .. code-block:: bash

      $ sudo ip link set dev br0 up
      $ sudo ip netns exec ns1 ip link set dev tap1 up
      $ sudo ip netns exec ns2 ip link set dev tap2 up

**Verification**: Use ``ip netns exec ns1 ping <ns2_ip>`` to test connectivity between the namespaces.

Exercise 11: Monitoring and Debugging TUN/TAP Traffic
-----------------------------------------------------

**Objective**: Monitor and debug traffic on TUN/TAP devices using advanced tools.

**Steps**:

1. Install ``tcpdump`` and ``wireshark``
   
   .. code-block:: bash

      $ sudo apt-get install tcpdump wireshark

2. Capture Traffic on TUN Device:
   
   .. code-block:: bash

      $ sudo tcpdump -i tun0 -w tun0_traffic.pcap

3. Capture Traffic on TAP Device:
   
   .. code-block:: bash

      $ sudo tcpdump -i tap0 -w tap0_traffic.pcap

4. Analyze Traffic with Wireshark:
   
   - Open the captured ``.pcap`` files in Wireshark for detailed analysis.

**Verification**: Use Wireshark to inspect and analyze the captured traffic for any anomalies or issues.




Linux Bridges
=============

What is a Linux Bridge?
-----------------------

A Linux bridge acts like a virtual network switch. It forwards Ethernet frames between network interfaces based on their MAC addresses. This allows devices connected to different interfaces to communicate with each other seamlessly.

Key Features of Linux Bridges
-----------------------------

1. Layer 2 Operation: Bridges operate at the data link layer, handling Ethernet frames and MAC addresses.
2. Transparent Bridging: Bridges forward traffic transparently, meaning devices on either side of the bridge are unaware of its presence.
3. Spanning Tree Protocol (STP): Bridges can use STP to prevent network loops and ensure a loop-free topology.
4. VLAN Support: Bridges can handle VLAN-tagged traffic, allowing for network segmentation and isolation.

Common Use Cases
----------------

1. Virtualization: Bridges are commonly used in virtualized environments to connect virtual machines (VMs) to the host network.
2. Network Segmentation: Bridges can be used to segment networks for better traffic management and security.
3. Network Redundancy: Bridges can help create redundant network paths to ensure high availability.

Basic Commands for Managing Bridges
-----------------------------------

Here are some basic commands to create and manage bridges using the ``iproute2`` package:

- Create a Bridge:
  
  .. code-block:: bash

     $ sudo ip link add name br0 type bridge

  This command creates a new bridge interface named ``br0``.

- Add an Interface to the Bridge:
  
  .. code-block:: bash

     $ sudo ip link set dev eth0 master br0

  This adds the Ethernet interface ``eth0`` to the bridge ``br0``.

- Bring Up the Bridge Interface:
  
  .. code-block:: bash

     $ sudo ip link set dev br0 up

  This command activates the bridge interface.

- Assign an IP Address to the Bridge:
  
  .. code-block:: bash

     $ sudo ip addr add 192.168.1.100/24 dev br0

  This assigns an IP address to the bridge interface ``br0``.

- Show Bridge Configuration:
  
  .. code-block:: bash

     $ sudo bridge link

  This command displays the current bridge configuration and the interfaces associated with it.

Example Configuration
---------------------

Here’s an example of setting up a bridge and adding interfaces to it:

1. Create the Bridge:
   
   .. code-block:: bash

      $ sudo ip link add name br0 type bridge

2. Add Interfaces to the Bridge:
   
   .. code-block:: bash

      $ sudo ip link set dev eth0 master br0
      $ sudo ip link set dev eth1 master br0

3. Bring Up the Bridge and Interfaces:
   
   .. code-block:: bash

      $ sudo ip link set dev br0 up
      $ sudo ip link set dev eth0 up
      $ sudo ip link set dev eth1 up

4. Assign an IP Address to the Bridge:
   
   .. code-block:: bash

      $ sudo ip addr add 192.168.1.100/24 dev br0





Bridge Utilities in Linux using iproute2
========================================

Exercise 12: Bridge Creation
----------------------------

**Objective**: Create a basic network bridge using ``iproute2``.

**Steps**:

1. Create a Bridge Interface:
   
   .. code-block:: bash

      $ sudo ip link add name br0 type bridge

   This command creates a new bridge interface named ``br0``.

2. Bring Up the Bridge Interface:
   
   .. code-block:: bash

      $ sudo ip link set dev br0 up

   This command activates the bridge interface.

**Verification**: Use ``ip link show br0`` to verify the bridge configuration. You should see ``br0`` listed with its status as ``UP``.

Exercise 13: Adding Interfaces to a Bridge
------------------------------------------

**Objective**: Add multiple interfaces to a bridge.

**Steps**:

1. Add an Ethernet Interface to the Bridge:
   
   .. code-block:: bash

      $ sudo ip link set dev eth0 master br0

   This command adds the Ethernet interface ``eth0`` to the bridge ``br0``.

2. Add Another Ethernet Interface:
   
   .. code-block:: bash

      $ sudo ip link set dev eth1 master br0

   This adds the Ethernet interface ``eth1`` to the bridge ``br0``.

3. Bring Up the Interfaces:
   
   .. code-block:: bash

      $ sudo ip link set dev eth0 up
      $ sudo ip link set dev eth1 up

   These commands activate the Ethernet interfaces.

**Verification**: Use ``bridge link`` to verify that both ``eth0`` and ``eth1`` are part of the bridge ``br0``.

Exercise 14: Assigning an IP Address to the Bridge
--------------------------------------------------

**Objective**: Assign a static IP address to the bridge.

**Steps**:

1. Assign an IP Address:
   
   .. code-block:: bash

      $ sudo ip addr add 192.168.1.100/24 dev br0

   This command assigns the IP address ``192.168.1.100`` with a subnet mask of ``255.255.255.0`` to the bridge interface ``br0``.

2. Bring Up the Bridge Interface:
   
   .. code-block:: bash

      $ sudo ip link set dev br0 up

   This command ensures the bridge interface is active.

**Verification**: Use ``ip addr show br0`` to verify the IP address assignment. You should see the assigned IP address listed under ``br0``.

Exercise 15: Removing Interfaces from a Bridge
----------------------------------------------

**Objective**: Remove an interface from a bridge.

**Steps**:

1. Remove an Interface:
   
   .. code-block:: bash

      $ sudo ip link set dev eth0 nomaster

   This command removes the Ethernet interface ``eth0`` from the bridge ``br0``.

2. Bring Down the Bridge Interface:
   
   .. code-block:: bash

      $ sudo ip link set dev br0 down

   This command deactivates the bridge interface.

3. Delete the Bridge:
   
   .. code-block:: bash

      $ sudo ip link delete br0 type bridge

   This command deletes the bridge interface ``br0``.

**Verification**: Use ``ip link show`` to verify the interface removal and bridge deletion. The bridge ``br0`` should no longer be listed.

Exercise 16: Monitoring Bridge Traffic
--------------------------------------

**Objective**: Monitor traffic on the bridge

**Steps**:

1. Install ``tcpdump``
   
   .. code-block:: bash

      $ sudo apt-get install tcpdump

   This command installs the ``tcpdump`` tool if it's not already installed.

2. Monitor Traffic:
   
   .. code-block:: bash

      $ sudo tcpdump -i br0

   This command starts monitoring traffic on the bridge interface ``br0``.

**Verification**: Observe the traffic being captured on the bridge interface. You should see packets being displayed in real-time.

Exercise 17: Configuring Bridge with VLANs
------------------------------------------

**Objective**: Configure a bridge with VLAN tagging.

**Steps**:

1. Create a VLAN Interface:
   
   .. code-block:: bash

      $ sudo ip link add link eth0 name eth0.10 type vlan id 10

   This command creates a VLAN interface ``eth0.10`` with VLAN ID 10 on the Ethernet interface ``eth0``.

2. Add the VLAN Interface to the Bridge:
   
   .. code-block:: bash

      $ sudo ip link set dev eth0.10 master br0

   This command adds the VLAN interface ``eth0.10`` to the bridge ``br0``.

3. Bring Up the VLAN and Bridge Interfaces:
   
   .. code-block:: bash

      $ sudo ip link set dev eth0.10 up
      $ sudo ip link set dev br0 up

   These commands activate the VLAN and bridge interfaces.

**Verification**: Use ``bridge vlan`` to verify the VLAN configuration. You should see the VLAN interface ``eth0.10`` listed under the bridge ``br0``.

