import filter_packets
import packet_parser
import compute_metrics

l1 = []
l2 = []
l3 = []
l4 = []

nodes = ["Node1.txt", "Node2.txt", "Node3.txt", "Node4.txt"]

for node in nodes:

    filter_packets.filter_packets(node)

nodes_filtered = ["Node1_filtered.txt", "Node2_filtered.txt", "Node3_filtered.txt", "Node4_filtered.txt"]
addresses = ["192.168.100.1", "192.168.100.2", "192.168.200.1", "192.168.200.2"]

i = 0
for filtered in nodes_filtered:

    node_name_list = filtered.split("_")
    node_name = node_name_list[0]

    packet_parser.packet_parser(filtered, addresses[i], l1, l2, l3, l4)

    print(str(node_name))
    compute_metrics.compute_metrics(l1, l2, l3, l4)

    i += 1
