# Run Scripts Locally
`pip install -r reqs.txt`

`python HVAC_attack.py`

# Generic Container with all scripts
## make container
`docker build -t emwoj/cs6301_proj:latest .`

## start container
`docker run -it emwoj/cs6301_proj:latest /bin/sh`

## run scripts
`python HVAC_attack.py`

# Script Specific Container
## make container 
`docker build -t emwoj/cs6301_hvac:1.0 -f hvac/Dockerfile .`

## start container
`docker run -i emwoj/cs6301_hvac:1.0`

