 # Linux commands
 # Moving around
- pwd : shows which folder i am in .
- cd folder name: goes into the folder.
- ls : lists what is inside a folder.

# Files
- mkdir name: makes a folder.
- touch name: makes an empty file.
- cat name: shows what is in the file.

# Servers
- EC2 : a computer I rent from AWS
- ssh ubuntu@PUBLIC_IP : logs in to the server
- nginx : a program that hands out my web page
- /var/www/html/index.html : the page nginx shows

# Docker
- docker ps -a : lists my containers
- docker run -d -p 8081:80 --name my-nginx nginx : runs nginx in a container
- docker stop my-nginx : stops it
- docker rm my-nginx : removes it
- Run my page in Docker (change 8082 if the port is busy):
  docker run -d -p 8082:80 --name my-page -v "$(pwd)":/usr/share/nginx/html:ro nginx
- Stop it: docker stop my-page
- Remove it: docker rm my-page

# Python
- python3 file.py : runs a Python script
- check_site.py : checks if one website is up or down
- check_sites.py : checks a list of websites and prints UP or DOWN for each
- try / except : tries something, and does something else if it fails
- for url in urls : repeats the same steps for each item in a list

# Deploying
- git clone <address> : downloads a project from GitHub to the server
- sudo cp index.html /var/www/html/ : puts my page where nginx serves it
