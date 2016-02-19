# Bitmap IP lookup Poject
## Switch and Routing - [Politecnico di Milano](http://www.polimi.it/ "Polimi Website") (2015/2016 1st Semester)

#### Steps to deploy virtual network with RYU Controler on Switches
##### Start the mininet
```
sudo mn --custom (path to topology-file).py --topo mytopo --mac --controller remote --pre (path to configuration file)
```
##### Start the controller
Requires for the config, tree, node and controler file to be in the app directory of Ryu
```
cd (ryu directory)
PYTHONPATH=. ./bin/ryu-manager ryu/app/(controler_file).py
```
Note: The files related to the algorithm must be in the same directory as the controller file. The configuration file must be named config.

#### Important Links
* [Switch and Routing](https://www11.ceda.polimi.it/schedaincarico/schedaincarico/controller/scheda_pubblica/SchedaPublic.do?&evn_default=evento&c_classe=617586&__pj0=0&__pj1=cafee3a3315408a73e29ad42bdc45521 "Course Page")
* [Mininet](http://mininet.org/)
* [OpenFlow](https://www.opennetworking.org/sdn-resources/openflow)
* [RYU SDN Framework](http://osrg.github.io/ryu/)

#### Group 4
* Nuno Bajanca (@NBajanca)
* Vladimir Tomov (@vtomov92)
* Konstantin Tsolev (@KTsolev)
* Francisco Santos (@franciscof93)
* Alim Mohamed (@oxnitrogen)

#### Professors
* Guido Maier
* Navin Kukreja
