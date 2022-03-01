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


-------
# all the tutorials I've used in this project

- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

CORS:
- https://www.youtube.com/watch?v=vWl5XcvQBx0
- https://www.youtube.com/watch?v=goToXTC96Co


- https://github.com/adatlaborhu/jarvic/blob/master/goonline.py
- https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- https://stackoverflow.com/questions/9713058/send-post-data-using-xmlhttprequest

— security: fixing headers and the Python script + SSL
— separated analytics server

- https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/
- https://www.pythonanywhere.com/forums/topic/2673/

issue: IOS
- https://www.npmjs.com/package/whatwg-fetch
- http://reputablejournal.com/adventures-with-flask-cors.html#.XmmAEJNKjqQ
- https://stackoverflow.com/questions/36811623/cors-request-with-flask-api-jquery-post-request-results-in-options
