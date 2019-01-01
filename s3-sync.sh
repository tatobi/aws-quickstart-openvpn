#!/bin/bash

aws s3 sync ./ s3://tatobi-aws-quickstart-openvpn/ --exclude ".git/*"


