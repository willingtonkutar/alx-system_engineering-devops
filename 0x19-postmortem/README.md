# Postmortem Report: Web Stack Outage

![a postmortem report image](https://github.com/user-attachments/assets/55bf0f17-d0d2-42da-942f-e49427f59a77)

## Issue Summary
**Duration of Outage:** July 1, 2025, 10:00 AM - 12:00 PM (EAT)

**Impact:** The primary web service was down, resulting in 80% of users being unable to access the site. Users experienced error messages and slow loading times.

**Root Cause:** The root cause was a misconfiguration in the Nginx server that led to a denial of service when traffic spiked unexpectedly.

![someone who is late for something](https://github.com/user-attachments/assets/2cae79c8-8bbe-43d9-99b8-b14daa713ba5)

## Timeline
- **10:00 AM:** Issue detected by monitoring alert indicating high error rates.
- **10:05 AM:** On-call engineer received the alert and began investigation.
- **10:10 AM:** Initial assumption was a database overload.
- **10:15 AM:** Database queries checked, but no anomalies found.
- **10:30 AM:** Misleading path taken, assuming it was a network issue.
- **10:45 AM:** Network team confirmed no issues.
- **11:00 AM:** Focus shifted to application server logs; identified repeated errors in Nginx configuration.
- **11:15 AM:** Incident escalated to the web server team.
- **11:30 AM:** Misconfiguration in Nginx identified and corrected.
- **11:45 AM:** Nginx server restarted, services began to recover.
- **12:00 PM:** Full service restoration confirmed, users could access the site without issues.

## Root Cause and Resolution
**Root Cause:** The Nginx server configuration had an incorrect setting that limited the number of allowed connections, causing the server to deny new connections when traffic spiked.

**Resolution:** The misconfigured line in the Nginx configuration file was corrected, and the server was restarted. The corrected configuration increased the allowed number of connections, preventing the denial of service.

## Corrective and Preventative Measures
### Improvements/Fixes:
- **Review and update Nginx configuration settings** to ensure they are optimized for high traffic.
- **Implement automated configuration validation** to catch misconfigurations before they cause issues.
- **Enhance monitoring** to detect and alert on specific configuration-related errors.

### Tasks to Address the Issue:
1. **Patch Nginx Server:**
   - Update the Nginx configuration file with correct settings.
   - Restart the server to apply changes.

2. **Add Monitoring on Server Memory:**
   - Implement monitoring tools to track server memory usage and connection limits.
   - Set up alerts for when memory usage or connections approach critical levels.

3. **Automate Configuration Validation:**
   - Develop a script to validate Nginx configuration settings upon deployment.
   - Integrate validation script into the CI/CD pipeline.
