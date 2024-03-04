# build docker 
docker build -t spleeter-serverless-docker .
#  remove any docker container with the same name IF Exists
/usr/local/bin/docker rm -f spleeter-container || true
# run docker container
/usr/local/bin/docker  run -d --name spleeter-container -p 80:80 -e DEV=True spleeter-serverless-docker