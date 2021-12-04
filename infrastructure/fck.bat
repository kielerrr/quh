kube config get-contexts
kube config use {{{{ k8s_context }}}}
kube config get-contexts

docker stop sftp
docker container rm {{{{ docker_hub_registry }}}}/sftps --force
docker image rm {{{{ docker_hub_registry }}}}/sftp --force

docker build sftp/sftp-image -t {{{{ docker_hub_registry }}}}/sftp
docker push {{{{ docker_hub_registry }}}}/sftp


kubectl create namespace logs
helm dependency update {{{{ k8s_root_dir }}}}\{{{{ k8s_cluster_name }}}}\infrastructure\logs\charts\loki-stack
helm upgrade --install traefik {{{{ k8s_root_dir }}}}\{{{{ k8s_cluster_name }}}}\infrastructure\traefik --history-max 3
helm upgrade --install logs -n logs {{{{ k8s_root_dir }}}}\{{{{ k8s_cluster_name }}}}\infrastructure\logs\charts\loki-stack --history-max 3
helm upgrade --install sftp {{{{ k8s_root_dir }}}}\{{{{ k8s_cluster_name }}}}\infrastructure\sftp --history-max 3

@REM helm delete traefik
@REM helm delete logs -n logs
@REM helm delete sftp
@REM helm delete {{{{ app1_name }}}}
