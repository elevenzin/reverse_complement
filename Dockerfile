FROM python:3.9

# set directory fo the app
WORKDIR /app

# copy everything to the container
COPY . /app
COPY requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt
 	

# run the app
CMD ["python", "./app.py"]


