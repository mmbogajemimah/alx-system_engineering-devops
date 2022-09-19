## Description
The 3 server web infrastructure is protected, controlled, and provides encrypted traffic.

### For every additional element, why you are adding it

#### What are firewalls for
By serving as an intermediary between the internal network and the external network and restricting incoming traffic that meets the aforementioned requirements, firewalls help to safeguard the network (or web servers, in any case) from unauthorized and undesired users.

#### Why is the traffic served over HTTPS
The SSL certificate is used to encrypt communication between web servers and the outside network in order to prevent network sniffers and man-in-the-middle attacks from exposing sensitive data. The SSL certificates guarantee identification, integrity, and privacy.

#### What monitoring is used for
#### How the monitoring tool is collecting data

The servers and external network are monitored by the monitoring clients. They evaluate the servers' operations and performance, assess their general health, and notify the administrators if something is amiss. The monitoring program keeps an eye on the servers and gives the admins important performance indicators. It checks the servers' accessibility automatically, evaluates response times, and sends alerts for a variety of defects, including missing or corrupted data, security flaws, and other problems.

### Explain what the issues are with this infrastructure: 

#### Why terminating SSL at the load balancer level is an issue
When SSL is disabled at the load balancer level, no encryption is applied to the communication going between the load balancer and the web servers.

#### Why having only one MySQL server capable of accepting writes is an issue
A problem with only having one MySQL server is that it might be a single point of failure for the web architecture and is not scalable.

#### Why having servers with all the same components (database, web server and application server) might be a problem
When all the components on a server are the same, they compete for resources like CPU, memory, I/O, etc., which can result in subpar performance and make it challenging to identify the problem's root cause. A arrangement like this is difficult to scale.