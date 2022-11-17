def compute_metrics(node):
    file = open(node)
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
    reply_bytes_sent=0
    reply_bytes_received=0
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
            final[6:9] = [' '.join(final[6:9])]
            if final[2]=="192.168.100.1" and final[6]=="Echo (ping) request":
                req_sent_list.append(final)
                request_sent+=1
            if final[3]=="192.168.100.1" and final[6]=="Echo (ping) request":
                req_received_list.append(final)
                request_received+=1
            line=file.readline()
        elif "Echo (ping) reply" in line:
            line=line.strip().split(" ")
            final=[]
            for item in line:
                if item != "":
                    final.append(item)
            final[6:9] = [' '.join(final[6:9])]
            if final[2]=="192.168.100.1" and final[6]=="Echo (ping) reply":
                reply_sent_list.append(final)
                reply_sent+=1
            if final[3]=="192.168.100.1" and final[6]=="Echo (ping) reply":
                reply_received_list.append(final)
                reply_received+=1
            line=file.readline()
        else:
            line=file.readline()
    for packet in req_sent_list:
        request_bytes_sent+=int(packet[5])

    for packet in req_received_list:
        request_bytes_received+=int(packet[5])

    for packet in reply_sent_list:
        reply_bytes_sent+=int(packet[5])
        
    for packet in reply_received_list:
        reply_bytes_received+=int(packet[5])

    print("Requests Sent: " + str(request_sent))
    print("Requests Received: " + str(request_received))
    print("Replies Sent: " + str(reply_sent))
    print("Replies Received: " + str(reply_received))

    print("Echo Request Bytes Sent: " + str(request_bytes_sent))
    print("Echo Request Bytes Received: " + str(request_bytes_received))
    print("Echo Reply Bytes Sent: " + str(reply_bytes_sent))
    print("Echo Reply Bytes Received: " + str(reply_bytes_received))
    
    

compute_metrics("Node1_filtered.txt")