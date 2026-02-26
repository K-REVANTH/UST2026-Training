# Automated Backup & Cleanup Script

## Skill Focus
Backup Automation

## Problem Statement
Application data must be backed up daily.

## Objective
Build a shell script that:

- Creates timestamped backups
- Compresses them
- Deletes old backups based on retention policy
- Logs backup status

## Approach

Identify what needs to be backed up. (Eg: `/var/www/app`)

Create a backup directory. (Eg: `/home/ec2-user/backups`)

Generate a timestamp, so that each backup file is unique  

Compress the data, by using `tar` with gzip compression.

Apply retention policy; delete backups older than X days.

Log everything; success or failure with date and time.

Automate - Schedule using cron to run daily.
