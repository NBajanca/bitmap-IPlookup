from mininet.topo import Topo

class MyTopo( Topo ):
    "Topology for 4 switches and 4 hosts per switch"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches -- switch s1 hosts h1, h2,h3,h4 --
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        s1 = self.addSwitch( 's1' )
			
		# Add hosts and switches -- switch s2 hosts h5, h6,h7,h8 --
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        s2 = self.addSwitch( 's2' )
		
		# Add hosts and switches -- switch s3 hosts h9, h10,h11,h12 --
        h9 = self.addHost( 'h9' )
        h10 = self.addHost( 'h10' )
        h11 = self.addHost( 'h11' )
        h12 = self.addHost( 'h12' )
        s3 = self.addSwitch( 's3' )
		
		# Add hosts and switches -- switch s4 hosts h13, h14,h15,h16 --
        h13 = self.addHost( 'h13' )
        h14 = self.addHost( 'h14' )
        h15 = self.addHost( 'h15' )
        h16 = self.addHost( 'h16' )
        s4 = self.addSwitch( 's4' )
		
		
		
		

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s1 )
        self.addLink( h4, s1 )
		
		self.addLink( h5, s2 )
        self.addLink( h6, s2 )
        self.addLink( h7, s2 )
        self.addLink( h8, s2 )
		
		self.addLink( h9, s3 )
        self.addLink( h10, s3 )
        self.addLink( h11, s3 )
        self.addLink( h12, s3 )
		
		self.addLink( h13, s4 )
        self.addLink( h14, s4 )
        self.addLink( h15, s4 )
        self.addLink( h16, s4 )
		
		
		
		


topos = { 'mytopo': ( lambda: MyTopo() ) }
