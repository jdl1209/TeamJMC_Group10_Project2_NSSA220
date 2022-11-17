def compute_metrics(node):
    file = open(node)
    line = file.readline()
    i=0
    request_sent=0
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
            request_data+=int(final[5])
            request_sent+=1
            line=file.readline()
        else:
            line=file.readline()

    print("Requests Sent: " + str(request_sent))
    print("Total Request Data: " + str(request_data))
    
    

compute_metrics("Node1_filtered.txt")