FROM python:3.8

WORKDIR /code

COPY ./reqs.txt .

RUN pip install -r reqs.txt

COPY ./lauchApp_attack.py .

CMD ["python", "./lauchApp_attack.py"]
