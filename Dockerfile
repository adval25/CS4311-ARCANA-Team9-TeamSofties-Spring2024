#use an offical Python runtime as parent image
FROM python:3.11.5

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python","-u", "app.py"]