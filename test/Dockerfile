#FROM jupyter/base-notebook:latest
FROM python:3.7

WORKDIR /app

COPY . /app/

RUN pip3 install --prefer-binary -r requirements.txt

CMD jupyter nbconvert --execute /app/tmp/notebooks/housing-price-index-us.ipynb --output-dir /app/