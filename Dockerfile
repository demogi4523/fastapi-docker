FROM python:3.8-slim

WORKDIR /app/
ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD main.py /app/

EXPOSE 8001

CMD ["main:app", "-b", "0.0.0.0:8001", "--reload"]

# RUN hypercorn main:app -b 0.0.0.0:8001 --reload
