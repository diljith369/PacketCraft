from django.shortcuts import render
from . import form_Packet
from . import ScapyPacket
from pathlib import Path
from CraftIt.models import PacketDetails

def packet_craft(request):
    #if request.method == "GET":
    form_pkt=form_Packet.PacketForm()
    print(request.method)
    #print("Destination IP : " + form_pkt.cleaned_data['dstIP'])
    if request.method == 'POST':
        form_pkt=form_Packet.PacketForm(request.POST)
        if form_pkt.is_valid():
            sourceIP=form_pkt.cleaned_data['sourceIP']
            dstIP= form_pkt.cleaned_data['dstIP']
            sourcePort=form_pkt.cleaned_data.get("sourcePort")
            destinationPort = form_pkt.cleaned_data.get("destinationPort")
            packetCount=form_pkt.cleaned_data.get("packetCount")
            packetInterval=form_pkt.cleaned_data.get("packetInterval")
            payload=form_pkt.cleaned_data['payload']
            packetType = form_pkt.cleaned_data.get("packetType")
            protocol=form_pkt.cleaned_data.get("protocol")
            flags=form_pkt.cleaned_data.get("flags")
            ttlValue = form_pkt.cleaned_data.get("ttlValue")
            print(request.POST)
            if flags:
                allflags = "".join(str(val) for val in flags)
            else:
                allflags =""
                #print("all flags : " + allflags)
            #print("TTL Value :" +str(ttlValue))
            #print("PacketType" + packetType)
            #print("Protocol" + protocol)
            #print(sourceIP)
            #print("Destination IP : " +dstIP)
            #print(payload)
            packetToSend = ScapyPacket.CraftPacket(sourceIP,dstIP,sourcePort,destinationPort,packetCount,packetInterval,payload,protocol,ttlValue,packetType,allflags)
            summary = packetToSend.sendandreceive()

            '''
            chkResFile = Path("packetResult.txt")
            if chkResFile.exists():
                readSummary = open(chkResFile,"r")
                summary = readSummary.readline()
                readSummary.close()
            else:
                summary = "Please make sure that App has enough permissions ."

            print("Summary from Scapy:" + summary)
            '''

            urPkt = PacketDetails(db_srcIP=sourceIP,db_destIP=dstIP,db_summary=summary)
            urPkt.save()

            packet_summary = PacketDetails.objects.all().values()
            srcipFromdb = packet_summary[0]['db_srcIP']
            destIPFromdb = packet_summary[0]['db_destIP']
            summaryFromdb = packet_summary[0]['db_summary']

            lst_Packet = [{"SOURCEIP":srcipFromdb ,"DESTINATIONIP":destIPFromdb,"SUMMARY":summaryFromdb}]
            #print("summary from DB " + str(packet_summary['db_summary']))
            dict_processedPacket = {'summary' : lst_Packet}
            PacketDetails.objects.all().delete()
            #print("Soure IP : " + srcipFromdb)
            #print("Destination IP :" + dict_processedPacket['DESTINATIONIP'])
            #print("Summary :" + dict_processedPacket['SUMMARY'])

            return render(request,'CraftIt/YourPacket.html',dict_processedPacket)
            #pkt = form_pkt.cleaned_data['packetType']
            #pkt = dict(form_pkt.fields['packetType'])[packetType]
            #typeP = dict(form_pkt.fields['packetType'].choices)[form_pkt.cleaned_data['packetType']]
            #typeP = form_pkt.cleaned_data.get('packetType')

        else:
            print('invalid')
            typeP = request.POST
            print("Post Data:" + str(typeP))
    else:
        return render(request,'CraftIt/form_Packet.html', {'form':form_pkt})
    #return render(request,'CraftIt/form_Packet.html', {'form':form_pkt})


# Create your views here.
