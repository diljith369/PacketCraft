1 . Create your Virtual Env
    virtualenv -p /usr/bin/python3.5 envName 
2 . Activate the Envv 
    source envName/bin/activate
3 . Install Django
    pip3 install django
4 . Install scapy 
    pip3 install scapy-python3
5. Runserver (Please change the permission of manage.py inside PacketDesigner folder {chmod +x manage.py}) 
   python manage.py runserver  (will be ready to use on port 8000)
