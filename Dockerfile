FROM python


COPY ./web-serv/* /webserv/

WORKDIR /webserv

RUN pip install Flask
RUN pip install redis

CMD ["python", "./main.py"]



