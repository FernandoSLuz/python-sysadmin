
FROM python:3.6

WORKDIR /app

COPY ex_7.py /app/app.py

RUN pip install flask jwt pymongo

CMD [ "python", "app.py"]