FROM python:3.8

WORKDIR /code

COPY reqs.txt .

RUN pip install -r reqs.txt

COPY HVAC_attack.py .

CMD ["python", "./HVAC_attack.py"]
