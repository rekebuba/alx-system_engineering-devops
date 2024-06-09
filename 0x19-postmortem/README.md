# Postmortem: Web Stack Debugging #3 Outage

## Issue Summary

- **Duration:** The outage lasted for 2 hours and 45 minutes, from 10:15 AM to 1:00 PM EAT.
- **Impact:** During the outage, the Apache server returned a 500 Internal Server Error for all incoming requests. This affected approximately 85% of our users, resulting in service unavailability and a significant drop in user engagement and transactions.
- **Root Cause:** The root cause was a misnamed configuration file that the Apache server failed to recognize, leading to the 500 error response.

## Timeline

- **10:15 AM EAT** - Issue detected: Monitoring alert triggered by a spike in 500 error responses.
- **10:17 AM EAT** - Initial investigation began: The engineering team started examining server logs and error messages.
- **10:30 AM EAT** - Misleading path: Assumed the issue was due to a missing file, leading to searches for non-existent files.
- **11:00 AM EAT** - Escalation: The incident escalated to the senior DevOps team for deeper analysis.
- **11:30 AM EAT** - Deeper investigation: Identified that the error was due to a misnamed configuration file.
- **12:00 PM EAT** - Misnamed file corrected: The file was renamed correctly and the Apache server configuration was updated.
- **12:15 PM EAT** - Server restart: Apache server was restarted to apply the changes.
- **12:30 PM EAT** - Monitoring: Post-restart monitoring showed a significant drop in error rates.
- **1:00 PM EAT** - Issue resolved: Confirmed that the service was fully restored and stable.

## Root Cause and Resolution

### Root Cause

The issue was caused by a configuration file named incorrectly. Apache relies on specific configuration files to operate correctly. In this instance, a critical configuration file had a typo in its name, causing Apache to fail in loading necessary settings and resulting in a 500 Internal Server Error.

### Resolution

To fix the issue, the following steps were taken:

1. **Identification:** The team identified that the error logs pointed to a missing configuration directive, which led to the discovery of the misnamed file.
2. **Correction:** The file was renamed to match the expected configuration name.
3. **Update Configuration:** Apache configuration was reloaded to acknowledge the corrected file.
4. **Restart Server:** The Apache server was restarted to ensure all configurations were correctly loaded.

## Corrective and Preventative Measures

### Improvements

- **Enhanced Monitoring:** Implement more granular monitoring to detect specific configuration errors.
- **Configuration Management:** Introduce stricter checks and validation for configuration files before deployment.
- **Documentation:** Improve documentation on naming conventions and critical configuration files.

### Tasks

1. **Patch Monitoring System:** Update the monitoring system to alert on specific configuration errors.
2. **Implement Pre-deployment Validation:** Add a script to validate configuration file names before deployment.
3. **Training Session:** Conduct a training session for the engineering team on common configuration issues and debugging techniques.
4. **Review Documentation:** Update internal documentation to include detailed naming conventions and examples of correct configurations.
5. **Automate Configuration Checks:** Develop an automated tool to check for common misconfigurations before they are applied to the production environment.

By addressing these areas, we aim to prevent similar issues in the future and improve our overall system reliability.
