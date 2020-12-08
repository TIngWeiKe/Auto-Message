FROM python:3.7

FROM python:3
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/
COPY entrypoint.sh /code/entrypoint.sh

EXPOSE 9000

