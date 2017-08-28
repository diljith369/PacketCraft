from scapy.all import *

class CraftPacket():

    def __init__(self, sourceIP, destIP, sourcePort, destinationPort,packetCount, packetInterval,payload, protocol,ttlValue,packetType,flags):
        self.sourceIP = sourceIP
        self.destIP = destIP
        self.sourcePort = sourcePort
        self.destinationPort = destinationPort
        self.packetCount = packetCount
        self.packetInterval = packetInterval
        self.payload=payload
        self.protocol =  protocol
        self.ttlValue =  ttlValue
        self.packetType =  packetType
        self.flags =  flags


    def sendandreceive(self):
        if  self.protocol == "tcp":
            packetToSend = self.CreateTcpLayerPacket()
        elif self.protocol =="udp":
            packetToSend = self.CreateUdpLayerPacket()
        else:
            packetToSend = self.CreatePingPacket()


        res, noans = srloop(packetToSend,count= self.packetCount, inter= self.packetInterval)
        print(str(packetToSend.show))
        #pktSummary=""

        if len(res) > 0:
            if  self.protocol == "tcp":
                rhost = str(res[0][1].sprintf(r" %IP.src%")) +"\n"
                rport= str(res[0][1].sport) + "(" + str(res[0][1].sprintf(r" %TCP.sport%")) + ")" +"\n"
                rflags = str(res[0][1].sprintf(r" %TCP.flags%"))

                pktSummary = "RHOST : " + rhost + " RPORT : " + rport  + " Flag(s) :  " + rflags
            elif self.protocol == "icmp":
                pktSummary = (str(res[1][0].dst) + " is UP.")
        elif  len(noans) >  0:
            pktSummary = ("Something Went Wrong !!")

        return pktSummary

    def GetSummaryOfSuccessfullPackets(self,res):
        return ("RHOST : " + str(res[1][0].dst) + "RPORT : " + str(res[1][0].dport) + "Flag from RHOST :  " + str(res[1][0].flags))

    def captureSuccessReturnInFile(self,res):
        breakCount =1
        fo = open("packetResult.txt", "w")
        for snd,rcv in res:
            if breakCount == 1:
                if  self.protocol == "tcp":
                    fo.write(rcv.sprintf(r"RHOST <<==>> %IP.src% RPORT <<==>> %TCP.sport% RFlags <<==>> %TCP.flags% "))
                elif  self.protocol =="icmp":
                    fo.write(rcv.sprintf(r"%IP.src% is Up"))
                #pktSummary =  pktSummary.join(snd.sprintf(r"Local PORT ==>> %TCP.sport% Local IP ==>> %IP.src% Local TCP Flags ==>> %TCP.flags%")) + "\n"
                    breakCount = breakCount +1
            if breakCount > 1:
                break
        fo.close()

    def captureFailedReturnInFile(self,res):
        breakCount =1
        fo = open("packetResult.txt", "w")
        fo.write("Something Went Wrong !!")
        fo.close()


    def CreateTcpLayerPacket(self):
        pktNwLayer=IP()
        if self.sourceIP:
            pktNwLayer.src= self.sourceIP
        pktNwLayer.dst= self.destIP
        pktNwLayer.ttl=   self.ttlValue

        pktTrLayer =  TCP(sport=self.sourcePort,dport=self.destinationPort,flags=self.flags)
        pktToReturn = pktNwLayer/pktTrLayer/self.payload
        return pktToReturn

    def CreateUdpLayerPacket(self):
        pktNwLayer=IP()
        if  self.sourceIP:
            pktNwLayer.src= self.sourceIP
        pktNwLayer.dst= self.destIP
        pktNwLayer.ttl=   self.ttlValue
        pktTrLayer =  UDP(sport=self.sourcePort,dport=self.destinationPort)
        pktToReturn = pktNwLayer/pktTrLayer/self.payload
        return pktToReturn

    def CreatePingPacket(self):
        pktNwLayer=IP()
        if  self.sourceIP:
            pktNwLayer.src= self.sourceIP
        pktNwLayer.dst= self.destIP
        pktToReturn = pktNwLayer/ICMP()/self.payload
        return pktToReturn




    #def sendTCP():

    #def sendUDP():

    #def sendHTTP():

    #def sendEther():

    #def sendWIFI():
