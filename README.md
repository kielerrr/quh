# quh

Starter Kubernetes clusters with infrastructure, routing and a front/back app with detachable sftp volume for source files.
                                                     
- HTTP/TCP routing: traefik
- Frontend: vite vue-ts
- Backend: fastapi sqlite
- Log/metric havers: loki prometheus promtail
- Logs GUI: grafana


Defaults are configured to deploy on Digital Ocean. To deploy on another server or minikube, adjust storageClass and privateVolumes to connect using their respective values. Paths and .bat files are Windows format but can be easily adjusted to linux paths and shell script. An attempt is made to include screenshots of issues that may occur with points of importance highlighted.

Source files are stored in a detachable volume which is accessible with built in sftp server and ssh keys.   The benefit here is if you run into any issues, *it is safe to destroy the entire cluster,  and rebuild it fresh everytime* with configuration tweaks. Do not delete the detachable Volume with source files.

IDE used in the examples is  https://k8slens.dev/

Edit cluster_vars in `write_cluster_vars.py`
See screenshots below to 
Once you run the next step, the script will replace all placeholders ie `{{{{ foo }}}}` with the value in `cluster_vars`. It's difficult to undo this step so it's recommended to backup your working directory in case you need to redo.

If using Digital Ocean, create a cluster and set kubectl to use the context for the cluster. If using minikube or another server, make sure bash/cmd scripts are setting kubectl to your target context.

Run

    # python write_cluster_vars.py

Run

    .\fckyea.bat\

Run checks and tweak anything that may be stuck.

![Run setup commands](how-to-make-it-happen\5.png)
![Final cluster resource map](how-to-make-it-happen\9.png)
![Frontend up](how-to-make-it-happen\17.png)
![Backend ups](how-to-make-it-happen\15.png)
![Backend ups](how-to-make-it-happen\18.png)
![Backend ups](how-to-make-it-happen\7.png)
![Backend ups](how-to-make-it-happen\19.png)
![Backend ups](how-to-make-it-happen\10.png)
![Backend ups](how-to-make-it-happen\4.png)
###Run this if running into sftp issues.
![Backend ups](how-to-make-it-happen\16.png)

###App1 is an example app. Both the frontend and backend are running in  their own container and wrapped in a deployment. Logs are auto captured and delivered to Loki and Prometheus and then readable live in Grafana.
![Backend ups](how-to-make-it-happen\14.png)
![Backend ups](how-to-make-it-happen\13.png)

###Setup an SFTP connection to upload source files.
![Backend ups](how-to-make-it-happen\12.png)

###This will go green when source files are loaded in correct directories with correct permissions.
![Backend ups](how-to-make-it-happen\11.png)

###If using Digital Ocean: Point domain nameservers to ns1.digitalocean.com, ns2.digitalocean.com. After you have deployed the cluster, Traefik will automatically create a Loadbalancer and a Volume
![Backend ups](how-to-make-it-happen\1.png)

###NYC1 is recomended. Note where to put node pool and name in  `cluster_vars`
![Backend ups](how-to-make-it-happen\2.png)
![Backend ups](how-to-make-it-happen\3.png)

###When the cluster is up and the load balancer is ready, use the ip address of your new load balancer as the value for domains A records.
![Backend ups](how-to-make-it-happen\6.png)


                                                         

