# Digital Ocean

## table of contents


## how to setup VM on digital Ocean and setup VM
- Create a droplet ( ref: https://youtu.be/0sOvCWFmrtA?t=43553 )
- Login to VM using ssh
  - ssh root@<ip-address>
  - enter the password created during the VM creation
- install packages
  - `sudo apt update && sudo apt upgrade -y`
  - Check for - `python3 --version`
  - install pip - `sudo apt install python3-pip`
  - `sudo pip3 install virtualenv`
  - `sudo apt install postgresql postgresql-contrib -y`

## how to connect to postgresql
- check for psql `psql --version`
- change the root user: postgres
  - `su postgres`
- to change the listen_address: https://youtu.be/0sOvCWFmrtA?t=44340