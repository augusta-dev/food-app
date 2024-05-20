FROM python:3.12-alpine3.18
LABEL maintainer='localhost:3000'

ENV PYTHONUNBUFFERED 1
ENV DEV=false

# Install busybox to get 'sh' and necessary build dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt

# Optionally copy the development requirements
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./app /app
WORKDIR /app
EXPOSE 3000

# Create virtual environment and install Python packages
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt

# Install development requirements if DEV is true
RUN if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi

RUN adduser -D -H app-user

# Clean up
RUN rm -rf /tmp

ENV PATH='/py/bin:$PATH'

# Optional: You can add a non-Django-specific user if needed
# RUN adduser --disabled-password --no-create-home app-user

# Uncomment and modify the CMD line to run your application
CMD ["python", "app.py"]
