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
                h0 = self.addHost( 'h0' )
                h1 = self.addHost( 'h1' )
                h2 = self.addHost( 'h2' )
                h3 = self.addHost( 'h3' )
                h4 = self.addHost( 'h4' )
                h5 = self.addHost( 'h5' )
                h6 = self.addHost( 'h6' )
                h7 = self.addHost( 'h7' )
                h8 = self.addHost( 'h8' )
                h9 = self.addHost( 'h9' )

                # Add switches
                s0 = self.addSwitch( 's0', listenPort=6634 )
                s1 = self.addSwitch( 's1', listenPort=6635 )
                s2 = self.addSwitch( 's2', listenPort=6636 )
                s3 = self.addSwitch( 's3', listenPort=6637 )
                s4 = self.addSwitch( 's4', listenPort=6638 )
                s5 = self.addSwitch( 's5', listenPort=6639 )
                s6 = self.addSwitch( 's6', listenPort=6640 )
                s7 = self.addSwitch( 's7', listenPort=6641 )
                s8 = self.addSwitch( 's8', listenPort=6642 )
                s9 = self.addSwitch( 's9', listenPort=6643 )

                # Add links between hosts and switches
                self.addLink( h0, s0 ) # h0-eth0 <-> s0-eth1
                self.addLink( h1, s1 ) # h1-eth0 <-> s1-eth1
                self.addLink( h2, s2 ) # h2-eth0 <-> s2-eth1
                self.addLink( h3, s3 ) # h3-eth0 <-> s3-eth1
                self.addLink( h4, s4 ) # h4-eth0 <-> s4-eth1
                self.addLink( h5, s5 ) # h5-eth0 <-> s5-eth1
                self.addLink( h6, s6 ) # h6-eth0 <-> s6-eth1
                self.addLink( h7, s7 ) # h7-eth0 <-> s7-eth1
                self.addLink( h8, s8 ) # h8-eth0 <-> s8-eth1
                self.addLink( h9, s9 ) # h9-eth0 <-> s9-eth1

                # Add links between switches, with bandwidth 100Mbps
                self.addLink( s0, s1, bw=100 ) # s0-eth2 <-> s1-eth2, Bandwidth = 100Mbps
                self.addLink( s0, s2, bw=100 ) # s0-eth3 <-> s2-eth2, Bandwidth = 100Mbps
                self.addLink( s1, s2, bw=100 ) # s1-eth3 <-> s2-eth3, Bandwidth = 100Mbps
                self.addLink( s2, s3, bw=100 ) # s2-eth4 <-> s3-eth2, Bandwidth = 100Mbps
                self.addLink( s3, s4, bw=100 ) # s3-eth3 <-> s4-eth2, Bandwidth = 100Mbps
                self.addLink( s3, s6, bw=100 ) # s3-eth4 <-> s6-eth2, Bandwidth = 100Mbps
                self.addLink( s4, s5, bw=100 ) # s4-eth3 <-> s5-eth2, Bandwidth = 100Mbps
                self.addLink( s5, s7, bw=100 ) # s5-eth3 <-> s7-eth2, Bandwidth = 100Mbps
                self.addLink( s6, s7, bw=100 ) # s6-eth3 <-> s7-eth3, Bandwidth = 100Mbps
                self.addLink( s7, s8, bw=100 ) # s7-eth4 <-> s8-eth2, Bandwidth = 100Mbps
                self.addLink( s7, s9, bw=100 ) # s7-eth5 <-> s9-eth2, Bandwidth = 100Mbps
                self.addLink( s8, s9, bw=100 ) # s8-eth3 <-> s9-eth3, Bandwidth = 100Mbps

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

        h7 = net.get( 'h7' )
        h7.intf( 'h7-eth0' ).setIP( '10.0.7.2', 24 )
        h7.intf( 'h7-eth0' ).setMAC( '0A:00:07:02:00:00' )

        h8 = net.get( 'h8' )
        h8.intf( 'h8-eth0' ).setIP( '10.0.8.2', 24 )
        h8.intf( 'h8-eth0' ).setMAC( '0A:00:08:02:00:00' )

        h9 = net.get( 'h9' )
        h9.intf( 'h9-eth0' ).setIP( '10.0.9.2', 24 )
        h9.intf( 'h9-eth0' ).setMAC( '0A:00:09:02:00:00' )

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
        s2.intf( 's2-eth4' ).setMAC( '0A:00:0C:FE:00:04' )

        s3 = net.get( 's3' )
        s3.intf( 's3-eth1' ).setMAC( '0A:00:03:01:00:01' )
        s3.intf( 's3-eth2' ).setMAC( '0A:00:0D:FE:00:02' )
        s3.intf( 's3-eth3' ).setMAC( '0A:00:0E:01:00:03' )
        s3.intf( 's3-eth4' ).setMAC( '0A:00:0F:01:00:04' )

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
        s6.intf( 's6-eth3' ).setMAC( '0A:00:12:01:00:03' )

        s7 = net.get( 's7' )
        s7.intf( 's7-eth1' ).setMAC( '0A:00:07:01:00:01' )
        s7.intf( 's7-eth2' ).setMAC( '0A:00:11:FE:00:02' )
        s7.intf( 's7-eth3' ).setMAC( '0A:00:12:FE:00:03' )
        s7.intf( 's7-eth4' ).setMAC( '0A:00:13:01:00:04' )
        s7.intf( 's7-eth5' ).setMAC( '0A:00:14:01:00:05' )

        s8 = net.get( 's8' )
        s8.intf( 's8-eth1' ).setMAC( '0A:00:08:01:00:01' )
        s8.intf( 's8-eth2' ).setMAC( '0A:00:13:FE:00:02' )
        s8.intf( 's8-eth3' ).setMAC( '0A:00:15:01:00:03' )

        s9 = net.get( 's9' )
        s9.intf( 's9-eth1' ).setMAC( '0A:00:09:01:00:01' )
        s9.intf( 's9-eth2' ).setMAC( '0A:00:14:FE:00:02' )
        s9.intf( 's9-eth3' ).setMAC( '0A:00:15:FE:00:03' )

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
        h7.cmd( 'route add default gw 10.0.7.1 dev h7-eth0' )
        h8.cmd( 'route add default gw 10.0.8.1 dev h8-eth0' )
        h9.cmd( 'route add default gw 10.0.9.1 dev h9-eth0' )

        # Add arp cache entries for hosts
        h0.cmd( 'arp -s 10.0.0.1 0A:00:00:01:00:01 -i h0-eth0' )
        h1.cmd( 'arp -s 10.0.1.1 0A:00:01:01:00:01 -i h1-eth0' )
        h2.cmd( 'arp -s 10.0.2.1 0A:00:02:01:00:01 -i h2-eth0' )
        h3.cmd( 'arp -s 10.0.3.1 0A:00:03:01:00:01 -i h3-eth0' )
        h4.cmd( 'arp -s 10.0.4.1 0A:00:04:01:00:01 -i h4-eth0' )
        h5.cmd( 'arp -s 10.0.5.1 0A:00:05:01:00:01 -i h5-eth0' )
        h6.cmd( 'arp -s 10.0.6.1 0A:00:06:01:00:01 -i h6-eth0' )
        h7.cmd( 'arp -s 10.0.7.1 0A:00:07:01:00:01 -i h7-eth0' )
        h8.cmd( 'arp -s 10.0.8.1 0A:00:08:01:00:01 -i h8-eth0' )
        h9.cmd( 'arp -s 10.0.9.1 0A:00:09:01:00:01 -i h9-eth0' )

        # Open Mininet Command Line Interface
        CLI(net)

        # Teardown and cleanup
        net.stop()

if __name__ == '__main__':
    setLogLevel('info')
run()
