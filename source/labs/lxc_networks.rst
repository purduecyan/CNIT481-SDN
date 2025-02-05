**************************
LXC and Virtual Networking
**************************

LXC or Linux Containers is a lightweight virtualization technology that allows you to run multiple isolated Linux systems on a single host. LXC provides a way to create and manage system or application containers, which are similar to virtual machines but with less overhead. This guide provides an overview of LXC networking concepts and how to configure virtual networks for LXC containers. More information on LXC can be found in the `LXC documentation <https://linuxcontainers.org/lxc/introduction/>`_.


Connecting Two LXC VMs Using TAP Devices
========================================

This guide provides detailed instructions for connecting two LXC VMs (``vm1`` and ``vm2``) using TAP devices and a bridge.

1. Install LXC
--------------

First, ensure that LXC is installed on your host machine.

.. code-block:: bash

   sudo apt update
   sudo apt install lxc lxc-templates

2. Create the LXC VMs
---------------------

LXC containers are created using templates. In this example, we will use the Ubuntu template to create the VMs. Other templates are available for different Linux distributions. LXC templates ship with the LXC package and can be found in the ``/usr/share/lxc/templates`` directory.

To list available templates, use the following command:

.. code-block:: bash

   ls /usr/share/lxc/templates

In this guide, we will use the Ubuntu template to create the VMs.

Create the LXC containers for ``vm1`` and ``vm2``. Replace ``vm1`` and ``vm2`` with the names of your choice. The ``-t`` option specifies the template to use.

.. code-block:: bash

   sudo lxc-create -n vm1 -t ubuntu
   sudo lxc-create -n vm2 -t ubuntu

3. Create a Bridge on the Host
------------------------------

Create a bridge interface on the host to act as a virtual switch. This bridge will connect the TAP devices used by the VMs. Replace ``br0`` with the name of your choice. The bridge interface can be created using the ``ip`` command. 

.. code-block:: bash

   sudo ip link add name br0 type bridge
   sudo ip link set dev br0 up

4. Create TAP Devices for each VM
---------------------------------

Create TAP devices for each LXC VM to connect the VMs to the bridge. Replace ``tap0`` and ``tap1`` with the names of your choice.

.. code-block:: bash

   sudo ip tuntap add dev tap0 mode tap
   sudo ip tuntap add dev tap1 mode tap
   sudo ip link set dev tap0 up
   sudo ip link set dev tap1 up

5. Add TAP Devices to the Bridge
--------------------------------

Add the TAP devices to the bridge interface. This allows the VMs to communicate with each other through the bridge. 

.. code-block:: bash

   sudo ip link set dev tap0 master br0
   sudo ip link set dev tap1 master br0

6. Configure LXC VM Network Settings
------------------------------------

Edit the network configuration for each VM to use the TAP devices. The configuration files for LXC VMs are located in the ``/var/lib/lxc`` directory. Each VM has its own configuration file. 

For VM1 (``/var/lib/lxc/vm1/config``):

.. code-block:: ini

   lxc.net.0.type = veth
   lxc.net.0.link = br0
   lxc.net.0.flags = up
   lxc.net.0.veth.pair = tap0

For VM2 (``/var/lib/lxc/vm2/config``):

.. code-block:: ini

   lxc.net.0.type = veth
   lxc.net.0.link = br0
   lxc.net.0.flags = up
   lxc.net.0.veth.pair = tap1

7. Start the LXC VMs
--------------------

Start both LXC VMs. 

.. code-block:: bash

   sudo lxc-start -n vm1
   sudo lxc-start -n vm2

You can check the status of the VMs using the following command: 

.. code-block:: bash

   sudo lxc-ls -f

The option ``-f`` provides detailed information about the containers.


8. Assign IP Addresses to the VMs
---------------------------------

To login to the VMs, use the ``lxc-attach`` command.

Assign IP addresses to the network interfaces within each VM. The IP addresses should be in the same subnet to allow communication between the VMs. 

For VM1:

.. code-block:: bash

   sudo lxc-attach -n vm1
   ip addr add 192.168.1.101/24 dev eth0
   ip link set dev eth0 up
   exit

For VM2:

.. code-block:: bash

   sudo lxc-attach -n vm2
   ip addr add 192.168.1.102/24 dev eth0
   ip link set dev eth0 up
   exit

9. Test Connectivity
--------------------

Test the connectivity between the two VMs by pinging from one VM to the other.

**From VM1**:

.. code-block:: bash

   sudo lxc-attach -n vm1
   ping 192.168.1.102

**From VM2**:

.. code-block:: bash

   sudo lxc-attach -n vm2
   ping 192.168.1.101

Network Configuration Explanation
---------------------------------

