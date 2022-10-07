FROM python:3.10-alpine
ARG POETRY_VERSION="1.2.1"
WORKDIR /workspace

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

RUN /usr/local/bin/python -m pip install -q --upgrade pip && \
    pip install -q poetry=="$POETRY_VERSION"

WORKDIR /workspace
COPY . /workspace

RUN poetry config virtualenvs.create false && \
    poetry install
