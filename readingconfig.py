#Differents modes of reading the file
NOINFO = 0
INFOIP = 1
INFOGTAWAY = 2

#Types of stored information
PREFIX = 0
MASK = 1
GTWY = 2

NUMB = 0
COUNT = 1

class ReadingFromFile:

    switch_ip = {}
    mac_to_port = {}
    switch = {}
    ip_to_mac = {}

    def __init__(self, filename):
        self.read_file(filename)

    @staticmethod
    def split_line(line, mode):
        """
        Split the line given depending on its type
        INFOIP return a list of the id, the prefix and the mask value
        INFOGTAWAY returns a list of the id and the ip of the switch
        the default mode just returns the state for the reading
        """

        line_s = line.split(' ')

        if (mode ==INFOIP):
            d = [line_s[0],line_s[3].replace('\n', ''),'']
            d[0]=int(d[0][1:])
            val_s = d[1].split('/')
            d[1]=val_s[0]
            d[2]=val_s[1]
        elif (mode==INFOGTAWAY):
            d = [line_s[0],line_s[5].replace('\n', '')]
            d[0]=int(d[0][1:])
        else:
            d = line_s[1]

        return d
        

    def read_file(self, filename):
        """Reads the config file and then create the necessary dictionaries 
	    to create the topology of the network	
	    """

        state = NOINFO
        buffer = {}
        counter = 0
        count =1

        fr=open(filename, 'r')

        for line in fr:
            if (line != "\n"):
                state = self.split_line(line,NOINFO)

                if (state == "ifconfig"):
                    line_splitted=self.split_line(line,INFOIP)
                    buffer[line_splitted[0]]= {}
                    buffer[line_splitted[0]][PREFIX] = line_splitted[1]
                    buffer[line_splitted[0]][MASK] = line_splitted[2]	
				
                elif (state == "route"):
                    a=self.split_line(line,INFOGTAWAY)
                    buffer[a[0]][GTWY] = a[1]


        visited=[]
        counter_mac = 0
        count_mtp = {}

        for key,val in sorted(buffer.items()):

            numb = str(count)
            counter_mac=counter_mac+1
            self.ip_to_mac[buffer[key][PREFIX]]="00:00:00:00:00:"+str(format(counter_mac,'02x'))


            if not (any(buffer[key][GTWY] in s for s in visited)):
                self.switch[numb] = [buffer[key][GTWY], buffer[key][MASK],"00:00:00:11:11:"+str(format(counter_mac,'02x')) , "s"+numb, numb]
                self.switch_ip[buffer[key][GTWY]]=[str(count)]

                self.mac_to_port[numb]={}
                self.mac_to_port[numb]["00:00:00:00:00:"+str(format(counter_mac,'02x'))]= 1

                count_mtp[buffer[key][GTWY]] = {}
                count_mtp[buffer[key][GTWY]][NUMB] = numb
                count_mtp[buffer[key][GTWY]][COUNT] = 1

                visited.append(buffer[key][GTWY])
                count= count+1
				
            else:
                count_mtp[buffer[key][GTWY]][COUNT] += 1
                self.mac_to_port[count_mtp[buffer[key][GTWY]][NUMB]]["00:00:00:00:00:"+str(format(counter_mac,'02x'))]= count_mtp[buffer[key][GTWY]][COUNT]
                
        print("zzzzzzzzzzzzzzzzzz")
        print (self.mac_to_port)
        print("zzzzzzzzzzzzzzzzzz")
        print (self.switch)
        print("zzzzzzzzzzzzzzzzzz")
        print (self.switch_ip)
        print("zzzzzzzzzzzzzzzzzz")
        print (self.ip_to_mac)
        print ("asfasdfsdf")      

        fr.close()

a = ReadingFromFile('config12')
    
            
