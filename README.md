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

- __fast caching DNS:__ cacheing dnsmasq installed and used on server side, pushed to VPN client,

- __cheap EC2 instances:__ t2 and t3 classes,

- seamless teardown,

- __ALL AWS regions supported__ by dynamic AMI selection,

- based on __Ubuntu 18.04LTS__ latest version by dynamic version selection.


## Prerequisities

You need to have an AWS account, the deployment user needs full EC2 and IAM rights.


## Quic Start deploy

Click on the AWS QuicKstart URLs __below__ to deploy different AWS regions. They will open the AWS CloudFormnation stacks page, the you need just give a few options and start it.


### Europe

*Ireland:* [AWS: eu-west-1](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*London:* [AWS: eu-west-2](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Paris:* [AWS: eu-west-3](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)


*Frankfurt:* [AWS: eu-central-1](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Stockholm:* [AWS: eu-north-1](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

### North America

*US North Virginia:* [AWS: us-east-1](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*US Ohio:* [AWS: us-east-2](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*US North California:* [AWS: us-west-1](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*US Oregon:* [AWS: us-west-2](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Canada Central:* [AWS: ca-central-1](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

### South America

*Sao Paulo:* [AWS: sa-east-1](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

### Asia Pacific, Australia, Japan

*Mumbai, India:* [AWS: ap-south-1](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Seoul, South Korea:* [AWS: ap-northeast-2](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Singapore:* [AWS: ap-southeast-1](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Sydney, Australia:* [AWS: ap-southeast-2](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

*Tokyo, Japan:* [AWS: ap-northeast-1](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=OpenVPN-Bastion&templateURL=https://s3-eu-west-1.amazonaws.com/tatobi-aws-quickstart-openvpn/cloudformation/ovpn-aws-deploy-vpc.yaml)

## AWS CloudFormation paramaters




