from mininet.topo import Topo

class MyTopo( Topo ):
    "Topology for 16 switches and 4 hosts per switch"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches 
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        s1 = self.addSwitch( 's1' )
            
        # Add hosts and switches 
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        s2 = self.addSwitch( 's2' )
        
        # Add hosts and switches 
        h9 = self.addHost( 'h9' )
        h10 = self.addHost( 'h10' )
        h11 = self.addHost( 'h11' )
        h12 = self.addHost( 'h12' )
        s3 = self.addSwitch( 's3' )
        
        # Add hosts and switches 
        h13 = self.addHost( 'h13' )
        h14 = self.addHost( 'h14' )
        h15 = self.addHost( 'h15' )
        h16 = self.addHost( 'h16' )
        s4 = self.addSwitch( 's4' )
        
        
         # Add hosts and switches 
        h17 = self.addHost( 'h17' )
        h18 = self.addHost( 'h18' )
        h19 = self.addHost( 'h19' )
        h20 = self.addHost( 'h20' )
        s5 = self.addSwitch( 's5' )
            
        # Add hosts and switches 
        h21 = self.addHost( 'h21' )
        h22 = self.addHost( 'h22' )
        h23 = self.addHost( 'h23' )
        h24 = self.addHost( 'h24' )
        s6 = self.addSwitch( 's6' )
        
        # Add hosts and switches 
        h25 = self.addHost( 'h25' )
        h26 = self.addHost( 'h26' )
        h27 = self.addHost( 'h27' )
        h28 = self.addHost( 'h28' )
        s7 = self.addSwitch( 's7' )
        
        # Add hosts and switches 
        h29 = self.addHost( 'h29' )
        h30 = self.addHost( 'h30' )
        h31 = self.addHost( 'h31' )
        h32 = self.addHost( 'h32' )
        s8 = self.addSwitch( 's8' )
        
        
         # Add hosts and switches 
        h33 = self.addHost( 'h33' )
        h34 = self.addHost( 'h34' )
        h35 = self.addHost( 'h35' )
        h36 = self.addHost( 'h36' )
        s9 = self.addSwitch( 's9' )
            
        # Add hosts and switches 
        h37 = self.addHost( 'h37' )
        h38 = self.addHost( 'h38' )
        h39 = self.addHost( 'h39' )
        h40 = self.addHost( 'h40' )
        s10 = self.addSwitch( 's10' )
        
        # Add hosts and switches 
        h41 = self.addHost( 'h41' )
        h42 = self.addHost( 'h42' )
        h43 = self.addHost( 'h43' )
        h44 = self.addHost( 'h44' )
        s11 = self.addSwitch( 's11' )
        
        # Add hosts and switches 
        h45 = self.addHost( 'h45' )
        h46 = self.addHost( 'h46' )
        h47 = self.addHost( 'h47' )
        h48 = self.addHost( 'h48' )
        s12 = self.addSwitch( 's12' )
        
        
         # Add hosts and switches 
        h49 = self.addHost( 'h49' )
        h50 = self.addHost( 'h50' )
        h51 = self.addHost( 'h51' )
        h52 = self.addHost( 'h52' )
        s13 = self.addSwitch( 's13' )
            
        # Add hosts and switches 
        h53 = self.addHost( 'h53' )
        h54 = self.addHost( 'h54' )
        h55 = self.addHost( 'h55' )
        h56 = self.addHost( 'h56' )
        s14 = self.addSwitch( 's14' )
        
        # Add hosts and switches
        h57 = self.addHost( 'h57' )
        h58 = self.addHost( 'h58' )
        h59 = self.addHost( 'h59' )
        h60 = self.addHost( 'h60' )
        s15 = self.addSwitch( 's15' )
        
        # Add hosts and switches 
        h61 = self.addHost( 'h61' )
        h62 = self.addHost( 'h62' )
        h63 = self.addHost( 'h63' )
        h64 = self.addHost( 'h64' )
        s16 = self.addSwitch( 's16' )
        
        
        
        
        
        
        
        
        

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
        
        # Add links
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
        
        # Add links
        self.addLink( h33, s9 )
        self.addLink( h34, s9 )
        self.addLink( h35, s9 )
        self.addLink( h36, s9 )
        
        self.addLink( h37, s10 )
        self.addLink( h38, s10 )
        self.addLink( h39, s10 )
        self.addLink( h40, s10 )
        
        self.addLink( h41, s11 )
        self.addLink( h42, s11 )
        self.addLink( h43, s11 )
        self.addLink( h44, s11 )
        
        self.addLink( h45, s12 )
        self.addLink( h46, s12 )
        self.addLink( h47, s12 )
        self.addLink( h48, s12 )
        
        # Add links
        self.addLink( h49, s13 )
        self.addLink( h50, s13 )
        self.addLink( h51, s13 )
        self.addLink( h52, s13 )
        
        self.addLink( h53, s14 )
        self.addLink( h54, s14 )
        self.addLink( h55, s14 )
        self.addLink( h56, s14 )
        
        self.addLink( h57, s15 )
        self.addLink( h58, s15 )
        self.addLink( h59, s15 )
        self.addLink( h60, s15 )
        
        self.addLink( h61, s16 )
        self.addLink( h62, s16 )
        self.addLink( h63, s16 )
        self.addLink( h64, s16 )
        
        
        
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
