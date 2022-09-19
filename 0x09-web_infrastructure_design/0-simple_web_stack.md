## Description

 This is a basic web infrastructure that runs a website that can be accessed through www.foobar.com. The network of the server is not secured by SSL certificates or firewalls. The server's resources which are the CPU, RAM, and SSD must be shared by each component (database, application server).

 ## Specifics of the Infrastructure
 # A Server:
 A server is  computer hardware or software that offers services to other computers, often known as clients.

 # Role of a domain name
 To give an IP Address a human-friendly nickname. The Domain Name System maps the IP address and domain name alias (DNS)

 # What type of DNS record www is in www.foobar.com
www.foobar.com, The word foobar.com is the domain name in this case; the word www is a subdomain. www is used as a CNAME record with the value foobar.com, and DNS uses this information to determine the website's IP address.

 # What is the role of the web server
The web server is software or hardware that processes HTTP or HTTPS requests and returns the requested resource's content or an error message in response.

 # What is the role of the application server
installing, running, hosting, and providing related services to end users, IT services, and organizations, as well as facilitating the hosting and delivery of high-end consumer or corporate applications

 # What is the role of the database
to keep a database of arranged data that can be conveniently accessed, maintained, and updated

 # What is the server using to communicate with the computer of the user requesting the website
Through the TCP/IP protocol suite, communication between the client and the server takes place through the internet network.

 ## What the issues are with this infrastructure: 

 # SPOF
 This infrastructure contains several SPOFs (single points of failure). For instance, the entire website would be unavailable if the MySQL database server went down.

 # Downtime when maintenance needed 
 Users won't be able to access the services during downtime when it is updated since there isn't another server that can step in. This demands that the entire system be shut down.

 # Cannot scale if too much incoming traffic
 Because all the necessary components are on a single server, scaling this system would be challenging. When the server starts getting a lot of requests, it may rapidly run out of resources or begin to slow down.