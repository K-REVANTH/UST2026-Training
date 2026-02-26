## sudo mkdir -p /var/www/app
Created the directory `/var/www/app`.

## echo "Sample data 1" | sudo tee /var/www/app/file1.txt
## echo "Sample data 2" | sudo tee /var/www/app/file2.txt
Created a file named `file1.txt` and `file2.txt`, and wrote the content into it.

## ls /var/www/app
The application directory now contains two files.

## sudo chown -R ec2-user:ec2-user /var/www/app
It changed ownership of the directory and its contents, so that the backup script can access the directory without sudo.

## nano backup_cleanup.sh
It Opened the backup script file for editing.

## chmod +x backup_cleanup.sh
It gave execute permission to the script. Without this, the script cannot be run.

## ./backup_cleanup.sh
It executed the backup script. Internally, the script:
- Created backups directory
- Generated timestamp
- Compressed `/var/www/app`
- Created `.tar.gz` file
- Logged success
- Applied cleanup policy

## ls ~/backups
It creates a compressed backup file.

## cat ~/backup.log
Line 1:
Backup was successful.  
It shows:
- Backup file path
- Date and time of execution

Line 2:
Cleanup process ran successfully.  
This means the retention policy logic was executed (even if no old files existed).
