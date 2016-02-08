# Bitmap IP lookup Poject
## Switch and Routing - [Politecnico di Milano](http://www.polimi.it/ "Polimi Website") (2015/2016 1st Semester)

#### Steps to deploy virtual network with RYU Controler on Switches
1. Start the mininet
```
cd (topology and configuration files directory)
sudo mn --custom (topology-file).py --topo mytopo --mac --controller remote --pre (configuration file)
```
2. Start the controller
```
cd (ryu directory)
PYTHONPATH=. ./bin/ryu-manager ryu/app/(controler_file).py
```
Note: The files related to the bitmap algorithm must be in the same directory as the controller file

#### Important Links
* [Switch and Routing](https://www11.ceda.polimi.it/schedaincarico/schedaincarico/controller/scheda_pubblica/SchedaPublic.do?&evn_default=evento&c_classe=617586&__pj0=0&__pj1=cafee3a3315408a73e29ad42bdc45521 "Course Page")
* [Mininet](http://mininet.org/)
* [OpenFlow](https://www.opennetworking.org/sdn-resources/openflow)
* [RYU SDN Framework](http://osrg.github.io/ryu/)

#### Group 4
* Nuno Bajanca (@NBajanca)
* Vladimir Tomov
* Konstantin Tsolev (@KTsolev)
* Francisco Santos (@franciscof93)
* Alim Mohamed (@oxnitrogen)
