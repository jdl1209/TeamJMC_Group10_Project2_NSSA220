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

    total_f_size=0
    

    for packet in req_sent_list:
        request_bytes_sent+=int(packet[5])
        request_data_sent+=int(packet[5])-42
        total_f_size+=int(packet[5])

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
    delay_times=[]
    count=0
    while count<= len(req_sent_list)-1:
        rtt=float(reply_received_list[count][1])-float(req_sent_list[count][1])
        hop_count=(float(req_sent_list[count][9].split("=")[1])-float(reply_received_list[count][9].split("=")[1]))+1
        hops.append(hop_count)
        times.append(rtt)
        
        count+=1

    count2=0
    while count2 <= len(req_received_list)-1:
        delay=float(reply_sent_list[count2][1])-float(req_received_list[count2][1])
        delay_times.append(delay)
        count2+=1

    total_rtt=0
    total_hop=0
    total_time=0
    for rtt in times:
        total_rtt+=rtt
    for hop in hops:
        total_hop+=hop
    for delay in delay_times:
        total_time+=delay
    
    average_delay=round(total_time/len(delay_times)*1000000, 2)
    
    average=round(total_rtt/len(times)*1000,2)
    average_hop=round(total_hop/len(hops),2)

    throughput=round((total_f_size/total_rtt)/1000, 1)
    goodput=round((request_data_sent/total_rtt)/1000, 1)
  
    
    print("Requests Sent: " + str(request_sent))
    print("Requests Received: " + str(request_received))
    print("Replies Sent: " + str(reply_sent))
    print("Replies Received: " + str(reply_received))

    print("Echo Request Bytes Sent: " + str(request_bytes_sent))
    print("Echo Request Bytes Received: " + str(request_bytes_received))
    print("Echo Request Data Sent: " + str(request_data_sent))
    print("Echo Request Data Received: " + str(request_data_received) + "\n")

    print("Average RTT (ms): " + str(average))
    print("Echo Request Throughput (kB/sec): " + str(throughput))
    print("Echo Request Goodput (kB/sec): " + str(goodput))
    print("Average Reply Delay (us): " + str(average_delay) + "\n")

    print("Average Hops: " + str(average_hop) + "\n")

    f = open("Project2_Output_TeamJMC.csv", "a")
    f.write("\n\nEcho Requests Sent,Echo Requests Received, Echo Replies Sent,Echo Replies Received\n")
    f.write(str(request_sent)  + "," + str(request_received) + "," + str(reply_sent)  + "," + str(reply_received) + "\n")
    f.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
    f.write(str(request_bytes_sent) + "," + str(request_bytes_received) + "\n")
    f.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)" + "\n")
    f.write(str(request_data_sent) + "," + str(request_data_received) + "\n\n")
    f.write("Average RTT (milliseconds)" + "," + str(average) + "\n")
    f.write("Echo Request Throughput (kB/sec)" + "," + str(throughput) + "\n")
    f.write("Echo Request Goodput (kB/sec)" + "," + str(goodput) + "\n")
    f.write("Average Reply Delay (microseconds)" + "," + str(average_delay) + "\n")
    f.write("Average Echo Request Hop Count" + "," + str(average_hop) + "\n\n")

    f.close()


