# Generic Container with all scripts Example
## make container
docker build -t emwoj/cs6301_hvac:latest .

## start container
docker run -it emwoj/cs6301_hvac:latest /bin/sh

## run scripts
python HVAC_attack.py

# Script Specific Container Example
## make container 
docker build -t emwoj/cs6301_hvac:1.0 -f hvac/Dockerfile .

## start container
docker run -i emwoj/cs6301_hvac:1.0

