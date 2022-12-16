#FROM jupyter/base-notebook
#COPY . /app/
#WORKDIR /app
#RUN pip3 install -r requirements2.txt
#RUN base-notebook "./tmp/notebooks/housing-price-index-us.ipynb"

# FROM jupyter/base-notebook
# COPY . /app/
# WORKDIR /app
# RUN set -ex \
#    && conda install --quiet --yes \
#    # choose the Python packages you need
#    'matplotlib==3.3.2' \
#    'numpy==1.19.2' \
#    'numpydoc==1.1.0' \
#    'scikit-learn==0.23.2' \
#    'scipy==1.5.2' \
#    'seaborn==0.11.0' \
#    'statsmodels==0.12.0' \
#    'pandas==1.1.3' \
#    && conda clean --all -f -y \
#    # install Jupyter Lab extensions you need
#    && jupyter labextension install jupyterlab-plotly@4.9.0 --no-build \
#    && jupyter lab build -y \
#    && jupyter lab clean -y \
#    && rm -rf "/home/${NB_USER}/.cache/yarn" \
#    && rm -rf "/home/${NB_USER}/.node-gyp" \
#    && fix-permissions "${CONDA_DIR}" \
#    && fix-permissions "/home/${NB_USER}"

# Let's use the image base-notebook to build our image on top of it
FROM jupyter/base-notebook

# Let's change to root user to install java 8
USER root

# Install java 8
RUN apt-get update \
    && echo "Updated apt-get" \
    && apt-get install -y openjdk-8-jre \
    && echo "Installed openjdk 8"
    
COPY . /app/
WORKDIR /app
# Install kotlin kernel for jupyter using conda
RUN conda install -y -c jetbrains kotlin-jupyter-kernel && echo "Kotlin Jupyter kernel installed via conda"

RUN pip3 install -r requirements2.txt
RUN base-notebook "./tmp/notebooks/housing-price-index-us.ipynb"

# Let's change to  "$NB_USER" command so the image runs as a non root user by default
USER $NB_UID

#Let's define this parameter to install jupyter lab instead of the default juyter notebook command so we don't have to use it when running the container with the option -e
ENV JUPYTER_ENABLE_LAB=yes