FROM node:current-buster
EXPOSE 3400
WORKDIR /home/sftp/app1/front/
RUN apt update -y
RUN apt install net-tools curl nano mlocate nodejs npm -y
RUN curl -sL https://deb.nodesource.com/setup_12.x |  bash -
# RUN npm install @vite/vitejs -y
RUN npm install --global http-server
# RUN npm install @vite/vitejs -y
# RUN npm init vite@latest -y vite  -- --template vue-ts
#USER 1000
COPY . .
RUN npm install
#CMD ["bash"]

CMD ["npx", "http-server", "/home/sftp/{{{{ app1_name }}}}/front/dist", "--port", "3400", "-a", "0.0.0.0", "-d", "false", "--cors"]
# npx http-server /home/sftp/{{{{ app1_name }}}}/front/dist --port 3400 -a 0.0.0.0 -d false --cors
#npx vite --port 3400 --host --debug -l debug
#npx vite --port 3400 --host 0.0.0.0  --https  --strictPort
#CMD ["vite --port 3400 --strictPort -l debug -d  -w --host 0.0.0.0"]


#CMD ["npx", "vite", "--port", "3400", "--strictPort", "-l", "info", "-d", "", "--host", "0.0.0.0"]

#npx vite --port 3400 --strictPort -l info -d  --host 0.0.0.0
#CMD ["npm", "run", "dev", "-p", "3400","--host", "0.0.0.0"]
#npm run dev -p 3400 --host 0.0.0.0





































