# Disk Usage Alert Script

## Skill Focus
Monitoring and Alerting

## Problem Statement
Production systems run out of disk space without warning.

## Objective
Build a shell script that:
- Monitors disk usage
- Triggers alert when threshold is exceeded
- Logs alert details
- Can run via cron

## Approach

### Check disk space
Use a command like df to see how much disk is used.

### Decide a limit
Say 80%. If usage goes above 80%, we consider it risky.

### Compare current usage with the limit
If current usage >= 80%, then trigger alert.
If limit is crossed; then print warning message, then save it in a log file. We can optionally send email / notification

### Automate it
Run this script every 5 or 10 minutes using cron.
