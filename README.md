<h1 align="center">Hi 👋 We are <a href="https://github.com/ElianDochev" target="blank">
Eliyan Dochev</a> and <a href="https://github.com/VividVice" target="blank">Vasiliy Novikov!</a> </h1>

<h2 align="center">Get started with React and Gatsby</h3>

<h3 align="center" > <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30" height="30" style="margin-right: 10px;">Get in touch with us 🤝 </h3>

<div style="display: flex; flex-direction: row; justify-content: center; align-items: center;">
  <p align="center">
  <h1 align="center"> Eliyan Dochev </h1>
   <div align="center"  class="icons-social" style="margin-left: 10px;">
          <a style="margin-left: 10px;"  target="_blank" href="https://www.linkedin.com/in/elian-dochev-8a53a9250/">
  			<img  style="width: 40px; height: 40px" src="https://img.icons8.com/doodle/40/000000/linkedin--v2.png"></a>
          <a style="margin-left: 10px;" target="_blank" href="https://github.com/ElianDochev">
  		<img  style="width: 40px; height: 40px" src="https://img.icons8.com/doodle/40/000000/github--v1.png"></a>
  		<a style="margin-left: 5px;" target="_blank" href="mailto:eliyan.dochev@epitech.eu">
  					<img style="width: 40px; height: 40px" src="https://image.similarpng.com/very-thumbnail/2021/09/Outlook-icon-on-transparent-background-PNG.png" ></a>
        </div>
  </p>

# Introduction

In this workshop, you will learn how to deploy a simple Flask application on AWS EC2. You will also learn how to
use ssh to connect and use Docker to build and run your application.

## Account and Instance Setup

### Step 1

Create an [AWS Account](https://aws.amazon.com/)

### Step 2

Access [AWS Management Console](https://aws.amazon.com/console/)

### Step 3

Launch an EC2 Instance

Docs: [Lanching an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance)

### Step 4

Open port for ssh connection 22 TCP and 5000 TCP for Flask server

Docs: [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)

### Step 5

Connect to your EC2 instance using SSH

Docs: [Connecting to Your Linux Instance Using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

## Account and Instance Setup

### Step 1

Install Docker on your EC2 instance via snap

```bash
sudo apt update # this updates the package manager
sudo apt install snapd # this installs snap
sudo snap install docker # this installs docker
sudo snap refresh docker --channel=latest/edge
sudo groupadd docker # this creates a docker group
sudo usermod -aG docker $USER # this makes docker run without sudo
newgrp docker # this makes docker run without sudo
```

### Step 2

Transfer /app dir to your EC2 instance

```bash
scp -i <path_to_pem_file> -r <path_to_app_dir> ubuntu@<ec2_public_ip>:/home/ubuntu
```

Docs: [What is a Pem file](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)

### Step 3

Configure Firewall (Security Group):
Make sure that your EC2 instance's security group allows traffic on the port you're using for Flask (default is 5000). Configure the inbound rules accordingly.

[How to configure security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)

### Step 4

Run the Flask app on your EC2 instance

```bash
docker-compose up --build
```

### Step 5

Access the App:
Visit your EC2 instance's public IP address or DNS followed by the port number (default is 5000)

Docs: [Public IPv4 addresses and external DNS hostnames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses)

### Bonus

Set up Nginx as a Reverse Proxy (Optional but Recommended):
For better performance and security, consider setting up Nginx as a reverse proxy

Set up Gunicorn
For production use, it's recommended to use a production-ready server like Gunicorn.
