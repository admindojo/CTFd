<h2 class="display-4">Getting started</h2>

1. Install required tools
2. [Choose a training](https://admindojo.org/challenges)
3. Start the pre-configured VirtualMachine
4. Read the objectives and implement them
5. Run `admindojo check ` to verify your solution
6. Track your progress at admindojo.org(optional)



<h3 class="lead">Install required tools</h3>

1. [install VirtualBox](https://www.virtualbox.org/)
2. [install Vagrant](https://www.vagrantup.com/downloads.html)
3. [install git](https://git-scm.com/downloads) 
4. clone the training-repository `git clone https://github.com/admindojo/admindojo-trainings.git`
    - it's also possible to just [download the trainings](https://github.com/admindojo/admindojo-trainings/archive/master.zip) - but git provides easier updates via `git pull` 

<p class="text-muted"><small>(Requirements: Windows/Mac/Linux, 10-20GB SSD, 2GB RAM, internet)</small></p>


<h3 class="lead">Start training</h3>

1. Open Powershell(Windows) or Terminal(Mac&Linux)
2. Go into the cloned repository
3. Go to a training directory
    - e.g. `cd webserver-apache-basic-1-ub18`
4. Type `vagrant up`
    - Vagrant will now build the VM. The first run can take a while 
5. Type `vagrant ssh`
    - You're now inside the VM and can start the training
6. Run `admindojo` for instructions


<h3 class="lead">Track progress at admindojo.org</h3>

To track your progress online, you'll get a `token` after completing a training. Go to [challenges](https://admindojo.org/challenges), open a training and submit the `token`.


<h2 class="display-4">Nice to know</h2>
Starting and rebooting the VM differs from normal operation because admindōjō utilizes [Vagrant](https://www.vagrantup.com):

- Use `vagrant ssh` to login/jump into the VM
- Exit the VM with _cms+D_ or `exit`
- To reboot the VM, please use the command `vagrant reload` from inside the training directory on your host
- To shutdown the VM, please use the command `vagrant halt` from inside the training directory on your host

<h3 class="lead">Username and password</h3>

Your user with sudo permission:

- username: `vagrant`
- password: `vagrant`

<h3 class="lead">Reset/Delete VM</h3>

- reset VM
    1. exit the VM with _cmd+D_ or `exit`
    2. inside training directory: `vagrant destroy` (VM needs to be running)
    3. start again: `vagrant up`
- delete VM
    1. exit the VM with _cmd+D_ or `exit`
    2. inside training directory: `vagrant destroy` (VM needs to be running)
    

<h3 class="lead">Update trainings/Download latest trainings</h3>

1. Open Powershell(Windows) or Terminal(Mac&Linux)
2. Change into cloned repository
3. run `git pull`


<h2 class="display-4">For advanced users</h2>

In case you are familiar with vagrant and ssh you can SSH directly to your admindojo box(SSH could require changes to the Vagrantfile depending on the Box Version).

Since admindōjō uses real-world tools under the hood you're able to use their native functions:

- Vagrant 
    - [Official documentation](https://www.vagrantup.com/docs/cli/)
    - [Cheat Sheet by wpscholar](https://gist.github.com/wpscholar/a49594e2e2b918f4d0c4)
- VirtualBox
    - [Official documentation](https://www.virtualbox.org/wiki/End-user_documentation)
- InSpec 
    - [Official documentation](https://www.inspec.io/docs/reference/cli/)