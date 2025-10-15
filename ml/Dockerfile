FROM python:3.10-slim
WORKDIR /ml
COPY requirements.txt /ml/requirements.txt
RUN pip install --no-cache-dir -r /ml/requirements.txt
COPY . /ml
ENTRYPOINT ["python"]
