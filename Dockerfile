FROM python:3.7-stretch

WORKDIR /dbapp

COPY . /dbapp

RUN pip install pipenv
RUN pipenv install

EXPOSE 5000

CMD ["pipenv","run","python","api/views/database_interface.py"]
