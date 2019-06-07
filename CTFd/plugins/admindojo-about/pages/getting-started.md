<p class="lead">admindōjō provides an <strong>easy to setup environment</strong> to train <strong>real-world Linux administration tasks</strong>.</p>
<p class="lead">Trainings contain real-world scenarios and in-depth explanations.Yout solution gets verified and rated - this way you know exactly if you implemented best-practices.</p>
<p class="lead">To keep you motivated, admindōjō allows you to track your progress online and compete with others!<br/>
<strong>admindōjō is not just a simulation</strong>! admindōjō uses unmodified Linux images and real-world objectives - everything that you learn is fully
applicable to a standard Linux installation!</p>
                
<h2 class="display-4">Getting started</h2>

1. Install required tools
2. [Browse trainings](https://admindojo.org/challenges)
3. Start the pre-configured VirtualMachine
4. Read the objectives and implement them
5. Run `admindojo check ` to verify your solution
6. Track your progress at admindojo.org(optional)


<h3 class="lead">Install required tools</h3>

1. [install VirtualBox](https://www.virtualbox.org/)
2. [install Vagrant](https://www.vagrantup.com/downloads.html)
3. [install git](https://git-scm.com/downloads) 
4. clone training-repository `git clone https://github.com/admindojo/admindojo-trainings.git`
    - it's also possible to just [download the trainings](https://github.com/admindojo/admindojo-trainings/archive/master.zip) - but git provides easier updates via `git pull` 

<small>Requirements: Windows/Mac/Linux, 10-20GB SSD, 2GB RAM, internet</small

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


<h2 class="display-4">Usage</h2>
<h3 class="lead">General</h3>
admindōjō heavily utilizes [Vagrant](https://www.vagrantup.com), starting and rebooting the VM differs from normal operation:

- Use `vagrant ssh` to login/jump into the VM
- Eexit the VM with _cms+D_ or `exit`
- To reboot/shutdown the VM, please use the vagrant commands `vagrant reload` and `vagrant halt`, since it does some _magical configuration_ to the VM. You must be inside the training directory to use these commands(One VM per training)

<h3 class="lead">Username and password</h3>

Your user with sudo permission:

- username: `vagrant`
- password: `vagrant`

<h3 class="lead">Shutdown, reset</h3>

- shutdown
    1. exit the VM with _cmd+D_ or `exit`
    2. inside training directory: `vagrant halt`
    
- start over (delete VM)
    1. exit the VM with _cmd+D_ or `exit`
    2. inside training directory: `vagrant destroy` and `vagrant up` to start again
    
<h3 class="lead">Remove VM after finishing a training</h3>

- inside training directory: `vagrant destroy` (VM needs to be running)

<h3 class="lead">Update admindojo</h3>

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