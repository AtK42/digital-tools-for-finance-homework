FROM jupyter/base-notebook
#FROM python:3.8.5

COPY . /app/

WORKDIR /app

RUN pip3 install --prefer-binary -r requirements.txt

CMD jupyter nbconvert --execute /app/tmp/notebooks/housing-price-index-us.ipynb --output-dir /app/