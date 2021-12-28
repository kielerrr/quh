kube config get-contexts
kube config use do-nyc1-quh
kube config get-contexts

docker stop sftp
docker container rm kielerrr/sftps --force
docker image rm kielerrr/sftp --force

docker build sftp/sftp-image -t kielerrr/sftp
docker push kielerrr/sftp


kubectl create namespace logs
helm dependency update C:\Users\luser\.kube\quh\infrastructure\logs\charts\loki-stack
helm upgrade --install traefik C:\Users\luser\.kube\quh\infrastructure\traefik --history-max 3
helm upgrade --install logs -n logs C:\Users\luser\.kube\quh\infrastructure\logs\charts\loki-stack --history-max 3
helm upgrade --install sftp C:\Users\luser\.kube\quh\infrastructure\sftp --history-max 3

@REM helm delete traefik
@REM helm delete logs -n logs
@REM helm delete sftp
@REM helm delete geocode
