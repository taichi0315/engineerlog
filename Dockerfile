FROM taichi0315/pyenv-ubuntu:latest
RUN mkdir /root/mysite

RUN apt-get update && apt-get install -y libjpeg-dev

ADD ./mysite /root/mysite/
WORKDIR /root/mysite
RUN pipenv install
RUN pipenv run python manage.py makemigrations && \
    pipenv run python manage.py migrate && \
    pipenv run python manage.py shell -c "from engineerlog.models import AppUser; AppUser.objects.create_superuser('admin', 'admin@localhost', 'password')"

CMD ["pipenv","run","python","manage.py","runserver","0.0.0.0:8000"]


