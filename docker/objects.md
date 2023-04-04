# Docker Core Concepts

## Images

Basically a set of instructions for creating a Docker container. It is read only. You can specify the operating system, image as well as what applications and configurations you require to make your by your application. Dockerfiles are how programmers tell Docker what kind of image to make and how to run it. When you change a the file and rebuild the image only the necessary parts are changed and everything else stays the same. 

## Containers

Containers are images in action. They are the consciousness to Dockers physical brain the image. They can be started, stopped, moved, and deleted, they can connect to multiple networks, and even be copied live into a new image.
