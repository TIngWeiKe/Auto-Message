# #!/bin/sh

# # wait for PSQL server to start
# ./wait-for-it.sh pg:5432 -t 30
# if [ -f /code/celerybeat.pid ]
# then
#     rm -rf /code/celerybeat.pid
#     rm -rf /code/celerybeat-schedule
# fi

# # compile javascripts
# # cd /code/wwwroot-orig/omnianalytics && yarn install
# # cd /code/wwwroot-orig/omnianalytics && bash ./compile.sh

# # double check python dependencies
# cd /code/ && /root/site/bin/pip3 install -r requirements.txt

# # migrate db, so we have the latest db schema
# cd /code/ && /root/site/bin/python manage.py migrate

# # load default template
# /root/site/bin/python manage.py loaddata ma_cms/fixtures/default_templates.json

# # start development server on public ip interface, on port 8000
# if [ -e "/code/credentials.json" ]; then
#   echo "import /code/credentials.json"
#   export GOOGLE_APPLICATION_CREDENTIALS="$(cat /code/credentials.json)" && echo ${GOOGLE_APPLICATION_CREDENTIALS}
# else
#   echo "Not import credentials.json"
# fi
cd /code/ && /root/site/bin/python manage.py runserver 0.0.0.0:8000