- Bridge (``br0``): Acts as a virtual switch connecting the TAP devices.
- TAP Devices (``tap0``, ``tap1``): Serve as virtual network interfaces for the VMs.
- LXC VM Configuration: Configures the VMs to use the TAP devices and assigns IP addresses for communication.



Exercises
=========

Develop solutions for the following configurations using TUN/TAP/bridge devices on LXC containers.

Bridging using Routed Subnets
-----------------------------

This solution should enable communication between the host and VM (bidirectional). Assign a new IP subnet to the host's bridge interface, and do not use the subnet anywhere else. The VMs should be configured using different tap interfaces and MAC addresses. The IP of each VM should be in the same subnet as the subnet of the bridge so that the host and VMs can communicate.


.. graphviz::
   :caption: Bridging using Routed Subnets
   :align: center

      digraph G {
      rankdir=TB;
      node [shape=box];

      subgraph cluster_host {
         label = "Host";
         style=filled;
         color=lightgrey;
         
         bridge [label="Bridge Interface (br0)\nIP: 192.168.1.1/24"];
         tap1 [label="TAP Interface (tap0)\nMAC: 00:11:22:33:44:55"];
         tap2 [label="TAP Interface (tap1)\nMAC: 00:11:22:33:44:66"];
         
         bridge -> tap1 [label="192.168.1.2"];
         bridge -> tap2 [label="192.168.1.3"];
      }

      subgraph cluster_vm1 {
         label = "VM1";
         style=filled;
         color=lightblue;
         
         vm1 [label="VM1\nIP: 192.168.1.2"];
      }

      subgraph cluster_vm2 {
         label = "VM2";
         style=filled;
         color=lightblue;
         
         vm2 [label="VM2\nIP: 192.168.1.3"];
      }

      tap1 -> vm1;
      tap2 -> vm2;
      }


Bridge using Routed Subnet, VMs connect to the Internet using Host LAN
----------------------------------------------------------------------

This solution should provide Internet access to the VMs. Extend the previous configuration by enabling routing (i.e., IP forwarding on the host) and use iptables to set up a rule to perform IP masquerading on packets leaving the en* interface. This allows multiple devices on the private network to share a single public IP address for outbound traffic.



.. graphviz::
   :caption: Bridge using Routed Subnet, VMs connect to the Internet using Host LAN
   :align: center

      digraph G {
         rankdir=TB;
         node [shape=box];

         subgraph cluster_host {
            label = "Host";
            style=filled;
            color=lightgrey;
            
            bridge [label="Bridge Interface (br0)\nIP: 192.168.1.1/24"];
            tap1 [label="TAP Interface (tap0)\nMAC: 00:11:22:33:44:55"];
            tap2 [label="TAP Interface (tap1)\nMAC: 00:11:22:33:44:66"];
            enp [label="External Interface (enp2s0)\nPublic IP"];
            
            bridge -> tap1 [label="192.168.1.2"];
            bridge -> tap2 [label="192.168.1.3"];
            bridge -> enp [label="IP Forwarding + iptables"];
         }

         subgraph cluster_vm1 {
            label = "VM1";
            style=filled;
            color=lightblue;
            
            vm1 [label="VM1\nIP: 192.168.1.2"];
         }

         subgraph cluster_vm2 {
            label = "VM2";
            style=filled;
            color=lightblue;
            
            vm2 [label="VM2\nIP: 192.168.1.3"];
         }

         tap1 -> vm1;
         tap2 -> vm2;
      }



Bridge to Layer 2 to connect the VM to the Host Switch with DHCP
----------------------------------------------------------------

This solution connects the VM to the same network switch as the host machine. For instance, if a DHCP server is present on the network and the host machine receives its IP address from this DHCP server, the VM can also obtain an IP address from the same DHCP server. This setup is commonly used in ESXi, Xen, or HyperV VM production environments.


.. graphviz::
   :caption: Bridge to Layer 2 to connect the VM to the Host Switch with DHCP
   :align: center

      digraph G {
         rankdir=TD;
         node [shape=box];

         subgraph cluster_network {
            label = "Network";
            style=filled;
            color=lightgrey;
            
            dhcp [label="DHCP Server"];
            switch [label="Network Switch"];
            
            dhcp -> switch;
         }

         subgraph cluster_host {
            label = "Host";
            style=filled;
            color=lightblue;
            
            host [label="Host Machine\nIP from DHCP"];
            bridge [label="Bridge Interface (br0)"];
            tap1 [label="TAP Interface (tap0)"];
            
            host -> bridge;
            bridge -> tap1;
            switch -> host;
         }

         subgraph cluster_vm {
            label = "VM";
            style=filled;
            color=lightgreen;
            
            vm [label="VM\nIP from DHCP"];
            
            tap1 -> vm;
            switch -> vm;
         }
      }