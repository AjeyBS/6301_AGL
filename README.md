# Generic Container with all scripts

# Script Specific Container
## make container 
docker build -t \<imageName\>:\<tag\> -f \<dir\> .
docker build -t emwoj/cs6301_hvac:1.0 -f hvac/Dockerfile .

## start container
docker run -i \<imageName\>:\<tag\>
docker run -i emwoj/cs6301_hvac:1.0

