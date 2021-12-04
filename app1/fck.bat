
kube config get-contexts
kube config use {{{{ k8s_context }}}}
kube config get-contexts


helm delete {{{{ app1_name }}}}
docker stop front-{{{{ app1_name }}}}
docker stop back-{{{{ app1_name }}}}
docker container rm {{{{ docker_hub_registry }}}}/front-{{{{ app1_name }}}} --force
docker container rm {{{{ docker_hub_registry }}}}/back-{{{{ app1_name }}}} --force
docker image rm {{{{ docker_hub_registry }}}}/front-{{{{ app1_name }}}} --force
docker image rm {{{{ docker_hub_registry }}}}/back-{{{{ app1_name }}}} --force





docker build front -t {{{{ docker_hub_registry }}}}/front-{{{{ app1_name }}}}
docker build back -t {{{{ docker_hub_registry }}}}/back-{{{{ app1_name }}}}

docker push {{{{ docker_hub_registry }}}}/front-{{{{ app1_name }}}}
docker push {{{{ docker_hub_registry }}}}/back-{{{{ app1_name }}}}


helm upgrade --install {{{{ app1_name }}}} helm  --debug --force --history-max=3
@REM helm upgrade --install {{{{ app1_name }}}} helm  --set DO_AUTH_TOKEN={{{{ do_auth_token_value }}}}   --force
@REM kubectl apply -f ..\back
@REM kubectl apply -f ..\front
                      
                                    
