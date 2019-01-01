# OpenVPN init commands

## vars

Edit vars first, scroll to bottom. It has the global configuration like ports, logs.

## create-server

Create the OpenVPN server: UDP. Only internal traffic routed through the tunnel.

## create-server-tcp-gw

Create the OpenVPN server: TCP. Usually TCP 443, HTTPS. Port is configured in vars (above). ALL traffic (gateway mode) routed through the tunnel.

## build-key-embed {config_name}

Create client configuration file, embedded style, UDP, route only internal traffic.

Find {config_name} in: /etc/openvpn/keys/

## build-key-embed-tcp-commongw {config_name}

Create client configuration file, embedded style, TCP, route ALL traffic.

Find {config_name} in: /etc/openvpn/keys/

## revoke-client {config_name}

Revoke a client configuration and certificate.



















