# use jupyter base image
FROM jupyter/base-notebook:latest
# since we use a jupyter notebook and not a python script we don't use the python base image
#FROM python:3.7

# set the working directors
WORKDIR /app

# copy everything to the current working directory
COPY . /app/

# install all necessary packages at the defined versions
RUN pip install --prefer-binary -r requirements2.txt

# run the jupyter notebook that should execute all code within the notebook but specifically make and save some plots
CMD jupyter nbconvert --execute /app/tmp/notebooks/housing-price-index-us.ipynb --output-dir /app/