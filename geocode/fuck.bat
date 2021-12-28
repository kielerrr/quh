
kube config get-contexts
kube config use do-nyc1-quh
kube config get-contexts


helm delete geocode
docker stop front-geocode
docker stop back-geocode
docker container rm kielerrr/front-geocode --force
docker container rm kielerrr/back-geocode --force
docker image rm kielerrr/front-geocode --force
docker image rm kielerrr/back-geocode --force





docker build front -t kielerrr/front-geocode
docker build back -t kielerrr/back-geocode

docker push kielerrr/front-geocode
docker push kielerrr/back-geocode


helm upgrade --install geocode helm  --debug --force --history-max=3
@REM helm upgrade --install geocode helm  --set DO_AUTH_TOKEN=cab2a40e-f872-48f5-998f-4eacdee63e6c   --force
@REM kubectl apply -f ..\back
@REM kubectl apply -f ..\front
                      
                                    
