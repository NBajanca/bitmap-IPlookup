# bitmap-IPlookup
Switch and Routing Project | Politecnico di Milano

To start the mininet (need to be in the topology and config files directory): 
```
sudo mn --custom topology.py --topo mytopo --mac --controller remote --pre config
```

To start the controller:
```
PYTHONPATH=. ./bin/ryu-manager ryu/app/simple_switch.py
```
