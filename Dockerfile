# syntax=docker/dockerfile:1.4

FROM python:3.11
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY todo/ /app/todo
COPY todo_app/ /app/todo_app
COPY entrypoint.sh manage.py /app/
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]