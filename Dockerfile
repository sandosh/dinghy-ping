from kennethreitz/pipenv

EXPOSE 5042/tcp

COPY . /app
CMD python3 api.py address 0.0.0.0
