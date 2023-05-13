![](https://i.postimg.cc/dtrMWD8M/david-pupaza-he-Nw-Um-Et-Zzo-unsplash.jpg)

## Issue Summary:
- Duration of the outage: May 7, 2023, at 8:15 AM EDT - May 7, 2023, at 9:00 AM EDT
- Impact: Users trying to access the second web server were unable to do so during the outage.
- The service was completely down for 100% of the users trying to access it.
- The root cause was a misconfigured firewall rule that was blocking incoming traffic.

## Timeline:
- May 7, 2023, at 8:15 AM EDT: The issue was detected by a monitoring alert that showed that the second server was not responding to requests.
- Actions taken: The team investigated the second server logs and found no issues with the server.
- They then checked the load balancer logs and saw that requests were not reaching the second server.
- Misleading investigation/debugging paths that were taken: The team initially suspected a problem with the second server and spent time checking the server logs.
- The investigation was a misleading path because the issue was not with the server itself, but with incoming traffic.
- The incident was escalated to the network engineering team to investigate the network configuration.
- The incident was resolved by the network engineering team identifying the misconfigured firewall rule that was blocking incoming traffic to the second server and fixing it.

## Root cause and resolution:
- The root cause was a misconfigured firewall rule that was blocking incoming traffic to this server.
- The issue was fixed by the network engineering team identifying the misconfigured firewall rule and fixing it.

## Corrective and preventative measures:
- To prevent similar issues from happening in the future, the team will implement regular network configuration reviews to ensure that firewall rules are correctly configured.
- Tasks to address the issue include:
  - Reviewing firewall rules for all servers to ensure that they are correctly configured
  - Implementing additional monitoring for incoming traffic to identify any further misconfigurations or anomalies
  - Reviewing incident response procedures to ensure that misconfigurations are quickly identified and resolved.
