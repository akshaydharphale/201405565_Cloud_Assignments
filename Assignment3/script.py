#!/usr/bin/python

import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    numOfSwitch = int(sys.argv[1])
    hostPerSwitch = int(sys.argv[2])
    total = numOfSwitch * 2   
    
    es = "10.0.0."
    od = "11.0.0."


    sw = []
    hc = 1
    for x in range (numOfSwitch):
	temp = "s"+str(x+1)
	switch = net.addSwitch(temp)
	
	hostname = "h"+str(hc)
	hostname = net.addHost(hostname,ip= es+str(x+1))
	net.addLink(hostname,switch)

	hc += 1
	hostname = "h"+str(hc) 
	hostname = net.addHost(hostname,ip= od+str(x+1))
	net.addLink(hostname,switch)
	hc += 1
	sw.append(switch)


    info( '*** Adding hosts\n' )   

    info( '*** Creating links\n' )
 
    for x in range(len(sw)-1):
	net.addLink(sw[x],sw[x+1])	


    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
