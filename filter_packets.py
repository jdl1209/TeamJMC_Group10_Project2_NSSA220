def filter_packets(text_file):
    #Creates the name of the new filtered file being created
    text_file_number=text_file.split(".")
    text_file_filtered=text_file_number[0]+"_filtered.txt"
    
    file=open(text_file)
    line=file.readline()

    #Default messages to be identified when reading file
    request="Echo (ping) request"
    reply="Echo (ping) reply"

    #Creates an empty final list
    overall_list=[]
    while line:
        """
        If the 'request' or 'reply' is found within the line being read, the following data will be added to a temporary list
        
        No.       Time        Source        Destination       Protocol        Length    Info
        #         time(sec)   Src IP        Dest IP           protocol type   bytes     id/seq/ttl

        hex information
        """
        
        if (request in line) or (reply in line):
            temp_list=[]
            line=line.strip()

            #Creates the Header for each Request/Reply
            temp_list.append("No.  Time \t\t   Source \t\t\t     Destination   \t\t   Protocol Length Info")
            
            #Appends the line being read: Frame Number, Time, Source, Destination, Protocol, Length, Info
            temp_list.append(line)
            line=file.readline()

            """
            ICMP echo Requests/Replys have 5 lines of Hex Information
            After the base info is recorded (described above), the 5
            are added to the temp_list 
            """
            i=0
            while i < 6:
                line=line.strip()
                temp_list.append(line)
                line=file.readline()
                i+=1

            #All information from the frame being read is added to the overall list as its own item
            overall_list.append(temp_list)

        #If no Request/Reply is found, the line is ignored and the file continues to be read
        else:
            line=file.readline()
            continue
    file.close()


    # Writes the filtered data to a new file: Node*_filtered.txt
    with open(text_file_filtered, "w") as n2:   
        for items in overall_list:
            # Formats each item in the overall_list to be written to the text file
            string=items[0] + "\n" + items[1] + "\n" + items[2] + items[3] + "\n" + items[4] + "\n" +items[5] + "\n" + items[6] + "\n" + items[7] + "\n\n"
            n2.write(string)

