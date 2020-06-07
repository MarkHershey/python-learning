# Deploy a Flask Server on Ubuntu using Apache2

ref: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

restart apache server
```
sudo service apache2 restart
```


```bash
cd /var/www/
```

```
drwxr-xr-x  4 root root 4096 May 14 17:35 .
drwxr-xr-x 14 root root 4096 May 14 16:31 ..
drwxr-xr-x  3 root root 4096 May 14 20:38 WebDevLearning
drwxr-xr-x  2 root root 4096 May 14 16:31 html
```

```
4 drwxr-xr-x 6 root root 4096 Jun  7 08:56 WebDevLearning
4 -rw-r--r-- 1 root root  363 May 14 20:22 WebDevLearning.wsgi
4 -rw------- 1 root root  413 May 14 20:38 WebDevLearning.wsgi.save
```


`WebDevLearning.wsgi`

```python
#!/usr/bin/python3

activate_this = '/var/www/WebDevLearning/WebDevLearning/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/WebDevLearning/")

from WebDevLearning import app as application
application.secret_key = 'Add your secret key'
```
