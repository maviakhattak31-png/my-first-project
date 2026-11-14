- My first cloud project

I launched an Ubuntu server on AWS EC2, installed nginx,
and served my own web page from it.

Files:
- index.html : my web page
- linux-notes.md : my Linux command notes

- check_sites.py : a Python script that checks if websites are up or down

# How I deployed this project

1. I launched an Ubuntu server on AWS EC2 (a t3.micro, free-plan size).
2. I logged in from my own terminal with SSH and an SSH key.
3. I installed nginx, a program that serves web pages.
4. I downloaded this project onto the server with git clone.
5. I copied index.html into /var/www/html so nginx would show it.
6. I opened the server's public address in a browser and saw my page.
7. I ran check_sites.py on the server to check if websites are up or down.
8. I stopped the server afterwards so it would not use credits.

# What I learned
- A server is a computer I rent from AWS and control from the terminal.
- nginx is a program on the server. It hands out the web page I choose.
- SSH keys let me log in without a password.
- Git and GitHub let me move my work from my PC to a server.
