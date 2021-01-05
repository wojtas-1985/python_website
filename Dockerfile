# Docker file for Image Deployment
FROM ubuntu:latest
LABEL maintainer=wojtas-1985
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
