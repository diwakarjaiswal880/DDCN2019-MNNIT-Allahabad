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
                h1 = self.addHost( 'h1' )
                h2 = self.addHost( 'h2' )
                h3 = self.addHost( 'h3' )
		

		# Add switches
                s1 = self.addSwitch( 's1', listenPort=6635 )
   
		# Add links between hosts and switches
                self.addLink( h1, s1 ) # h1-eth0 <-> s1-eth1
                self.addLink( h2, s1 ) # h2-eth0 <-> s2-eth1

		# Add links between switches, with bandwidth 100Mbps
                self.addLink( s0, s4, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps
		self.addLink( s1, s4, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps
		self.addLink( s2, s5, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps
		self.addLink( s3, s5, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps
		self.addLink( s4, s6, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps
		self.addLink( s5, s6, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps

def run():
        "Create and configure network"
        topo = CSLRTopo()
        net = Mininet( topo=topo, link=TCLink, controller=None )

        # Set interface IP and MAC addresses for hosts
        h0 = net.get( 'h0' )
        h0.intf( 'h0-eth0' ).setIP( '10.0.0.2', 24 )
        h0.intf( 'h0-eth0' ).setMAC( '0A:00:00:02:00:00' )
	
	h1 = net.get( 'h1' )
        h1.intf( 'h1-eth0' ).setIP( '10.0.1.2', 24 )
        h1.intf( 'h1-eth0' ).setMAC( '0A:00:01:02:00:00' )

        h2 = net.get( 'h2' )
        h2.intf( 'h2-eth0' ).setIP( '10.0.2.2', 24 )
        h2.intf( 'h2-eth0' ).setMAC( '0A:00:02:02:00:00' )

        h3 = net.get( 'h3' )
        h3.intf( 'h3-eth0' ).setIP( '10.0.3.2', 24 )
        h3.intf( 'h3-eth0' ).setMAC( '0A:00:03:02:00:00' )

        h4 = net.get( 'h4' )
        h4.intf( 'h4-eth0' ).setIP( '10.0.4.2', 24 )
        h4.intf( 'h4-eth0' ).setMAC( '0A:00:04:02:00:00' )

        h5 = net.get( 'h5' )
        h5.intf( 'h5-eth0' ).setIP( '10.0.5.2', 24 )
        h5.intf( 'h5-eth0' ).setMAC( '0A:00:05:02:00:00' )

        h6 = net.get( 'h6' )
        h6.intf( 'h6-eth0' ).setIP( '10.0.6.2', 24 )
        h6.intf( 'h6-eth0' ).setMAC( '0A:00:06:02:00:00' )

	# Set interface MAC address for switches (NOTE: IP
        # addresses are not assigned to switch interfaces)
        s0 = net.get( 's0' )
        s0.intf( 's0-eth1' ).setMAC( '0A:00:00:01:00:01' )
        s0.intf( 's0-eth2' ).setMAC( '0A:00:0A:01:00:02' )
        s0.intf( 's0-eth3' ).setMAC( '0A:00:0B:01:00:03' )

	s1 = net.get( 's1' )
        s1.intf( 's1-eth1' ).setMAC( '0A:00:01:01:00:01' )
        s1.intf( 's1-eth2' ).setMAC( '0A:00:0A:FE:00:02' )
        s1.intf( 's1-eth3' ).setMAC( '0A:00:0C:01:00:03' )

        s2 = net.get( 's2' )
        s2.intf( 's2-eth1' ).setMAC( '0A:00:02:01:00:01' )
        s2.intf( 's2-eth2' ).setMAC( '0A:00:0B:FE:00:02' )
        s2.intf( 's2-eth3' ).setMAC( '0A:00:0D:01:00:03' )

        s3 = net.get( 's3' )
        s3.intf( 's3-eth1' ).setMAC( '0A:00:03:01:00:01' )
        s3.intf( 's3-eth2' ).setMAC( '0A:00:0D:FE:00:02' )
        s3.intf( 's3-eth3' ).setMAC( '0A:00:0E:01:00:03' )

        s4 = net.get( 's4' )
        s4.intf( 's4-eth1' ).setMAC( '0A:00:04:01:00:01' )
        s4.intf( 's4-eth2' ).setMAC( '0A:00:0E:FE:00:02' )
        s4.intf( 's4-eth3' ).setMAC( '0A:00:10:01:00:03' )

        s5 = net.get( 's5' )
        s5.intf( 's5-eth1' ).setMAC( '0A:00:05:01:00:01' )
        s5.intf( 's5-eth2' ).setMAC( '0A:00:10:FE:00:02' )
        s5.intf( 's5-eth3' ).setMAC( '0A:00:11:01:00:03' )

        s6 = net.get( 's6' )
        s6.intf( 's6-eth1' ).setMAC( '0A:00:06:01:00:01' )
        s6.intf( 's6-eth2' ).setMAC( '0A:00:0F:FE:00:02' )

	net.start()

	 # Add routing table entries for hosts (NOTE: The gateway
		# IPs 10.0.X.1 are not assigned to switch interfaces)

	h0.cmd( 'route add default gw 10.0.0.1 dev h0-eth0' )
        h1.cmd( 'route add default gw 10.0.1.1 dev h1-eth0' )
        h2.cmd( 'route add default gw 10.0.2.1 dev h2-eth0' )
        h3.cmd( 'route add default gw 10.0.3.1 dev h3-eth0' )
        h4.cmd( 'route add default gw 10.0.4.1 dev h4-eth0' )
        h5.cmd( 'route add default gw 10.0.5.1 dev h5-eth0' )
        h6.cmd( 'route add default gw 10.0.6.1 dev h6-eth0' )
	
	# Add arp cache entries for hosts
        h0.cmd( 'arp -s 10.0.0.1 0A:00:00:01:00:01 -i h0-eth0' )
        h1.cmd( 'arp -s 10.0.1.1 0A:00:01:01:00:01 -i h1-eth0' )
        h2.cmd( 'arp -s 10.0.2.1 0A:00:02:01:00:01 -i h2-eth0' )
        h3.cmd( 'arp -s 10.0.3.1 0A:00:03:01:00:01 -i h3-eth0' )
        h4.cmd( 'arp -s 10.0.4.1 0A:00:04:01:00:01 -i h4-eth0' )
        h5.cmd( 'arp -s 10.0.5.1 0A:00:05:01:00:01 -i h5-eth0' )
        h6.cmd( 'arp -s 10.0.6.1 0A:00:06:01:00:01 -i h6-eth0' )

	# Open Mininet Command Line Interface
        CLI(net)

        # Teardown and cleanup
        net.stop()

if __name__ == '__main__':
    setLogLevel('info')
run()











