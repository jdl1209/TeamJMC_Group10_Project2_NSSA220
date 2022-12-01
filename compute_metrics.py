import packet_parser
def compute_metrics(req_sent_list, req_received_list, reply_sent_list, reply_received_list):

    # Calculates how many requests/replies were sent/received
    request_sent=len(req_sent_list)
    request_received=len(req_received_list)
    reply_sent=len(reply_sent_list)
    reply_received=len(reply_received_list)

    # Variables for bytes sent/received
    request_bytes_sent=0
    request_bytes_received=0
    request_data_sent=0
    request_data_received=0

    for packet in req_sent_list:
        request_bytes_sent+=int(packet[5])
        # NO IDEA IF WE'RE SUPPOSED TO SUBTRACT 42 BUT THE NUMBERS ARE CORRECT??
        request_data_sent+=int(packet[5])-42

    for packet in req_received_list:
        request_bytes_received+=int(packet[5])
        request_data_received+=int(packet[5])-42
    

    """
    Goes through the requests sent and recieved for the chosen 
    IP address and subtracts the time the reply was received from
    the time the request was sent.

    That time is added to an overall list of times

    A loop goes through the list of time and adds all times together

    That total time is divided by how many times were recorded to
    find the average RTT
    """
    times=[]
    hops=[]
    count=0
    while count<= len(req_sent_list)-1:
        rtt=float(reply_received_list[count][1])-float(req_sent_list[count][1])
        hop_count=(float(req_sent_list[count][9].split("=")[1])-float(reply_received_list[count][9].split("=")[1]))+1
        hops.append(hop_count)
        times.append(rtt)
        count+=1

    total=0
    total_hop=0
    for rtt in times:
        total+=rtt
    for hop in hops:
        total_hop+=hop
    
    average=round(total/len(times)*1000,2)
    average_hop=round(total_hop/len(hops),2)
  
    print("Requests Sent: " + str(request_sent))
    print("Requests Received: " + str(request_received))
    print("Replies Sent: " + str(reply_sent))
    print("Replies Received: " + str(reply_received))

    print("Echo Request Bytes Sent: " + str(request_bytes_sent))
    print("Echo Request Bytes Received: " + str(request_bytes_received))
    print("Echo Request Data Sent: " + str(request_data_sent))
    print("Echo Request Data Received: " + str(request_data_received) + "\n")

    print("Average RTT (ms): " + str(average))
    print("Echo Request Throughput (kB/sec): ")
    print("Echo Request Goodput (kB/sec): ")
    print("Average Reply Delay (us): " + "\n")

    print("Average Hops: " + str(average_hop))
  

l1=[]
l2=[]
l3=[]
l4=[]
packet_parser.packet_parser("Node1_filtered.txt", "192.168.100.1", l1, l2, l3, l4)
compute_metrics(l1, l2, l3, l4)


