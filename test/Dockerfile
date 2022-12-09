FROM python:3.8.5

COPY /requirements.txt /tmp/

RUN pip3 install --requirement /tmp/requirements.txt

COPY . /tmp/

CMD ["python", "./tmp/notebooks/housing-price-index-us.ipynb"]

RUN docker cp CONTAINER:/tmp/reports/figures/ /reports/figures