NOINFO = 0
INFOIP = 1
INFOGTAWAY = 2

PREFIX = 0
MASK = 1
GTWY = 2

NUMB = 0
COUNT = 1

def split_line(line, mode):
    line_s = line.split(' ')

    if (mode ==INFOIP):
        d = [line_s[0],line_s[3].replace('\n', '')]
        d[0]=d[0][1:]
    elif (mode==INFOGTAWAY):
        d = [line_s[0],line_s[5].replace('\n', '')]
        d[0]=d[0][1:]
    else:
        d = line_s[1]

    return d

fr=open('config', 'r')

state = NOINFO
buffer = {}
counter = 0
switch_ip = {}
mac_to_port = {}
switch = {}
ip_to_mac = {}
count =1

for line in fr:
    
    if (line != "\n"):
        state = split_line(line,NOINFO)
            
        if (state == "ifconfig"):
            a=split_line(line,INFOIP)
            val_s = a[1].split('/')
            buffer[a[0]]= {}
            buffer[a[0]][PREFIX] = [val_s[0]]
            buffer[a[0]][MASK] = [val_s[1]]
                
        
        elif (state == "route"):
            a=split_line(line,INFOGTAWAY)
            buffer[a[0]][GTWY] = a[1]
         
"""#print ("buffer")
#print (buffer)
print("aaaaaaaaa")
#print(buffer2)
print("bbbbbbbbb")
print(buffer)
#print(buffer_n)
print("bbbbbbbbb")

print ("buffer")
print (buffer)"""

guardados=[]
counter_mac = 0
count_mtp = {}



for key,val in sorted(buffer.items()):

    numb = str(count)

    counter_mac=counter_mac+1
    ip_to_mac[buffer[key][PREFIX][0]]=["00:00:00:00:00:"+str(format(counter_mac,'02x'))]
   
    if not (any(buffer[key][GTWY] in s for s in guardados)):
        switch[numb] = [buffer[key][GTWY], buffer[key][MASK],"00:00:00:11:11:"+str(format(counter_mac,'02x')) , "s"+numb, numb]
        switch_ip[buffer[key][GTWY]]=[str(count)]

        mac_to_port[numb]={}
        mac_to_port[numb]["00:00:00:00:00:"+str(format(counter_mac,'02x'))]= 1

        count_mtp[buffer[key][GTWY]] = {}
        count_mtp[buffer[key][GTWY]][NUMB] = numb
        count_mtp[buffer[key][GTWY]][COUNT] = 1

        guardados.append(buffer[key][GTWY])
        count= count+1
        
    else:
        count_mtp[buffer[key][GTWY]][COUNT] += 1
        mac_to_port[count_mtp[buffer[key][GTWY]][NUMB]]["00:00:00:00:00:"+str(format(counter_mac,'02x'))]= count_mtp[buffer[key][GTWY]][COUNT]
 
print("zzzzzzzzzzzzzzzzzz")
print (mac_to_port)
print("zzzzzzzzzzzzzzzzzz")
print (switch)
print("zzzzzzzzzzzzzzzzzz")
print (switch_ip)
print("zzzzzzzzzzzzzzzzzz")
print (ip_to_mac)
print ("asfasdfsdf")




fr.close()
