def filter_packets(text_file):
    text_file_number=text_file.split(".")
    text_file_filtered=text_file_number[0]+"_filtered.txt"
    
    file=open(text_file)
    line=file.readline()
    request="Echo (ping) request"
    reply="Echo (ping) reply"
    overall_list=[]
    while line:
        if (request in line) or (reply in line):
            temp_list=[]
            line=line.strip()
            temp_list.append("No.  Time \t\t   Source \t\t\t     Destination   \t\t   Protocol Length Info")
            temp_list.append(line)
            line=file.readline()
            i=0
            while i < 6:
                line=line.strip()
                temp_list.append(line)
                line=file.readline()
                i+=1
            overall_list.append(temp_list)
        else:
            line=file.readline()
            continue
    file.close()


    with open(text_file_filtered, "w") as n2:   
        for items in overall_list:
            string=items[0] + "\n" + items[1] + "\n" + items[2] + items[3] + "\n" + items[4] + "\n" +items[5] + "\n" + items[6] + "\n" + items[7] + "\n\n"
            n2.write(string)

def main():
    filter_packets("Node1.txt")
    filter_packets("Node2.txt")
    filter_packets("Node3.txt")
    filter_packets("Node4.txt")
main()
