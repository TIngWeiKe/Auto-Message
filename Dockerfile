FROM python:3.7

WORKDIR /usr/src/django

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy Project
COPY . /usr/src/django

EXPOSE 9000

COPY ./entrypoint.sh /usr/src/django/entrypoint.sh
ENTRYPOINT ["/usr/src/django/entrypoint.sh"]



# FROM python:3.7

# FROM python:3
# ENV PYTHONUNBUFFERED=1

# COPY requirements.txt /code/
# RUN pip install -r /code/requirements.txt

# COPY . /code/
# COPY entrypoint.sh /code/entrypoint.sh

# EXPOSE 9000

