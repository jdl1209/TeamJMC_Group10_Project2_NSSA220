def packet_parser(node_file, address, req_s_list, req_r_list, reply_s_list, reply_r_list):
    file = open(node_file)
    line = file.readline()
    
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
                req_s_list.append(final)
                
            if final[3]==address and final[6]=="Echo (ping) request":
                req_r_list.append(final)
    
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
                reply_s_list.append(final)
               
            if final[3]==address and final[6]=="Echo (ping) reply":
                reply_r_list.append(final)
                
            line=file.readline()
        else:
            line=file.readline()     
    file.close()
    
    
l1=[]
l2=[]
l3=[]
l4=[]
packet_parser("Node1_filtered.txt", "192.168.100.1",l1, l2, l3, l4)
print(l4)


