import argparse
from socket import *

def ScanConnection(targetHost,targetPort):
    try:    
        Socket=socket(AF_INET,SOCK_STREAM)       
        Socket.connect((targetHost,targetPort))
        print ("%d tcp open" % targetPort)
    except:       
        print ("%d tcp closed" % targetPort)
    finally:
        Socket.close()

def ScanPorts(targetHost,targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print("Unknown Host")
        exit(0)

    try:
        targetName = gethostbyaddr(targetIP)
        print ("Result for: " + targetName[0])
    except:
        print ("Result for: " + targetIP)

    setdefaulttimeout(10)

    for targetPort in targetPorts:
        ScanConnection(targetHost, int(targetPort))

def Main():
    parser = argparse.ArgumentParser('Port scanner')
    parser.add_argument("-a","--address", type=str, help="The IP address")
    parser.add_argument("-p","--port", type=str, help="The port numbers")
    args = parser.parse_args()

    ipaddress = args.address
    portNumbers = args.port.split(',')

    ScanPorts(ipaddress,portNumbers)
        
if __name__ == "__main__":
	Main()
