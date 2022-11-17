def compute_metrics(node):
    file = open(node)
    line = file.readline()
    i=0
    request_sent=0
    request_received=0
    reply_sent=0
    reply_received=0
    request_data=0
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
                request_sent+=1
            if final[3]=="192.168.100.1" and final[6]=="Echo (ping) request":
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
                reply_sent+=1
            if final[3]=="192.168.100.1" and final[6]=="Echo (ping) reply":
                reply_received+=1
            line=file.readline()
        else:
            line=file.readline()

    print("Requests Sent: " + str(request_sent))
    print("Requests Received: " + str(request_received))
    print("Replies Sent: " + str(reply_sent))
    print("Replies Received: " + str(reply_received))
    
    

compute_metrics("Node1_filtered.txt")