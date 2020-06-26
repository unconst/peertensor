## Peerstore Server

# Run locally
1. Install python

```
# Install python dependencies
pip install -r requirments.txt

# Install protocol.
pip install -e .

# Run the server
python server.py

# Run the test client
python client.py
```

# Run remote on Digital Ocean
1. Install Docker

1. Install Docker Machine

```
# Get API-token on Digital Ocean as $TOKEN
$ TOKEN=(your api token)

# Create a remote instance
$ docker-machine create --driver digitalocean --digitalocean-size s-4vcpu-8gb --digitalocean-access-token ${TOKEN} peerstore

# Switch to instance context
$ eval $(docker-machine env peerstore)

# Build the docker image.
$ docker build -t peerstore .

# Run the server
$ docker run -it -p 8888:8888 peerstore server.py

# Get instance ip address
$ ipaddress=$(eval docker-machine ip peerstore)

# Test the server 
python client --address=$ipaddress
```




