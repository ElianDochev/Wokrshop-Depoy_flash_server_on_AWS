h1 align="center">Hi 👋 We are <a href="https://github.com/ElianDochev" target="blank">
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

  <p align="center">
  <h1 align="center"> Vasiliy Novikov </h1>

   <div align="center"  class="icons-social" style="margin-left: 10px;">
          <a style="margin-left: 10px;"  target="_blank" href="#!/">
  			<img  style="width: 40px; height: 40px" src="https://img.icons8.com/doodle/40/000000/linkedin--v2.png"></a>
          <a style="margin-left: 10px;" target="_blank" href="#!">
  		<img  style="width: 40px; height: 40px" src="https://img.icons8.com/doodle/40/000000/github--v1.png"></a>
  		<a style="margin-left: 5px;" target="_blank" href="mailto:#!">
  					<img style="width: 40px; height: 40px" src="https://image.similarpng.com/very-thumbnail/2021/09/Outlook-icon-on-transparent-background-PNG.png" ></a>
        </div>
  </p>
</div>

# Introduction

In this workshop, you will learn how to deploy a simple Flask application on AWS EC2. You will also learn how to
use ssh to connect and use Docker to build and run your application.

## Account and Instance Setup

### Step 1

Create an [AWS Account](https://aws.amazon.com/)

### Step 2

Access AWS Management Console

### Step 3

Launch an EC2 Instance

### Step 4

Open port for ssh connection 22 TCP and 5000 TCP for Flask server

### Step 5
Connect to your EC2 instance using SSH

### Step 6

Install Flask on your EC2 Instance:
Connect to your EC2 instance using SSH and install Flask.

### Step 7

Create a Simple Flask App:
Create a simple flask app that prints hello world on the index endpoint

### Step 8

Configure Firewall (Security Group):
Make sure that your EC2 instance's security group allows traffic on the port you're using for Flask (default is 5000). Configure the inbound rules accordingly.

### Step 9

Run the Flask App:
Run your Flask app on your EC2 instance. Make sure to run it on 0.0.0.0 so it's accessible from the outside:

### Step 10

Access the App:
Visit your EC2 instance's public IP address or DNS followed by the port number (default is 5000)

### Step 11

Set up Gunicorn
For production use, it's recommended to use a production-ready server like Gunicorn.

### Bonus

Set up Nginx as a Reverse Proxy (Optional but Recommended):
For better performance and security, consider setting up Nginx as a reverse proxy
