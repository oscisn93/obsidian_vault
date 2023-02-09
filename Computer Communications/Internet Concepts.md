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

# Chapter 2
**Application Layer**:

A network app runs on differnet end systems, communicate over networks. There is no need for software for network devices since the applications run on end user  devices.

**Client-server paradignm**: server hosts the application data on a permanent ip address, often hosted in data centers for scalability. The client only communicates with the server, dynamic Ip

peer to peer: no server(not always on), direct communication among systems
A process is a program running within a host, and inter-process communication is the manner in which they communicate. When processes are on different hosts they must instead communicate through messages. A client process is a process that initiates communication whereas a server process is one that waits to be contacted.

**Sockets**: A process sends and recievies messages via sockets which are analgous to doors. Sending pushes message out of door, sending relies on transport infrastructure, not the concern  of the socket. In order to receive a message the process must have an identifier which includes IP and port numbers on the host. 

transport services: data integrity ( data must be reliable), timing (low delay), throughput (minimum throughput), security  (encryption, integrity)

TCP a reliable transport sevice, equipped with flow control, congestion control, is connection oriented. However does not guarantee timing, minimum throughput, security

UDP is an unreliable data transfer protocol,which does not provide reliabilty,flow ocntrol, congestion, timing throughput, security, or connection setup. Why UDP? We still need it depite its unreliabilty- faster for particular tasks.

Vanilla TCP and UDP not secure/unecrypted
TLS is an encryption layer on top of TCP
HTTP is a web application protocol for communication between client and server.
HTTP uses TCP, client makes a TCP connection on port 80, server accepts connections and then HTTP messages are exchanged. Once all messages have been exchanged, the connection is closed.
Teo types of HTTP conncetions. Nonpersistent, a new connection must be open for each request. For persistent, a connection is kept open and active for as long as requests are coming in and connection is terminated. RTT is th e time for a small packet to travel from client to server and back. nonpersistent responste time = 2RTT+ transmission time. A web cache seeks to configure browser without involving the origin server. All HTTP requests go to hte cache, if the object is in the cache and the object is up to date, the web cache return its version, ohterwise request is forwarded to the origin server. Acts as a proxy that reduces network load, typically installed by an ISP. conditional get (if-modified-since).

HTTP3 uses UDP.
Three components of email
- user agents
- mail servers
- simple mail transfer protocol (SMTP)
**user agent**: mial reader, refers to the device and application the user is using to read, edit, adn send emails.
uses TCP, three phases of sending: 1. handshaking, transfer of messages, closure. messages are in 7-bit ASCII.
HTTP is a pull protocol and SMTP is push.  IMAP is used to receive emails.

The DNS is the directory of the internet. It maps ip addresses to urls. Distributed db, in heirarchy of many servers. functions as a load distrubuter as there are multiple web servers that corresspond to a single URL.

Root servers have the addresses of top level domain servers. such as the .com or .net servers. TLD servers have the addresses of the authoritative servers who have the ip addresses of the hosts mapped to the required URLs.

Local dns name serves act as a cache and are not a part of the heirarchy.
Iterated query means that each server responds with the address whereas recursive means that the query is forwarded at each step.
resource record format: name, value, type, ttl


