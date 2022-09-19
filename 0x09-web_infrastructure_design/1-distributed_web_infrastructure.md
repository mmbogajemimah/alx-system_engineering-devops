# Explain some specifics about this infrastructure: 
### For every additional element, why you are adding it:

This is a distributed web infrastructure. With the assistance of a server that balances the load between the two servers, this distributed web architecture tries to lower the amount of traffic to the primary server by spreading some of the burden to a replica server.

### Specifics About This Infrastructure
#### What distribution algorithm your load balancer is configured with and how it works

The configuration and operation of the load balancer are based on the distribution algorithm.
The Round Robin distribution technique is specified in the HAProxy load balancer. According to their weights, the load balancer behind each server is used in turn by this method. Due to the fact that the servers' processing time is allocated equally, it is also likely the smoothest and most equitable method. Round Robin is a dynamic method that enables real-time modification of server weights.

#### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both

An Active-Passive arrangement rather than an Active-Active setup is enabled by the HAProxy load-balancer. To avoid any one node from becoming overwhelmed in an Active-Active configuration, the load balancer spreads workloads across all nodes. Throughput and response times will also significantly improve because there will be more nodes accessible to service. On the other side, not all nodes will be active in an Active-Passive configuration (capable of receiving workloads at all times). If there are two nodes, for instance, the second node must be inactive or in standby mode if the first node is currently operational. If the preceding node is inactive, the next passive node, or the second one, can become active.

#### How a database Primary-Replica (Master-Slave) cluster works.
A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

#### The difference between the Primary node and the Replica node in regard to the application.
The Replica node may conduct read operations while the Primary node handles all the write operations the site requires, which reduces read traffic to the Primary node.


### Issues With This Infrastructure

The entire website would be unable to update itself if the Primary MySQL database server went down including adding or removing users. Additionally, SPOFs include the load-balancing server and the application server that connects to the main database server.

#### Security issues.
Because an SSL certificate isn't used to encrypt the data being carried over the network, hackers may monitor the network. Since no firewall has been deployed on any server, there is no mechanism to prevent illegitimate IP addresses.

#### No monitoring.
Since the servers are not being monitored, we have no means of knowing their condition.