# isitwo

A small tool to manage EC2 instances from command line.

Having to open the EC2 console every time you have to spin up a machine is quite annoying, especially if you have a 2-factor authentication set up.
Using the AWS CLI requires you to remember the instance ids and changing the instance type is not that easy, so I wrote this small script to handle listing instances, start, stop and changing instance type on the fly.

Available commands:

- `list-instances`: overview of the available instances with their information
- `start-instance`: start the instance with the provided name 
- `stop-instance`: stop the instance with the provided name 
- `change-instance-type`: change the specified instance type to the selected one
