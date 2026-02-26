## nano disk_alert.sh
It opens the file `disk_alert.sh` in the Nano text editor to create/modify the shell script.

## df -h
It displays disk usage of all mounted filesystems. This is used here to manually verify the actual disk usage of the system.

## chmod +x disk_alert.sh
It adds execute permission to the script. Without execute permission, Linux will not allow the script to run.

## ./disk_alert.sh
It executes the script.

## cat disk_alert.log
It displays the contents of the file. It is used to verify that alert messages were successfully logged.
