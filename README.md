Project: Tournament Results

This project is designed to utlize the PostgreSQL database to keep track of players and matches played in a Swiss-style tournament.

First of all, you will need to perform several installs if not already installed on your device.

You will need to install Python (https://www.python.org/downloads/), Git (https://git-scm.com/downloads), Vagrant (https://www.vagrantup.com/), VirtualBox (https://www.virtualbox.org/). Follow the instructions on the page.

1. Open up Terminal, and change to the desired parent directory (i.e. cd Desktop/).
2. Using Git, clone the VM configuration: 
3. git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack
3. Change directory to the vagrant folder (cd fullstack/vagrant/).
4. Using Git, clone the following project: 
git clone https://github.com/thealexismarie3/udacity_full_stack.git tournament
5. Run vagrant by entering: vagrant up
6. Enter vagrant ssh to log into Vagrant VM.
7. Change to the tournament directory (cd /vagrant/tournament/).
8. Use the psql command to run psql interface, followed by \i tournament.sql to build/access the database.
9. Exit the psql interface using control+D.
10. To test the database, enter:
python tournament_test.py

No known bugs.