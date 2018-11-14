# swarm-meta
A basic Docker Swarm metadata service for a non-AWS environment.

The goal of this service is to provide similar functionality that the docker4x/meta-aws official container provides.

## Usage:
**NOTE**: Should only ever be run on manager nodes.
`docker run --log-driver=json-file  --log-opt max-size=50m --name=swarm-meta --restart=always -d -p $NODE_IP:9024:8080 -v /var/run/docker.sock:/var/run/docker.sock stroebs/swarm-meta:18.06.1-ce`
- `NODE_IP`: Needs to be set manually by calling script. The CaaS I am using does not have a metadata service.

The difference between the official docker4x container and this one is that of security. The official container will check that the calling instance belongs to the security group (meaning it's in the same swarm), whereas this one assumes security is handled otherwise.