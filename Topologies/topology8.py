from mininet.topo import Topo

class MyTopo( Topo ):
    "Topology for 8 switches and 4 hosts per switch"

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
		
		 # Add hosts and switches -- switch s5 hosts h17, h18,h19,h20 --
        h17 = self.addHost( 'h17' )
        h18 = self.addHost( 'h18' )
        h19 = self.addHost( 'h19' )
        h20 = self.addHost( 'h20' )
        s5 = self.addSwitch( 's5' )
			
		# Add hosts and switches -- switch s6 hosts h21, h22,h23,h24 --
        h21 = self.addHost( 'h21' )
        h22 = self.addHost( 'h22' )
        h23 = self.addHost( 'h23' )
        h24 = self.addHost( 'h24' )
        s6 = self.addSwitch( 's6' )
		
		# Add hosts and switches -- switch s7 hosts h25, h26,h27,h28 --
        h25 = self.addHost( 'h25' )
        h26 = self.addHost( 'h26' )
        h27 = self.addHost( 'h27' )
        h28 = self.addHost( 'h28' )
        s7 = self.addSwitch( 's7' )
		
		# Add hosts and switches -- switch s8 hosts h29, h30,h31,h32 --
        h29 = self.addHost( 'h29' )
        h30 = self.addHost( 'h30' )
        h31 = self.addHost( 'h31' )
        h32 = self.addHost( 'h32' )
        s8 = self.addSwitch( 's8' )
		
		
		
		

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
		
		self.addLink( h17, s5 )
        self.addLink( h18, s5 )
        self.addLink( h19, s5 )
        self.addLink( h20, s5 )
		
		self.addLink( h21, s6 )
        self.addLink( h22, s6 )
        self.addLink( h23, s6 )
        self.addLink( h24, s6 )
		
		self.addLink( h25, s7 )
        self.addLink( h26, s7 )
        self.addLink( h27, s7 )
        self.addLink( h28, s7 )
		
		self.addLink( h29, s8 )
        self.addLink( h30, s8 )
        self.addLink( h31, s8 )
        self.addLink( h32, s8 )
		
		
		
		


topos = { 'mytopo': ( lambda: MyTopo() ) }
