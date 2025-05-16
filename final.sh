#!/bin/bash
# Create a directory to store the result files in the container
mkdir -p /home/doc-bd-a1/result

# Copy the output files from the container to the result directory
docker cp <29cab78ca3edcdfc024c5b43344de35fd1ba4326c3318cda4770b87f6083bdd1>:/home/doc-bd-a1/*.csv /home/doc-bd-a1/result/
docker cp <29cab78ca3edcdfc024c5b43344de35fd1ba4326c3318cda4770b87f6083bdd1>:/home/doc-bd-a1/*.txt /home/doc-bd-a1/result/
docker cp <29cab78ca3edcdfc024c5b43344de35fd1ba4326c3318cda4770b87f6083bdd1>:/home/doc-bd-a1/vis.png /home/doc-bd-a1/result/

# Copy the result directory from the container to the local machine
docker cp <29cab78ca3edcdfc024c5b43344de35fd1ba4326c3318cda4770b87f6083bdd1>:/home/doc-bd-a1/result/. "E:\Gam3a\big data\bd-a1\service-result/"

docker stop <29cab78ca3edcdfc024c5b43344de35fd1ba4326c3318cda4770b87f6083bdd1>
