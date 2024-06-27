# Jupyter images recently moved from DockerHub server to RedHat 'quay'
# we reflect that in the address. Image will be pulled from the webpage 'quay.io'
FROM quay.io/jupyter/base-notebook 

USER root
# Copy our vectorSDK package
# Dont forget that dockerfile should be in the same folder as our package
COPY . /home/pyvectorSDK


RUN pip install /home/pyvectorSDK/
#ENV VIRTUAL_ENV=/home/vectorSDK
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# USER $NB_USER
# this is important part. Jupyter notebooks are used with web browsers
# a web browser will connect to jupyter with this port, default if 8888
EXPOSE 8888

# Run Jupyter Notebook
CMD ["start-notebook.sh"]
