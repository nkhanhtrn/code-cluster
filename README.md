# code-cluster
Running cluster of cost-optimal Cloud Coder

# Archirecture

```
---------------                         -----------------
|             |                         |               |
|   web app   | ------ API call ------> |  code-server  | 
|             |                         |               |
---------------                         -----------------
   always on                           only on when needed
```
   
 # Deployment
 - populate `config.ini`
 - `virtualenv env && source env/bin/activate`
 - `./deploy.sh`
 
