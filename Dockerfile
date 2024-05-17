FROM python:3.12-alpine3.18
LABEL maintainer='localhost:3000'

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 3000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp 

RUN adduser --disabled-password --no-create-home app-user

ENV PATH='/py/bin:$PATH'

CMD ["python", "app.py"]