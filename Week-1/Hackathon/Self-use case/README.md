# Post-Deployment Validation Framework (Self use case)

## PROBLEM

After a production deployment, the application becomes unstable due to process duplication, port conflicts, network misconfiguration, configuration drift, permission changes, and increasing error logs. An automated system is required to detect these issues, remediate recoverable problems, validate application health, and determine whether the deployment should be marked successful or failed.

---

## APPROACH

### Initial Setup
Define application name, expected port, expected user/group, configuration file location, log file location, structured exit codes, logging mechanism.

### Process Check
Verify application is running, and ensure only one instance is active. If not running → Fail deployment.

### Port Check
Confirm expected port is bound and ensure correct process owns the port. If port conflict detected → Fail deployment.

### Log Check
Count occurrences of ERROR, TIMEOUT and CONNECTION_REFUSED. If errors exceed threshold → Mark unstable.  

### Health Check
Call health endpoint using `curl`. If HTTP 200 → Success, Else → Fail deployment. 

### Return Status
Exit 0 → Success, Exit 1 → Failure.
