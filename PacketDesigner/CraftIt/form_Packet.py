from django import forms
from django.core import validators
import random

class PacketForm(forms.Form):

    TCP_FLAGS =(("S", "SYN"),
                        ("A","ACK"),
                        ("R","RST"),("U","URG"),("P","PSH"),("F","FIN"))
    PROTOCOL_LIST = (('tcp','TCP'),('udp','UDP'),('icmp','ICMP'))
    PACKET_TYPE=(('ETH','EtherNet'),('WIFI','WiFi'))


    sourceIP= forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Source IP',required=False)
    dstIP = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Destination IP or Domain')
    protocol = forms.ChoiceField( widget=forms.Select(attrs={'class':'form-control'}),label='Protocol',choices=PROTOCOL_LIST,required=False)
    sourcePort=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','size': 5}),label='Source Port',required=False,initial=random.randrange(1024,65535));
    destinationPort= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','size': 5}),label='Dest Port(s)',initial=445,required=False)
    packetType = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','name': 'packetType'}),label='Packet Type',choices=PACKET_TYPE,required=True)
    packetCount=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Packet Count',initial= 1,required=False)
    packetInterval= forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Packet Interval',required=False,initial=1.0)
    payload= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','size': 32}),label='Payload',max_length=32,required=False,initial="Hello Packet")
    fuzz = forms.ChoiceField( widget=forms.Select(attrs={'class':'form-control'}),label='Fuzz',choices=(('fT','TCP'),('fU','UDP')),required=False)
    flags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox-inline'}),choices=TCP_FLAGS,required=False)
    ttlValue = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='TTL',required=False,initial=1)
