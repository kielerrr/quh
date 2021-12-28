# syntax=docker/dockerfile:1.3-labs
FROM python:3.9
EXPOSE 5000
WORKDIR /home/sftp/geocode/back/
ENV DOCKER_BUILDKIT=1
RUN apt update -y
RUN apt install net-tools curl nano mlocate nodejs wget npm  -y



COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt                


RUN mkdir -p src
COPY src/* src

COPY main.py .


#uvicorn main:app --host 0.0.0.0 --port 5000 --proxy-headers --log-level trace --use-colors --access-log --interface asgi3 --reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--proxy-headers", "--log-level", "debug", "--use-colors", "--access-log", "--interface", "asgi3", "--reload"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--proxy-headers", "--use-colors", "--access-log", "--interface", "asgi3", "--reload"]
