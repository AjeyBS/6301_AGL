FROM python:3.8

WORKDIR /code

COPY ./reqs.txt .

RUN pip install -r reqs.txt

COPY ./connectivity_attack.py .

CMD ["python", "./connectivity_attack.py"]
