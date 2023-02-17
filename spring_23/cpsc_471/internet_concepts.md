# Chapter 1

The modern internet is composed of hundreds of millions of connected computers, communication links, amd switches, along with billions of users with multiple internet-connected devices. However despite its complexity, there is apparently a simple structure that we can examine to understand it. And the best way to kick that off is with a basic overview of that structure and the internet in general.

From a high level the internet is composed of 12 types of devices: hosts/end systems, servers, mobile computers/laptops, routers, link-layer switches, base stations, cellphone towers, cellphones/tablets, datacenters, workstations, infrastructure components, and various home devices/appliances. Today, up to half the population of the world own mobile devices- and that number is only going to grow. End systems are connected through communication links and packet switches. Communication links are the physical mediums that enable communication. Transmission rates refer to how much data can be transmitted per unit time, measured in bits per second. Packets are the system defined transmission segments along with header bytes, that are used to transmit data via communication links. 

In order to reduce the effects of noise on signals we send an inverted signal that is then decoded into the original signal. Known as a differential pair. The cables are twisted so that the signals are bounded- that is the signals mimic one anothers strengths, etc. Allows for higher speed of transmission. The number of twists per inch correlates with the speed, however, this also requires higher amounts of copper.

coaxial cables were one of the original ethernet cable mediums. they can only transmit 100's of Mbps per channel.
Modems wil decrease transmission rates if there is alot of noise affecting the data being transmitted. Fiber optic cables do not suffer from this but are subject to (atenuation?)

Network core consists of two core functions forwardinga and routing

circuit switching alternative to packet switching. not as efficient.
Involves Frequency Division Multiplexing and Time Division Multiplexing
packet switching supports more users ata the same time.

Packet swithcing is best for when users dont use it all the time(bursty data). Can cause pakage delay and buffer overflow due to congestion. 
Circuit-like behavior: Used fo r audio and video apps

Distributed internet networks are more scalable because they do not require all devices to have connecctions to all other devices.

There are four sources of delay for packet switching: transmission delay, propagation delay, queueing delay, and nodal processing delay. Each one has a formula (plug into excel spreadsheet and put note!)

traceroute program will give us information about the delay of a packet along the network. can be used to map the hops between the routers(security vulnerabilty) `tracert <url>` on Windoze.
best effort: lost packers may be retransmitted by prev node, source ned system, or not at all.
No guranatee that packets arrive in order

**Throughput** is the rate at which bits are sent from sender to receiver. instanteaneous id the rate at a given point in time and the average over a longer period of time

	if you have multiple connections the throughput is always the slowest. 

We use layering in oredre to divide  a complex system into its constituent functions to make it easier to reasin about. Each layer in the stack provides a single service. 
The internet protocol stack incolves the application, transport, network, kink and physical layers. the lower layers have faster speeds and provide services to the layer immediately above them. 
On the receivng side the signal is processed in reverse order (layers)

**2/10 Chapter One Quiz, in-class, bring laptop**




