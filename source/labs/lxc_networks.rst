**************************
LXC and Virtual Networking
**************************

LXC or Linux Containers is a lightweight virtualization technology that allows you to run multiple isolated Linux systems on a single host. LXC provides a way to create and manage system or application containers, which are similar to virtual machines but with less overhead. This guide provides an overview of LXC networking concepts and how to configure virtual networks for LXC containers. More information on LXC can be found in the ``LXC documentation <https://linuxcontainers.org/lxc/introduction/>``_.


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

