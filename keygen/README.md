# OpenVPN service management commands

To use them, first open a SSM (or SSH if you have) session and gain root access (*sudo su -*).

## source ./vars

Edit *vars* file first, (do not modify if you have a running server) scroll to bottom. It has the global configuration like ports, logs.

## ./create-server

For __VPC_ONLY_UDP443__!

__NOTE:__ Do not use it if you have a running server. It creates new OpenVPN server service: UDP. Only internal traffic routed through the tunnel.

## ./create-server-tcp-gw

For __ALL_GATEWAY_TCP443__!

__NOTE:__ Do not use it if you have a running server. It creates new OpenVPN server service: TCP. Usually TCP 443, HTTPS. Port is configured in vars (above). ALL traffic (gateway mode) routed through the tunnel.

## ./build-key-embed {config_name}

For __VPC_ONLY_UDP443__!

Create client configuration file, embedded style, UDP, route only internal traffic.

Find and download OpenVPN config {config_name} in: /etc/openvpn/keys/{config_name}/{config_name}.ovpn

## ./build-key-embed-tcp-commongw {config_name}

For __ALL_GATEWAY_TCP443__!

Create client configuration file, embedded style, TCP, route ALL traffic.

Find and download OpenVPN config {config_name} in: /etc/openvpn/keys/{config_name}/{config_name}.ovpn

## ./revoke-client {config_name}

Revoke a client configuration and certificate. It automatically revoke the config, the config won't work anymore.



















