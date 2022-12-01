def packet_parser(node_file, address):
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
