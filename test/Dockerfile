FROM python:3.8.5

COPY . /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python "./tmp/notebooks/housing-price-index-us.ipynb"

RUN docker cp -a CONTAINER:/app/images /reports/figures