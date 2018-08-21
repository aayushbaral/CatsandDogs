FROM python:3.6.2

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY cats_dogs_model.hdf5 ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./flaskapp.py", "--host=0.0.0.0"]


