# Dokerfile to create the container for the ERAU CS 399 Server
FROM python:3.11
MAINTAINER Wolf Paulus <wolf@paulus.com>

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Phoenix /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

COPY . /cicd
RUN pip install --no-cache-dir --upgrade -r /cicd/requirements.txt
RUN chmod +x /cicd/healthcheck.sh
WORKDIR /cicd/

#  prevents Python from writing .pyc files to disk
#  ensures that the python output is sent straight to terminal (e.g. your container log) without being first buffered
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/cicd/src
CMD ["python3.11", "src/ws.py"]
