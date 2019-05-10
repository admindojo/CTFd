adminDōjō provides an **easy to setup environment** to train **real-world Linux administration tasks** in preconfigured VirtualMachines.

Each training contains a real-world scenario and in-depth explanations.


Each training gets verified and rated - this way you know exactly if you implemented best-practices.

To help motivating yourself, adminDōjō allows you to track your progress online and compete with others!

**adminDōjō is not just a simulation**!

adminDōjō uses unmodified Linux images and real-world objectives - everything that you learn is fully applicable to a standard Linux installation! 

## Getting started 

1. Install required tools
2. [Browse trainings](https://admindojo.org/challenges)
3. Start the preconfigured VM
4. Read the objectives and implement them
5. Run `admindojo check ` to verify your solution


### Requirements
- Windows, Mac, Linux
- 10-20GB HDD for VMs
- 1-2GB RAM for VMs
- Internet connection to download VMs (~500MB once + 50-100MB per training)
- Due to the usage of VirtualBox, you can't run Docker or Hyper-V in parallel with VirtualBox. See [Vagrants documentation](https://www.vagrantup.com/docs/installation/)


### Install required tools
adminDōjō utilizes some third-party tools: 

1. [install VirtualBox](https://www.virtualbox.org/)
2. [install Vagrant](https://www.vagrantup.com/downloads.html)
3. [install git](https://git-scm.com/downloads) 
4. clone training-repository `git clone https://github.com/admindojo/admindojo-training.git`
    - it is also possible to just [download the trainings](https://github.com/admindojo/admindojo-training/archive/master.zip) - but git provides easier updates via `git pull` 

### Start training
1. Open Powershell(Windows) or Terminal(Mac&Linux)
2. Change into cloned repository
3. Change to a training directory
    - e.g. `cd webserver-apache-basic-1-ub18`
4. Type `vagrant up`
    - Vagrant will now build the VM. The first run can take a while 
5. Type `vagrant ssh`
    - You're now inside the VM and can start the training
6. Run `admindojo` for instructions


### Tracking progress at admindojo.org
To track your progress online, you'll get a `token` after completing a training. Go to [challenges](https://admindojo.org/challenges), open a training and submit the `token`.

You do need to [register](https://admindojo.org/register) at admindojo.org to track your progress.
(In case you're familliar with CTFs, you'll be familliar with the process.)

## Usage
### General
adminDōjō heavily utilizes [Vagrant](https://www.vagrantup.com) thus starting and rebooting the VM differs from normal operation:

- Use `vagrant ssh` to login/jump into the VM
- You exit the VM with _cms+D_ or `exit`
- Please use the vagrant commands `vagrant reload` and `vagrant halt` to reboot/shutdown the VM since it does some _magical configuration_ to the VM. You must be inside the training directory to use these commands(One VM per training)
- Your user is the default vagrant user _vagrant_

### Username and password

Your user with sudo permission:
- username: `vagrant`
- password: `vagrant`

### Shutdown, reset

- shutdown
    1. exit the VM with _cmd+D_ or `exit`
    2. inside training directory: `vagrant halt`
- start over (delete VM)
    1. exit the VM with _cmd+D_ or `exit`
    2. inside training directory: `vagrant destroy` and `vagrant up` to start again
    
### Remove VM after finishing a training
- inside training directory: `vagrant destroy` (VM needs to be running)

### Update admindojo
1. Open Powershell(Windows) or Terminal(Mac&Linux)
2. Change into cloned repository
3. run `git pull`


## For advanced users

In case you are familiar with vagrant and ssh you can SSH directly to your admindojo box(SSH could require changes to the Vagrantfile depending on the Box Version).

Since adminDōjō uses real-world tools under the hood you're able to use their native functions:

- Vagrant 
    - [Official documentation](https://www.vagrantup.com/docs/cli/)
    - [Cheat Sheet by wpscholar](https://gist.github.com/wpscholar/a49594e2e2b918f4d0c4)
- VirtualBox
    - [Official documentation](https://www.virtualbox.org/wiki/End-user_documentation)
- InSpec 
    - [Official documentation](https://www.inspec.io/docs/reference/cli/)