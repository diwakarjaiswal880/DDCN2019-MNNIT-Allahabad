"""Topology with 10 switches and 10 hosts
"""

from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
class CSLRTopo( Topo ):

        def __init__( self ):
                "Create Topology"

                # Initialize topology
                Topo.__init__( self )

                # Add hosts
                h1 = self.addHost( 'h1')
                h2 = self.addHost( 'h2')
                h3 = self.addHost( 'h3')
                h4 = self.addHost( 'h4')
		

		# Add switches
                s1 = self.addSwitch( 's1', listenPort=6635 )
                s2 = self.addSwitch( 's2', listenPort=6636 )
                s3 = self.addSwitch( 's3', listenPort=6637 )
                s4 = self.addSwitch( 's4', listenPort=6638 )

		# Add links between hosts and switches
                self.addLink( h1, s1 ) # h0-eth0 <-> s0-eth1
                self.addLink( h2, s1 ) # h1-eth0 <-> s1-eth1
                self.addLink( h3, s4 ) # h2-eth0 <-> s2-eth1
                self.addLink( h4, s4 ) # h3-eth0 <-> s3-eth1

		# Add links between switches, with bandwidth 100Mbps
                self.addLink( s1, s2, bw=1 ) # s0-eth2 <-> s1-eth2, Bandwidth = 1Mbps
		self.addLink( s1, s3, bw=10 ) # s0-eth2 <-> s1-eth2, Bandwidth = 10Mbps
		self.addLink( s4, s2, bw=1 ) # s0-eth2 <-> s1-eth2, Bandwidth = 1Mbps
		self.addLink( s4, s3, bw=10 ) # s0-eth2 <-> s1-eth2, Bandwidth = 10Mbps


def run():
        "Create and configure network"
        topo = CSLRTopo()
        net = Mininet( topo=topo, link=TCLink, controller=None )
	"""
        # Set interface IP and MAC addresses for hosts
	
	h1 = net.get( 'h1' )
        h1.intf( 'h1-eth0' ).setIP( '10.0.0.1', 24 )
        h1.intf( 'h1-eth0' ).setMAC( '0A:00:01:02:00:00' )

        h2 = net.get( 'h2' )
        h2.intf( 'h2-eth0' ).setIP( '10.0.0.2', 24 )
        h2.intf( 'h2-eth0' ).setMAC( '0A:00:02:02:00:00' )

        h3 = net.get( 'h3' )
        h3.intf( 'h3-eth0' ).setIP( '10.0.0.3', 24 )
        h3.intf( 'h3-eth0' ).setMAC( '0A:00:03:02:00:00' )

        h4 = net.get( 'h4' )
        h4.intf( 'h4-eth0' ).setIP( '10.0.0.4', 24 )
        h4.intf( 'h4-eth0' ).setMAC( '0A:00:04:02:00:00' )


	# Set interface MAC address for switches (NOTE: IP
        # addresses are not assigned to switch interfaces)
 
	s1 = net.get( 's1' )
        s1.intf( 's1-eth1' ).setMAC( '0A:00:01:01:00:01' )
        s1.intf( 's1-eth2' ).setMAC( '0A:00:0A:FE:00:02' )
        s1.intf( 's1-eth3' ).setMAC( '0A:00:0C:01:00:03' )
	s1.intf( 's1-eth4' ).setMAC( '0A:00:0B:01:00:04' )

        s2 = net.get( 's2' )
        s2.intf( 's2-eth1' ).setMAC( '0A:00:02:01:00:01' )
        s2.intf( 's2-eth2' ).setMAC( '0A:00:0B:FE:00:02' )

        s3 = net.get( 's3' )
        s3.intf( 's3-eth1' ).setMAC( '0A:00:03:01:00:01' )
        s3.intf( 's3-eth2' ).setMAC( '0A:00:0D:FE:00:02' )

        s4 = net.get( 's4' )
        s4.intf( 's4-eth1' ).setMAC( '0A:00:04:01:00:01' )
        s4.intf( 's4-eth2' ).setMAC( '0A:00:0E:FE:00:02' )
        s4.intf( 's4-eth3' ).setMAC( '0A:00:10:01:00:03' )
	s4.intf( 's4-eth4' ).setMAC( '0A:00:0D:01:00:04' )

	net.start()

	 # Add routing table entries for hosts (NOTE: The gateway
		# IPs 10.0.X.1 are not assigned to switch interfaces)

        
 	h1.cmd( 'route add default gw 10.0.0.1 dev h1-eth0' )
        h2.cmd( 'route add default gw 10.0.0.2 dev h2-eth0' )
        h3.cmd( 'route add default gw 10.0.0.3 dev h3-eth0' )
        h4.cmd( 'route add default gw 10.0.0.4 dev h4-eth0' )
	
	# Add arp cache entries for hosts
        h1.cmd( 'arp -s 10.0.0.1 0A:00:01:01:00:01 -i h1-eth0' )
        h2.cmd( 'arp -s 10.0.0.2 0A:00:02:01:00:01 -i h2-eth0' )
        h3.cmd( 'arp -s 10.0.0.3 0A:00:03:01:00:01 -i h3-eth0' )
        h4.cmd( 'arp -s 10.0.0.4 0A:00:04:01:00:01 -i h4-eth0' )
        """
	net.start()
	# Open Mininet Command Line Interface
        CLI(net)
	
        # Teardown and cleanup
        net.stop()

if __name__ == '__main__':
    setLogLevel('info')
run()











