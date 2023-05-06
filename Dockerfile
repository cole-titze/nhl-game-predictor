FROM arm64v8/python:slim
WORKDIR /app

# Running as root
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3-pip freetds-dev freetds-bin libssl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Switch to non-root user:
RUN useradd appuser
USER appuser

ENV PYTHONPATH="${PYTHONPATH}:~/app"
ENTRYPOINT [ "python", "./LocalRunning/local_running.py" ]