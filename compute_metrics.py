def compute_metrics(node_file, address):
    file = open(node_file)
    line = file.readline()

    # Totals of Requests/Replies Sent & Recieved
    request_sent=0
    request_received=0
    reply_sent=0
    reply_received=0

    # Lists for Requests/Replies Sent & Recieved
    req_sent_list=[]
    req_received_list=[]
    reply_sent_list=[]
    reply_received_list=[]

    request_bytes_sent=0
    request_bytes_received=0
    request_data_sent=0
    request_data_received=0

    # Find average time of requests and subtract average response time??
    times=[]
    

    """
    If Source is 192.168.100.1 and echo request == Request Sent, add that line to its own list
    If Destination is 192.168.100.1 and echo request == Request Recieved, add that line to its own list
    Repeat both of these steps for Echo Replies
    """

    while line:
        line=file.readline()
        if "Echo (ping) request" in line:
            line=line.strip().split(" ")
            final=[]
            for item in line:
                if item != "":
                    final.append(item)

            # Fixes Some formatting
            final[6:9] = [' '.join(final[6:9])]
            final[10:13] = [' '.join(final[10:13])]
            final[10] = final[10].replace("(", "")
            final[10] = final[10].replace(")", "")
            
            if final[2]==address and final[6]=="Echo (ping) request":
                req_sent_list.append(final)
                request_sent+=1
            if final[3]==address and final[6]=="Echo (ping) request":
                req_received_list.append(final)
                request_received+=1
            line=file.readline()
        elif "Echo (ping) reply" in line:
            line=line.strip().split(" ")
            final=[]
            for item in line:
                if item != "":
                    final.append(item)

            # Fixes Some formatting        
            final[6:9] = [' '.join(final[6:9])]
            final[10:13] = [' '.join(final[10:13])]
            final[10] = final[10].replace("(", "")
            final[10] = final[10].replace(")", "")
            
            if final[2]==address and final[6]=="Echo (ping) reply":
                reply_sent_list.append(final)
                reply_sent+=1
            if final[3]==address and final[6]=="Echo (ping) reply":
                reply_received_list.append(final)
                reply_received+=1
            line=file.readline()
        else:
            line=file.readline()
    file.close()

    for packet in req_sent_list:
        request_bytes_sent+=int(packet[5])
        # NO IDEA IF WE'RE SUPPOSED TO SUBTRACT 42 BUT THE NUMBERS ARE CORRECT??
        request_data_sent+=int(packet[5])-42

    for packet in req_received_list:
        request_bytes_received+=int(packet[5])
        request_data_received+=int(packet[5])-42
    
    count=0
    while count<= len(req_sent_list)-1:
        rtt=float(reply_received_list[count][1])-float(req_sent_list[count][1])
        times.append(rtt)
        count+=1

    total=0
    for rtt in times:
        total+=rtt
    
    average=round(total/len(times)*1000,2)

    



    print("Requests Sent: " + str(request_sent))
    print("Requests Received: " + str(request_received))
    print("Replies Sent: " + str(reply_sent))
    print("Replies Received: " + str(reply_received))

    print("Echo Request Bytes Sent: " + str(request_bytes_sent))
    print("Echo Request Bytes Received: " + str(request_bytes_received))
    print("Echo Request Data Sent: " + str(request_data_sent))
    print("Echo Request Data Received: " + str(request_data_received) + "\n")

    print("Average RTT (ms): " + str(average))

    

compute_metrics("Node1_filtered.txt", "192.168.100.1")

