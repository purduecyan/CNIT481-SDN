import subprocess

def create_bridge(bridge_name):
    subprocess.run(["ovs-vsctl", "add-br", bridge_name], check=True)
    print(f"Bridge {bridge_name} created.")

def add_port(bridge_name, port_name):
    subprocess.run(["ovs-vsctl", "add-port", bridge_name, port_name], check=True)
    print(f"Port {port_name} added to bridge {bridge_name}.")

def add_openflow_rule(bridge_name, rule):
    subprocess.run(["ovs-ofctl", "add-flow", bridge_name, rule], check=True)
    print(f"OpenFlow rule '{rule}' added to bridge {bridge_name}.")

def apply_qos(port_name, max_rate, min_rate):
    subprocess.run(["ovs-vsctl", "set", "port", port_name, "qos=@newqos", "--",
                    "--id=@newqos", "create", "qos", "type=linux-htb", f"other-config:max-rate={max_rate}", "queues:0=@q0", "--",
                    "--id=@q0", "create", "queue", f"other-config:min-rate={min_rate}", f"other-config:max-rate={max_rate}"], check=True)
    print(f"QoS applied to port {port_name} with max rate {max_rate} and min rate {min_rate}.")

if __name__ == "__main__":
    # Create OVS bridge
    create_bridge("br0")

    # Add interfaces to the bridge
    add_port("br0", "eth1")
    add_port("br0", "eth2")

    # Set up normal traffic flow from c1 to s1
    add_openflow_rule("br0", "in_port=1,actions=output:2")

    # Apply QoS to traffic from c2 to s1
    apply_qos("eth2", 1000000000, 500000000)

    # Add flow for QoS traffic
    add_openflow_rule("br0", "in_port=2,actions=set_queue:0,output:2")
    