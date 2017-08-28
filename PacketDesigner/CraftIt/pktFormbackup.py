from django import forms
from django.core import validators

class PacketForm(forms.Form):

    TCP_FLAGS =(("S", "SYN"),
                        ("A","ACK"),
                        ("R","RST"),("U","URG"),("P","PSH"),("F","FIN"))
    PROTOCOL_LIST = (('tcp','TCP'),('udp','UDP'),('icmp','ICMP'),('http','HTTP'),('ftp','FTP'),('telnet','TELNET'))
    PACKET_TYPE=(('ETH','EtherNet'),('WIFI','WiFi'))

    sourceIP= forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Source IP',required=False)
    dstIP = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Destination IP')
    protocol = forms.ChoiceField( widget=forms.Select(attrs={'class':'form-control'}),label='Protocol',choices=PROTOCOL_LIST,required=False)
    sourcePort=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','size': 5}),label='Source Port',required=False,validators=[validators.MaxValueValidator(65535)]);
    destinationPort= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','size': 5}),label='Destination Port',min_value=1,max_value=65535,required=False)
    packetType = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','name': 'packetType'}),label='Packet Type',choices=PACKET_TYPE,required=True)
    packetCount=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Packet Count',min_value=1,max_value=65535,required=False)
    packetInterval= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Packet Interval',min_value=1,max_value=65535,required=False)
    payload= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','size': 32}),label='Payload',max_length=32,required=False)
    fuzz = forms.ChoiceField( widget=forms.Select(attrs={'class':'form-control'}),label='Fuzz',choices=(('fT','TCP'),('fU','UDP')),required=False)
    flags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox-inline'}),choices=TCP_FLAGS,required=False);

    sourceIP= forms.GenericIPAddressField(widget=forms.TextInput(),label='Source IP',required=False)
    dstIP = forms.GenericIPAddressField(widget=forms.TextInput(),label='Destination IP')
    protocol = forms.ChoiceField( widget=forms.Select(),label='Protocol',choices=PROTOCOL_LIST,required=False)
    sourcePort=forms.IntegerField(widget=forms.NumberInput(attrs={'size': 5}),label='Source Port',required=False,validators=[validators.MaxValueValidator(65535)]);
    destinationPort= forms.IntegerField(widget=forms.NumberInput(attrs={'size': 5}),label='Destination Port',min_value=1,max_value=65535,required=False)
    packetType = forms.ChoiceField(widget=forms.Select(),label='Packet Type',choices=PACKET_TYPE,required=True)
    packetCount=forms.IntegerField(widget=forms.NumberInput(),label='Packet Count',min_value=1,max_value=65535,required=False)
    packetInterval= forms.IntegerField(widget=forms.NumberInput(),label='Packet Interval',min_value=1,max_value=65535,required=False)
    payload= forms.CharField(widget=forms.TextInput(attrs={'size': 32}),label='Payload',max_length=32,required=False)
    fuzz = forms.ChoiceField( widget=forms.Select(),label='Fuzz',choices=(('fT','TCP'),('fU','UDP')),required=False)
    flags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=TCP_FLAGS,required=False);
