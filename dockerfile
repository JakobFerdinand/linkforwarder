FROM python:3-alpine

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app

EXPOSE 5000
CMD [ "python", "./linkforwarder.py" ]
