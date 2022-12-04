![My Image](https://i.redd.it/vri4ra46xi531.jpg)
## COMPANY XYZ SERVER FAIL INCIDENT REPORT

#### Issue Summary
On November 26th 4:33 PM EAT all the servers of companyXYZ backend went down. This was caused  by rebooting one faulty server. On rebooting this server an error from another server caused all servers to go down too.

Impact
All CompanyXYZ servers were down for 1 hour, this led to the users being unable to receive 200 response messages to their requests in that timeframe. The users reported receiving 500 error messages from www.companyXYZ.com and its subdomains.
 
#### Time-line (EAT)
At 2:55 PM CloudFare reported an issue on their side with one of our servers hosted by their company.
At 4:00 PM it was observed that another server was behaving in an unexpected way with lower CPU usage than normal
At 4:23 PM an alert was received from dogwatch that notified us of slow response times of the backend, this was linked to the fact that only 5 servers of 7 servers were functioning correctly.
At 4:27 PM it was decided by our engineers to reboot the server with low CPU usage to reduce the response times.
At 4:33 PM it was found that restarting the server caused all the other servers to stop working.

#### Root Cause
The root cause of the servers going down was caused by server cloudFlare reported to having problems. The server was not connected to the load balancer, but the server was still connected to cache data. When the server was rebooted it tried to connect to the load balancer, all servers failed because they tried to update their cache but could not connect to the node that had cloudFlare issues.

#### Resolution and Recovery
CompanyXYZ disabled the other faulty server, with this action all other servers recovered immediately. After investigating the faulty server it was deemed safe to restart it, all the servers were up and running again at 5:33 PM EAT.

#### Corrective and Preventive Measures
Making the caching process a separate service. This ensures that when their is an issue with data caching one server can not affect the other servers
Setting up new alerts for data transfer and CPU thresholds that could indicate a similar situation.
Increasing the number of servers to increase the number of fall-back possibilities in the future.
