sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s -f /home/box/web/etc/hello.py /etc/gunicorn.d/test
sudo service gunicorn restart
gunicorn -b 0.0.0.0:8080 hello:app