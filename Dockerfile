FROM python:3.9.8-slim

WORKDIR /
COPY /GoodInternetOrComplain/db/ /db/
COPY . .

ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install
RUN pip install --no-cache --upgrade pip setuptools
RUN pip install -r GoodInternetOrComplain/requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]