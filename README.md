# AWS Quick Start for OpenVPN 

Deploy secure OpenVPN easy-to-use connection to an existing AWS VPC in 2 minutes, via a single click.


## Features

- very easy to deploy via AWS Quickstart URLs and AWS CloudFormation,

- __one-click download openvpn config__ via an S3 signed URL (no need to SSH to host) from CloudFormation Output tab,

- __embedded vpn config__ file: contains everything you need, muliple config file created at once (up to 100),

- fully tested on: __Windows 10, Linux (Ubuntu), Android, Mac OSX (tunnlebrick)__,

- __secure:__ SHA512 channel auth, AES-256-CBC encryption, TLS 1.2 forced (openvpn > v2.3.10  or higher client versions needed!), __NO SSH__, access instance via AWS SSM only, internal DNS,

- __traffic routing options:__ __gateway/TCP443 (HTTPS)__ or VPC only/UDP443 - mostly unblocked from everywhere,

- __anonymous:__ no VPN log files on servers, use AWS DNS server forced through the tunnel,

- __fast cacheing DNS:__ cacheing dnsmasq installed and used on server side, pushed to VPN client,

- __cheap EC2 instances:__ t2 and t3 classes,

- seamless teardown,

- __ALL AWS regions supported__ by dynamic AMI selection,

- based on __Ubuntu 18.04LTS__ latest version by dynamic version selection.


## Prerequisities

You need to have an AWS account, the deployment user needs full EC2 and IAM rights.


## Deployment

Use the AWS QuicKstart URLs to deploy different AWS regions:




