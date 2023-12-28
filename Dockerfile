FROM python:3.12
WORKDIR /Test2
COPY ./requirements.txt /Test2/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /Test2/app
WORKDIR /Test2/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]