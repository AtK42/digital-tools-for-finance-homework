# use jupyter base image
#FROM jupyter/base-notebook:latest

# since we use a jupyter notebook and not a python script we are not sure whether to use the python base image or python
# for compatibility with certain packages, python <= 3.7 is required
FROM python:3.7

# set the working directors
WORKDIR /app

# copy everything to the current working directory
COPY . /app/

# install all necessary packages at the defined versions
# Note that, we got various errors when trying to install the packages (especially numpy), first some issue with gcc which we tried to solve by 
# installing a C complier which didn't work, we also tried building the image with different versions of the packages (for which the code still runs)
# we also tried building it on a mac (unix) and windows but all to no avail.
# Since we do not understand the error we get now, and thus have no idea where the problem lies, we leave the initial code which we think
# should technically be correct.
# Note2, we also tried (as suggested) building image from github.com/jupyter/docker-stats with version 3.7 but that one fails when building
# error code: "failed to compute cache key: "/start.sh" not found: not found".
RUN pip install --prefer-binary -r requirements2.txt

# run the jupyter notebook that should execute all code within the notebook but specifically make and save some plots
CMD jupyter nbconvert --execute /app/tmp/notebooks/housing-price-index-us.ipynb --output-dir /app/