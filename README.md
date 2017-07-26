You can use Pl-sql developer or Toad in order to export text of stored procedures into the disk, 
but if you don't want to do this manual tasks you can just use some programming language in order to automate the process.
You can find simple example here. 
It uses 4 python libraries: os, shutil to work with file system, cx_Oracle to work with Oracle database and threading to execute repetetive task.

The script exports the following oracle database entities:

PACKAGES
VIEWS
PROCEDURES
FUNCTIONS
TYPES
JOBS
TABLES