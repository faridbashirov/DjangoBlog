FROM python
ARG DIR=/code

WORKDIR $DIR

RUN apt update

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# uWSGI will listen on this port
EXPOSE 8050

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
# RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

# Start uWSGI
CMD [ "uwsgi", "--ini", "uwsgi.ini"]