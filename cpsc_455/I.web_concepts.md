
World Wide Web: information system which allows us to access documents via uniform address locators (URLs) and online applications. Invented by Tim Bernerns-Lee

Common attack types: Cross-site Scripting  (XSS), SQL Injections, Local File Inclusion, Remote File Inclusion, Cookie Stealing...

In order to prevent attacks, our web apps must be designed with seccuity in mid so that attacking our appplications doesn't even make sense and discover techniques to discover and fix vulnerabilities in existing apps. 

## WWW Architecture

**client-server atchitecture**
- server stores pages and resources including html css, js, images and other files. always up and running and listens for requests
- client requests resouces from server using http(hypertext transfer protocol) which defines how servers and browsers communicate with one another
HTTP Requests are sent via the TCP, which is the medium by which the devices  form a connecction and simulates reliability 

Two types of messages: request and response
- first line is the method and the name of the resource requested as well as the version of http being used
- second part is the header which contains several fields which are sort of configurations for the message. Host is required, which is the name of the domain on the server that the client is trying to access. User-Agent tells the server what broeser and version the message is being sent from. Keep-Alive and Connection fields are to tell the server whether the tcp connection should be kept open so that future requests can be easily made, the former is a time in seconds. This is a request but it is up to the server if the connection will be kept alive
- lastly we have a body section (entity body) which contains data being transfered between the devices

Wth the POST method the data is sent in the entity body whereas with the GET method the data is sent in the url

HEAD method asks server to leave requested object out of response. Useful for testing, may not want the page since it may contain alot of data. PUT method allows us to upload files in entity body to the path in the URL. DELETE asks the server to delete a file.

Responses: First line contains the status http version, followed by header lines, and data requested by the html file. 

**Domain Name Service**: a system which maps (resolves) urls to IP addresses so that a client can make a connection. 

A heirarchy of servers throughout the internet/world. The dns server can know what sites you visited so you may want to use an alternate dns if you are concerned with privacy.

**Cookies**: provide a way for browsers to keep track of the state- that is, what other sites and pages the user has visited and requests they have made
Four components:
	1. header line of HTTP response message
	2. header line of HTTP request message
	3. file kept on user's host, managed by browser
	4. backend db at website

**Web Caches**: sends all HTTP reqs to cache, if the request was fulfilled previously, and web page has not changed, cache object will be sent otherwise returns object from origin server

#### Web App Architectures

An architecture is a framework that  defines the structure of the application, identifies its components and describes how they interact. At the highest level there is the client and the server- decisions are then  made regarding what is stored or executed in which component.

The frontend consists of JS code that sends data in HTTP requests to the server. The backend receives and processes/executes the requests- may access in databases.

Functionality is organized into three layers: Presentation Layer, Business Logic Layer, and Data Access Layer

The presentation layer's job is to receive user requests and generate a UI. Handles all user interaction. The business logic layer implements logic for handling operations: for example, logging in or transaction. The data access layer is responsible for access and store data.

The main web architectures
- **monolithic**: All the app logic is in the same codebase and runs in the same runtime/system. Leads to simplified development, debugging, mainaintance, reduced complexity, and good performance (no network communication necessary). However, there is poor scalibilty, and lack of modularity.
- **microservices**: a collection of lightweight independent services running on different systems that communicate via a network. Each service can be developed independently, modularity and scalabilty, different languages and runtimes can be used. However, there is more overhead in order to communicate between services because there are different systems that have to communicate through the network. 
- **serverless**: each function is deployed in the cloud, and user interacts through an API gateway, cloud provider automatically scales the resources as needed. The difference between the serverless and microservices is that serverless is function based and only up and running while the function is executing. Reduces costs, improves scalabilty, easily deploy functions, and reduces need to manage infrastructure. However, serverless architectures are cloud provider dependent, can result in vendor lock-in, and harder to debug.
- **progressive**: delivers rich immersive experience via a web browser as if it is a native app. Works offline by caching data while the user is online. Disadvantages are that there is additional complexity and development costs.
- **single page**: the client requests the webpage once, and dynamically updates parts of the page as needed without reloading the entire page. A chat app is an example. Fast performance, and more intuitive for users. However, testing takes more time, unsaved work may be lost, and intial page load is slower.

The choice of architecture affects the applications security, scalabilty, and maintainability for various reasons. Architectures can be mixed in a single application.
