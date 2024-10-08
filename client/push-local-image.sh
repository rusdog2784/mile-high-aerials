#!/bin/bash

# Login to Docker Hub
echo -e "Logging into Docker Hub as rusdog2784. Please enter the password for the account, if prompted."
docker login --username rusdog2784

# Build and push the server image
imageName="rusdog2784/mile-high-aerials-client-image"
imageTag="local"
echo -e "Building and pushing the image to: $imageName:$imageTag"
docker build -t "$imageName:$imageTag" --platform linux/amd64 .
docker push "$imageName:$imageTag"

echo -e "Image build and push complete."
