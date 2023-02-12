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