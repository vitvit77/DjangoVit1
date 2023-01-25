FROM python:3.10 AS compiler
COPY /jobs /app/jobs
COPY /main /app/main
COPY /staticfiles /app/staticfiles
COPY manage.py /app/manage.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt
WORKDIR /app
CMD /opt/venv/bin/python3.10 manage.py runserver 0.0.0.0:8001
