FROM arm64v8/python:3.10-slim
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python3-pip freetds-dev freetds-bin libssl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:~/app"
ENTRYPOINT [ "python", "./LocalRunning/local_running.py" ]