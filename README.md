# simple_user_log
A simple way of logging your website usage if you want to ditch Google Analytics

I've created this project to replace Google Analytics with a simpler, better, more flexible and more privacy-friendly method.
It basically logs usage data of your website to your data server anonymously. You can create the same charts as you have in GA and more.
For that, you'll have to use Python and SQL.

For the logging, you'll need:
- a proper domain name for your data server so you can run it with https
- https certificate for your data server (recommended: https://letsencrypt.org/)
- Python 3.x
- Flask running in a virtual environment (tutorial: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)
- The Python script for the backend I've shared in this repo
- The JavaScript script implemented to your website -- also find in this repo
