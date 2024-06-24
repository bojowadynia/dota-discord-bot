FROM mcr.microsoft.com/devcontainers/python:1-3.7-bullseye

ENV PYTHONUNBUFFERED 1

COPY ./python3.7/ /usr/local/lib/python3.7/

ENV DB_NAME=asdf
ENV DB_USER=asdf
ENV DB_PW=asdf
ENV DB_HOST=db
ENV DB_PORT=3306

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
