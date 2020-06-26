
function start_service() {

  function teardown() {
    echo "=== tear down. ==="
    eval $(docker-machine env -u)
    echo "docker-machine stop peerstore & docker-machine rm peerstore --force "
    exit 0
  }
  trap teardown INT SIGHUP SIGINT SIGTERM ERR EXIT

  echo "=== initializing remote host. ==="
  if [[ "$(docker-machine ls | grep peerstore)" ]]; then
    # Host already exists.
    echo "peerstore droplet already exists."
  else
    echo "Creating Droplet: peerstore"
    DROPLET_CREATE="docker-machine create --driver digitalocean --digitalocean-size s-4vcpu-8gb --digitalocean-access-token $DOTOKEN peerstore"
    echo "Create command: $DROPLET_CREATE"
    eval $DROPLET_CREATE
  fi

  # Set the docker context to the droplet.
  echo "=== switching droplet context. ==="
  eval $(docker-machine env peerstore)

  # Stop the container if it is already running.
  if [[ "$(docker ps -a | grep peerstore)" ]]; then
    echo "=== stopping peerstore ==="
    docker stop peerstore || true
    docker rm peerstore || true
  fi

  # Find the external ip address for this droplet.
  serve_address=$(eval docker-machine ip peerstore)
  echo "serve_address: $serve_address:$port"

  # Run docker service.
  echo "=== run the docker container on remote host. ==="
  docker run --rm --name peerstore -d -t \
  -p $port:$port \
  frolvlad/alpine-python3 /bin/bash -c "./start.sh"

  echo "=== follow ==="
  docker logs bittensor-$identity --follow
}


# Main function.
function main() {
  
  echo "██████╗░██╗████████╗████████╗███████╗███╗░░██╗░██████╗░█████╗░██████╗░"
  echo "██╔══██╗██║╚══██╔══╝╚══██╔══╝██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗"
  echo "██████╦╝██║░░░██║░░░░░░██║░░░█████╗░░██╔██╗██║╚█████╗░██║░░██║██████╔╝"
  echo "██╔══██╗██║░░░██║░░░░░░██║░░░██╔══╝░░██║╚████║░╚═══██╗██║░░██║██╔══██╗"
  echo "██████╦╝██║░░░██║░░░░░░██║░░░███████╗██║░╚███║██████╔╝╚█████╔╝██║░░██║"
  echo "╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚═╝"

  start_service
}

main
