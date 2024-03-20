HW 3 GH repo: https://github.com/roblee04/CSEN241 

Task 1:

1. What is the output of “nodes” and “net”

mininet> nodes
available nodes are:  
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7

mininet> net
h1 h1-eth0:s3-eth2
h2 h2-eth0:s3-eth3
h3 h3-eth0:s4-eth2
h4 h4-eth0:s4-eth3
h5 h5-eth0:s6-eth2
h6 h6-eth0:s6-eth3
h7 h7-eth0:s7-eth2
h8 h8-eth0:s7-eth3
s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0
c0


2. What is the output of “h7 ifconfig

mininet> h7 ifconfig
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
       inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
       inet6 fe80::58ef:a4ff:fef7:e400  prefixlen 64  scopeid 0x20<link>
       ether 5a:ef:a4:f7:e4:00  txqueuelen 1000  (Ethernet)
       RX packets 155  bytes 11886 (11.6 KiB)
       RX errors 0  dropped 0  overruns 0  frame 0
       TX packets 12  bytes 936 (936.0 B)
       TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
       inet 127.0.0.1  netmask 255.0.0.0
       inet6 ::1  prefixlen 128  scopeid 0x10<host>
       loop  txqueuelen 1000  (Local Loopback)
       RX packets 0  bytes 0 (0.0 B)
       RX errors 0  dropped 0  overruns 0  frame 0
       TX packets 0  bytes 0 (0.0 B)
       TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0



Task 2:
Questions
1. Draw the function call graph of this controller. For example, once a packet comes to the controller, which function is the first to be called, which one is the second, and so forth?

We turn the POX on, which turns on the start switch. When a packet reaches the switch the function _handle_PacketIn() is called by the start switch to get the incoming packet.
next function calls are shown in the following function call graph:

start_switch() : _handle_PacketIn() -> act_like_hub() -> resend_packet() -> send(msg)

2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long does it take (on average) to ping for each case?

avg - h1 - h2 : 4.387
avg - h1 - h8 : 15.391

b. What is the minimum and maximum ping you have observed?

h1-h2: min : 1.825, max : 6.881
h1-h8: min : 5.600, max : 22.127

c. What is the difference, and why?

The ping times are longer in the second case i.e., from h1 to h8 because the second case goes through a larger number of jumps than in the first case.

from h1-h2 : only s3
from h1-h8 : s3,s2,s1,s5,s7

3. Run “iperf h1 h2” and “iperf h1 h8”
a. What is “iperf” used for?

In general, Iperf is a tool for network performance measurement and tuning, however, in this case, iperf is used to determine the bandwidth between 2 hosts in the network. 

Two hosts running iperf are limiting the network link. It is used to determine the amount of data transferred between any two nodes on a network connection.

b. What is the throughput for each case?

second values are throughputs:
mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2 
*** Results: ['20.1 Mbits/sec', '23.1 Mbits/sec']
mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8 
*** Results: ['4.62 Mbits/sec', '5.37 Mbits/sec']


c. What is the difference, and explain the reasons for the difference.

The difference is around 17 Mbits/sec. The throughput is higher between h1 and h2 than between h1 and h8 (same as ping time being slower) because there is a lower number of jumps between h1 and h2 and more data can be sent in less time. On the converse, because the number of jumps between h1 and h8 is higher, less data is transferred in a given amount of time.


4. Which of the switches observe traffic? Please describe your way for observing such traffic on switches (e.g., adding some functions in the “of_tutorial” controller)

We can observe the traffic info by adding log.info("Switch observing traffic: "% s % (self.connection)" to the line number 107 "of tutorial"  log.debug("Installing flow..."), # Maybe the log statement should have source/destination/port?) controller. We know that all switches monitor traffic, particularly when they are overloaded with packets. The event listener function _handle PacketIn is invoked whenever a packet is received.

Task 3:
1. Describe how the above code works, such as how the "MAC to Port" map is established.
You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).

The act_like_switch function in our code shows where MAC addresses are located.
The controller maps a MAC address to which a sender wants to send a message to. This also shows the controller's speed when delivering packets to already known addresses, as the packet is simply directed to that known port. The function just floods the packet to all destinations if the destination is unknown because flooding occurs less frequently.
Establishment process could be well understood by seeing the output for a ping of 1 packet from h1 to h2.


2. (Comment out all prints before doing this experiment) Have h1 ping h2, and h1 ping
h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long did it take (on average) to ping for each case?

avg - h1-h2 - 4.153
avg - h1-h8 - 13.376

b. What is the minimum and maximum ping you have observed?

h1-h2: min : 1.119, max : 4.920
h1-h8: min : 2.678, max : 21.529

c. Any difference from Task 2 and why do you think there is a change if there is?

Task 3(in both cases) has a slight edge over the ping statistics than task 2, it might be due to the lack of network congestion, which was found in task 2. As mapping is done, the switches can easily send packets to the corresponding ports.



3. Q.3 Run “iperf h1 h2” and “iperf h1 h8”.
a. What is the throughput for each case?

mininet> iperf h1 h2
*** Iperf: testing TCP bandwidth between h1 and h2 
*** Results: ['65.2 Mbits/sec', '65.8 Mbits/sec']
mininet> iperf h1 h8
*** Iperf: testing TCP bandwidth between h1 and h8 
*** Results: ['4.10 Mbits/sec', '4.66 Mbits/sec']

b. What is the difference from Task 2 and why do you think there is a change if there is?

In the first case, the throughput is almost thrice because routes are more pre-computed and learned with changes in the controller. Also there'll be less network congestion as mac_to_port map has learned all the ports.

